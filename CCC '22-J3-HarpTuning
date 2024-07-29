tuning = input()
tuning_list = []
new_list = []
numbers = "1234567890"

for i in tuning:
    tuning_list.append(i)
    
for char in tuning_list:
    if char != "+" and char != "-":
        new_list.append(char)
    if char == "+":
        new_list.append(" tighten ")
    if char == "-":
        new_list.append(" loosen ")
    if char in numbers:
        new_list.append("\n")

print("".join(new_list))
