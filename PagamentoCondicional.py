#Cálculo de pagamento com condicional

hours = input("Horas realizadas: ")
rate = input("Digite a quantidade de horas: ")

#Validação da informação inserida pelo usuário
try: 
    h = float(hours)
    r = float(rate)
except:
    print("Por favor, insira um valor numérico e tente novamente.")
    quit()
    
if h>40 :
    pagamento = h * r
    acrescimo = (h-40) * (r*0.5)
    pagamentofinal = pagamento + acrescimo
else: 
    pagamentofinal = h * r
print("O seu pagamento final é:", pagamentofinal)
