def main():
    kilogram = input("Enter a weight in Kg to be converted into lbs...")

    kilogram = float(kilogram)

    pounds = kilogram * 2.20462

    print(f"{kilogram}kg is equal to {pounds} in pounds(lbs)")

if __name__ == '__main__':
    main()

