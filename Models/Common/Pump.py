import Insulin, BasalProfile

class Pump:
    def __init__(self, insulin:Insulin, basal:BasalProfile):
        """

        :param insulin:
        :param basal:
        """
        self.insulin = insulin
        self.basal = basal