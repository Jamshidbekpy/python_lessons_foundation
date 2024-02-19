"""
name,surname,address kabi listlarga ma'lum odamlar haqidagi ma'lumotlar mos ravishda kiritiladi.
Odamlar soni noma'lum deb qaralsin.Avval ro'yxatlarga mos ravishda insonlarning ma'lumotlarini qo'shamiz.
So'ng shunday search funksiya o'ylab topishimiz kerakki,qidiruvga agar qandaydir parametrni(name,surname,address) kiritsak,aynan shu
parametrdan boshqa, shu insonga ta'luqli boshqa parametrlarni((surname,address),(name,address),(name,surname)) chiqarsin.
"""
#Muallif Jamshidbek
def get_info(search, a):
    b = len(a)//3
    for i in range(len(a)):
        if a[i].lower() == search.lower():
            if i <= b-1:
                print(f"Tabriklaymiz siz ro'yxatda mavjud ismni kiritdingiz.Siz izlagan ushbu {a[i].capitalize()} ismli kishining familiyasi {a[i + b].capitalize()}.Yashash shahri {a[i + 2*b].capitalize()} ")
            elif i > b-1 and i <= b+3:
                print(f"Tabriklaymiz siz ro'yxatda mavjud familiya kiritdingiz.Siz izlagan ushbu {a[i].capitalize()} familiyali kishining ismi {a[i -b].capitalize()}.Yashash shahri {a[i + b].capitalize()} ")
            else:
                print(f"Tabriklaymiz siz ro'yxatda mavjud shaharni kiritdingiz.Siz izlagan ushbu {a[i].capitalize()} shaharda yashovchi kishining ismi {a[i - 2*b].capitalize()}.Familiyasi {a[i - b].capitalize()} ")

name = ["Jonibek", "Shohruh", "Jonibek", "Shohjahon"]
surname = ["Yorqulov", "Xasanov", "Aliyev", "Xasanov"]
address = ["Samarqand", "Buxoro", "Navoiy", "Toshkent"]

search = input("Qidirish uchun parametr(ism,familiya,shahar) kiriting:")
a = name + surname + address
get_info(search, a)

# Muallif Umidjon
# Tartiblanmagan holda ba'zi o'zgartirishlar bilan masala yechimi
# print([f'{name[i].capitalize()} {surname[i].capitalize()} {address[i].capitalize()}dan' for i in range(4) if search.lower() == name[i].lower() or search.lower() == surname[i].lower() or search.lower() == address[i].lower()])
