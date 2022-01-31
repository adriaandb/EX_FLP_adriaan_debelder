import mod_vertalers as mv

lijst={}
lijst=mv.de_vertalers_antwerpen


def toon_moedertaal(lijst):
    print("-------------------------------")
    print("lijst van vertalers met moedertaal naar keuze:")
    taal=input("toon vertalers die taal naar keuze machtig zijn")
    for key, value in lijst.items():
        print("Naam: " + key + "',Moedertaal: " + lijst[key]["moedertaal"] + ", Beschikbaar: " + lijst[key][
            "beschikbaar"])
        for tl in value:
            print(value[tl])
            if tl == "talen":
                # print(value[x])

                for y in value[tl]:
                    if value[y]==taal:
                        print("gelukt")
                    else:
                        pass
                    #print(y)


toon_moedertaal(lijst)