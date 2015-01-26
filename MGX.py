from time import sleep as wait
#from collections import defaultdict
first_list = []
sec_list = []
alpha = []
for i in range(65, 65+26):
    alpha.append(chr(i))

#Startup
print(" -------------------------------------- \n"\
      "|     MGX Sample Number Generator      |\n"\
      "|    By: Kyle Hamer   v0.1    2014     |\n"\
      " -------------------------------------- \n\n")
wait(2)

# One Time Information
runum = raw_input("What is the run number?\n>>> ") #Run number for file name

while True: #Which Machine?
    machine = raw_input("Is this being run on Dad or Dave? \n>>> ")
    machine = machine.upper()
    if machine == 'DAD' or machine == 'DAVE':
        break
    else:
        print("Invalid response. Try again.")
        wait(1)
        continue
        
while True: # Bact or Fung Run?
    BorF = raw_input("Bacterial (BACT) or Fungal (FUNG) Run? \n>>> ")
    BorF = BorF.upper()
    if BorF == "BACT" or BorF == "FUNG":
        break
    else:
        print("Invalid response. Try again.")
        wait(1)
        continue

# Sample Information

print "What is the prefix?"
while True:
    prefix = raw_input(">>> ")
    if bool(prefix) == False:
        break
    else:
        print "What is the range of the suffixes?"
        wait(1)
        print "Lowest number?"
        low = int(raw_input(">>> "))
        print "Highest Number?"
        high = int(raw_input(">>> ")) + 1
        print "Any missing numbers?"
        ignore = []
        while True:
            test = raw_input(">>> ")
            if bool(test) == False:
                break
            elif '-' in test:
                [test_min, test_max] = test.split('-')
                for i in range(int(test_min), int(test_max)+1):
                    ignore.append(i)
            else:
                test = int(test)
                if test not in range(low, high):
                    print "Try Again."
                    continue
                else:
                    ignore.append(test)
            print "Any more missing numbers?"

        print "Multiple colonies on one plate?"
        mult = {}
        while True:
            test = raw_input(">>> ")
            if bool(test) == False:
                break
            else:
                test = int(test)
                if test not in range(low, high):
                    print "Try Again."
                    continue
                else:
                    test_num = int(raw_input("How many colonies?\n>>> "))
                    mult[test] = test_num
            print("Any more multiple colonies?")

        print "Any repeat samples?"
        rep = []
        while True:
            test = raw_input(">>> ")
            if bool(test) == False:
                break
            else:
                test = int(test)
                if test not in range(low, high):
                    print "Try Again."
                    continue
                else:
                    rep.append(test)
            print("Any more repeat samples?")
            
        for i in range(low, high): # Add that prefix to first_list
            if i in ignore:
                continue
            elif i < 10: #Minimum 2 digit suffix
                if i in mult: #If multiple colonies on plate
                    for let in range(mult[i]): #Add letters
                        first_list.append(prefix + "." + '0' + str(i) + alpha[let])
                else:
                    first_list.append(prefix + "." + '0' + str(i))
            else:
                if i in mult:
                    for let in range(mult[i]):
                        first_list.append(prefix + "." + str(i) + alpha[let])
                else:
                    first_list.append(prefix + "." + str(i))
            if i in rep: #If repeat sample
                first_list[-1] = first_list[-1] + "R" #add 'R'

        print("Is there another prefix?")

#end repeat
first_list.append(BorF + "NEGW")
first_list.append(BorF + "POS")

if len(first_list) > 48:
    print "Too many samples!"
    wait(1)
    quit()

if len(first_list) < 3:
    print "Must have samples!"
    wait(1)
    quit()

for item in first_list:
    sec_list.append(item + "_F")
    if len(sec_list)%8 == 0:
        count = 7
        while count >= 0:
            sec_list.append(first_list[first_list.index(item) - count] + "_R")
            count -= 1
while len(sec_list)%8 != 0:
    sec_list.append('HIDI')

if sec_list[-1] == 'HIDI':
    count = -8
    while count < 0:
        if sec_list[count] == 'HIDI':
            break
        else:
            sec_list.append(sec_list[count][:-1] + "R")

while len(sec_list)%8 != 0:
    sec_list.append('HIDI')

for last in sec_list: #Remove in final copy
    print last

record = open(runum + '.txt', 'w')
count = 0
for last in sec_list:
    record.write(last)
    count += 1
    if count < len(sec_list):
        record.write('\n')
record.close()
