#all attributes in human model

class Human:

    def __init__(self,name:str, carbs_glycemia_ratio:float, insulin_glycemia_ratio:float):
        """
        :param name:
        :param carbs_glycemia_ratio:
        :param insulin_glycemia_ratio:
        """

        self.name = name
        self.CGR = carbs_glycemia_ratio
        self.IGR = insulin_glycemia_ratio

    def __str__(self):
        return f"Status:{self.name}"