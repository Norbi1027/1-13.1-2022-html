
def napp():

    napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

    mikor =int(input("Hány nap mulva mész nyaralni? "))

    napIn = input("Milyen nap van ma? ").lower()
    napIndex = None

    for i in range(0, len(napok)):
        if napIn == napok[i].lower():
            napIndex = i
    vissza = (napIndex + mikor)%7 

    print("Ma",napIn,"van",mikor,"nappal ezelőtt voltál nyaralni, az a nap:",napok[vissza])


napp()