from src.exception import DataFileError

class weight_filter:
    def __init__(self, weights, min_weight):
        self.min_weight=min_weight
        self.weights=weights

    def caleculate_length(self, orfs):
        try:
            weight = sum(self.weights[amino] for amino in orfs)
        except KeyError as error:
            raise DataFileError(f"this amino '{error.args[0]}'is not fond")
        
        weight +=18.015
        return weight
    
    def caleculate_weight(self, orfs,logger=None):
        accepted_weight=[]

        for orf in orfs:
            weight=self.caleculate_weight(orf.protein)

            if weight >= self.min_weight:
                accepted_weight.append(orf)
            elif logger:
                logger.warning(f"orf at '{orf.start_pos}',that weight is little ")

        return accepted_weight