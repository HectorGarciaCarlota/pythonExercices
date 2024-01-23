def main():
    water = float(input("How much water did you spend this month? "))
    price: float = 6
    match water:
        case _ if water < 50:
            price
        case _ if 50 <= water <= 200:
            price = water * 0.1 + 6
        case _ if water > 200:
            price = water * 0.3 + 6

    print(f"The price is: {price}")

if __name__ == "__main__":
    main()