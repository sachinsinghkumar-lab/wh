print("BITWISE SWAP CHALLENGE\n")

a = 10
b = 20

print("Part 1: Swap Without Third Variable")
print("Before:", a, b)

a = a + b
b = a - b
a = a - b

print("After :", a, b)

x = 15
y = 25

print("\nPart 2: XOR Swap")
print("Before:", x, y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After :", x, y)

num = 5

print("\nPart 3: Left Shift")
print(num, "<< 1 =", num << 1)
print(num, "<< 2 =", num << 2)
print(num, "<< 3 =", num << 3)

n1 = -8
n2 = 6

print("\nPart 4: Sign Detection")

if (n1 < 0) ^ (n2 < 0):
    print("Different signs")
else:
    print("Same signs")

dividend = 17
divisor = 4

quotient = 0
remainder = dividend

while remainder >= divisor:
    remainder -= divisor
    quotient += 1

print("\npart 5: Divide Without /")
print("Quotient =", quotient)
print("Remainder =", remainder)
