def clear():
    print("\n"*30)
from logotipo import logo
print(logo)
dictionary = {}
answer = 0
lista = []
print("Welcome to the blind auction!")
while answer != "no":
    name = input("What's your name? ")
    bid = input("What's your bid? ")
    new_bid = ""
    moeda =""
    for char in bid:
        if char in ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            new_bid += char
        else:
            moeda += char
    new_bid = int(new_bid)
    lista.append(new_bid)
    dictionary[name] = new_bid
    answer = input("Are there any other bidders? ").lower()
    clear()
highest = max(lista)
for nombre in dictionary:
    valor = dictionary[nombre]
    if valor == highest:
        highest = str(highest)
        highest = moeda + highest
        winner = nombre
        break
print(f"The winner is {winner} with a bid of {highest}")

