class FASTARecord:
    """Represent a single record parsed from a FASTA file.

    Attributes:
        id: Unique identifier extracted from the FASTA header.
        description: Optional description or organism information from the header.
        sequence: DNA sequence associated with the record.
    """