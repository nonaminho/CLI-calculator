from operations import *

def main():
    print("🧮 Welcome to CLI Calculator 🧮")

    while True:
        print("""\n\nPlease, select operation
1) Add
2) Subtract
3) Multiplication
4) Division
5) Exit""")
        
        operation = input("Enter operation: ")

        if operation == '5':
            print("Bye!")
            break
        try: 
            a = float(input("Value 1: "))
            b = float(input("Value 2: "))
        except ValueError:
            print("Please, enter 2 numeric values (Real numbers)")
            continue

        if operation == "1":
            print(f"Result: {add(a, b)}")
        elif operation == "2":
            print(f"Result: {subtraction(a, b)}")
        elif operation == "3":
            print(f"Result: {multiplication(a, b)}")
        elif operation == "4":
            print(f"Result: {division(a, b)}")
        else:
            print("Invalid operation")
        
if __name__ == "__main__":
    main()