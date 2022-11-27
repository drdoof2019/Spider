import os

# eğer proje dizini yoksa dizini oluşturur (proje adı ile)
def dosya_dizini_olustur(dizin_adi):
    if not os.path.exists(dizin_adi):
        print(f"Dizin oluşturuluyor: {dizin_adi}")
        os.makedirs(dizin_adi)

# dosya_dizini_olustur("sivasgovtr")

def veri_dosyaları_olustur(proje_adi, ana_url):
    kuyruk = proje_adi + '\kuyruk.txt'
    tamamlanan = proje_adi + r'\tamamlanan.txt'

    if not os.path.isfile(kuyruk):
        dosya_yazdirma(kuyruk, ana_url)
    if not os.path.isfile(tamamlanan):
        dosya_yazdirma(tamamlanan, '')

# dosya oluşturma fonksiyonu
def dosya_yazdirma(path, veri):
    with open(path, 'w', encoding='utf-8') as dosya:
        dosya.write(veri)

# veri_dosyaları_olustur("sivasgovtr", "https://www.sivas.edu.tr/")

# varolan dosyaya veri ekleme
def dosya_veri_ekleme(path, veri):
    with open(path, "a", encoding='utf-8') as dosya:
        dosya.write(veri + "\n")


# dosyanın içeriğini temizleyen fonksiyon
def dosya_icerik_silme(path):
    with open(path, 'w', encoding='utf-8') as dosya:
        pass


# bir dosyayı okuyup her satırını set(küme)'ye çeviren f'n
def dosyadan_kumeye(dosya_ismi):
    result = set()
    with open(dosya_ismi, 'rt', encoding='utf-8') as dosya:
        for line in dosya:
            result.add(line.replace('\n', ''))
    return result


# bir set'in üzerinde gezerek içerisindeki her elemanı yeni bir satır olacak şekilde dosyaya yaz
def kumeden_dosyaya(links, path):
    dosya_icerik_silme(path)
    for link in sorted(links):
        dosya_veri_ekleme(path, link)












