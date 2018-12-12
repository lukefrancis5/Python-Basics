def convert(temp, unit):
    unit = unit.lower()

    if unit == "c":
        temp = 9.0 / 5.0 * temp + 32
        return "%s degrees Fahrenheit"% temp
    if unit == "f":
        temp = (temp - 32) / 9.0 * 5.0
        return "% degrees Celcius"% temp

inputtemp = int(input("What is the temperature?:\n"))
inputunit = str(input("Please enter the unit of measure (c or f):\n"))

print(convert(inputtemp, inputunit))
