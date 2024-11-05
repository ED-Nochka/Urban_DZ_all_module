def password(n):
    pass_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
print('Для сверки пароля: ')
for i in range(3, 21):
    result = password(i)
    print(f"{i} - {result}")

n = int(input('Введите число от 3 до 20: '))
result = password(n)
print(f'Верный пароль: ', result)