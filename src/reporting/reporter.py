import os
def write_report(orfs, path):
    with open(os.path.join(path,"report.txt"), "w", encoding="utf-8") as file:
        for orf in orfs:
            if orf.is_complete:
                status = "Complete"
            else:
                status = "Incomplete"
            
            file.write(
                f"ID: {orf.id}\n"
                f"Strand: {orf.strand}\n"
                f"Frame: {orf.frame}\n"
                f"Start Position: {orf.start_pos}\n"
                f"Protein: {orf.protein}\n"
                f"Status: {status}\n\n"
            )