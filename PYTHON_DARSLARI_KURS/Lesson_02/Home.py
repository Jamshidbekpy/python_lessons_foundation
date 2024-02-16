#string
variable=" Jamshidbek TATU talabasi "

print(variable.title())
print(variable.capitalize())
print(variable.upper())
print(variable.lower())

print(len(variable))

print(variable.strip())
print(variable.lstrip())
print(variable.rstrip())

print(variable.find("'t"))
print(variable.find('t',17))
print(variable.find('T',12,15))

print(variable.index('a'))

print(variable.replace('Jamshidbek','Alimurod'))
print(variable.replace('a','l',2))

#True False
print(variable.startswith('Jamshidbek'))
print(variable.endswith('talabasi'))
print(variable.istitle())
print(variable.isdigit())
print(variable.isupper())
print(variable.islower())
print(variable.isalpha())
print(variable.isalnum())
print(variable.isspace())

print(variable.split())
print(variable.rsplit())
print(variable.split("T"))
print(variable.split("T",1))

print('20 yosh '.join(variable))

print(variable.center(len(variable)+12))     #Ikki tomoniga 6 tadan belgi qo'shadi
print(variable.center(len(variable)+12), '*')
print(variable.ljust(len(variable)+12,'*'))
print(variable.rjust(len(variable)+12,'*'))

print(dir(variable))      #dunder metodlar

print(variable.zfill(35))


variable2= "Alimurod ICT Akademiyasi talabasi "

print(variable2.title())
print(variable2.capitalize())
print(variable2.upper())
print(variable2.lower())

print(len(variable2))

print(variable2.strip())
print(variable2.lstrip())
print(variable2.rstrip())

print(variable2.find("'t"))
print(variable2.find('t',17))
print(variable2.find('T',12,15))

print(variable2.index('a'))

print(variable2.replace('Jamshidbek','Alimurod'))
print(variable2.replace('a','l',2))

#True False
print(variable2.startswith('Jamshidbek'))
print(variable2.endswith('talabasi'))
print(variable2.istitle())
print(variable2.isdigit())
print(variable2.isupper())
print(variable2.islower())
print(variable2.isalpha())
print(variable2.isalnum())
print(variable2.isspace())

print(variable2.split())
print(variable2.rsplit())
print(variable2.split("T"))
print(variable2.split("T",1))

print('20 yosh '.join(variable2))

print(variable2.center(len(variable)+12))     #Ikki tomoniga 6 tadan belgi qo'shadi
print(variable2.center(len(variable)+12), '*')
print(variable2.ljust(len(variable)+12,'*'))
print(variable2.rjust(len(variable)+12,'*'))

print(dir(variable2))      #dunder metodlar

print(variable2.zfill(35))





