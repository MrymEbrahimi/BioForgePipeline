def parse_fasta(file_path):
    """Parse a FASTA file and return its records.

    The parser reads multiple FASTA records, extracts the identifier
    and description from each header, ignores blank lines, and converts
    DNA sequences to uppercase.

    Args:
        file_path: Path to the FASTA input file.

    Raises:
        FastaFormatError: If the file is empty or a sequence appears
            without a FASTA header.
    """