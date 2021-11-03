# CENG 111 - LAB1 (FALL 2021)

## Genel Bilgiler

1. Duyurular [ODTUCLASS](https://odtuclass.metu.edu.tr) üzerinden yapılacaktır. Duyuru geldiği zaman, **eXXXXXX@metu.edu.tr** hesabınıza bilgi e-mail'i gönderilecektir. E-mail hesaplarınızı her gün **en az bir defa** kontrol etmelisiniz. Aynı şekilde **eXXXXXXX@ceng.metu.edu.tr** adresinizi de kontrol etmelisiniz.
2. Ceng111 dersinin [web sayfasında](http://ceng.metu.edu.tr/ceng111) ders programı vs. yanında ekstra öğrenim materyalleri de mevcuttur.
3. Görünüşe göre **21 Aralık** dışında her hafta salı lab var(**Section2 için**).
4. Önümüzdeki **3** labda, linux komutlarını öğreneceğiz. **4.** labda ise **LINUX QUIZ** olacak.
5. **LINUX QUIZ**'den sonra, python ile programlamayı öğrenmeye başlayacağız ve her hafta bir önceki hafta öğrendiklerimizle ilgili quiz olacak.
6. Linux komutlarını öğrenirken [Lab Manual](https://user.ceng.metu.edu.tr/~ceng111/lab_manual_2014.pdf)'e göz gezdirerek öğreneceğimiz konular hakkında fikir sahibi olunması yararlı olacaktır.
7. [COW](https://cow.ceng.metu.edu.tr/)' da duyurular yapılmaktadır. Burayı da düzenli bir şekilde kontrol etmek gerekiyor.

## Ubuntu kurulumu hakkında

1. Windowun yanına Ubuntu'yu kurabilirsiniz (dual boot). Computer Club'ın hazırlamış olduğu [Windows'da Ubuntu Yüklü USB Oluşturma](https://www.youtube.com/watch?v=14dUdnKGLlY) ve [Windows'un Yanına Ubuntu Kurulumu (Dual Boot)](https://www.youtube.com/watch?v=6GywlAIJ8F4) vidyolarında kurulumun nasıl yapıldığı anlatılmaktadır.
2. İlk seçenek yerine sanal makine kurarak (**VirtualBox**) hali hazırda kullandığınız işletim sistemi yanına ubuntu kurabilirsiniz. Nasıl yapılacağıyla ilgili şu [tutorial](https://www.youtube.com/watch?v=x5MhydijWmc)'ı inceleyebilirsiniz.

# Linux'a giriş

Lablarımızda bilgisayarlar(inekler) Linux işletim sisteminin Ubuntu dağıtımı kullanılmaktadır. Ilerleyen sınıflarda, bölüm ödevleri ve projelerinde işleri rahat sürdürebilmek için Linux dağıtımlarında komut satırında(terminal) temel işlemleri yapmayı öğrenmek gerekir.


1. **Dosya(File)**: Dosyalar içerisinde bilgi depolayan elemanlardır. İçindeki bilgi birbirinin ardına eklenen **byte**'lardan oluşur.
2. **Klasör(Directory)**: Dosyaları gruplamak için kullanılan elemanlardır. Her **dosya** bir klasör içinde bulunmalıdır. Klasörler, dosyaları gruplandırarak daha kolay bulmamızı sağlar.

## Linux Klasör Yapısı

Linux dağıtımlarında klasörler aşağıdaki ağaç yapısı şeklindedir.

![linux klasör ağaç yapısı](resources/lab1Resources/linuxKlasorAgacYapisi.png)

Ağacın en tepesinde özel "**/** " sembolüyle belirtilen root klasörü vardır. **Root**, linux işletim sisteminde bütün dosya ve klasörleri içeren klasördür. Yani klasör ağaç yapısının en tepesinde yer almaktadır.

## Peki ineklerde terminal açınca ya da login olunca hangi klasörde başlıyoruz?

İneklerde ssh ile login olduğumuz zaman veya lablarda terminal açtığımızda ismi kendi kullanıcı adımız (**eXXXXXXX**) olan klasörde başlıyoruz. Bu klasör bizim "**home**" klasörümüzdür. **Home** klasörünü "**~**" sembolüyle gösteririz.

Örneğin labda 11. inek'te login olup terminal açtığımızda;

```bash
eXXXXXXX@inek11:~$
```

gibi bir komut satırını görürüz. Burada;

- **eXXXXXXX**: kullanıcı adı
- **inek11**: host makinanın adı
- **~**: içinde bulunduğumuz klasör

### PATH KAVRAMI

Linux klasör sistemindeki ağaç yapısını düşünecek olursak bu yapıdaki yukarıdan aşağı yönlü çizebileceğimiz yollara **PATH** denir.

Bu durumda **home** klasörümüzün **PATH**'i "**/home/bsXX/eXXXXXXX**" olacaktır.

Bölümümüzde öğrencilerin kendilerine ait **home** klasörleri **bsXX** şeklinde klasörler içinde toplanmıştır. Ve her **bsXX** klasörü içinde **eXXXXXXX** şeklinde öğrenci klasörleri bulunmaktadır.

Örnek olarak **e2098929** kullanıcı adına sahip öğrencinin **home** klasörünün **PATH**'i aşağıda gösterilmiştir.

![Login olunca home nerede](resources/lab1Resources/loginOluncaHomeNerede.png)

Klasörlerin **PATH** lerini **3** şekilde ifade edebiliriz.

- Root(" / ") klasöründen itibaren söz konusu klasöre kadar olan **path** şeklinde (**absolute path**)
- İçinde bulunduğumuz klasöre göre (**relative path**)
- Home klasörü ('~') ne göre (**relative path to home**)

Yukarıdaki resme göre şu anda **/home/bs06** klasöründe bulunduğumuzu düşünelim. Bu klasörden **/home/bs06/e2098929** klasörüne giden **path**'i 3 şekilde de yazabiliriz;

- "**/home/bs06/e2098929**" (**absolute path**)
- "**e2098929**" (**relative path**)
- "**~**" (**relative path to home**)

Dosyaların **path**'leri de aynı klasörler gibi yazılır.

## Permissions

Her dosya ve klasörün güvenlik nedeniyle izinleri vardır (**permissions**). Bu izinler kullanıcı tipine göre 3 gruba(**owner**,**group**,**other**) ayrılmıştır ve her gruba özel 3 adet(**read**,**write**,**execute**) izin tipi vardır.

<br/>

![Permissions](resources/lab1Resources/permissions.png)

yukarıdaki resimde **r**, **w** ve **x** 'lerin değerleri 0 ya da 1 olabilir. Buna göre. 0 ise izin yok, 1 ise izin var demektir;

- **r -> read**: Dosya için izin varsa okunabilir. Klasör için izin varsa içindeki elemanları görüntüleyebiliriz.
- **w -> write**: Dosya için izin varsa dosyayı değiştirebiliriz. Klasör için izin varsa içinde yeni dosyalar/klasörler oluşturup silebiliriz.
- **x -> execute**: Dosya için izin varsa dosyayı çalıştırabiliriz. Klasör için izin varsa o klasörün içine girebiliriz.

Yukarıdaki resimde owner, group ve other için ayrı **r**, **w** ve **x** izinlerinin olduğunu gördük. Bu izinler 0 ya da 1 olabiliyor.

## LAB1 KOMUTLAR

- `cd`






