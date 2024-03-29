from re import findall,sub,match

inf_reg = r'Jamshidbek'
tel_reg  = r'\+998\s\d{9}'
txt_reg = r'Oʻzbekiston'
txt_soz = r'[A-Za-z]{1,20}'
login = r'^[A-Z][a-z][A-Za-z0-9_]{5,10}$'
parol = r'^[A-Z][a-z][_@#$%&][A-Za-z0-9_@#$%&]{8,20}$'
txt_inf = 'Mening ismim Jamshidbek.Men INTERNATION school da tahsil olaman.'
with open('uzbekistan.txt',encoding='utf-8') as uzbekistan:
    uzbekistan = uzbekistan.read()
    royxat = findall(txt_reg,uzbekistan)
    royxat2 = findall(txt_soz,uzbekistan)
print('Ushbu uzbekistan.txt faylidagi matnda',len(royxat),'ta Oʻzbekiston','va',len(royxat2),'ta soʻz bor.')
while True:
    l = input('Loginni kiriting: ')
    if match(login,l):
        break
    else:
        print('Loginni yaratimadi!Formatni to\'g\'ri kiriting.')
while True:
    p = input('Parolni kiriting: ')
    if match(parol,p):
        break
    else:
        print('Parolni yaratimadi!Formatni to\'g\'ri kiriting.')        
print('Akkaunt yaratildi: Loginni:',l,'Parol:',p)
with open('tel_nomer.txt',encoding='utf-8') as tel_nomerlar:
    tel_nomerlar = tel_nomerlar.read()
    tel_nomerlar = findall(tel_reg,tel_nomerlar)
    print(tel_nomerlar)
    
reg_inf = sub(inf_reg,'Alimurod',txt_inf)
print(reg_inf)

