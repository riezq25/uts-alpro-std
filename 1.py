def getBonus(pembelian):
    if pembelian >= 30000000:
        return "Tiket PP Malaysia"
    elif pembelian < 30000000 and pembelian >= 12000000:
        return "Tiket ke Mataram"
    elif pembelian < 12000000 and pembelian >= 6000000:
        return "Tiket ke Bali"
    elif pembelian < 6000000 and pembelian >= 2000000:
        return "Diskon 5%"
    else:
        return "Tidak ada bonus"


pembelian = int(input("Masukkan total pembelian: "))
bonus = getBonus(pembelian)
print("Jumlah pembelian: ", pembelian)
print("Bonus yang didapat: " + bonus)
