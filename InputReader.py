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
                    input_Symbols = ""
                    for k in range(start,len(line)):
                        input_Symbols = input_Symbols + line[k]

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
                    Props = ""
                    for k in range(start,len(line)):
                        Props = Props + line[k]

            
        input.close()
        input_Symbols = cleanup(input_Symbols)
        Internal = cleanup(Internal)
        External = cleanup(External)
        Props = Props.replace("[","")
        Props = Props.replace("]","")
        
        Symbols = math_list(input_Symbols)
        Internal = math_list(Internal)
        External = math_list(External)
        print(Props)
        print(props_list(Props))

        return inputs
#replaces some unwanted nonsense from the input file
def cleanup(string):
    string = string.replace(" ","")
    string = string.replace("[","")
    string = string.replace("\n","")
    string = string.replace("]","")
    string = string.replace(",","")
    return string
# Just makes the internal and external inputs math symbols
def math_list(String):
    result = []
    for i in range(len(String)):
        result.append(Symbol(String[i]))
    return result    
#Lists out the propagators and will eventually put then in  mathematical format. 

def props_list(String):
    j = 0
    Propagators = []
    for i in range(len(String)):
        if j == 2:
            temp = ""
            for k in range(start,i+1):
                temp = temp + String[k]
            Propagators.append(temp)
            j = 0 
        
        if String[i] == '(':
            start = i 
        
        if String[i] == '*':
            j+=1

    #Trying to get the propagators out of a string and in a mathematical format
    #so they can be manipulated. 
    for i in range(len(Propagators)):
        times = 0
        number_times = 0
        Open_P = Propagators[i].count('(')
        Close_P = Propagators[i].count(')')
        Propagators[i] = Propagators[i].replace("(","")
        Propagators[i] = Propagators[i].replace(")","")
        print(Propagators[i])
        for j in range(len(Propagators[i])):
            if Propagators[i][j] == '-':
                minus = j
            if Propagators[i][j] == '*':
                number_times += 1 
                times = j
        power = int(Propagators[i][times + 1])
        Propagators[i] = Propagators[i].replace(Propagators[i][times + 1],"")
        Propagators[i] = Propagators[i].replace("-","")
        Propagators[i] = Propagators[i].replace("*","")

        print(minus)
        print(times)


    return Propagators    
            
Reader=Reader("input.DAT")

Reader.Input_filereader()
