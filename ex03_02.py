hrs = input("Enter the number of hours:")
rate = input("Enter rate per hour:")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error: Print hrs and rate in number format.")
result = hrs * rate
print(result)