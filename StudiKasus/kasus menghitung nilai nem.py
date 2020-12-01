nilai_pelajaran = [{
    "nama_pelajaran": {
        "bahasa indonesia": 7.50,
        "bahasa inggris": 6.50,
        "matematika": 7.70,
        "IPA": 6.30
    }
}]


def menghitung_nem(b_indo, b_ing, mtk, ipa):
    return b_indo + b_ing + mtk + ipa


def jika(nem):
    if nem > 27:
        grade = "A"
    else:
        grade = "B"

    print ( f"Nem anda = {hasil_return} is {grade}" )


# print(nilai_pelajaran[0]["nama_pelajaran"]["bahasa indonesia"])
hasil_return = menghitung_nem ( b_indo=nilai_pelajaran[0]["nama_pelajaran"]["bahasa indonesia"],
                                b_ing=nilai_pelajaran[0]["nama_pelajaran"]["bahasa inggris"],
                                mtk=nilai_pelajaran[0]["nama_pelajaran"]["matematika"],
                                ipa=nilai_pelajaran[0]["nama_pelajaran"]["IPA"],
                                )


nem_didapatkan = jika ( hasil_return )
