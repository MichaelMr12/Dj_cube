import sys

# считывание списка из входного потока
lst_in = ['Муму','Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
i = 0 
# здесь продолжайте программу (используйте список lst_in)
while i<len(lst_in):
    if ' ' in lst_in[i]:
        del lst_in[i]
    i+=1
print(*lst_in)