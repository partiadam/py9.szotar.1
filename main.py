'''
1. Feladat
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, és azt hogy rendelkezik-e érvényes oltással veszettség ellen! 
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!
'''

beker = input('Kutya neve: ')
beker1 = int(input('Kutya életkora: '))
beker2 = input('Kutya fajtája: ')
beker3 = input('A kutya rendelkezik-e oltással veszettség ellen?: ')

kutya_adatok = {
    'kutya_neve': beker,
    'kutya_kora': beker1,
    'kutya_fajtaja': beker2,
    'veszettseg_elleni_oltassal_rendelkezik_e': beker3
}

print(kutya_adatok)