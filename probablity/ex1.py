
from typing import List

result = []

def recursion(targetSum: int, numberOfDice: int, currentSum: int, sum: List[int]):
    if(currentSum == targetSum):
        result.append(sum)
        return sum
    
    if len(sum) >= numberOfDice:
        return None
    
    for i in range(1,7):
        runningSum = currentSum + i
        if(runningSum <= targetSum):
            temp = sum.copy()
            temp.append(i)
            recursion(targetSum, numberOfDice, runningSum, temp)
    
    return None


recursion(22, 4, 0, [])   
print(result)