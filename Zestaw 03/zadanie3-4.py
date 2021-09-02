filepath = "pakiet_IP.txt"
f = open(filepath, "r")

dane = f.readlines()
linia1 = dane[0]
linia2 = dane[1]
linia3 = dane[2]
linia4 = dane[3]
linia5 = dane[4]

f.close()
linia1 = linia1.strip('\n')
linia2 = linia2.strip('\n')
linia3 = linia3.strip('\n')
linia4 = linia4.strip('\n')
linia5 = linia5.strip('\n')

wersja_pro = linia1[0]
wersja_pro = int(wersja_pro, 16)
print("Wersja protokołu: "+str(wersja_pro))
print(" ")

zr_adr_IP = linia1[36:]
zr_adr_IP = [int(i, 16) for i in zr_adr_IP.split()]
print("Adres źródłowy IP: "+str(zr_adr_IP))
print(" ")

doc_adr_IP = linia2[0:11]
doc_adr_IP = [int(i, 16) for i in doc_adr_IP.split()]
print("Adres docelowy IP: "+str(doc_adr_IP))
print(" ")

typ_pro = linia1[27:29]
typ_pro = int(typ_pro, 16)
print("Typ protokołu warstwy wyższej: "+str(typ_pro))
print(" ")

if typ_pro == 6:#TCP
    nr_zr_portu_TCP = linia2[12:14] + linia2[15:17]
    nr_zr_portu_TCP = int(nr_zr_portu_TCP, 16)
    print("Nr źródłowy portu TCP: "+str(nr_zr_portu_TCP))
    print(" ")
    
    nr_dol_portu_TCP = linia2[18:20] + linia2[21:23]
    nr_dol_portu_TCP = int(nr_dol_portu_TCP, 16)
    print("Nr docelowy portu TCP: "+str(nr_dol_portu_TCP))
    print(" ")

    dane = linia4[12:] + " " + linia5
    dane = [''.join(chr(int(i, 16)) for i in dane.split())]
    print(dane)

