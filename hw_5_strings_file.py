#1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено
# только четное количество таких слов.

def remove_from_3_to_5_ch(my_file):
    """ Function removes from a text file an even number of words
    containing from 3 to 5 characters."""

    with open(my_file) as reader_ex, open('example_new.txt', 'w') as writer_ex:

        for line in reader_ex:
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

            writer_ex.write(f'{line2} \n')

remove_from_3_to_5_ch('example.txt')

#2)Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев,
# фамилии которых начинаются с букв К и С.

def get_phone_CK(my_file):
    """Function creates a new text file that contains telephones
     last names starting with the letters K and C."""

    with open(my_file) as reader_ph, open('phone_num_new.txt', 'w') as writer_ph:
        for line in reader_ph:
            for item in line:
                if item.startswith('C') or item.startswith('K'):
                    writer_ph.write(line)

get_phone_CK('phone_num.txt')

#3) Получить файл, в котором текст выровнен по правому краю путем
# равномерного добавления пробелов.

def get_right_aligned(my_file):
    """Function creates a new text file in which the text is right aligned. """

    with open(my_file) as reader_example, open('example_new_2.txt', 'w') as writer_example:
        file = reader_example.readlines()
        #find the maximum length of lines
        len_line = []
        for line in file:
            len_line.append(len(line))
        max_len = max(len_line)

        for line in file:
            line = line.rstrip('\n')
            writer_example.write(f'{line.rjust(max_len)}\n')

get_right_aligned('example.txt')


#4)Дан текстовый файл со статистикой посещения сайта за неделю.
# Каждая строка содержит ip адрес, время и название дня недели
# (например, 139.18.150.126 23:12:44 sunday). Создайте новый текстовый файл,
# который бы содержал список ip без повторений из первого файла.
# Для каждого ip укажите количество посещений, наиболее популярный день недели.
# Последней строкой в файле добавьте наиболее популярный отрезок времени
# в сутках длиной один час в целом для сайта.

def get_more_from_visit_file(my_file):
    """ Function creates a new text file that contains ip, number of visits,
    most popular day of the week and most popular time"""

    def most_frequent(list_var):
        """ Returns the most frequent value """
        count = {}
        for j in list_var:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
        max_count = max(count, key=count.get)
        return max_count

    with open(my_file) as reader_st:
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

    with open('visit_st_new.txt', 'w') as writer_st:
        for key, value in ip.items():
            if key in ip_day:
                writer_st.write(f'{key}: total visits - {value}, most popular day - {most_frequent(ip_day[key])} \n')
        writer_st.write(f'Most popular time from {most_frequent(time)} to {int(most_frequent(time)) + 1} ')

get_more_from_visit_file('visit_st.txt')
