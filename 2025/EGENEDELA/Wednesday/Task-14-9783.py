from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:22]

for x in alph:
    num1 = int(f'18{x}89957', 22)
    num2 = int(f'80{x}33', 22)
    num3 = int(f'521{x}6', 22)
    summ = num1 + num2 + num3
    if summ % 21 == 0:
        print(summ // 21)
        break