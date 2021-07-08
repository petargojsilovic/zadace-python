import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko',
         'Dario', 'Mihael','Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan',
         'Ante', 'Ivan','Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip',
         'Tomislav', 'Luka', 'Ivan','Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija',
         'Luka', 'Ana','Emanuel','Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante',
         'Marijan','Mario','Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan',
         'Freda', 'Kristina','Josip', 'Lucija']

ucenici = {}
brojacJedinice = 0
brojacUkupno = 0
brojJedinica = 0
brojDvojki = 0
brojTrojki = 0
brojCetvorki = 0
brojPetica = 0

for ime in imena:
    ocjena = random.randint(1, 5)
    ucenici[ime] = ocjena
    brojacUkupno += 1
    if ocjena > 1:
        brojacJedinice += 1
    postotak = (brojacJedinice / brojacUkupno) * 100


for ime in ucenici:
    ocjena = ucenici[ime]
    if ocjena == 5:
        brojPetica += 1
    elif ocjena == 4:
        brojCetvorki += 1
    elif ocjena == 3:
        brojTrojki += 1
    elif ocjena == 2:
        brojDvojki += 1
    else:
        brojJedinica += 1

print(ucenici)
print("Broj petica:", brojPetica, "Broj četvorki:", brojCetvorki, "Broj trica:", brojTrojki, "Broj dvica:", brojDvojki,
      "Broj jedinica:", brojJedinica)
print("Postotak prolaznosti je:", postotak, "%")
