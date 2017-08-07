def celsius_to_fahrenheit(celsius):
    farenheit = celsius * 9.0 / 5 + 32
    return farenheit

def fahrenheit_to_celsius(farenheit):
    celsius = 5 / 9 * (farenheit - 32)
    return celsius

def main():
    celsius = float(input("celsius:"))
    fahrenheit = float(input("fahrenheit:"))
    print("celsius to fahrenheit is: ", celsius_to_fahrenheit(celsius))
    print("fahrenheit to celsius is: ", fahrenheit_to_celsius(fahrenheit))
main()
