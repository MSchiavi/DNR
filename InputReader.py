def Input_filereader(inFile):
    inputs = []
    start = 0
    with open(inFile) as input:
        for i, line in enumerate(input):
            if i == 11:
                
                for j in range(len(line)):
                    if line[j] == ":":
                        start = j + 1
                        break
                TripTime2 = ""
                for k in range(start,len(line)):
                    TripTime2 = TripTime2 + line[k]
            if i == 13:
                for j in range(len(line)):
                    if line[j] ==":":
                        start = j + 1
                        break
                KillSpeed = ""
                for k in range(start,len(line)):
                    KillSpeed = KillSpeed + line[k]

            if i == 15:
                for j in range(len(line)):
                    if line[j] == ":":
                        start = j+1
                        break
                Events = ""
                for k in range(start,len(line)):
                    Events = Events + line[k]
            if i == 17:
                for j in range(len(line)):
                    if line[j] == ":":
                        start = j + 1
                        break
                Bin = ""
                for k in range(start,len(line)):
                    Bin = Bin + line[k]
    
        inputs.append(int(TripTime2.replace(" ",""))*60)
        inputs.append(int(KillSpeed.replace(" ","")))
        inputs.append(int(Events.replace(" ","")))
        inputs.append(float(Bin.replace(" ","")))
# Inputs array [ Time of trip in seconds, average kill time in seconds, Number of Events ]
    
    input.close()

    return inputs
