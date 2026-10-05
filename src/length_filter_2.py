from src.exceptions import DataFileError

class length_filter :
    def __init__(self , min_length):
        self.min_length=min_length

    def caleculate_length(self, orfs, logger=None ):
        accepted=[]

        for n in orfs :
            if len(n) >= self.min_length :
                accepted.append(n)
            else:
                logger.warning(f"protein '{n}' is short at {n.start_pos} ")
            
        return accepted