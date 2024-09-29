largest = None
smallest = None
inputs = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        inputs.append(float(num))
    except:
        print("Invalid input")
    

inputs.sort()
print("Maximum is " +  str(int(inputs[len(inputs) - 1])))
print("Minimum is " + str(int(inputs[0])))