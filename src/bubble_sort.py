def bubble_sort(items):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(items) - 1):
            if items[index] > items[index + 1]:
                swapped = True
                items[index], items[index + 1] = items[index + 1], items[index]

def test_bubble_sort():
    """should correctly sort floats from lowest to highest when provided in reverse order"""
    floats = [5.5, 4.4, 3.3, 2.2, 1.1]
    bubble_sort(floats)
    assert floats == [1.1, 2.2, 3.3, 4.4, 5.5]

def main():
    floats = []
    for i in range(int(input("How many elements do you want to sort: "))):
        floats.append(float(input("Enter a list element: ")))
    bubble_sort(floats)
    print("\nSorted:", floats)

if __name__ == '__main__':
    main()