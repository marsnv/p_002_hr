"""Основной модуль программы"""
import p_hr_def01
#import p_hr_def02

def main():
    """Основная процедура программы"""
    myfolder = 'c:/db_files/'
    current_section=9
    while current_section !="0":
        #clear()
        p_hr_def01.display_menu_section()
        current_section = input("С каким разделом работать? : ")
        if current_section == "0":
            print("Закончили...")
        elif current_section == "1":
            print("Работаем с Кадрами")
            current_unit = 9
            while current_unit !="0":
                p_hr_def01.display_menu_unit()
                current_unit = input("Введите код отдела с которым будем работать: ")
                if current_unit == "0":
                    print("Закончили...")
                elif current_unit != "0":
                    myfilename = "hr_"+str(current_unit)+".txt"
                    myfile, myfilename = p_hr_def01.open_myfile(myfolder+myfilename, 'a')
                    p_hr_def01.work_hr_file(myfile, myfilename)
        else:
            print("*-*")
print(locals())
main()
