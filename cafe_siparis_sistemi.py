import sqlite3  

baglanti = sqlite3.connect("kafe.db")
print("veritabanına bağlandık")
baglanti.close()

#Sipariş Tablosu Oluştur
def tablo_olustur():
    baglanti= sqlite3.connect("kafe.db")
    cursor = baglanti.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS siparisler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    musteri_adi TEXT NOT NULL,
    urun TEXT NOT NULL,
    fiyat INTEGER,
    adet INTEGER
    )
    """)
    baglanti.commit()
    baglanti.close()
    print("Tablo oluşturuldu")

tablo_olustur()

# 3. SİPARİŞ EKLEME
def ekle():

    baglanti = sqlite3.connect("kafe.db")
    cursor = baglanti.cursor()

    musteri_adi = input("Müşteri adı: ")
    urun = input("Ürün: ")
    fiyat = int(input("Fiyat: "))
    adet = int(input("Adet: "))

    cursor.execute(
        "INSERT INTO siparisler (musteri_adi, urun, fiyat, adet) VALUES (?, ?, ?, ?)",
        (musteri_adi, urun, fiyat, adet)
    )

    baglanti.commit()
    print("Sipariş başarıyla eklendi!")

    baglanti.close()

#ekle()

# 4. SİPARİŞ GÜNCELLEME
def guncelle():

    baglanti = sqlite3.connect("kafe.db")
    cursor = baglanti.cursor()

    siparis_id = int(input("Güncellenecek sipariş ID: "))

    musteri_adi = input("Yeni müşteri adı: ")
    urun = input("Yeni ürün: ")
    fiyat = int(input("Yeni fiyat: "))
    adet = int(input("Yeni adet: "))

    cursor.execute(
        """UPDATE siparisler
        SET musteri_adi = ?, urun = ?, fiyat = ?, adet = ?
        WHERE id = ?""",
        (musteri_adi, urun, fiyat, adet, siparis_id)
    )

    baglanti.commit()

    if cursor.rowcount > 0:
        print("Sipariş başarıyla güncellendi!")
    else:
        print("Bu ID ile kayıtlı sipariş bulunamadı.")

    baglanti.close()

#guncelle()

# 5. SİPARİŞ İPTALİ
def siparis_iptali():

    baglanti = sqlite3.connect("kafe.db")
    cursor = baglanti.cursor()

    siparis_id = int(input("İptal edilecek sipariş ID: "))

    cursor.execute(
        "DELETE FROM siparisler WHERE id = ?",
        (siparis_id,)
    )

    baglanti.commit()

    if cursor.rowcount > 0:
        print("Sipariş başarıyla iptal edildi!")
    else:
        print("Bu ID ile kayıtlı sipariş bulunamadı.")

    baglanti.close()

siparis_iptali()