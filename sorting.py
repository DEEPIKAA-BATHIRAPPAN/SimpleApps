def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

while True:
    print("\n--- Sorting Program ---")
    print("1. Ascending Order")
    print("2. Descending Order")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "3":
        print("Thank you!")
        break

    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    sorted_numbers = bubble_sort(numbers)

    if choice == "1":
        print("Ascending Order:", sorted_numbers)
    elif choice == "2":
        print("Descending Order:", sorted_numbers[::-1])
    else:
        print("Invalid Choice")