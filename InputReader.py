from sympy import Symbol

class Reader:




    def __init__(self,File):
        self.inFile = File




    def Input_filereader(self):
        inputs = []
        start = 0
        with open(self.inFile) as input:
            for i, line in enumerate(input):
                if i == 9:
                
                    for j in range(len(line)):
                        if line[j] == ":":
                            start = j + 1
                            break
                    Symbols = ""
                    for k in range(start,len(line)):
                        Symbols = Symbols + line[k]

                if i == 11:
                
                    for j in range(len(line)):
                        if line[j] == ":":
                            start = j + 1
                            break
                    Internal = ""
                    for k in range(start,len(line)):
                        Internal = Internal + line[k]
                if i == 13:
                    for j in range(len(line)):
                        if line[j] ==":":
                            start = j + 1
                            break
                    External = ""
                    for k in range(start,len(line)):
                        External = External + line[k]

                if i == 15:
                    for j in range(len(line)):
                        if line[j] == ":":
                            start = j+1
                            break
                    Propagators = ""
                    for k in range(start,len(line)):
                        Propagators = Propagators + line[k]
            Symbols = Symbols.replace(" ","")
            Internal = Internal.replace(" ","")
            External = External.replace(" ","")
            Propagators = Propagators.replace(" ","")
            Symbols = Symbols.replace("\n","")
            
            inputs.append(Internal.replace("\n",""))
            inputs.append(External.replace("\n",""))
            inputs.append(Propagators.replace("\n",""))
            

        input.close()
        for i in range(len(inputs)):
            
            inputs[i] = filter(lambda a: a != '[', list(inputs[i]))
            inputs[i] = filter(lambda a: a != ']', list(inputs[i]))
            inputs[i] = filter(lambda a: a != ',', list(inputs[i]))
        


        for i in range(len(Symbols)):
            a = Symbols[i] # error here 'str' object does not support item assignment
            Symbols[i] = Symbol('a')
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                inputs[i][j] = int(inputs[i][j])


        return inputs

Reader=Reader("input.DAT")

print(Reader.Input_filereader())
