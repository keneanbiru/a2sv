class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend // divisor))
        rem = dividend % divisor
        if rem == 0:
            return "".join(fraction)

        fraction.append(".")
        map_dict = {}
        while rem != 0:
            if rem in map_dict:
                fraction.insert(map_dict[rem], "(")
                fraction.append(")")
                break
            map_dict[rem] = len(fraction)
            rem *= 10
            fraction.append(str(rem // divisor))
            rem %= divisor

        return "".join(fraction)