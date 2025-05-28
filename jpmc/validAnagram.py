
class ValidAnagram:
    
    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2 


    def execute(self):
        if len(self.str1) != len(self.str2):
            return False
        
        i = 0
        j = len(self.str1) -1
        result = True

        while i < len(self.str1):
            if self.str1[i] == self.str2[j]:
                i = i + 1
                j = j - 1
                continue
            return False
        
        return result


sol = ValidAnagram("ear", "rae")
sol = ValidAnagram("random", "modnar")
sol = ValidAnagram("kinder", "rednik")
print(sol.execute())