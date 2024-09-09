numbers = [1,2,32,31,5]
numbers.append(20)
numbers.insert(0,0)
numbers.remove(20)
numbers.pop()

numbers2 = numbers.copy()
numbers.sort(reverse=True)
print(numbers.index(2))
print(15 in numbers)
print(numbers)
print(numbers2)

numbers = [1,1,23,4,5,6]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print (unique)