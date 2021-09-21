from prettytable import PrettyTable, DOUBLE_BORDER

header = ["x"]
rangeA, rangeB = -20, 0
ausgerechneterWerte = ["f(x)=x^2"]

def isNegative(number):
    if number < 0:
        return True
    else:
        return False

print("                 Wertetabellenrechner")
rangeA = int(input("von: "))
rangeB = int(input("bis einschleißlich: "))

for x in range(rangeA, rangeB + 1):
    ausgerechneterWerte.append(x ** 2)
    print(x ** 2)

for wert in range(rangeA, rangeB + 1):
    header.append(wert)

if not isNegative(rangeB - rangeA):
    if rangeB - rangeA < 30:
        myTable = PrettyTable(header)
        myTable.set_style(DOUBLE_BORDER)
        myTable.add_row(ausgerechneterWerte)
        print(myTable)
else:
    print("Unterschied darf nicht negativ sein.")