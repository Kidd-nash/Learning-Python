def main():
    first_value = float(input("Enter any number..."))

    second_value = float(input("Enter another number..."))

    if first_value == second_value:
        print(f"{first_value} is equal to {second_value}")
    elif first_value > second_value:
        print(f"{first_value} is greater than {second_value}")
    elif first_value < second_value:
        print(f"{first_value} is less than {second_value}")
    elif first_value != second_value:
        print(f"{first_value} is not equal to {second_value}")
    else:
        print(f"{first_value} else un {second_value}")

if __name__ == '__main__':
    main()
