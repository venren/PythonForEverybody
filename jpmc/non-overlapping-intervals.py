class nonOverlappingInterval:

    def __init__(self, input):
        self.input = input
        self.processing = input
        self.result = []

    def execute(self):
        safeToRemove = 0
        visited = set()
        for entry_input in self.input:
            if entry_input[0] in visited and entry_input[1] in visited:
                safeToRemove = safeToRemove +1
                continue

            visited.update(range(entry_input[0], entry_input[1]+1))

        return visited

rand = [[1,2],[1,2],[1,2]]
rand = [[1,2],[2,3],[3,4],[1,3]]
rand =  [[1,2],[2,3]]
rand = [[1,3],[2,6],[8,10],[15,18]]
sol = nonOverlappingInterval(rand)
#print(sol.execute())

##sort
rand = [[2,3],[1,5],[4,8],[6,10],[5,6]]
rand.sort(key= lambda i: i[0])
print(rand)