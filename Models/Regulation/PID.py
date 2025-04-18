class PID:
    def __init__(self, kP: float, kI: float, kD: float):
        """
        :param kP:
        :param kI:
        :param kD:
        """
        self.kP = kP
        self.kI = kI
        self.kD = kD

    def calculate_regulation(target : float, input: float) -> float:
        return 0