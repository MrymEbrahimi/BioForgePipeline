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
                logger.warning(f"protein '{orf.protein}' is short at {orf.start_pos} ")
            
        return accepted
    
class weight_filter:
    def __init__(self, weights, min_weight):
        self.min_weight=min_weight
        self.weights=weights

    def caleculate_length(self, orfs):
        try:
            weight = 0
            for amino in protein:
                weight += self.weights[amino]

            weight +=18.015

        except KeyError as error:
            raise DataFileError(f"this amino '{error.args[0]}'is not fond")
        
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

class Total_orf:
    def __init__(self, min_length, min_weight, weights):
        self.length_filter = length_filter(min_length)
        self.weight_filter = weight_filter(min_weight)

    def Calculation( self, orfs, logger=None):
        orfs =self.length_filter.caleculate_length(orfs.logger)
        orfs =self.weight_filter.caleculate_weight(orfs.logger)

        return orfs
