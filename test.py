from sympy.parsing.sympy_parser import parse_expr

with open("Double_Box.DAT") as input:
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
#print(Internal)
#print(External)
print(Props," nothing")

Propagators = []
temp = ""

Props = Props.replace("[","")
#Props = Props.replace("]","")
Props = Props.replace(" ","")

for i in range(len(Props)):
	if Props[i] == "]":
		Propagators.append(temp)
	if Props[i] != ",":
		temp = temp + Props[i]
	else:
		Propagators.append(temp)
		temp = ""

print(Propagators,"split up")
for i in range(len(Propagators)):
	Propagators[i] = parse_expr(Propagators[i])


print(Propagators,"end")