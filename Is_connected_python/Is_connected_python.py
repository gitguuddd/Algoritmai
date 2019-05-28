import sys
from collections import defaultdict

x = []


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Function to print a BFS of graph

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            x.append(s)
            print (s," ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g=Graph()

fileName = "jungus1.off"

# reading from the file
file = open(fileName, "r")

# check if file is open
if file.mode != 'r':
    print("There is no file in directory with the name: ", fileName)
    sys.exit()

content = file.readlines()

if content[0] != "OFF\n":
    print("File's header is incorrect")
    sys.exit()

geoInfo = content[1].split()
vertices = int(geoInfo[0])
faces = int(geoInfo[1])

del content[0:vertices + 2]

for line in content:
    numbers = line.split()

    numberOfVertices = numbers.pop(0)
    for i in range(0, int(numberOfVertices)):
        numbers[i]
    if i==3:
        g.addEdge(int(numbers[0]), int(numbers[1]))
        g.addEdge(int(numbers[1]), int(numbers[2]))
        g.addEdge(int(numbers[2]), int(numbers[3]))
        g.addEdge(int(numbers[3]), int(numbers[0]))
    if i==2:
        g.addEdge(int(numbers[0]), int(numbers[1]))
        g.addEdge(int(numbers[1]), int(numbers[2]))
        g.addEdge(int(numbers[2]), int(numbers[0]))
g.BFS(0)
if len(x)==int(vertices):
    print("OFF failo grafas yra jungusis")
if len(x)!=int(vertices):
    print("OFF failo grafas nėra jungusis")