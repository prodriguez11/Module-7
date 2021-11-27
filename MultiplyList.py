# multiply each number in the passed list L

def multiply(L):
    total = 1
    for n in L:
        total *= n
    return total
print(multiply((5, 2, 7, -1)))



