def Unknown(x, y):
    if x < y:
        print(x+y)
        return (Unknown(x+1,y)*2)
    elif x == y:
        return 1
    else:
        print(x+y)
        return (Unknown(x-1, y)//2)
'''print("RECURSIVE")
print(f"x = 10, y = 15")
print(Unknown(10, 15))
print("")
print(f"x = 10, y = 10")
print(Unknown(10, 10))
print("")
print(f"x = 15, y = 10")
print(Unknown(15, 10))'''

def IterativeUnknown(x, y):
    total = 1
    while (x != y):
        print(x + y)
        if x < y:
            x += 1
            total *= 2
        else:
            x -= 1
            total //= 2
    return total

'''print("ITERATIVE")
print(f"x = 10, y = 15")
print(IterativeUnknown(10, 15))
print("")
print(f"x = 10, y = 10")
print(IterativeUnknown(10, 10))
print("")
print(f"x = 15, y = 10")
print(IterativeUnknown(15, 10))'''

