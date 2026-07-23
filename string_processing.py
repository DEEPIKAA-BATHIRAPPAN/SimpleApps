while True:
    print("\n--- String Processing ---")
    print("1. Reverse String")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Count Characters")
    print("5. Count Words")
    print("6. Check Palindrome")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you!")
        break

    text = input("Enter a string: ")

    if choice == "1":
        print("Reverse:", text[::-1])

    elif choice == "2":
        print("Uppercase:", text.upper())

    elif choice == "3":
        print("Lowercase:", text.lower())

    elif choice == "4":
        print("Characters:", len(text))

    elif choice == "5":
        print("Words:", len(text.split()))

    elif choice == "6":
        if text == text[::-1]:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    else:
        print("Invalid Choice")