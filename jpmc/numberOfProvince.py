#https://leetcode.com/problems/number-of-provinces/description/
#https://leetcode.com/problems/redundant-connection/

class Provinces:

    def __init__(self, input):
        self.visited = set()
        self.isConnected = input

    def dfs(self, i):
        self.visited.add(i)
        for j in range(len(self.isConnected[i])):
            if self.isConnected[i][j] and j not in self.visited:
                self.dfs(j)

    def execute(self):
        num_province = 0
        for i in range(len(self.isConnected)):
            if i not in self.visited:
                num_province += 1
                self.dfs(i)
        return num_province


input = [[1,0,1,1],[0,1,1,0],[1,1,1,0],[1,0,0,1]]  
input = [[1,1,0],[1,1,0],[0,0,1]]  
input = [[1,0,0],[0,1,0],[0,0,1]]
Prov =Provinces(input)
print(Prov.execute())