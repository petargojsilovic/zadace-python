def pozdrav(ime):
    print("Pozdrav", ime + "!")


dobrodošao = lambda ime: print("Dobrodošao", ime + "!")


def poziv(funkcija):
    funkcija("IME")


print(poziv(pozdrav))
print(poziv(dobrodošao))
