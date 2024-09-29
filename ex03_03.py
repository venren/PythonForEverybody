score = input("Enter Score: ")
score = float(score)
if score > 1.0 or score < 0.0:
    print("Score should be between 0.0 to 1.0")
    exit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("E")