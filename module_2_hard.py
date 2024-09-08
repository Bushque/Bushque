def password_(n):
    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
            print(pairs)

    result = ""

    for pair in pairs:
        sum_pair = sum(pair)
        if n % sum_pair == 0:
            result += f"{pair[0]}{pair[1]}"
            print(result)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = password_(n)
    print(f"Пароль: {password}")
else:
    print("Число не от 3 до 20.")
