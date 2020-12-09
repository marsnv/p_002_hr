def open_myfile(filename, currentmode):
    #print("OPEN_"+filename+"_mode_"+currentmode+"_")
    myfile = open(r''+filename,currentmode)
    return myfile, filename

def close_myfile(myfile):
    myfile.close()

def read_myfile(myfile):
    line = myfile.readline()
    while line != '':
        print(line)
        line = myfile.readline()

def display_menu_division():
    print("*** Дирекция: ")
    print("1 - Финансовая: ")
    print("2 - Коммерческая: ")

def display_menu_department():
    print("*** Управление: ")
    print("11 - Финансы, Казначейство: ")
    print("12 - Финансы, Бухгалтерия: ")
    print("21 - Коммерция, Продажи: ")
    print("22 - Коммерция, Закупки: ")

def display_menu_unit():
    print("*** Отдел: ")
    print("111 - Финансы, Казначейство, Банк: ")
    print("112 - Финансы, Казначейство, Бюджет: ")
    print("121 - Финансы, Бухгалтерия, Учет: ")
    print("122 - Финансы, Бухгалтерия, Бюджет: ")
    print("211 - Коммерция, Продажи, Представители: ")
    print("212 - Коммерция, Продажи, Отгрузка: ")
    print("221 - Коммерция, Закупки, Менеджеры: ")
    print("222 - Коммерция, Закупки, Хранение: ")
    print("0 - Вернуться к выбору Раздела")


def display_menu_section():
    print("*** Разделы: ")
    print("0 - Закончить работу")
    print("1 - Кадровая информация")

def display_menu_hr():
    print("**************************")
    print("0 - Закончить ввод данных")
    print("1 - Вывести данные о сотрудниках текущего отдела")
    print("2 - Добавить сотрудника")
    print("3 - Изменить сотрудника")
    print("4 - Удалить сотрудника")


def open_new_file():
    myfolder = "c:\myfiles\\"
    myfilename = input("Введите имя файла:")
    myfile, myfilename = open_myfile(myfolder+myfilename, 'a')
    return myfile, myfilename

def clear():
    import os
    import subprocess
    if os.name == 'posix':
        #os.system('clear')
        subprocess.call("clear", shell=True)
    elif os.name in ('ce', 'nt', 'dos'):
        #os.system('cls')
        subprocess.call("cls", shell=True)

def work_hr_file(myfile, myfilename):
    current_section=9
    while current_section !="0":
        display_menu_hr()
        current_section = input("Введите номер варианта : ")
        if current_section == "0":
            print("Закончили...")
        elif current_section == "1":
            close_myfile(myfile)
            myfile, myfilename = open_myfile(myfilename, 'r')
            read_myfile(myfile)
            close_myfile(myfile)
            myfile, myfilename = open_myfile(myfilename, 'a')
        elif current_section == "2":
            myfile.write(input("Введите фамилию нового сотрудника : "))
            myfile.write("\n")
            myfile.write(input("Введите имя нового сотрудника : "))
            myfile.write("\n")
            myfile.write(input("Введите отчество нового сотрудника : "))
            myfile.write("\n")
            myfile.write(input("Введите дату рождения нового сотрудника (дд.мм.гггг) : "))
            myfile.write("\n")
            myfile.write(input("Введите оклад нового сотрудника : "))
            myfile.write("\n")
