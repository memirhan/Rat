
# Remote Access Trojan (RAT)

Bu proje, Python programlama dili kullanılarak geliştirilmiş bir Remote Access Trojan (RAT) scriptidir. RAT, kötü niyetli kişilerin hedef bilgisayara veya cihaza uzaktan erişim sağlamasına olanak tanıyan bir tür zararlı yazılımdır. Bu tür yazılımlar, hedef bilgisayar üzerinde tam kontrol sağlayarak kullanıcının farkında olmadan çeşitli işlemler gerçekleştirebilir.

## Özellikler

- Hedef PC’den Dosya İndirme: Saldırgan, hedef bilgisayarın dosya sistemine erişerek, uzaktaki cihazdan istediği dosyayı kendi sistemine indirebilir. Bu, kritik verilerin çalınması veya önemli belgelerin ele geçirilmesi gibi tehlikeli sonuçlar doğurabilir.
- Dosya Yükleme: Saldırgan, kendi bilgisayarından hedef bilgisayara dosya yükleyebilir. Bu, kötü amaçlı yazılımlar veya zararlı kodlar yerleştirilerek hedef cihazın işlevselliğine zarar verilmesi ya da daha fazla erişim sağlanması amacıyla kullanılabilir.
- Dosya Oluşturma: RAT scripti, hedef bilgisayarda uzaktan dosya oluşturma yeteneğine sahiptir. Bu, saldırganın belirli komut dosyaları ya da yeni zararlı yazılımlar ekleyerek sistem üzerinde daha fazla kontrol sağlamasına yardımcı olabilir.
- Dosya Silme: Hedef bilgisayarda mevcut dosyalar saldırgan tarafından silinebilir. Bu, kritik dosyaların kaybolmasına veya hedef sistemin işleyişinin bozulmasına neden olabilir.
- Bilgisayara Yerleşme: RAT scripti, hedef cihazda kalıcı hale gelme özelliğine sahiptir. Yani bilgisayar her açıldığında otomatik olarak başlatılabilir ve böylece sürekli uzaktan erişim sağlanabilir. Bu genellikle sistem başlangıcında çalışan dosyalara veya kayıt defteri (Windows için) gibi kalıcı depolama noktalarına kendini yerleştirerek gerçekleştirilir.

  
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/memirhan/Rat
```

Proje dizinine gidin

```bash
  cd Rat
```

Dinleyiciyi çalıştırın

```bash
  python dinleyici.py
```
  
## Geri Bildirim

Projeyi geliştirmek, eksik yönlerini bildirmek vb. lütfen memirhansumer@gmail.com adresinden bana ulaşın.

  