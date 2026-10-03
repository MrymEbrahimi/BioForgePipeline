def annotate(orfs):
    counter = 1
    for orf in orfs:
        orf.id = f"BFG_{counter:03d}"
        counter += 1

    return orfs