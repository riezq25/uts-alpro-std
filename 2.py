print("Hitung Pajak Tahunan Berdasarkan Penghasilan")

penghasilan = int(input("Masukkan Penghasilan Tahunan Anda:"))
mod = penghasilan-30000000

if penghasilan < 30000000:
    pajak = penghasilan*5/100
    print("Pajak = ", pajak)
elif penghasilan >= 30000000 and mod < 30000000:
    pajak2 = (30000000*5/100)+(mod*15/100)
    print("Pajak = ", pajak2)
elif penghasilan >= 30000000 and mod >= 30000000:
    pajak3 = (30000000*5/100)+(mod*20/100)
    print("Pajak = ", pajak3)
