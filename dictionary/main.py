# customer  = {
#     "name":"Joby John",
#     "age" : 30,
#     "is_verified": True
# }

# print(customer.get("bday", "unavailable"))

# customer["bday"] = "28-10-12"

# print(customer)

# digit = {
#     0:"zero",
#     1:"one", 
#     2:"two",
#     3:"Three",
#     4:"four",
#     5:"five"}

# output = ""
# phone = input("Phone: ")

# for ch in phone:
#     output += digit.get(int(ch), "_")
#     output+=" "

# print(output)

message = input(">")
message = message.split(' ')

output = ""
emojis = {
    ":(": "😢",
     ":)":"😊"
     }
for word in message:
    output += emojis.get(word,word) + " "
    

print(f"meassage: {output}")
