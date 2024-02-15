#### string

matn = "saLom DunYo     dunyo"

# print(matn.title())
# print(matn.capitalize())


# print(matn.upper())
# print(matn.lower())

# print(len(matn))
# a = matn.strip()
# print(a)
# print(len(a))

# print(matn + 'new')
# print(matn.strip() + 'new')
# print(matn.rstrip() + 'new')
# print(matn.lstrip() + 'new')




# print(matn.find('dunyo'))
# print(matn.find('o', 4, 9))
# print(matn.find('o', 11))

# print(matn.index('w'))

matn = "salom DunYo  salom   dunyo, salom"

# print(matn.replace('salom', 'xayr'))
# print(matn.replace('salom', 'xayr',2))


# print(matn.startswith('saLom'))
# print(matn.endswith('dunyo'))

new = 'Salom Dunyo'
# print(new.istitle())
# print('HELLO WORLaD '.isupper())
# print('salom A'.islower())

m = '123a'
n = 'assd'
w = 'qweqr1234'
# print(m.isdigit())
# # n = int(m)
# # print(type(n))

# print(n.isalpha())

# print(w.isalnum())


new = 'Salom Dunyo. Salom Hayot'
# n = new.split('o')
# n = new.split()
# n = new.split(' ', 1)
# print(n)

new_s = ['Salom', 'Dunyo.', 'Salom', 'Hayot']


# yangi_l = ' '.join(new_s)
yangi_l = ' | '.join(new_s)
# print(yangi_l)

d = 'salom dunyo'
# print(d)
# print(d[4]) # index
# print(d[2:5])  # start, end-1
# print(d[2:9:2])  # start, end-1, step

# print(d[3:])
# print(d[:5])
# y = d
# print(d[::3])

print(d[::-1])



o = "salom salom salom salom salom"
s = "salom"
h = s.center(len(o))
print(o)
# print(h)
# print(len(h))
# print(len(o))
print(s.center(len(o)))
print(s.ljust(len(o))+'o')
print(s.rjust(len(o)))
# print(s.center(len(o), '*'))


# print(dir(123))
# print(dir(s))


# s = '_'
# # print(s.zfill(4))

# b = s.isidentifier()
# print(b)



