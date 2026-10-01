class Protein:
    """Represent a protein sequence.

    Attributes:
        sequence: Amino acid sequence of the protein.
    """

    def weight(self, weights_dict):
        """Calculate the molecular weight of the protein.

        Args:
            weights_dict: Dictionary mapping amino acids to their weights.

        Returns:
            The total molecular weight of the protein.
        """