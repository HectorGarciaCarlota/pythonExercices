def ex2():
    def menu():
        while True:
            try:
                user_input = input("1. Bitllet senzill\n2. TCasual\n3. TMes\n4. TTrimestre\n5. TJove\nChoose an option: ")
                user_choice = int(user_input)

                if 1 <= user_choice <= 5:
                    return user_choice
                else:
                    print("Please choose a number between 1 and 5")
            except ValueError:
                print("Please enter a valid integer")

    def request_zones():
        while True:
            try:
                user_input_zones = input("Quantes zones vols? (1-4 zones): ")
                user_choice_zones = int(user_input_zones)

                if 1 <= user_choice_zones <= 4:
                    return user_choice_zones
                else:
                    print("Please choose a number between 1 and 4")
            except ValueError:
                print("Please enter a valid integer")

    def calcularPreu(tarjeta, num_zones):
        match num_zones:
            case 1:
                return tarjeta
            case 2:
                return tarjeta * 1.35
            case 3:
                return tarjeta * 1.89
            case 4:
                return tarjeta * 2

    def checkMoney(dineros):
        monedes = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
        if dineros in monedes:
            return True
        else:
            return False

    def pagament(preuFinal: float):
        money: float = 0.0

        while money < preuFinal:
            try:
                diners_input = input("Introdueix diners: ")
                diners = float(diners_input)

                if checkMoney(diners):
                    money += diners
                    if money < preuFinal:
                        print(f"Falten {preuFinal - money:.2f} diners")
                    else:
                        print(f"Sobren {money - preuFinal:.2f} diners")
                else:
                    print("Moneda no acceptada.")
            except ValueError:
                print("Please enter a valid float")

        print("Pagament completat.")

    while True:
        user_choice = menu()

        zones_chosen = request_zones()

        match user_choice:
            case 1:
                print("Bitllet senzill selected")
                preuFinal = calcularPreu(2.20, zones_chosen)
                print(f"El preu final és: {preuFinal:.2f} euros")
                pagament(preuFinal)
            case 2:
                print("TCasual selected")
                preuFinal = calcularPreu(10.20, zones_chosen)
                print(f"El preu final és: {preuFinal:.2f} euros")
                pagament(preuFinal)
            case 3:
                print("TMes selected")
                preuFinal = calcularPreu(54.00, zones_chosen)
                print(f"El preu final és: {preuFinal:.2f} euros")
                pagament(preuFinal)
            case 4:
                print("TTrimestre selected")
                preuFinal = calcularPreu(145.30, zones_chosen)
                print(f"El preu final és: {preuFinal:.2f} euros")
                pagament(preuFinal)
            case 5:
                print("TJove selected")
                preuFinal = calcularPreu(105.00, zones_chosen)
                print(f"El preu final és: {preuFinal:.2f} euros")
                pagament(preuFinal)




if __name__ == "__main__":
    ex2()