list = []
list_out = []
first_string = ''
number = ''
file = open('data.txt', 'r')
string = file.readline()
string_out = ''
while True:
    if string != '':
        list.append(string)
        string = file.readline()
    else:
        break

for work_string in list:
    for eliment in work_string.split():
        for word_eliment in eliment:
            if word_eliment.isalpha() or word_eliment == '(':
                first_string += word_eliment
                continue
            elif word_eliment.isdigit():
                number += word_eliment
                continue
            elif word_eliment == ')':
                numbers = int(number)
                first_string += str(numbers - 1) + ')'
                string_out += first_string
                number = ''
                first_string = ''
                continue
            elif word_eliment == '-':
                string_out += ' ' + '-' + '>' + ' '
                continue
            elif word_eliment[-1] == '.':
                string_out += '....'
                list_out.append(string_out)
                string_out = ''
                break

with open("finish_file.txt", "w") as file:
    for words in list_out:
        file.write(words + '\n')
