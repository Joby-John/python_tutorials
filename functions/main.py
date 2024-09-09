def greet(name, lastname):
    print(f"hi {name} {lastname}")
    print("Good morning")

greet(input("Enter your name: "), lastname="John")# always use positional argument in first 

# for most part use posiional argumnet
# for increased readability for numeric argumnet use keyword argument


def square(number):
    return number*number

#by default python return none, so if any function call is passed to print and it has no return it will display none

result = square(int(input("Enter a NUmber: ")))

print(result)