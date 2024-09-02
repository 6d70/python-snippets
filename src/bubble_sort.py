def bubble_sort(items):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                swapped = True
                items[i], items[i + 1] = items[i + 1], items[i]


def test_bubble_sort():
    """should correctly sort floats from lowest to highest when provided in reverse order"""
    floats = [5.5, 4.4, 3.3, 2.2, 1.1]
    bubble_sort(floats)
    assert floats == [1.1, 2.2, 3.3, 4.4, 5.5]


def valid_int_input(message, error_message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)


def valid_float_input(message, error_message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_message)


def main():
    floats = []
    for i in range(
        valid_int_input(
            "How many elements do you want to sort: ",
            "Invalid input. Please enter an integer.",
        )
    ):
        floats.append(
            valid_float_input(
                f"Enter list element {i + 1}: ", "Invalid input. Please enter a float."
            )
        )
    bubble_sort(floats)
    print("\nSorted:", floats)


if __name__ == "__main__":
    main()
