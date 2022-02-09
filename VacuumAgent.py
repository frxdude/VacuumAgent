import numpy as np
from operator import itemgetter

operations = ["NoOperation", "Suck"]
operation_code = [1, 2]


class Vacuum:

    def __init__(self, name):
        self.name = name

    def handleVacuum(self, op_code, roomno, ci):
        if op_code == 1:
            vacuumMoves[roomno][ci] = operations[0]
        elif op_code == 2:
            vacuumMoves[roomno][ci] = operations[1]
            # data[roomno][ci] = "Clean"


data_types = ["Dirty", "Clean"]

print("heden uruutei ve : ")
step = int(input())

rows, cols = (int(step), int(step))

data = []
vacuumMoves = []
roomAnalysis = []

for x in range(0, cols):
    row = []
    vacuumRow = []
    roomAnalysisRow = []
    for x in range(0, rows):
        row.append("")
        vacuumRow.append("")
        roomAnalysisRow.append("0")
    roomAnalysis.append(roomAnalysisRow);
    vacuumMoves.append(vacuumRow)
    data.append(row)

for i in range(step):
    for j in range(step):
        data[i][j] = data_types[np.random.randint(0, 2)]
        roomAnalysis[i][0] = str(i)
        if data[i][j] == "Dirty":
            roomAnalysis[i][1] = str(int(roomAnalysis[i][1]) + 1)


def printData():
    print("----- Uruunii umnuh data -----")
    for r in range(int(step)):
        print(data[r])


def clearAndPrint():
    for q in range(step):
        for w in range(step):
            if vacuumMoves[q][w] == "Suck":
                data[q][w] = "Clean"
                roomAnalysis[q][1] = str(int(roomAnalysis[q][1]) - 1)

    print("----- " + vacuum.name + " nertei Agentiin uildluud -----")
    for k in range(int(step)):
        print(vacuumMoves[k])
    print("\n----- Uruunii daraah data -----")
    for p in range(int(step)):
        print(data[p])


print("----- Random hiisen uruunii data -----")
for i in range(int(step)):
    print(data[i])

print("----- Uruunii bohir hesguudiin too -----")
for i in range(int(step)):
    print("room No : " + str(i + 1) + " bohir hesgiin too : " + str(roomAnalysis[i][1]))

vacuum = Vacuum("B180910040")
while (True):
    print("\n----- Commands -----")
    print("\n- 1. Auto          -")
    print("\n- 2. Manual        -")
    print("\n--------------------")

    command = int(input())

    if command == 1:
        roomno = int(sorted(roomAnalysis, key=itemgetter(1))[step - 1][0])
        printData()
        for j in range(step):
            if data[roomno][j] == "Dirty":
                vacuum.handleVacuum(2, roomno, j)
            elif data[roomno][j] == "Clean":
                vacuum.handleVacuum(1, roomno, j)
        clearAndPrint()
    elif command == 2:
        print("\nhed dugeer uruug tseverleh ve : ")
        roomno = int(input()) - 1

        printData()

        for j in range(step):
            if data[roomno][j] == "Dirty":
                vacuum.handleVacuum(2, roomno, j)
            elif data[roomno][j] == "Clean":
                vacuum.handleVacuum(1, roomno, j)
        clearAndPrint()
    else:
        print("----- Songoltoo zuw oruulna uu")
