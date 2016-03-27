class AStable555(object):
    """
    Calculations for 555 timers
    """

    @staticmethod
    def timeHigh(Ra, Rb, C):
        """
        Calculates the time that the output of the timer is high.

        :param Ra: The resistance of kOhm resitor A, the top one.
        :param Rb: The resistance in kOhm of resistor B, the bottom one.
        :param C: The capacitance in uF of the timing capacitor.
        """
        return 0.693*(Ra*1000+Rb*1000)*C/1000000

    @staticmethod
    def timeLow(Rb, C):
        """
        Calculates the time that the output of the timer is low.

        :param Rb: The resistance in kOhm of resistor B, the bottom one.
        :param C: The capacitance in uF of the timing capacitor.
        """
        return 0.693*(Rb*1000)*C/1000000
