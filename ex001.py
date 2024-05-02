nome = input("digite seu nome: ")
email = input("Digite aqui seu e-mail: ")

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao:]
print(posicao)

#pegar primeiro nome do usuario
posicao = nome.find(" ")
primeironome = nome[:posicao]
print(primeironome)

