# ProcessData.py
# Name:
# Date:
# Assignment:

def main():
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')

    for line in inFile:
        data = line.split()
        first = data[0]
        last = data[1]
        idNum = data[3]
        major = data[6]
        year = data[5]

        student_id = makeID(first, last, idNum)
        major_year = makemajoryear(major, year)
        output = last + "," + first + "," + student_id + "," + major_year + "\n"
        outFile.write(output)

    inFile.close()
    outFile.close()

def makeID(first, last, idNum):
    while len(last) < 5:
        last = last + "X"
    id = first[0] + last + idNum[len(idNum)-3:] 
    return id

def makemajoryear(majorName, yearName):
    majorcode = majorName[:3].upper()
   
    if yearName == "Freshman":
        yearName = "FR"
    elif yearName == "Sophomore":
        yearName = "SO"
    elif yearName == "Junior":
        yearName = "JR"
    elif yearName == "Senior":
        yearName = "SR"

    return majorcode + "-" + yearName

if __name__ == '__main__':
    main()