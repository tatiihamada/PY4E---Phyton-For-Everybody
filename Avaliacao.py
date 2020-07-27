#Código para o usuário inserir uma nota e verificar qual foi o seu conceito final
nota = input("Insira sua nota: ")

try: 
    notafinal = float(nota)
except:
    print("Por favor, insira um valor numérico e tente novamente.")
    quit()

if notafinal >= 0.9 :
    print("A")
elif notafinal >= 0.8:
    print("B")
elif notafinal >= 0.7:
    print("C")
elif notafinal >= 0.6:
    print("D")
elif notafinal <0.6:
    print("F")

    