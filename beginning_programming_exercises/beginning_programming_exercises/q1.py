# 1.	Ask the user for a temperature in Celsius and convert it to Fahrenheit.  Can use Alt 0176 to display the degree symbol
celcius = float(input("Temperature in C: "))
fahrenheit = celcius * 9/5 + 32
print(f"Celcius: {celcius} => Fahrenheit: {fahrenheit}")
