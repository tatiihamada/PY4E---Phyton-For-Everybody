#Código para extrair uma parte do texto

text = "X-DSPAM-Confidence:    0.8475"

x = text.find(' ')
print(x)
y = len(text)
print(y)

z = text[23:29]
w = float(z)
print(w)

    




