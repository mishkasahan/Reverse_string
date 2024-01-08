def reverse_string(stroka:str):
    a = len(stroka)
    if a == 1:
        return stroka[0]
    else:
        a -= 1
        return stroka[-1] + reverse_string(stroka[:-1:])


print(reverse_string("Hello")) # olleH