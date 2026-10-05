from .length_filter_2 import LengthFilter
from .weight_filter_2 import WeightFilter

class Total_orf:
    def __init__(self, min_length, min_weight, weights):
        self.length_filter_2 = LengthFilter(min_length)
        self.weight_filter_2 = WeightFilter(min_weight)

    def Calculation( self, orfs, logger=None):
        orfs =self.length_filter_2.Calculation(orfs.logger)
        orfs =self.weight_filter_2.Calculation(orfs.logger)

        return orfs