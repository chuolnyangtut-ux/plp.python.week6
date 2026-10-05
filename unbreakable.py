def safe_input_number():
    user_input = input("Enter a number: ")
    try:
        return int(user_input)
    except ValueError:
        return "Invalid input, not a number."

if __name__ == "__main__":
    result = safe_input_number()
    print(result)
