# 1st task

print(5*9**0.5)

# 2nd task

a, b = 9.99, 1000
if a > 9.98 and b != 1000.1:
    print(True)

# 3rd task

a, b = 1234 % 1000 // 10, 5678 % 1000 // 10
print(a + b)

# 4th task

a, b = 13.42, 42.13
round_a, round_b = round(a % 1, 2), round(b % 1, 2)
int_a, int_b = int(a), int(b)
if round_b == int_a / 100 or round_a == int_b / 100:
    print(True)
