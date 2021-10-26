#Menyimpan markah setiap murid dalam senarai
murid_1 = [87, 70, 80, 78]
murid_2 = [95, 80, 65, 75]
murid_3 = [74, 85, 90, 85]
murid_4 = [55, 85, 71, 68]
murid_5 = [65, 78, 68, 65]

nama = ["Ali bin Azmi", "Aminah binti Yusof", "Chong Yee Ling", "Dayang Minsu",
"Denish A/L Kathigasu"]


jumlah_1 = sum(murid_1)#87, 70, 80, 78
jumlah_2 = sum(murid_2)#95, 80, 65, 75
jumlah_3 = sum(murid_3)
jumlah_4 = sum(murid_4)
jumlah_5 = sum(murid_5)

jumlah = [jumlah_1, jumlah_2, jumlah_3, jumlah_4, jumlah_5]

tertinggi = max(jumlah)
terendah = min(jumlah)
indeks_tertinggi = jumlah.index(tertinggi) #jumlah.index(max(jumlah))
indeks_terendah = jumlah.index(terendah)

murid_markah_tertinggi = nama[indeks_tertinggi]
murid_markah_terendah = nama[indeks_terendah]

print(murid_markah_tertinggi, "memperoleh jumlah markah tertinggi, iaitu ", tertinggi)
print(murid_markah_terendah, "memperoleh jumlah markah terendah, iaitu ", terendah)