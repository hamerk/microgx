from time import sleep as wait
first_list = []
sec_list = []

# Startup
print(" ------------------------------------- \n"
      "|     MGX Sample Number Generator     |\n"
      "|    By: Kyle Hamer   v0.2    2015    |\n"
      " ------------------------------------- \n\n")
wait(1.5)

# One Time Information
print ("Who is the operator?")
op = raw_input(">>> ")

runum = raw_input("What is the run number?\n>>> ")  # Run number for file name

while True:  # Which Machine?
    machine = raw_input("Is this being run on Dad or Dave? \n>>> ")
    machine = machine.upper()
    if machine == 'DAD':
        text = "\t\t100\tResults_Group\tShort50\tPOP6\t\n"
        break
    elif machine == 'DAVE':
        text = "\t\t100\tResults_Group\tSHORTSEQPOP7\tPOP7\t\n"
        break
    else:
        print("Invalid response. Try again.")
        wait(1)
        continue

while True:  # Bact or Fung Run?
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
    if bool(prefix) is False:
        break
    else:
        print "What is the range of the suffixes?"
        wait(1)
        print "Lowest number?"
        low = int(raw_input(">>> "))
        print "Highest Number?"
        high = int(raw_input(">>> ")) + 1
        print "Any missing numbers?"  # Missing Numbers
        ignore = []
        while True:
            test = raw_input(">>> ")
            if bool(test) is False:
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

        print "Any suffixes have letters?"
        letters = {}
        while True:
            num = raw_input(">>> ")
            if bool(num) is False:
                break
            else:
                print "Which letters? (One at a time)"
                while True:
                    letter = raw_input(">>> ")
                    if bool(letter) is False:
                        break
                    else:
                        if num in letters.keys():
                            pass
                        else:
                            letters[num] = []
                        letters[num].append(letter)
                        print "Is there any more letters?"
            print "Any more suffixes with letters?"

        for i in range(low, high):  # Build first_list
            if i in ignore:  # ignore sample
                continue
            elif i < 10:  # Minimum 2 digit suffix
                if str(i) in letters:  # If sample has suffix
                    for let in range(len(letters[str(i)])):  # Add letters
                        first_list.append(prefix + "." + '0' + str(i) +
                                          letters[str(i)][let])
                else:
                    first_list.append(prefix + "." + '0' + str(i))
            else:
                if str(i) in letters:  # If sample has suffix
                    for let in range(len(letters[str(i)])):  # Add letters
                        first_list.append(prefix + "." + str(i) +
                                          letters[str(i)][let])
                else:
                    first_list.append(prefix + "." + str(i))

        print("Is there another prefix?")

# end repeat
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
    if len(sec_list) % 8 == 0:
        count = 7
        while count >= 0:
            sec_list.append(first_list[first_list.index(item) - count] + "_R")
            count -= 1
while len(sec_list) % 8 != 0:
    sec_list.append('HIDI')

if sec_list[-1] == 'HIDI':
    count = -8
    while count < 0:
        if sec_list[count] == 'HIDI':
            break
        else:
            sec_list.append(sec_list[count][:-1] + "R")

while len(sec_list) % 8 != 0:
    sec_list.append('HIDI')

# Create and write txt file

record = open(runum + '.txt', 'w')

count = 0
record.write("Container Name\tDescription\tContainerType\t \
              AppType\tOwner\tOperator\t\n")
record.write(runum + "\t\t96-Well\tRegular\tMGX\t" + op + "\t\n")
record.write("AppServer\tAppInstance\t\n")
record.write("SequencingAnalysis\t\n")
record.write("Well\tSample Name\tComment\tPriority\tResults Group 1\t \
             Instrument Protocol 1\tAnalysis Protocol 1\t\n")

for i in range(1, (len(sec_list)/8)+1):
    if i < 10:
        i = '0' + str(i)
    for x in [chr(a) for a in range(65, 73)]:
        record.write(x + str(i) + '\t' + sec_list[count]
                     + text)
        count += 1

record.close()