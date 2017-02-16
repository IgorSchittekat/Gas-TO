from System.ADTs.Table import *
from os import listdir, remove, path

class Execute:

    def executeInstruction(self, instruction):
        splitInstruction = instruction.split()
        if splitInstruction[0][:4] == "type":
            print("\nCreating datatype: " + splitInstruction[0][5:])
            if splitInstruction[0][5:9] == "hlin":
                size = splitInstruction[0].split(",")[1]
                self.table = Table("hlin", int(size))
                self.type = "hlin"
            elif splitInstruction[0][5:10] == "hquad":
                size = splitInstruction[0].split(",")[1]
                self.table = Table("hquad", int(size))
                self.type = "hquad"
            elif splitInstruction[0][5:9] == "hsep":
                size = splitInstruction[0].split(",")[1]
                chain = splitInstruction[0].split(",")[2]
                self.table = Table("hsep", int(size), chain)
                self.type = "hsep"
            else:
                self.table = Table(splitInstruction[0][5:])
                self.type = splitInstruction[0][5:]

        elif splitInstruction[0] == "insert":
            print(instruction)
            newItem = int(splitInstruction[1])
            self.table.insert(newItem)

        elif splitInstruction[0] == "delete":
            print(instruction)
            if len(splitInstruction) == 1:
                self.table.delete()
            else:
                searchKey = int(splitInstruction[1])
                self.table.delete(searchKey)

        elif splitInstruction[0] == "print":
            i = 1
            while path.exists("Output/ADTgraph/" + self.type + "-" + str(i) + ".dot"):
                i += 1
            outputFile = open("Output/ADTgraph/" + self.type + "-" + str(i) + ".dot", "a+")
            outputFile.write("digraph G {\n")
            code = self.table.visualize()
            outputFile.write(code)
            outputFile.write("\n}")
            outputFile.close()
            print("Output file created")



### DATA STRUCTURE INIT ###
execute = Execute()

### SYSTEM INIT ###
print("RUNNING VISUALIZE ADT")

# input selection
print("\n~AVAILABLE INPUT FILES~")
fileNumber = 1
files = listdir("Input/ADTgraph")

for file in files:
    print(str(fileNumber) + ") " + file)
    fileNumber += 1

while True:
    inputFileNumber = input(
        "\nSelect number of file you wish to use as input:\n")
    if int(inputFileNumber) not in range(1, len(files) + 1):
        print("Invalid file number, please try again")
    else:
        break

pathToInputFile = "Input/ADTgraph/" + files[int(inputFileNumber) - 1]
with open(pathToInputFile) as inputF:
    instructions = [instruction.strip() for instruction in
                    inputF.readlines() if
                    (instruction[0] != "#" and len(instruction) > 1)]

clearPrompt = input("Would you like to clear the Output folder? (Y/N)\n")
if clearPrompt.upper()[0] == "Y":
    files = [f for f in listdir("Output/ADTgraph")]
    for f in files:
        if f[0] == ".":
            continue
        remove("Output/ADTgraph/" + f)

### INPUT PROCESSING AND OUTPUT CREATION ###
instructions.reverse()
while len(instructions) > 0:
    nextInstruction = instructions.pop()
    execute.executeInstruction(nextInstruction)
