import re
string = input("Unesite string: ")
regex = "L.*([0-5 ]|[ 0-5]).*p"
result = re.findall(regex, string)
if result:
    print("Podudaranje")
else:
    print("Nema podudaranja")
