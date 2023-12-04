def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def get_operation_input():
    while True:
        operation = input("Entrez l'opération (+, -, *, /) : ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Opération non valide. Veuillez réessayer.")

def calculate_result(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Division par zéro. Veuillez réessayer.")

def display_history(history):
    print("Historique des opérations :")
    for entry in history:
        print(entry)

def main():
    print("Bienvenue dans la calculatrice simple.")

    history = []  # Liste pour stocker l'historique des opérations

    while True:
        num1 = get_number_input("Entrez le premier nombre : ")
        num2 = get_number_input("Entrez le deuxième nombre : ")

        operation = get_operation_input()

        result = calculate_result(num1, num2, operation)

        if result is not None:
            expression = f"{num1} {operation} {num2} = {result}"
            history.append(expression)
            print(f"Le résultat de {num1} {operation} {num2} est : {result}")

        display_history(history)

        clear_history = input("Voulez-vous effacer l'historique? (Oui/Non) : ").lower()
        if clear_history == 'oui':
            history.clear()

        another_calculation = input("Voulez-vous effectuer une autre opération? (Oui/Non) : ").lower()
        if another_calculation != 'oui':
            break

if __name__ == "__main__":
    main()
