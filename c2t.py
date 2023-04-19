import os
import math
from c2teng import *

os.system("cls")

division = []                                       # -----> Division of the quantity in 3 digits.
grupos   = []                                       # -----> List of digits grouped in 3.
cnvTxt   = []                                       # -----> List for groups of digits converted to text.
pTxtF    = ""                                       # -----> Initialization of the variable that will contain the final text string converted.
pTail    = " PESOS"                                 # -----> Last value of the final text string converted.

PV = {0:None,1:"MIL",2:"MILLONES"}                  # -----> Dictionary with the description of each one of the groups.

numInt = float(input("Cantidad a convertir: "))     # -----> Amount to convert.
numStr = str(math.trunc(numInt))                    # -----> "Integer" part of the amount to be converted.
numFlo = str(numInt)[str(numInt).find(".") + 1:]    # -----> The "decimal" part of the amount to convert.

numStr = numStr[::-1]                               # -----> I flip the amount to convert in order to separate in 3 digits groups.
inc = 1                                             # -----> I initialize the 3-digit counter.


# Process to divide the amount into groups of 3 digits.

for a in range(len(numStr)):
    if inc <= 3:
        division.append(numStr[a])
    else:
        division.reverse()
        grupos.insert(0,"".join(division))
        inc = 1
        division = []
        division.append(numStr[a])

    inc +=1

if division:
    division.reverse()
    grupos.insert(0,"".join(division))


# This part is to recognize what kind of text separator the program needs to select in the dictionary of groups.

if len(grupos) == 3:
    sldTxt = 2
elif len(grupos) == 2:
    sldTxt = 1
elif len(grupos) == 1:
    sldTxt = 0

# Process to convert amount to text.

for grupo in grupos:    
    tmpT1,tmpT2,tmpT3 = gEngine(grupo)

    if sldTxt == 0  and tmpT1 == None and tmpT2 == None and tmpT3 == "UN":
        pTail = " PESO"

    if sldTxt == 1 and tmpT1 == None and tmpT2 == None and tmpT3 == "UN":
        t3 = None

    cnvTxt.append(tmpT1)
    cnvTxt.append(tmpT2)
    cnvTxt.append(tmpT3)


    if sldTxt == 2 and tmpT1 == None and tmpT2 == None and tmpT3 == "UN":
        cnvTxt.append("MILLON")
    else:
        if int(grupo) > 0:
            cnvTxt.append(PV[sldTxt])
        else:
            cnvTxt.append(None)

    sldTxt -= 1


# Finishing the text string get from the conversion deleting extra blank spaces and empty groups.

for pTxt in cnvTxt:
    if pTxt != None:
        pTxtF = pTxtF + " " + pTxt


# Adding the "decimal" part to the final string text.

if len(numFlo) == 0:
    numFlo = "00"
elif len(numFlo) == 1:
    numFlo = numFlo + "0"

# Final result.
print(pTxtF[1:len(pTxtF)] + pTail + " " + numFlo + "/100 M.N.")