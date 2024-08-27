input_str = input("\n")
input_list = input_str.split()
 
lines = int(input_list[0])
 
floor = []
 
for i in range(lines):
 
    floor.append(list(input()))

for i in range(len(floor)):
    for j in range(len(floor[i])):
        if floor[i][j] == "W":
            if i - 1 >= 0 and floor[i-1][j] == ".":
                floor[i-1][j] = "C"
            if i + 1 < len(floor) and floor[i+1][j] == ".":
                floor[i+1][j] = "C"
            if j - 1 >= 0 and floor[i][j-1] == ".":
                floor[i][j-1] = "C"
            if j + 1 < len(floor[i]) and floor[i][j+1] == ".":
                floor[i][j+1] = "C"
 
for i in range(len(floor)):
    new_grid_str = "".join(floor[i])
    print(new_grid_str)
