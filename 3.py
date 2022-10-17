from datetime import date, datetime
import random
import prettytable


def randomName():
    firstNames = ['John', 'Jane', 'Bob', 'Alice',
                  'Mary', 'Joe', 'Tom', 'Sue', 'Bill', 'Sally']
    lastNames = ['Smith', 'Jones', 'Brown', 'Johnson', 'Williams',
                 'Miller', 'Davis', 'Wilson', 'Moore', 'Taylor']
    return firstNames[random.randint(0, len(firstNames) - 1)] + ' ' + lastNames[random.randint(0, len(lastNames) - 1)]


def generateDataMahasiswa(count):
    data = []
    for i in range(count):
        mhs = {
            'nim': datetime.today().strftime('%Y%m') + str(i),
            'nama': randomName(),
            'tugas': random.randint(40, 100),
            'quiz': random.randint(40, 100),
            'uts': random.randint(40, 100),
            'uas': random.randint(40, 100),
        }
        data.append(mhs)
    return data


def hitungGrade(nilai):
    if nilai >= 91:
        return 'A'
    elif nilai >= 80:
        return 'B+'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 70:
        return 'C+'
    elif nilai >= 60:
        return 'D'
    else:
        return 'E'


def formatDouble(value):
    return "{:.2f}".format(value)


def hitungNilaiAkhir(mahasiswa):
    for mhs in mahasiswa:
        nilaiAkhir = mhs['tugas'] * 0.2 + mhs['quiz'] * \
            0.2 + mhs['uts'] * 0.3 + mhs['uas'] * 0.3
        mhs['nilai_akhir'] = formatDouble(nilaiAkhir)
        mhs['grade'] = hitungGrade(float(mhs['nilai_akhir']))
    return mahasiswa


def printTableMahasiswaAwal(mahasiswa):
    table = prettytable.PrettyTable()
    table.field_names = ['NIM', 'Nama', 'Tugas', 'Quiz', 'UTS', 'UAS']
    for mhs in mahasiswa:
        table.add_row([mhs['nim'], mhs['nama'], mhs['tugas'],
                      mhs['quiz'], mhs['uts'], mhs['uas']])
    print(table)


def printTableMahasiswa(mahasiswa):
    table = prettytable.PrettyTable()
    table.field_names = ['NIM', 'Nama', 'Tugas',
                         'Quiz', 'UTS', 'UAS', 'Nilai Akhir', 'Grade']
    for mhs in mahasiswa:
        table.add_row([mhs['nim'], mhs['nama'], mhs['tugas'], mhs['quiz'],
                      mhs['uts'], mhs['uas'], mhs['nilai_akhir'], mhs['grade']])
    print(table)


def hitungJumlahGrade(mahasiswa):
    data = {
        'A': 0,
        'B+': 0,
        'B': 0,
        'C+': 0,
        'D': 0,
        'E': 0
    }
    for mhs in mahasiswa:
        data[mhs['grade']] += 1
    return data


def printDataGrade(grades):
    table = prettytable.PrettyTable()
    table.field_names = ['Grade', 'Jumlah']
    for grade in grades:
        table.add_row([grade, grades[grade]])

    print(table)


mahasiswaAwal = generateDataMahasiswa(10)
print('Data Mahasiswa')
printTableMahasiswaAwal(mahasiswaAwal)

print('\n==================================\n')

nilaiMahasiswa = hitungNilaiAkhir(mahasiswaAwal)
print('Data Nilai Mahasiswa')
printTableMahasiswa(nilaiMahasiswa)

print('\n==================================\n')
grades = hitungJumlahGrade(nilaiMahasiswa)
print('Data Nilai Mahasiswa')
printDataGrade(grades)
