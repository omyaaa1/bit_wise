#this is a simple impementation of calc using with using bitwise calculations.

def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def bitwise_sub(a, b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

def bitwise_multiply(a, b):
    res = 0
    while b > 0:
        if b & 1:
            res = bitwise_add(res, a)
        a <<= 1
        b >>= 1
    return res

def bitwise_div(a, b):
    c = 0
    for i in range(31, -1, -1):
        if (b << i) <= a:
            a = bitwise_sub(a, b << i)
            c |= (1 << i)
    return c
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int

print(bitwise_add(a,b))
print(bitwise_sub(a,b))
print(bitwise_multiply(a,b))
print(bitwise_div(a,b))



## this is the classic application of bit theory.
#glad if you till now.. make sure to star the repo.
