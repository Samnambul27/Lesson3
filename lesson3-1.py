def mu_f(num_1 = int(input('Введите число 1: ')), num_2 = int(input('Введите число 2: '))):
    if num_2 == 0:
        print('Ошибка, на 0 делить нельзя')
    mu_f = num_1 / num_2
    return mu_f
print(mu_f())