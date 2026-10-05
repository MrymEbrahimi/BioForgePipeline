import os
import sys
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from src.fasta.parser import parse_fasta
from src.fasta.validator import validate_dna
from src.orf.forward import find_orfs_forward
from src.orf.reverse import find_orfs_reverse
from src.translation.translation import translate
from src.filtering.filtering import LengthFilter
from src.reporting.annotator import annotate
from src.reporting.reporter import write_report

def run_pipeline(input_path: str, output_dir: str, min_length: int):
    
    logging.info(f"Starting BioForge Pipeline with input: {input_path}, output: {output_dir}, min_length: {min_length}")

    try:
        records = parse_fasta(input_path)
        logging.info(f"Successfully parsed {len(records)} records from FASTA file.")
    except Exception as e:
        logging.error(f"Error parsing FASTA file: {e}")
        sys.exit(1) 
    all_orfs = [] 
    
    for record in records:
        logging.info(f"Processing record ID: {record.id}")
        
        
        try:
            validate_dna(record.sequence)
        except Exception as e:
            logging.warning(f"Skipping record {record.id} due to invalid sequence: {e}")
            continue 
        dna_seq = record.sequence

        forward_orfs = find_orfs_forward(dna_seq)
        logging.info(f"Found {len(forward_orfs)} Forward ORFs for {record.id}.")
        
        reverse_orfs = find_orfs_reverse(dna_seq)
        logging.info(f"Found {len(reverse_orfs)} Reverse ORFs for {record.id}.")

        all_orfs.extend(forward_orfs)
        all_orfs.extend(reverse_orfs)

    if not all_orfs:
        logging.warning("No ORFs found in the entire input file.")
        
        write_report([], output_dir) 
        return

    from src.fasta.dna_ops import DNASequence
    from src.translation.data_loader import load_codon_table
    codon_table = load_codon_table("data/codon_table.txt")
    translated_orfs = []
    for orf in all_orfs:
        try:
            dna_obj = DNASequence(orf.protein)
            rna_seq = dna_obj.to_rna()
            protein_obj = translate(rna_seq, codon_table)
            orf.protein = protein_obj.sequence
            translated_orfs.append(orf)
        except Exception as e:
            logging.warning(f"Could not translate ORF at {orf.start_pos} ({orf.strand}): {e}")
            continue

    
    length_filter_obj = LengthFilter(min_length)
    filtered_orfs = length_filter_obj.caleculate_length(
        translated_orfs,
        logger=logging
    )
    logging.info(f"Filtered ORFs based on min_length {min_length}. Remaining: {len(filtered_orfs)}")
    
    annotated_orfs = annotate(filtered_orfs)
    logging.info("Annotated final ORFs.")

    write_report(annotated_orfs, output_dir)
    logging.info("Report generated successfully.")

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser(description="Run BioForge Pipeline directly.")
    parser.add_argument("--input", required=True, help="Path to input FASTA file")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--min-length", type=int, default=0, help="Minimum ORF length")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    run_pipeline(args.input, args.out, args.min_length)
