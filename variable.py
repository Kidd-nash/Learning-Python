def detect_type(value):
    try:
        int_value = int(value)
        return int_value, "int"
    except ValueError:
        try:
            float_value = float(value)
            return float_value, "float"
        except ValueError:
            return value, "str"

def main():
    raw_input = input("Enter something: ")
    actual_value, detected_type = detect_type(raw_input)

    print(f"You entered: {actual_value} (Type: {detected_type})")

    # Example: branching logic
    if detected_type == "int":
        print("You entered an integer, doubling it:", actual_value * 2)
    elif detected_type == "float":
        print("You entered a float, rounded value:", round(actual_value))
    else:
        print("You entered a string in text form.")

if __name__ == '__main__':
    main()
