print("POWER CHECK CHALLENGE\n")

n = 16

print("Step 1: n & (n - 1) Trick")
print("n =", n, "->", bin(n))
print("n - 1 =", n - 1, "->", bin(n - 1))
print("n & (n - 1) =", n & (n - 1))


def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0


print("\nStep 2: Power of 2")
print("16:", is_power_of_2(16))
print("18:", is_power_of_2(18))


def is_power_of_4(n):
    if not is_power_of_2(n):
        return False

    pos = 0
    while n > 1:
        n >>= 1
        pos += 1

    return pos % 2 == 0


print("\nStep 3: Power of 4")
print("16:", is_power_of_4(16))
print("8 :", is_power_of_4(8))


def is_power_of_8(n):
    if not is_power_of_2(n):
        return False

    pos = 0
    while n > 1:
        n >>= 1
        pos += 1

    return pos % 3 == 0


print("\nStep 4: Power of 8")
print("8 :", is_power_of_8(8))
print("16:", is_power_of_8(16))


def binary_power(base, exp):
    result = 1

    while exp > 0:
        if exp & 1:
            result *= base

        base *= base
        exp >>= 1

    return result


print("\nStep 5: Binary Exponentiation")
print("2^5 =", binary_power(2, 5))
print("3^4 =", binary_power(3, 4))

print("\nStep 6: Testing Numbers")

for num in [1, 2, 4, 8, 16, 32]:
    print(
        num,
        "Power of 2:", is_power_of_2(num),
        "Power of 4:", is_power_of_4(num),
        "Power of 8:", is_power_of_8(num)
    )
