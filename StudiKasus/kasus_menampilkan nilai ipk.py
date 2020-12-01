listWisuda = [{"nama":"razilsyah",
               "jurusan":"teknik komputer jaringan",
               "nilai":7},
              {"nama":"khalinda",
               "jurusan":"gamers",
               "nilai":9}
              ]

user = 0

while user != 3:
    print("===== DAFTAR WISUDAWAN =====")
    print("1.nama wisudawan")
    print("2.nilai tertinggi")
    print("3.exit")

    user = int(input("masukan daftar yang ingin di akses :"))
    if user == 1:
        counter = 0
        while counter < 1:
            for k, v in listWisuda[0].items():
                print(k, " : ", v)
            print("\n")
            for k, v in listWisuda[1].items():
                print(k, " : ", v)

            counter = counter + 1

    elif user == 2:
        print("===== nilai tertinggi =====")
        pass







