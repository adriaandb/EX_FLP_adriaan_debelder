import mod_vertalers as mv

lijst={}
lijst=mv.de_vertalers_antwerpen

def toon_tolk_taal(lijst):
    print("-------------------------------")
    print("beschikbare vertalers van je regio, plus de talen die ze geven:")
    for key, value in lijst.items():
        if lijst[key]["beschikbaar"] == "ja":
            print(key)
            for x in value:
                print(value[x])
                #if lijst[key]=="talen":
                    #print(value(x))
                    #for y in x:
                       # print(x[y])

toon_tolk_taal(lijst)