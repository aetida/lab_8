import random
import logging

logging.basicConfig(filename = "base_log.log", level=logging.INFO)

while True: #цикл обработки ввода количества бочонков
    try:
        num = int (input("Введите число больше 1:"))
        if num <= 0:
            print('неверный ввод\nповторите попытку')
        else:
            logging.info(f'количество бочонков:  {num}') #передача информации о количестве в log-файл
            break
    
    except ValueError:
        print('Неверный ввод\nповторите попытку')

num_list = [i+1 for i in range(num)] # заполнение списка номеров 

random.shuffle(num_list) # перемешивание номеров в списке 


for i in range(num): # цикл вывода номеров по одному
    input('нажмите Enter для вывода следующего числа ')
    logging.info("кнопка нажата") # передеча информации о нажатии на кнопку в log-файл
    print(num_list[i])
    logging.info(f"получено число: {num_list[i]}") # передеча информации о выпавшем числе в log-файл

logging.info("программа завершена")
