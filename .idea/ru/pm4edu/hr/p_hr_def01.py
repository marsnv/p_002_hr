"""Набор функций проекта"""
import os
import subprocess
def open_myfile(filename, currentmode):
    """Открывает файл filename в режиме currentmode"""
    #print("OPEN_"+filename+"_mode_"+currentmode+"_")
    myfile = open(r''+filename,currentmode)
    return myfile, filename

def close_myfile(myfile):
    """Закрывает файл myfile"""
    myfile.close()

def read_myfile(myfile):
    """Выводит построчно на экран содержимое файла myfile"""
    line = myfile.readline()
    while line != '':
        print(line)
        line = myfile.readline()

def read_hrfile(myfile):
    print('Т№'
          +' | '+'Ф'
          +' | '+'И'
          +' | '+'О'
          +' | '+'ДР'
          +' | '+'Оклад')
    tab_number = str(myfile.readline())
    while tab_number != '':
        f_staff = myfile.readline()
        n_staff = myfile.readline()
        o_staff = myfile.readline()
        bd_staff = myfile.readline()
        lc_staff = myfile.readline()
        print(tab_number.replace('\n','')
              +' | '+f_staff.replace('\n','')
              +' | '+n_staff.replace('\n','')
              +' | '+o_staff.replace('\n','')
              +' | '+bd_staff.replace('\n','')
              +' | '+lc_staff.replace('\n',''))
        tab_number = str(myfile.readline())

def display_menu_unit():
    """Меню с Отделами, универсально, когда нужно выбрать Отдел"""
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
    """Меню разделов программы"""
    print("*** Разделы: ")
    print("0 - Закончить работу")
    print("1 - Кадровая информация")

def display_menu_hr():
    "Меню для работы с Кадровой информацией выбранного Отдела"
    print("**************************")
    print("0 - Закончить ввод данных")
    print("1 - Вывести данные о сотрудниках текущего отдела")
    print("2 - Добавить сотрудника")
    print("3 - Изменить сотрудника")
    print("4 - Удалить сотрудника")


def open_new_file():
    """Открывает файл указанный пользоваталем, возращает открытый файл и полный его полный путь"""
    myfolder = 'c:/db_files/'
    myfilename = input("Введите имя файла:")
    myfile, myfilename = open_myfile(myfolder+myfilename, 'a')
    return myfile, myfilename

def new_tab_number(myfolder):
    if os.path.exists(myfolder+'hr_tab_numbers.txt') == False:
        tab_number = '1'
    else:
        hr_tab_numbers = open(r''+myfolder+'hr_tab_numbers.txt', 'r')
        tab_number = 1+int(hr_tab_numbers.readline())
        hr_tab_numbers.close()
    hr_tab_numbers = open(r''+myfolder+'hr_tab_numbers.txt', 'w')
    hr_tab_numbers.write(str(tab_number))
    hr_tab_numbers.write("\n")
    hr_tab_numbers.close()
    return tab_number

def add_new_staff(myfile,myfolder):
    """Позволяет добавить нового сотрудника в выбранном отделе"""
    myfile.write(str(new_tab_number(myfolder)))
    myfile.write("\n")
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

def delete_staff(myfile,myfolder,myfilename):
    """Позволяет удулить сотрудники по табельному номеру"""
    tab_number_deleted = str(input("Введите табельный номер удаляемого сотрудника : "))+"\n"
    close_myfile(myfile)
    myfile, myfilename = open_myfile(myfilename, 'r')
    tmp_myfile = open(r''+myfilename+'.tmp','w')
    tab_number = str(myfile.readline())
    while tab_number != '':
        f_staff = myfile.readline()
        n_staff = myfile.readline()
        o_staff = myfile.readline()
        bd_staff = myfile.readline()
        lc_staff = myfile.readline()
        if tab_number != tab_number_deleted:
            tmp_myfile.write(tab_number)
            tmp_myfile.write(f_staff)
            tmp_myfile.write(n_staff)
            tmp_myfile.write(o_staff)
            tmp_myfile.write(bd_staff)
            tmp_myfile.write(lc_staff)
        else:
            print("")
        tab_number = str(myfile.readline())
    tmp_myfile.close()
    close_myfile(myfile)
    os.remove(myfilename)
    os.rename(myfilename+'.tmp',myfilename)
    myfile, myfilename = open_myfile(myfilename, 'a')

def clear():
    """Очищает консоль"""
    if os.name == 'posix':
        #os.system('clear')
        subprocess.call("clear", shell=True)
    elif os.name in ('ce', 'nt', 'dos'):
        #os.system('cls')
        subprocess.call("cls", shell=True)

def work_hr_file(myfile, myfilename,myfolder):
    """Работа с Кадровой информацией выбранного отдела"""
    current_section=9
    while current_section !="0":
        display_menu_hr()
        current_section = input("Введите номер варианта : ")
        if current_section == "0":
            print("Закончили...")
        elif current_section == "1":
            close_myfile(myfile)
            myfile, myfilename = open_myfile(myfilename, 'r')
            read_hrfile(myfile)
            close_myfile(myfile)
            myfile, myfilename = open_myfile(myfilename, 'a')
        elif current_section == "2":
            add_new_staff(myfile,myfolder)
        elif current_section == "4":
            delete_staff(myfile,myfolder,myfilename)
