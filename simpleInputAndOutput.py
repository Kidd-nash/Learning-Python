def main():
    try:
        kilogram = float(input("Enter a weight in Kg to be converted into lbs..."))

        pounds = kilogram * 2.20462

        print(f"{kilogram}kg is equal to {pounds:.2f} in pounds(lbs)")

    except ValueError:
        print("Please enter a valid number...")

if __name__ == '__main__':
    main()

