# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, 'a+', encoding='utf-8')
    strings_positions = {}
    num_of_str = 1
    for i in strings:
        ft = file.tell()
        strings_positions[f'{num_of_str}, {ft}'] = str(i)
        file.write(str(i) + '\n')
        num_of_str += 1

    #print(file.tell())
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)