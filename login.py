import csv

def checkIt(userName):
    i=3
    pom = True
    unos = False
    lines=[]
    with open("login.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            if userName == line[0]:
                pom = False
                while i>0:
                    sifra = input(print("Unesite sifru"))
                    if sifra == line[1]:
                        print("Dobrodlosli u sistem!")
                        break
                    else:
                        print("Trazena sifra ne odgovara!")
                        if i==1:
                            print('Login zabranjen! Javite se adminu!')
                        i-=1
            else:
                continue
        if pom:
            odgovor = input(print('Trazeni korisnik ne postoji u bazi. Zelite li se registrovati'))
            if odgovor.lower() == 'da':
                sifra = input(print('Unesite sifru'))
                lines.append(userName)
                lines.append(sifra)
                unos = True
            else:
                print('Kraj aplikacije')
        if unos:
            with open("vjezba10.csv", 'a') as out:
                out.write("\n" + ','.join(lines))

username = input(print("Unesite kosirnicko ime:"))
checkIt(username)





