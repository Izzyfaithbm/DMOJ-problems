from collections import deque

n = int(input()) # rows
m = int(input()) # columns

field = []

for _ in range(n):
    field.append(list(input()))
    
starty = int(input())
startx = int(input())
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque([])
q.append((startx, starty))
total = 0

prices = {
    "S": 1,
    "M": 5,
    "L": 10
}

visited[starty][startx] = True

while q:
    x, y = q.popleft()
    total += prices[field[y][x]]
    
    if x+1 < m and not visited[y][x+1] and not field[y][x+1] == "*":
        visited[y][x+1] = True
        q.append((x+1, y))
    if x-1 >= 0 and not visited[y][x-1] and not field[y][x-1] == "*":
        visited[y][x-1] = True
        q.append((x-1, y))
    if y+1 < n and not visited[y+1][x] and not field[y+1][x] == "*":
        visited[y+1][x] = True
        q.append((x, y+1))
    if y-1 >= 0 and not visited[y-1][x] and not field[y-1][x] == "*":
        visited[y-1][x] = True
        q.append((x, y-1))
        
print(total)
