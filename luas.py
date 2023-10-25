print("======================")
print("program penghitung luas bangun datar")
print(''' 
pilih salah satu bangun datar:
1 = Luas persegi
2 = Luas lingkaran
3 = Luas segitiga
''')

pilihan = int(input ("Masukkan pilihan: "))
match pilihan:
    case 1:
        sisi = int(input("Masukkan sisi: "))
        luas = sisi * sisi
        print("Luas persegi dengan sisi ", sisi ," adalah: ", luas)
    case 2:
        jari = int(input("Masukkan jari-jari: "))
        luas = 3.14 * jari ** 2
        print("Luas lingkaran dengan jari-jari ", jari, " adalah", luas)
    case 3:
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        luas = 1/2 * alas * tinggi
        print("Luas segitiga dengan alas ", alas, " dan tinggi ", tinggi, " adalah: ", luas)