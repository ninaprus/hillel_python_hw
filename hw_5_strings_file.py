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


#3) Получить файл, в котором текст выровнен по правому краю путем
# равномерного добавления пробелов.

with open('example.txt') as reader2:
    file = reader2.readlines()
    #find the maximum length of lines
    len_line = []
    for line in file:
        len_line.append(len(line))
    max_len = max(len_line)

    for line in file:
        line = line.rstrip('\n')
        print(line.rjust(max_len))

#4)Дан текстовый файл со статистикой посещения сайта за неделю.
# Каждая строка содержит ip адрес, время и название дня недели
# (например, 139.18.150.126 23:12:44 sunday). Создайте новый текстовый файл,
# который бы содержал список ip без повторений из первого файла.
# Для каждого ip укажите количество посещений, наиболее популярный день недели.
# Последней строкой в файле добавьте наиболее популярный отрезок времени
# в сутках длиной один час в целом для сайта.

def most_frequent(list_var):
    """ Returns the most frequent value """
    count = {}
    for j in list_var:
        if j in count.keys():
            count[j] += 1
        else:
            count[j] = 1
    max_count = max(count, key=count.get)
    return max_count

with open('visit_st.txt', 'r') as reader_st:
    file = reader_st.readlines()

    ip = {}
    ip_day = {}
    time = []
    for line in file:
        line = line.split()
        time.append(line[1][0:2]) # only hours without minutes and seconds
        # ip{}
        if line[0] not in ip:
            ip[line[0]] = 1
        else:
            ip[line[0]] += 1
        #ip_day{}
        if line[0] not in ip_day:
            ip_day[line[0]] = []
            ip_day[line[0]].append(line[2])
        else:
            ip_day[line[0]].append(line[2])

with open('st_new.txt', 'w') as writer_st:
    for key, value in ip.items():
        if key in ip_day:
            writer_st.write(f'{key}: total visits - {value}, most popular day - {most_frequent(ip_day[key])} \n')
    writer_st.write(f'Most popular time from {most_frequent(time)} to {int(most_frequent(time)) + 1} ')
