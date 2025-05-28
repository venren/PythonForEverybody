class mergeIntervals:
    def __init__(self, input: list[list[int]]):
        self.input = input

    def formResult(self, input):
        result = []
        ind = 1
        startInd = ind
        while ind < len(input):
            if input[ind] == input[ind-1] + 1:
                ind = ind + 1
            else:
                result.append((startInd,ind-1))
                startInd = ind+1

            ind = ind+1
            

        return result

    def execute(self):
        full = set()
        for inp in self.input:
            curr = [k for k in range(inp[0], inp[1]+1)]
            curr = set(curr)
            full = full.union(curr)
        
        return self.formResult(sorted(list(full)))
    
#time-complexity - o(max number)

inp = [[1,3],[2,6],[8,10],[15,18]]
sol = mergeIntervals(inp)
print(sol.execute())


