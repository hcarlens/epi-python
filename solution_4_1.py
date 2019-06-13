

def parity(x):
    parity = 0
    while x:
        # track parity of final bit
        parity ^= (x & 1)

        # shift x
        x >>= 1
    return parity

def parity_64bit(x):
    pass

print(parity(3))