class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:       
        return [celsius + 273.15 + 0.0000, celsius * 1.80 + 32.00 + 0.0000]