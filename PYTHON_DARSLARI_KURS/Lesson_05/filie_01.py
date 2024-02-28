# from colorama import init, Fore, Back
# init(autoreset=True)
from datetime import datetime

database = {
    "ICHIMLIKLAR": {
        "Cola": {
            "Miqdori:": 50,
            "Narxi:": 15000,
            "Kelgan sanasi:": datetime(2024, 11, 3),
            "Yaroqlilik muddati KK.OO.YY:": datetime(2026, 5, 10),
            "Ishlab chiqarilgan mamlakati": "Uzbekiston"
        },
        "Pepsi": {
            "Miqdori:": 50,
            "Narxi:": 13000,
            "Kelgan sanasi:": datetime(2024, 11, 12),
            "Yaroqlilik muddati KK.OO.YY:": datetime(2026, 7, 23),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
    },
    "OZIQ-OVQAT": {
        "Non": {
            "Miqdori:": 50,
            "Narxi:": 1500,
            "Kelgan sanasi:": datetime(2024, 11, 7),
            "Yaroqlilik muddati KK.OO.YY:": datetime(2026, 8, 23),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
        "Yog": {
            "Miqdori:": 50,
            "Narxi:": 20000,
            "Kelgan sanasi:": datetime(2024, 11, 5),
            "Yaroqlilik muddati KK.OO.YY:": datetime(2026, 12, 23),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
    }
}
database1 = {}
database2 = {}
database3 = {}
list_select = ["ICHIMLIKLAR", "OZIQ-OVQAT"]

list_select_value_key_key = ["Miqdori:", "Narxi:", "Kelgan sanasi:", "Yaroqlilik muddati KK.OO.YY:", "Ishlab chiqarilgan mamlakati:"]
list_select_value_key = []
select_page_list = ["Add_product", "Sell_product", "Database", "Report"]
add_database = {}
while True:
    for i in select_page_list:
        print("",select_page_list.index(i)+1, i.lstrip())
    select_page = input("Yuqoridagi bo'limlardan birini tanlang 1/2/3/4/0:").strip()
    #_________________________________________________________________FINISH PROGRAMM_____________________________________________________
    if select_page == "0":
        print("DASTUR MUOFFAQQIYATLI YAKUNLANDI!".center(130))
        break
    #____________________________________________________________________ADD BOLIMI__________________________________________________________
    elif select_page == "1":
        while True:
            print(0, "CHIQISH")
            for i in range(len(list_select)):
                print(str(i+1), list_select[i])
            add_database_key = input("MAHSULOT TURKUMINI KIRITING 1/2/0:").strip()
            if add_database_key == "0":
                break
            if add_database_key.isdigit() and int(add_database_key) > 0 and int(add_database_key) < 3:
                add_database_key = list_select[int(add_database_key)-1]                           # add_database_key = "ICHIMLIKLAR" kirmagan holat no
                for key, value in database[add_database_key].items():
                    list_select_value_key.append(key)
                    
                print(0, "CHIQISH")
                for element in list_select_value_key:
                    print(list_select_value_key.index(element)+1, element)
                    
                add_database_value_key = input("Mahsulot nomerini kiriting:").capitalize().strip()
                
                if int(add_database_value_key) > 0 and int(add_database_value_key) < len(list_select_value_key):
                    
                    add_database_value_key = list_select_value_key[int(add_database_value_key)-1]
                    
                    #/////////////////////////////////////////////////////////////////////////////////////////
                if add_database_value_key in database[add_database_key]:                          # Berilgan Turkumni ichida bo'lsa
                    while True:
                        date_year = input("Yaroqlilik yili:")
                        if date_year.isdigit():
                            date_year = int(date_year)
                            break
                        else:
                            print("Yilni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")
                    if date_year < 2024:
                        print("Ushbu mahsulotning muddati o'tgan!Kechirasiz bazaga qo'sha olmaymiz!")
                        break
                    while True:
                        date_moth = input("Yaroqlilik oyi:")
                        if date_moth.isdigit() and int(date_moth) <= 12 and int(date_moth) > 0:
                            date_moth = int(date_moth)
                            break
                        else:
                            print("Oyni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")
                    while True:
                        date_day = input("Yaroqlilik kunini kiriting:")
                        if date_day.isdigit() and int(date_moth) > 0 and ((int(date_day) <= 31 and (date_moth % 2 == 1 and date_moth <= 7) or (date_moth % 2 == 0 and date_moth > 7)) or (int(date_day) <= 30 and (date_moth % 2 == 0 and date_moth <= 7 and date_moth != 2) or (date_moth % 2 == 1 and date_moth > 7)) or (date_year % 4 != 0 and int(date_day) <= 28 and date_moth == 2) or (date_year % 4 == 0 and int(date_day) <= 29 and date_moth == 2)):
                            date_day = int(date_moth)
                            break

                        else:
                            print("Kunni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")

                    add_database_value_key_value4 = datetime(date_year, date_moth, date_day)           #Yaroqlilik muddati

                    while True:
                        add_database_value_key_value1 = input(list_select_value_key_key[0])       #Miqdori
                        add_database_value_key_value2 = input(list_select_value_key_key[1])        #Narxi
                        if add_database_value_key_value1.isdigit() and int(add_database_value_key_value1) > 0 and add_database_value_key_value2.isdigit() and int(add_database_value_key_value2) > 0:
                            add_database_value_key_value1 = int(add_database_value_key_value1)
                            add_database_value_key_value2 = int(add_database_value_key_value2)
                            break
                        else:
                            print("Miqdori yoki narxini kiritishda xatolikka yo'l qo'ydingiz!")

                    add_database_value_key_value3 = datetime.now()                                #Kelgan sanasi

                    add_database_value_key_value5 = input(list_select_value_key_key[4])           #Mamlakati
                    database1[list_select_value_key_key[0]] = add_database_value_key_value1       # Miqdori
                    database1[list_select_value_key_key[1]] = add_database_value_key_value2       # Narxi
                    database1[list_select_value_key_key[2]] = add_database_value_key_value3       # Kelgan sanasi
                    database1[list_select_value_key_key[3]] = add_database_value_key_value4       # Yroqlilik muddati
                    database1[list_select_value_key_key[4]] = add_database_value_key_value5       # Ishlab chiqarilgan mamlakati
                    database2[add_database_value_key] = database1
                    print(database2)

                
                
                
                else:                                                                             # Berilgan Turkumni ichida bo'lmasa
                    pass
            else:
                print("TURKUMNI XATO TANLADINGIZ!ILTIMOS BOSHQATDAN TANLANG!")   
            
                
        


# sell_data = {
#     "ichimliklar" : {
#         "kola" : [
#             {
#                 "moqdori" : 10,
#                 "price" : 150000+5%,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 4,
#                 "price" : 150000+5%,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 2,
#                 "price" : 150000+5%,
#                 "date" :  "26.12.2024",
#             }
#         ],
#         "pepsi" : [
#             {
#                 "moqdori" : 10,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 4,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 2,
#                 "date" :  "26.12.2024",
#             }
#         ]
#     }
# }


# add_data = {
#     "ichimliklar" : {
#         "kola" : [
#             {
#                 "moqdori" : 10,
#                 "price" : 150000,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 4,
#                 "price" : 150000,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 2,
#                 "price" : 150000,
#                 "date" :  "26.12.2024",
#             }
#         ],
#         "pepsi" : [
#             {
#                 "moqdori" : 10,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 4,
#                 "date" :  "26.12.2024",
#             },
#             {
#                 "moqdori" : 2,
#                 "date" :  "26.12.2024",
#             }
#         ]
#     }
# }






