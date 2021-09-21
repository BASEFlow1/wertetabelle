from prettytable import PrettyTable, DOUBLE_BORDER
import parser

def isNegative(number):
    if number < 0:
        return True
    else:
        return False

print("Wertetabellenrechner\n---------------------")
formel = input("Formel {f(x) = ...}:")
formelFalsch = formel
formel = formel.replace("^", " ** ")
formel = formel.replace("f(x)=", "")
formel = formel.replace(" ", "")
code = parser.expr(formel).compile()
rangeA = int(input("von: "))
rangeB = int(input("bis einschleißlich: "))

header = ["x"]
ausgerechneterWerte = [formelFalsch]

for x in range(rangeA, rangeB + 1):
    ausgerechneterWerte.append(eval(code))

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