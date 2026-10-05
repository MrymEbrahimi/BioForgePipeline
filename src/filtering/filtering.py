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


class Total_orf:
    def __init__(self, min_length, min_weight, weights):
        self.length_filter_2 = length_filter(min_length)
        self.weight_filter_2 = weight_filter(min_weight)

    def Calculation( self, orfs, logger=None):
        orfs =self.length_filter_2.caleculate_length(orfs.logger)
        orfs =self.weight_filter_2.caleculate_length(orfs.logger)

        return orfs