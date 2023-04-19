# Dictionary that contains the "special" numbers in the Spanish language for Mexico.

SV = {1:"UN",2:"DOS",3:"TRES",4:"CUATRO",5:"CINCO",6:"SEIS",7:"SIETE",8:"OCHO",9:"NUEVE",10:"DIEZ",11:"ONCE",12:"DOCE",13:"TRECE",14:"CATORCE",15:"QUINCE",16:"DIECISEIS",17:"DIECISIETE",18:"DIECIOCHO",19:"DIECINUEVE",20:"VEINTE",21:"VEINTIUN",22:"VEINTIDOS",23:"VEINTITRES",24:"VEINTICUATRO",25:"VEINTICINCO",26:"VEINTISEIS",27:"VEINTISIETE",28:"VEINTIOCHO",29:"VEINTINUEVE",30:"TREINTA",40:"CUARENTA",50:"CINCUENTA",60:"SESENTA",70:"SETENTA",80:"OCHENTA",90:"NOVENTA",100:"CIEN",200:"DOSCIENTOS",300:"TRESCIENTOS",400:"CUATROCIENTOS",500:"QUINIENTOS",600:"SEISCIENTOS",700:"SETECIENTOS",800:"OCHOCIENTOS",900:"NOVECIENTOS"}


# Function to validate that the "complete" number is included in the dictionary.

def sNum(sn):
    if sn in SV: return True


# Functions to validate the number separated in the 3 digits (One function for each digit position).

def p1(p1N,p1L,p1S):
    if int(p1N) > 0:
        if sNum(int(p1N)):
            p1T = SV[int(p1N)]
            p1S = True
        else:
            p1N = p1N[0:1] + "00"
            p1T = SV[int(p1N)]
            if p1N == "100":
                p1T = "CIENTO"
            p1S = False
    else:
        p1T = None
        p1S = True
    
    return p1T, p1S

def p2(p2N,p2L,p2S):
    if int(p2N) > 0:
        if p2L == 3:
            p2N = p2N[1:3]
        if sNum(int(p2N)):
            p2T = SV[int(p2N)]
            p2S = True
        else:
            p2N = p2N[:1] + "0"
            p2N = SV[int(p2N)]
            p2T = p2N + " Y"
            p2S = False
    else:
        p2T = None
        p2S = False
    
    return p2T, p2S

def p3(p3N,p3L,p3S):
    if p3L == 3:
        p3N = p3N[2:]
    elif p3L == 2:
        p3N = p3N[1:]

    if int(p3N) == 0:
        p3T = None
    else:
        p3T = SV[int(p3N)]

    return p3T ,p3S


# Main function, launches the functions according to the number to convert.

def gEngine(gnum):
    tF1 = None
    tF2 = None
    tF3 = None
    sF = False

    fLen = len(gnum)

    if fLen == 3:
        tF1, sF = p1(gnum,fLen,sF)
        if not sF:
            tF2, sF = p2(gnum,fLen,sF)
            if not sF:
                tF3, sF = p3(gnum,fLen,sF)
    elif fLen == 2:
        tF2, sF = p2(gnum,fLen,sF)
        if not sF:
            tF3, sF = p3(gnum,fLen,sF)
    elif fLen == 1:
        tF3, sF = p3(gnum,fLen,sF)

    return tF1,tF2,tF3
