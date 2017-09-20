from pra8.silver_service_taxi import SilverServiceTaxi


def main():

    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)

main()
