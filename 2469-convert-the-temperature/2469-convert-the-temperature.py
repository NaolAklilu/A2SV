class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # calculate temperature in kelvin
        kelvin = celsius + 273.15 + 0.0000
        
        # Calculate tempetrature in Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00 + 0.0000
        
        return [kelvin, fahrenheit]