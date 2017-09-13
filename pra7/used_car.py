from pra7.car import Car

def main():
    my_car = Car("car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel, "\nodo =", my_car.odometer)
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =",limo.fuel,"\nodo =", limo.odometer)
    print(limo)

main()