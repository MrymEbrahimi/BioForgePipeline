def run_pipeline(input, out, min_length):
    """Run the complete BioForge processing pipeline.

    The pipeline parses FASTA input, validates sequences, detects ORFs,
    translates them, filters the results, annotates ORFs, and generates
    the final report.

    Args:
        input: Path to the input FASTA file.
        out: Path to the output directory.
        min_length: Minimum required length for filtering results.
    """