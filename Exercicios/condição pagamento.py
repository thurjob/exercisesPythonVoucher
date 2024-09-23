v = float(input("Digite o valor do produto: "))
c = float(input("Digite a forma de pagamento 1= pix, 2= uma parcela, 3= duas parcelas, 4 = três parcelas: "))

if c == 1:
    print (f'total a ser pago é {v - v*0.10 }')

else:
    if c == 2:
        print (f'total a ser pago é{v - v*0.05 }')
    
    if c == 3:
        print (f'valor de cada parcela é {v // 2} e o valor total do produto é {v}')
    
    if  c == 4:
        print (f'valor de cada parcela é {((v + v*0.10) / 3):.2f} e o valor total do produto é {v + v*0.10}')