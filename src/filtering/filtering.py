from src.exceptions import DataFileError
from src.translation.protein import Protein

class LengthFilter :
    def __init__(self , min_length):
        self.min_length=min_length

    def calculate_length(self, orfs, logger=None ):
        accepted=[]

        for orf in orfs :
            if len(orf.protein) >= self.min_length :
                accepted.append(orf)
            else:
                if logger:
                    logger.warning(f"protein '{orf.protein}' is short at {orf.start_pos} ")
            
        return accepted
    
from src.translation.protein import Protein

class WeightFilter:
    def __init__(self, weights, min_weight):
        self.weights = weights
        self.min_weight = min_weight

    def calculate_weight(self, orfs, logger=None):
        
        accepted = []
        for orf in orfs:
            try:
               
                protein_obj = Protein(orf.protein)
                
                weight = protein_obj.weight(self.weights)
                
                if weight >= self.min_weight:
                    accepted.append(orf)
                else:
                    if logger:
                        logger.warning(f"protein '{orf.protein}' has weight {weight:.2f} < {self.min_weight}")
            except Exception as e:
                if logger:
                    logger.warning(f"Could not calculate weight for ORF at {orf.start_pos}: {e}")
                continue
        return accepted

class Total_orf:
    def __init__(self, min_length, min_weight, weights):
        self.length_filter = LengthFilter(min_length)
        self.weight_filter = WeightFilter(weights , min_weight)

    def Calculation( self, orfs, logger=None):
        orfs =self.length_filter.caleculate_length(orfs , logger)
        orfs =self.weight_filter.caleculate_weight(orfs , logger)

        return orfs