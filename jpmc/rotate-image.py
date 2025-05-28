import numpy as np
class RotateImage:

    def __init__(self, input : list[list[int]]):
        self.input = input

    
    def execute(self):

        if len(self.input) != len(self.input[0]):
            print("not a square matrix!!")
            return self.input
        
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                temp = self.input[i][j]
                rand = len(self.input[0]) - i -1
                self.input[i][j] = self.input[j][rand]
                self.input[j][rand] = temp

        return self.input
    
    def clean(self):
        inputTrans = np.transpose(self.input)
        inputTrans = inputTrans.tolist()
        for row in inputTrans:
            row.reverse()
        return inputTrans   
    

input = [[1,2,3],[4,5,6],[7,8,9]]
print(input)
sol = RotateImage(input)
##print(sol.execute())

print(sol.clean())


        