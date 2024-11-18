# Игра на угадывание числа

start = 1
finish = 100
count = 0
variant = ''

print("Загадайте число от 1 до 100")
while variant != '1':
    number = int((start + finish) / 2)
    count += 1
    print(f"Попытка № {count}.")
    print(f"Это число {number} ?")
    print(" Если да, введите 1")
    print(" Eсли ваше число больше, введите 2")
    print(" Если ваше число меньше, введите 3")
    variant = input()
    match variant:
        case '1':
            print(" Ура, я угадал!\n С тебя шоколадка и можно выходить :)")
            exit()
        case '2':
            start = number
        case '3':
            finish = number
