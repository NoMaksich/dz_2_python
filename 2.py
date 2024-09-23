a = int(input("Введите число: "))

alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
result = str()

is_negative = a < 0
a = abs(a)

if a == 0:
    result = "0" 
else:
    while a:
        b=a%16
        a= a//16
        result = str(alphabet[b]) + result
    
if is_negative:
    result = "-" + result
    
print(result)