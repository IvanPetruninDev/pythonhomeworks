weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
z = 0
changed_weather_list = []

for elem in weather_list:
    is_number = False
    if elem.isnumeric():
        new_elem = f'{int(elem):02}'
        is_number = True
    elif elem[0] in ['-', '+'] and elem[1:].isnumeric():
        new_elem = f'{elem[0]}{int(elem[1:]):02}'
        is_number = True
    if is_number:
        changed_weather_list.append('"')
        changed_weather_list.append(new_elem)
        changed_weather_list.append('"')
    else:
        changed_weather_list.append(elem)

    print(changed_weather_list)




