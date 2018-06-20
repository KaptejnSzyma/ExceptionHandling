a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))

try:
    print(a/b)
except (ValueError, ZeroDivisionError):
    print("Your input was wrong, terminating program")