import os, sys, time, socket , random
#uwwu

h='\33[0;32m' #hijau
ht='\33[32;1m' #hijauterang
b='\033[34;1m' #biru
k='\33[93;1m' #kuning
e='\33[93;2m' #emas
me='\33[31;1m' #merah
cy='\033[36;1m' #cyan
u='\033[35;1m' #ungu
pu='\33[37;1m' #putih
hi='\33[30;1m' #hitam
hp='\33[92;7m' #hijauputih
x='\33[0m' #reset

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


def usage():
	os.system("clear")
	print
	mengetik(ht+"Dear Kamu,\33[31;1mYa Kamu , \33[0;32mYang Sedang Baca Ini")
	mengetik(b+"Kamu Mau Gak Jadi Pacar Aku")
	mengetik(me+"Aku Suka Sama Kamu:)")
	print
	print k+"1"+me+")"+ht+" Iya,Aku Terima"
	print k+"2"+me+")"+me+" Tidak,Maaf Kita Temenan Aja"
	print k+"3"+me+")"+k+" Aku Masih Ragu"
	print k+"4"+me+")"+u+" Tunggu Aku Pikirin Dulu"
	print
	love =raw_input(b+"Pilih Nomernya:)"+k+":"+ht)
	if love == '1' or love =='01':
	       mengetik(ht+"Makasih Yah Yang,Sudah Mau Nerima Aku Apa Adanya")
	print
	if love == '2' or love =='02':
	       mengetik(me+"Yaudah Aku Hargai,Makasi Telah Mewarnai Hidupku,Aku Terima Keputusanmu,Walau Sakit")
	       print
	if love == '3' or love == '03':
	       mengetik(k+"Owh,Gpp,Tenangkan Dulu Hatimu,Pikirkan Saja Dulu,Yang Terpenting,Aku Selalu Terima Keputusanmu")
	       print
	if love == '4' or love == '04':
	       mengetik(u+"Pikir Kan Saja Dulu,Aku Akan Tetap Setia Menanti Jawabanmu")
	       print
	

if __name__ == '__main__':
    usage()


