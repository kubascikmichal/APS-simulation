#common attributes for nutrition's such as carbs, protein, etc.
#period, amount
class Nutrition:

    def __init__(self, period: int, ratio:int, amount:int):
        """
        :param period: - time in minutes when the nutrition will start to affect glycemia
        :param ratio: - ratio nutrition to carbs
        :param amount: - weight of nutrition in meal
        """
        self.period = period
        self.ratio = ratio
        self.amount = amount