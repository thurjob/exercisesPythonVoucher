n = input("Digite um numero menor que 1000 ")

if(int(n) > 1000):
    print("Numero invalido")
else:
    if(int(n) >= 100):
        cent = int(n[0])
        deze = int(n[1])
        uni = int(n[2])
        centTxt = "centenas"
        dezeTxt = "Dezenas"
        uniTxt = "Unidades"

        if(cent == 1):
            centTxt = "Centena"
        if(deze == 1):
            dezeTxt = "Dezena"
        if(uni == 1):
            uniTxt = "Unidade"
        
        print(f"{n} = {cent} {centTxt}, {deze} {dezeTxt} e {uni} {uniTxt}")
    elif(int(n) >= 10 and int(n) < 99 ):
        deze = int(n[0])
        uni = int(n[1])
        dezeTxt = "Dezenas"
        uniTxt = "Unidades"
        if(deze == 1):
            dezeTxt = "Dezena"
        if(uni == 1):
            uniTxt = "Unidade"
        
        print(f"{n} = {deze} {dezeTxt} e {uni} {uniTxt}")
    else:
        uni = int(n)
        uniTxt = "Unidades"

        if(uni == 1):
            uniTxt = "Unidade"
        print(f"{n} = {uni} {uniTxt}")