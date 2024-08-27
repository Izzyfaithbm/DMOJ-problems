# BFS or DFS (interchangeable, but BFS is easier to program)

# like a spotify queue and go through tree in layers
# n is people m is comparisons 

from collections import deque # makes arrays go faster or else timeout 

n, m = map(int, input().split()) # shortcut for taking each input instead of converting to arrays and back to strings, etc

# make tree/array with number of people in it 
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)
    
p, q = map(int, input().split())

# append sends to right, append left sends to left 
def bfs(s, e):
    queue = deque([])
    # put the s (starting) node
    queue.append(s)
    visited = [False for _ in range(n+1)]
    
    #while queue is not empty
    while queue:
        #takes element from left
        v = queue.popleft()
        if v == e:
            return True
        
        for i in adj[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True
    return False

pq = bfs(p, q)
qp = bfs(q, p)

# if we can reach both of them from eachother
if pq and qp:
    print("unknown")
    
# p is not taller than q 
elif pq:
    print("no")

elif not pq and not qp:
    print("unknown")
        
# p is taller than q 
else:
    print("yes")
