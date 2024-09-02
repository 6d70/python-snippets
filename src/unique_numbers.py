def unique(values):
    unique_values = []
    for value in values:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

def test_unique():
    assert unique([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def valid_int_input(message, error_message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)

def main():
    numbers = []
    for i in range(
        valid_int_input(
            "How many elements do you want to dedupe: ",
            "Invalid input. Please enter an integer.",
        )
    ):
        numbers.append(
            valid_int_input(
                f"Enter list element {i + 1}: ", "Invalid input. Please enter an integer."
            )
        )
    print("Original list:", numbers)
    print("List after removing duplicates:", unique(numbers))


if __name__ == "__main__":
    main()
