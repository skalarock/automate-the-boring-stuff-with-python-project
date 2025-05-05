# performs collatz sequence operations until a 1 is returned

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


def main():
    print("Enter a number to start the collatz sequence:")
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
