def main():
    first_input = float(input("Enter your first number: "))
    second_input = float(input("Enter your second number: "))

    result_sum = first_input + second_input
    difference = first_input - second_input
    product = first_input * second_input
    quotient = first_input / second_input
    power = first_input ** second_input
    floor_quotient = first_input // second_input
    remainder = first_input % second_input

    print(f"You entered {first_input:.2f} as your first number and {second_input:.2f} as your second number.")
    print(
        f"The sum is {result_sum:.2f}, "
        f"difference is {difference:.2f}, "
        f"product is {product:.2f}, "
        f"quotient is {quotient:.2f}, "
        f"power is {power:.2f}, "
        f"floor quotient is {floor_quotient:.2f}, "
        f"and remainder is {remainder:.2f}."
    )

if __name__ == '__main__':
    main()
