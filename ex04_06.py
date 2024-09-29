def computepay(h, r):
    normalHr = 0
    extraHr = 0
    result = 0
    if h>40:
        normalHr = 40
        extraHr = h-40
    else:
        normalHr = h

    return ((normalHr * r) + (extraHr * 1.5 * r))

hrs = input("Enter Hours:")
r = input("Enter Rate:")
p = computepay(float(hrs), float(r))
print("Pay", p)