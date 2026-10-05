from .orf import ORF, Stop_Codon, Stop_Codons


def find_orfs_forward(dna):
    orfs = []

    for frame in range(3):
        start_pos = None
        protein = []

        for i in range(frame, len(dna) - 2, 3):
            codon = dna[i:i + 3]

            if start_pos is None and codon == START_CODON:
                start_pos = i
                protein = ["M"]

            elif start_pos is not None:
                if codon in STOP_CODONS:
                    is_complete = True

                    orf = ORF(
                        strand="Forward",
                        frame=frame,
                        start_pos=start_pos,
                        protein="".join(protein),
                        is_complete=is_complete
                    )

                    orfs.append(orf)
