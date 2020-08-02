#Código para extrair uma parte do texto

text = "X-DSPAM-Confidence: 0.8475"

x = text.find(':')

y = text[x+1:]
w = float(y)
print(w)






