number = int(input("Введите целое число: "))
val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
roman_num = ""
i = 0
while number > 0:
    for j in range(number // val[i]):
        roman_num += syms[i]
        number -= val[i]
    i += 1
    

print("Римское представление:"+ str(roman_num)) 