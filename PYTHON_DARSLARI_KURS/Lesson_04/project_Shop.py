# """
#                                            Database bo'limi
# """
database = {
    "Drinks (piece)": {
        "Kola": 142, "Pepsi": 154, "Fanta": 145, "Sayhun": 214, "Smile": 124
    },
    "Vegetables (kg)": {
        "Carrot": 1548.6, "Potatoes": 2156.2, "Onion": 1254.4, "Eggplant": 125
    },
    "Cereal-products (kg)": {
        "Rice": 4587, "Wheat": 3254.4, "Peas": 968, "Mosh": 658, "Bean": 859.2, "Corn": 1454
    },
    "Fruits (kg)": {
        "Banana": 125, "Apple": 457.7, "Apelsin": 786, "Apricot": 456
    },
    "Snacks (piece)": {
        "Chips": 300, "Chocolate": 500, "Candy": 700
    },
    "Dairy-products (kg)": {
        "Milk": 2000, "Cheese": 300, "Yogurt": 500
    },
    "Bakery-products (piece)": {
        "Bread": 200, "Croissant": 150, "Bagel": 100
    },
    "Meat (kg)": {
        "Beef": 500, "Chicken": 800, "Pork": 300
    },
    "Frozen-food (kg)": {
        "Fish": 400, "Shrimp": 600, "Pizza": 200
    },
    "Condiments (piece)": {
        "Salt": 500, "Pepper": 300, "Ketchup": 400
    },
    "Cleaning-products (piece)": {
        "Soap": 200, "Detergent": 300, "Bleach": 150
    }
}



add_or_sold = input("Mahsulot qo'shmoqchimisiz yoki sotmoqchimisiz: +/-:")


# """
#                                           Add_Product bo'limi
# """
if add_or_sold == "+":
    while True:
        add_product_key = input("Add product (Oilasi) /no:")
        if add_product_key != "no":
            if not (add_product_key in database):
                add_product_value = {}
                while True:
                    add_product_value_key = input("Add product name (nomi) /no:")
                    if add_product_value_key != "no":
                        if not (add_product_value_key in add_product_value):
                            add_product_value_value = int(input("Add_Miqdori:"))
                            add_product_value[add_product_value_key] = add_product_value_value
                        else:
                            add_product_value_value = int(input("Add_Miqdori:"))
                            add_product_value[add_product_value_key] += add_product_value_value
                    else:
                        break
                database[add_product_key] = add_product_value
            else:
                add_product_value_key = input("Add product name (nomi) /no:")
                if add_product_value_key != "no":
                    if not add_product_value_key in database[add_product_key]:
                        database[add_product_key][add_product_value_key] = int(input("Add_Miqdori:"))
                    else:
                        database[add_product_key][add_product_value_key] += int(input("Add_Midori:"))
        else:
            break

# """
#                                           Sold Product bo'limi
# """
elif add_or_sold == "-":
    while True:
        sold_product_key = input("Sold product (Oilasi) /no:")
        if sold_product_key != "no":
            if not(sold_product_key in database):
                print("Bizda bunday mahsulot yo'q edi!Istasangiz buyurma qilishingiz mumkin!")
                #Buyurtma bo'limiga yuboriladi
            else:
                # while True:
                sold_product_value = database[sold_product_key]
                sold_product_value_key = input("Sold product name (nomi) /n:")
                if not(sold_product_value_key in sold_product_value):
                    print("Bizda bunday mahsulot yo'q edi!Istasangiz buyurma qilishingiz mumkin!")
                    # Buyurtma bo'limiga yuboriladi
                else:
                    while True:
                        sold_product_value_value = int(input("Sold_Miqdori:"))

                        if database[sold_product_key][sold_product_value_key] >= sold_product_value_value:
                            database[sold_product_key][sold_product_value_key] -= sold_product_value_value
                            break
                        else:
                            print("Kechirasiz bizda ushbu mahsulot sizga kerakli miqdordan kam!Hohlasangiz kamroq oling.Olmasangiz 0 ni kiriting!")
        else:
            break
print(database)
# """
#                                                Buyurtma bo'limi
# """

# """
#                                                 Report bo'limi
# """



