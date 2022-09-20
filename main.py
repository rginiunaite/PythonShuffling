# file specifies a sequences to reshuffle
from altschulEriksonDinuclShuffle import *

file = '/home/rasa/Documents/DNA/cgDNA+_clean/cgDNA+_clean/SkirmantasData/AllCentresCh37/allsubsequenceswithCpG5to14Ch1.txt'

with open(file) as f:
    lines = f.readlines()


a = len(lines)

# print (difflib.ndiff(av, b)) whether the same

# to check differences
#output_list = [li for li in difflib.ndiff(av, b) if li[0] != ' ']
#print(output_list)

with open('shuffledCh1CpG10trial.txt', 'w') as f:


    for x in range(a-1):
        #print(dinuclShuffle(str.strip(lines[x+1])))
        f.write(dinuclShuffle(str.strip(lines[x+1])))
        f.write('\n')