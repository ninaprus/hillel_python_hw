#1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено
# только четное количество таких слов.

with open('example.txt') as reader:
    file = reader.readlines()

    for line in file:
        line = line.rstrip('.\n')
        line = line.split()
        len_3_5 = []
        counter = 0
        for item in line:
            if 3 <= len(item) <= 5:
                counter += 1
                len_3_5.append(item)
        #parity check
        if counter%2 == 0:
            line2 = ' '.join([item for item in line if item not in len_3_5])
        else:
            line2 = ' '.join([item for item in line if item not in len_3_5[0:-1]])

        print(f'{line2}')

#2)Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев,
# фамилии которых начинаются с букв К и С.

with open('phone_num.txt', 'r') as reader_ph, open('phone_num_new.txt', 'w') as writer_ph:
    for line in reader_ph:
        for item in line:
            if item.isalpha():
                if item.startswith('C') or item.startswith('K'):
                    writer_ph.write(line)