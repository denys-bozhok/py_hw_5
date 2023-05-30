numbers = []

def multiplication(numbers):

    print(f"Answer - {numbers[0] * numbers[1]}\n")

    numbers.clear()

def division(numbers):

    print(f"Answer - {numbers[0] / numbers[1]}\n")

    numbers.clear()

def addition(numbers):

    print(f"Answer - {numbers[0] + numbers[1]}\n")

    numbers.clear()

def subtraction(numbers):

    print(f"Answer - {numbers[0] - numbers[1]}\n")

    numbers.clear()


def hello():

    print("Hello! Enter action and 2 numbers for calculate!\n")


def number_list():

    num1 = int(input("Enter first Num\n"))

    num2 = int(input("Enter second Num\n"))

    numbers.append(num1)

    numbers.append(num2)

    print(f"\nYou was enter {numbers}\n")

    return numbers


def actions_list():

    actions = (
        {
            "division" : "/"
        },

        {
            "multiplication" : "*"
        },

        {
            "addition" : "+"
        },

        {
            "subtraction" : "-"
        }
    )

    print(f"Print action what U wonna do with entered numbers")

    i = 0

    for action in actions:

        for key in action:

            print(f"{i + 1}) For {key.upper()} press - '{action[key]}'")

            i += 1


def run():

    is_running = True

    while is_running:

        number_list()

        actions_list()

        print("enter 'q' for QUIT")

        choose_action = input("\nWhat you want to do?\n")

        match(choose_action):

            case "*":

                multiplication(numbers)

            case "/":

                division(numbers)

            case "+":

                addition(numbers)

            case "-":

                subtraction(numbers)

            case "q":

                is_running = False

                print("Goodbye")

            case _:

                print("Incorrect data")


def main():

    hello()

    run()


if __name__ == "__main__":
    main()