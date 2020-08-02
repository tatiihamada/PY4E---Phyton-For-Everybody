#Abrindo um arquivo .txt e trabalhando com as informações

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    upline = line.rstrip().upper()
    print(upline)



