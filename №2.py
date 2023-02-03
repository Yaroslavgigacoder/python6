lower_cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
upper_cyrillic = [chr(i) for i in range(ord('А'), ord('Я') + 1)]


def encrypt_caesar(msg, shift=3):
    temp = ''
    for i in msg:
        if i in lower_cyrillic:
            ind = lower_cyrillic.index(i)
            temp += lower_cyrillic[ind+shift]
        elif i in upper_cyrillic:
            ind = upper_cyrillic.index(i)
            temp += upper_cyrillic[ind+shift]    
        else: 
            temp += i
    return temp
def decrypt_caesar(msg, shift = 3):
    temp = ''
    for i in msg:
        if i in lower_cyrillic:
            ind = lower_cyrillic.index(i)
            temp += lower_cyrillic[ind-shift]
        elif i in upper_cyrillic:
            ind = upper_cyrillic.index(i)
            temp += upper_cyrillic[ind-shift]    
        else: 
            temp += i
    return temp

print(encrypt_caesar("Да здравствует салат Цезарь!"))    
print(decrypt_caesar("Зг кзугефхецих фгогх Щикгуя!"))