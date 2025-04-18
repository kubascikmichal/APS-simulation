#common attributes changing CGM data - activities, etc.
class CGM:
    def __init__(self, glycemia: int, trend: int):
        """

        :param glycemia:
        :param trend:
        """
        self.glycemia = glycemia
        self.trend = trend
