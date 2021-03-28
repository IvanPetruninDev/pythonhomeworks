employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for elem in employees:
    words = elem.split(' ')
    name = words[-1]
    print(f'Привет, {name.capitalize()}!')
