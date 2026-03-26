n = int(input("Enter a number: "))
number = n 
# Even / Odd check
if n & 1 == 0:
    print("Even")
else:
    print("Odd")

# Binary Palindrome check
ori = n
rev = 0

while n > 0:
    digit = n & 1
    rev = (rev << 1) | digit
    n = n >> 1

if rev == ori:
    print("Binary Palindrome")
else:
    print("Not Binary Palindrome")


print("-COVERSIONS VERSION")
binary = bin(number)
print("This is the binary version", binary)
print(format(number, '032b')) 
print(format(number, '032F'))

#use 32F for decimal and 32b for binary :)


#the temp code 

word = int(input("Enter a number: "))

key = 2   # fixed shift

# Encrypt
enc = word << key
print("Encrypted:", enc)

# Decrypt
dec = enc >> key
print("Decrypted:", dec)


#program to count a fact
fac = 1 


#this is the code for finding factorials and all using the bitwise operators 

w = int(input("Enter the number for which u want to find the factorial for: "))

def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b # Common set bits
        a = a ^ b          # Sum of bits where at least one is not set
        b = carry << 1     # Carry is shifted left
    return a 
def bitwise_multiply(x, y):
    result = 0 
    while y > 0:
        if y & 1:
            result = bitwise_add(result, x)
        x <<= 1
        y >> 1
    return result

def bitwise_factorial(n)
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(2, n+1)
        res = bitwise_multiply(res, i)
    return res  

#lets check out fac :)
print(bitwise_factorial(5))