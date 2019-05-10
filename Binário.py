n1=int(input('Digite um número: '))  #Nesta linha pede-se que o usuário digite um número inteiro,
#por isso é usado input para pedir que ele faça isso e int para dizer que o que vai ser digitado tem que ser um número inteiro.
mostra='' #É uma string vazia, ou seja, ainda não está definido o que está dentro dela.

while n1>0:  #Diz que deverá se repetir o que está dentro deste while enquanto que o número que o usuário digitou for maior que zero.
    if n1%2==0:  #Diz que se o resto da divisão do número que o usuário digitou for 0, deve-se executar o que está dentro deste if.
        mostra=mostra+'0'
        n1=n1/2
    elif n1%2==1:  #Diz que se o resto da divisão do número que o usuário digitou for 1, deve-se executar o que está dentro deste elif.
        mostra=mostra+'1'
        n1=(n1-1)/2

print(mostra[::-1])  #Mostra para o usuário o número que ele digitou em binário. [::-1] serve para inverter a ordem dos números,
#já que o binário é escrito com os restos da divisão da direita para a esquerda. 
