def hafta():
    n=int(input())
    if n<=7:
        if n==1:
            return "Dushanba"
        elif n==2:
            return "Seshanba"
        elif n==3:
            return "Chorshanba"
        elif n==4:
            return "Payshanba"
        elif n==5:
            return "Juma"
        elif n==6:
            return "Shanba"
        elif n==7:
            return "Yakshanba"
    else:
        print("Hafta kunini xato kiritdingiz!")
        return hafta()
print(hafta())