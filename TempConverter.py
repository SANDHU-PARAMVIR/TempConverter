# Temperature Converter
# Param Sandhu - 301118847

def menu():
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    pick = int(input("Enter a Choice: "))
    return pick

def toCelsius(f):
    return int((f - 32) / 1.8)

def toFahrenheit(c):
    return int(c * 1.8 + 32)

def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            # convert C to F
            c = eval(input("Enter Temperature in Celsius: "))
            print(str(c) + "C = " + str(toFahrenheit(c)) + "F")
        elif choice == 2:
            # convert F to C
            f = eval(input("Enter Temperature in Fahrenheit: "))
            print(str(f) + "F = " + str(toCelsius(f)) + "C")
        else:
            print("Invalid Entry")
        choice = menu()



main()
