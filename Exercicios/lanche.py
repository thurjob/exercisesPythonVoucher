l = float(input("Selecione o lanche: "))
b= float(input("Selecione a bebida: "))

if l == 100:
    v = 11.20
elif l == 101:
    v = 8.30
elif l == 102:
    v = 11.50
elif l == 103:
    v = 16.20

if b == 201:
    v += 6.00
elif b == 202:
    v += 7.50
elif b == 203:
    v += 4.70
    
print(f"O valor a pagar é {v}")
