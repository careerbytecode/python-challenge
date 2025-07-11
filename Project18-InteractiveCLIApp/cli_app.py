def calculator():
    try:
        num1 = float(input("First number: "))
        op = input("Operation (+, -, *, /): ")
        num2 = float(input("Second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator.")
    except ValueError:
        print("Please enter valid numbers.")

def word_search():
    text = input("Type a sentence: ")
    word = input("Word to find: ")
    if word.lower() in text.lower():
        print(f"'{word}' found!")
    else:
        print(f"'{word}' not found.")

def main():
    print("Welcome!")
    while True:
        print("\n1. Calculator")
        print("2. Word Search")
        print("3. Exit")
        choice = input("Choose (1-3): ")
        if choice == "1":
            calculator()
        elif choice == "2":
            word_search()
        elif choice == "3":
            print("bye")
            break
        else:
            print("Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
