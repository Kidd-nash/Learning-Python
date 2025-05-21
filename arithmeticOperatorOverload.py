def main():
    first_input = input("Enter your first number...")
    second_input = input("Enter your second number...")

    sum = first_input + second_input
    difference = first_input - second_input
    product = first_input * second_input
    quotient = first_input / second_input
    power = first_input ** second_input
    floor_quotient = first_input // second_input
    remainder = first_input % second_input

    print(f"You entered {first_input} as your first number and {second_input} as your second number")
    print(f"in which the sum is equal to {sum}, difference is equal to {difference}, product is equal to {product}, quotient is equal to {quotient}, power is equal to {power}, floor quotient is equal
    {floor quotient}, and last the remainder from its quotient {remainder}")

if __name__ == '__main__'
    main()
