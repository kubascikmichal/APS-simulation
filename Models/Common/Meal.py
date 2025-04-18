
import Nutrition

class Meal:
    def __init__(self, protein:Nutrition, fat:Nutrition, carbs:Nutrition):
        """
        :param protein:
        :param fat:
        :param carbs:
        """
        self.protein = protein
        self.fat = fat
        self.carbs = carbs