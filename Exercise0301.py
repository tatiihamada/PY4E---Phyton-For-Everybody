hours = input("Horas realizadas: ")
h = float(hours)
rate = input("Digite a quantidade de horas: ")
r = float(rate)

if h>40 :
    pagamento = h * r
    acrescimo = (h-40) * (r*0.5)
    pagamentofinal = pagamento + acrescimo
else: 
    pagamentofinal = h * r
print("O seu pagamento final é:", pagamentofinal)
