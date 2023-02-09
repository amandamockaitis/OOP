import InsectClass as ic


def main():
    mosquito = ic.Insect("mosquito", 2, 4)

    housefly = ic.Insect("housefly", 2, 4)

    housefly.flight_length()
    mosquito.flight_length()

    print(
        f"The number of miles {housefly.get_name()} can fly is: {housefly.get_flight()}"
    )
    print(
        f"The number of miles {mosquito.get_name()} can fly is: {mosquito.get_flight()}"
    )


main()
