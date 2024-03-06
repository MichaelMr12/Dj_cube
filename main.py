import sys

# # считывание списка из входного потока
# lst_in = ['Муму','Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
# i = 0
# # здесь продолжайте программу (используйте список lst_in)
# while i<len(lst_in):
#     if ' ' in lst_in[i]:
#         del lst_in[i]
#     i+=1
# print(*lst_in)
def move(string):
    for i in range(len(string) - 1, 0, -1):
        if string[i] == '1' and string[i - 1] == '0':
            string = list(string)
            string[i], string[i - 1] = '0', '1'
            string = ''.join(string)

            rzero = False
            string = string[:i] + ('1' * string[i:].count('1')).rjust(10 - i, '0')
            break
    return string


a = "0000011111"
print(a)
while a != "1111100000":
    a = move(a)
    print(a)