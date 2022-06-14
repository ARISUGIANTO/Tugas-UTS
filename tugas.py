# aplikasi sederhana berbasis python

print('''==============Konversi bilangan ke huruf==========
---------------------selamat mencoba-----------------------'''
      )


class Nilai_mahasiswa:
    def Cetak_nama():
        # untuk menampilkan macam macam ket nilai
        nilai = ('A : baik ', 'B : cukup baik', 'C : cukup ',
                 'D : kurang ', 'E :kurang sekali')
        for i in nilai:
            print(i)
        # berfungsi untuk mengimputan nilai mahasiswa
        nilai = int(input('masukan nilai dalam angka 1-100: '))

        hasil = "tidak ada"

        if nilai <= 100 and nilai > 80:
            hasil = 'A = Lulus'
        elif nilai <= 80 and nilai > 60:
            hasil = 'B Lulus'
        elif nilai <= 60 and nilai > 40:
            hasil = 'C = Lulus'
        elif nilai <= 40 and nilai > 20:
            hasil = 'D =  Lulus'
        elif nilai <= 20 and nilai >= 0:
            hasil = 'E = Tidak Lulus'
        print('Nilai {} =  {}'.format(nilai, hasil))


x = Nilai_mahasiswa
x.Cetak_nama()
