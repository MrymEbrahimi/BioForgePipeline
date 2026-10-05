from .orf import ORF, START_CODON, STOP_CODONS
def find_orfs_forward(dna):
    orfs = []

    for frame in range(3):
        i = frame

        while i < len(dna) - 2:
            codon = dna[i:i + 3]

            if codon == START_CODON:
                start_pos = i
                is_complete = False

                for j in range(i, len(dna) - 2, 3):
                    codon = dna[j:j + 3]

                    if codon in STOP_CODONS:
                        is_complete = True
                        break

                if is_complete:
                    orf_sequence = dna[start_pos:j + 3]
                    i = j + 3
                else:
                    orf_sequence = dna[start_pos:]
                    i = len(dna)

                orf = ORF(
                    strand="Forward",
                    frame=frame,
                    start_pos=start_pos,
                    protein=orf_sequence,
                    is_complete=is_complete
                )

                orfs.append(orf)

            else:
                i += 3

    return orfs


