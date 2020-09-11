f = open("compStats.txt", "r")

averages = []
count= 0

while True: 
    count += 1
  
    # Get next line from file 
    line = f.readline()

    allVals = 0

    for elem in line.strip().split():
        allVals += int(elem)
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break

    avg = allVals/len(line.strip().split())

    print(str(avg))