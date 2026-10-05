from src.exceptions import DataFileError

class length_filter :
    def __init__(self , min_length):
        self.min_length=min_length

    def caleculate_length(self, orfs, logger=None ):
        accepted=[]

        for orf in orfs :
            if len(orf.protein) >= self.min_length :
                accepted.append(orf)
            else:
                logger.warning(f"protein '{n.protein}' is short at {n.start_pos} ")
            
        return accepted