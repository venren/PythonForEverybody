
class topKFrequent:

    def __init__(self, input, k ):
        self.input = input
        self.k = k

    def execute(self):
        count_dict = {}
        entry_dict = {}

        for i in self.input:
            if i in entry_dict:
                entry_dict[i] = entry_dict[i] + 1
                count_dict.setdefault(entry_dict[i], set()).add(i)
            else:
                entry_dict[i] = 1
                count_dict.setdefault(1, set()).add(i)

        if self.k in count_dict:
            return count_dict[self.k]
        
        return([])
    

input = [1,1,1,2,2,3]
#input = [1]
sol = topKFrequent(input, 1)
print(sol.execute())



