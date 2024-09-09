try:
    age = int (input("Enter a Number: "))
    age = int(age)
    risk = 10/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")