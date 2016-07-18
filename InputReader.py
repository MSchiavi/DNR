from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr


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
        #Props = Props.replace("[","")
        #Props = Props.replace("]","")
        
        Symbols = math_list(input_Symbols)
        Internal = math_list(Internal)
        External = math_list(External)

        Propagators = props_list_2(Props)
        print(Propagators)
        inputs.append(Internal)
        inputs.append(External)
        inputs.append(Propagators)

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
def props_list_2(String):
    Propagators = []
    String = String.replace("[","")
   # String = String.replace("]","")
    String = String.replace(" ","")
    temp = ""

    for i in range(len(String)):
        if String[i] == "]":
            Propagators.append(temp)
        if String[i] != ",":
            temp = temp + String[i]
        else:
            Propagators.append(temp)
            temp = ""
    for i in range(len(Propagators)):
        Propagators[i] = parse_expr(Propagators[i])
    return Propagators
            
#Reader=Reader("input.DAT")

#print(Reader.Input_filereader())
