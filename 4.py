from fractions import Fraction

fraction1 = input("Введите первую дробь (формат a/b): ")
fraction2 = input("Введите вторую дробь (формат a/b): ")

frac1 = Fraction(fraction1)
frac2 = Fraction(fraction2)
    
sum_result = frac1 + frac2
product_result = frac1 * frac2
    
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)