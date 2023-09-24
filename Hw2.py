# def to_hex(num: int) -> str:
#     alphabet = '0123456789abcdef'
#     result = ''
#     while num != 0:
#         index = num % 16
#         num //= 16
#         result = alphabet[index] + result
#     return result

# user_num = int(input('Введите число: '))

# print(to_hex(user_num))







# def process_fractions(frac1_str, frac2_str):
#     num1, denom1 = map(int, frac1_str.split("/"))
#     num2, denom2 = map(int, frac2_str.split("/"))

#     sum_frac_num = num1 * denom2 + num2 * denom1
#     sum_frac_denom = denom1 * denom2
#     sum_frac = (sum_frac_num, sum_frac_denom)

#     prod_frac_num = num1 * num2
#     prod_frac_denom = denom1 * denom2
#     prod_frac = (prod_frac_num, prod_frac_denom)

#     return sum_frac, prod_frac

# frac1_str = input('Первая дробь вида “a/b”: ')
# frac2_str = input('Вторая дробь вида “a/b”: ')

# sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

# print(f"Сумма дробей = {sum_frac[0]}/{sum_frac[1]}")
# print(f"Произведение дробей = {prod_frac[0]}/{prod_frac[1]}")

