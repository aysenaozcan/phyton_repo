# Linkedin: https://www.linkedin.com/in/enessoztrk/
# Her zaman, 7/24 dilediğiniz zaman bana tüm sorularınızı sorabilirsiniz.

print("Miuul Yapay Zeka Bootcampine Hoş Geldiniz...")

##############################################################
# PYTHON VERİ YAPILARI (DATA STRUCTURES)
##############################################################

##############################################################
# 1. ATAMALAR ve TEMEL TİPLER (Variables)
##############################################################

# Tamsayı (Cebimizdeki Nakit) --> integer
para = 200
print(para)

# Ondalıklı Sayı (Ürün Fiyatı) --> float
fiyat = 12.5
print(fiyat)
# ---------------------------- --> integer & float (matematiksel işlem yapılabilir)

# Metin --> string
ayakkabı = "fdgdfahdsgh"
print(ayakkabı)

# Mantıksal (Login Oldu mu?) --> Boolen
giris_yapildi_mi = True
print(giris_yapildi_mi)


##############################################################
# 2. TİP DÖNÜŞÜMLERİ (Type Casting)
##############################################################
# Bazen etiket fiyatını (12.5) düz hesap (12) yapmak isteriz.

sayi = 10.7

# Float -> Int (. atar)
int(sayi)

# Int -> Float (Sonuna .0 ekler)
float(para)


##############################################################
# 3. MATEMATİKSEL İŞLEMLER
##############################################################
a = 5
b = 10

# Çarpma
a * 3

# Üs Alma (Karesi)
a ** 2

# İşlem Önceliği (Parantez içi, çarpma/bölme, toplama/çıkarma)
int(a * b / 2)


##############################################################
# 4. KARAKTER DİZİLERİ (STRINGS)
##############################################################
# Metinler üzerinde doktor, cerrah gibi çalışabiliriz.

nereden_ogrenilir = "Miuul Data Science"

# Dilimleme (Slicing) -> [Başla : Bitir(ama dahil değil)]
nereden_ogrenilir[0:6]

# Metin Metodları
len(nereden_ogrenilir)

nereden_ogrenilir.upper()

nereden_ogrenilir.lower()

nereden_ogrenilir.replace("Data", "Veri")

"Data" in nereden_ogrenilir



# Peki ya birden fazla veriyi taşımak istersek???????????????
##############################################################
# 5. LİSTELER (LISTS) -> [ ]
##############################################################
# Market sepetiniz olduğunu düşünün, içine her şeyi atabilirsiniz.
# Sıralıdır, değiştirilebilir.

sepet = ["Elma", "Süt", "Ekmek", 100] # Farklı türler bir arada olabilir

# Elemana erişim (0'dan başlar)
sepet[0]

# Listeyi değiştirme
sepet[1] = "Çikolatalı Süt"

# Ekleme & Çıkarma
sepet.append("Yumurta")  # Sona ekler !

sepet.pop(0)             # İlk elemanı (Elma) sepetten at

# Ekstra
mixed = [1, 2, "a", True, [10, 20, 30]]

mixed[1]
mixed[4][1]

##############################################################
# 6. SÖZLÜKLER (DICTIONARY) -> { }
##############################################################
# Bir ürünün etiketi.
# "Anahtar" (Key) ve "Değer" (Value) vardır. Sıra önemli değildir.

urun = {
    "marka": "Nike",
    "fiyat": 2000,
    "renk": "Beyaz"
}

# Veriye erişim (Etiketi oku)
urun["marka"]

# Değer güncelleme (Zam geldi!)
urun["fiyat"] = 4000

# Yeni özellik ekleme
urun["beden"] = 42


##############################################################
# 7. DEMETLER (TUPLE) -> ( )
##############################################################
# T.C. Kimlik numaranız veya Doğum tarihiniz.
# Listeye benzer AMA DEĞİŞTİRİLEMEZ. Güvenlik içindir.

kimlik = ("Ali", 123456789)

kimlik[0]

# HATA ALIRIZ:
# kimlik[0] = "Veli" -> TypeError verir!


##############################################################
# 8. KÜMELER (SET) -> { }
##############################################################
# Piyango torbası.
# İçinde sıralama yoktur ve HER ELEMAN BİR KERE YAZILIR (Tekrarı sevmez).

sayilar = {1, 2, 2, 2, 3, 4}

print(sayilar)


##############################################################
# FONKSİYONLAR, KOŞULLAR VE DÖNGÜLER
##############################################################

##############################################################
# 1. FONKSİYONLAR (FUNCTIONS)
##############################################################
# Fonksiyonlar bizim "Küçük Robotlarımızdır".
# Bir kere tanımlarız, istediğimiz kadar çalıştırırız (DRY Prensibi).

# | Kısım          | Anlamı                                          |
# | -------------- | ----------------------------------------------- |
# | `def`          | Define (Tanımla). Robotun inşası başlıyor.      |
# | `calculate`    | Robotun adı. Çağırırken bu ismi kullanacağız.   |
# | `(x)`          | Parametre. Robota vereceğimiz hammadde.         |
# | `return/print` | Sonuç. Robotun bize vereceği ürün.              |


def calculate(x):
    print("İşlem sonucu:", x * 2)

# Robotu çalıştıralım:
calculate(5)

calculate(2)


# -----------------------------------------------------------
# Birden Fazla Parametre (Gelişmiş Robot)
# -----------------------------------------------------------

def summer(a, b):
    print(a - b)

summer(7, 8)

# Sırayı karıştırırsak ne olur?
summer(b=7, a=8)


##############################################################
# Docstring: Kullanma Kılavuzu Yazmak
##############################################################
# Yazdığımız fonksiyonun ne işe yaradığını başkalarına anlatmak için.

def summer(a, b):
    """
    İki sayının toplamını ekrana yazdırır.
    Args:
        a (int, float): Birinci sayı
        b (int, float): İkinci sayı
    Returns:
        None
    """
    print(a + b)

summer(2, 4)


##############################################################
# Fonksiyon Gövdesi (Body) ve Sıralama
##############################################################

def say_hi():
    print("Merhaba!")
    print("Hello!")

say_hi()

def multi(a, b):
    c = a * b                  # Hesapla
    print("Islem ciktisi:", c) # Yazdır

multi(10, 9)


##############################################################
# Global ve Local Değişkenler (Evin İçi vs Sokak)
##############################################################
# Local: Sadece fonksiyonun içinde yaşar.
# Global: Her yerden erişilebilir.

store = []  # Global sepet

def add_element(a, b):
    result = a * b                      # Local (iş bitince silinir)
    store.append(result)                # Global sepete ekle
    print("Sepetin durumu:", store)

add_element(2, 5)

add_element(3, 10)


##############################################################
# Default (Varsayılan) Parametreler
##############################################################
# Kullanıcı değer girmeyi unutursa ne olsun?

def divide(a, b=1):  # b girilmezse 1 kabul et
    print(a / b)

divide(10)

divide(10, 2)


##############################################################
# RETURN: Sonucu "Şu an veya daha sonra kullanmak için"
##############################################################
# print() sadece gösterir, return() sonucu verir her yerde kullanılabilir.
# Sonucu başka işlemde kullanacaksak return şarttır!

def calculate(sicaklik, nem, sarj):
    """Sıcaklık ve nem toplamını şarja bölerek döndürür."""
    return (sicaklik + nem) / sarj

result = calculate(98, 10, 20)      # Sonucu bir değişkene atadık
print("Hesaplanan Veri:", result * 10)           # Ve üzerinde işlem yaptık



##############################################################
# 2. KOŞULLAR (CONDITIONS - IF/ELIF/ELSE)
##############################################################
# Bir "Görevli" yazıyoruz.

def number_check(number):
    if number > 10:
        print(number, "10'dan büyüktür.")
    elif number < 10:
        print(number, "10'dan küçüktür.")
    else:
        print(number, "tam 10'dur!")

number_check(6)
number_check(10)


# Reşitlik Kontrolü
age = 15

if age >= 18:
    print("Reşitsiniz")
else:
    print("Reşit değilsiniz")


# Hava Durumu Asistanı
temperature = 40

if temperature > 30:
    print("Hava çok sıcak")
elif temperature > 20:
    print("Hava güzel")
else:
    print("Hava serin")


##############################################################
# 3. DÖNGÜLER (FOR LOOPS) - "Her Biri İçin..."
##############################################################
# Elimizdeki bir listenin her elemanı için aynı işlemi yapmak.

numbers = [1, 2, 3, 4, 5]
students = ["Ali", "Ayşe", "Mehmet", "Zeynep"] # Öğrenci listesi

# Sayıları Yazdır
for num in numbers:
    print("Sayı:", num)

# Karelerini Al
for num in numbers:
    print(num, "karesi:", num**2)

students = ["Ali", "Ayşe", "Mehmet", "Zeynep"] # Öğrenci listesi

for student in students:
    print(student.upper())


##############################################################
# 4. DÖNGÜLER (WHILE LOOPS) - "-e Kadar..."
##############################################################
# Bir koşul doğru olduğu sürece çalışmaya devam eder.

# Sayaç Örneği
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Geri Sayım
n = 5
while n > 0:
    print(n)
    n -= 1


##############################################################
# BREAK & CONTINUE (Dur ve Devam Et)
##############################################################
# Döngülerin akışını değiştirmek için kullanılır.

# BREAK: "Aradığını buldun, artık dur."
# Sayı 3'ü bulunca işlemi bitir.
numbers = [1, 2, 3, 4, 5]

for num in numbers: # okey
    if num == 3:
        break
    print("Break örneği:", num)


# CONTINUE: "Bunu beğenmedim, sonrakine geç."
# Sayı 3'ü atla, diğerlerini yazdır.
for num in numbers:
    if num == 3: # 1 no 2 no # 4
        continue
    print("Continue örneği:", num)


##############################################################
# UYGULAMA: Kelime Uzunluklarını Ölçme
##############################################################
# Bir metin analiz aracı yapıyoruz.

words = ["apple", "banana", "cat", "hi"]

for w in words:
    print(w, "→ uzunluk:", len(w))


# K A H V E   M A K İ N E S İ
# Kahve Makinesi Örneğini Birlikte Sıfırdan Kodlayalım...

# 1. FONKSİYONLAR (Görev Emirleri):
#    - "Bana kahve yap" (Fonksiyon)
#    - "Sıcaklığı 90 derece olsun" (Parametre)
#
# 2. KOŞULLAR (Karar Mekanizması):
#    - "Eğer" (if) su bittiyse -> "Uyarı ver"
#    - "Değilse" (else) -> "Kahveyi yapmaya devam et"
#
# 3. DÖNGÜLER (Seri Üretim):
#    - "Elimdeki 10 bardağın hepsi dolana kadar" (while/for)
#    - "Kahve doldurmaya devam et"
def kahve_yap(bardak_sayisi, su_var_mi=True):
    print("☕ Kahve makinesi çalışıyor...")

    if su_var_mi == False:
        print("❌ Su yok! Lütfen su ekleyin.")
        return

    bardak = 1  # sayaç

    while bardak <= bardak_sayisi:
        print(str(bardak) + ". bardak dolduruluyor...")
        bardak = bardak + 1

    print("✅ Tüm kahveler hazır! Afiyet olsun ☕")


kahve_yap(3, True)
kahve_yap(3, False)



##############################################################
# PYTHON İLE VERİ ANALİZİ - NUMPY KÜTÜPHANESİ
###############################################

import numpy as np

###############################################
# 1. NEDEN NUMPY?
###############################################
# Elimizdeki sayıların hepsini 2 ile çarpmak istiyoruz.

# YOL 1: Klasik Python (Döngü ile)
sayilar = [1, 2, 3, 4]
sonuc = []
for x in sayilar:
    sonuc.append(x * 2)

print("Klasik Python Listesi:", sonuc)


# YOL 2: NumPy (Vektörel İşlem)
# Döngü yok! Sanki tek bir sayıymış gibi tüm listeyi aynı anda çarpar.
import numpy as np

sayilar_np = np.array([1, 2, 3, 4])
print("NumPy Array Sonucu:", sayilar_np * 2)


###############################################
# 2. ARRAY OLUŞTURMA (VERİ KUTULARI)
###############################################
# Veriyi analiz etmek için önce onu NumPy formatına (Array) çevirmeliyiz.

# Listeden Array oluşturma
a = np.array([1, 2, 3, 4, 5])
print("Array:", a)

# Rastgele Notlar Üretme
# 0 ile 100 arasında rastgele 5 not üret.
notlar = np.random.randint(0, 100, size=5)
print("Rastgele Notlar:", notlar)


###############################################
# 3. ARRAY ÖZELLİKLERİ
###############################################
# Elimizdeki verinin şekli nedir?

a = np.random.randint(10, size=6)
print("Verimiz:", a)

# ndim: Boyut Sayısı (1 boyutlu dizi mi, 2 boyutlu tablo mu?)
print("Boyut Sayısı (ndim):", a.ndim)

# shape: Şekil (Kaç satır, Kaç sütun?)
print("Şekil (shape):", a.shape)


###############################################
# 4. YENİDEN ŞEKİLLENDİRME (RESHAPE)
###############################################
# Elimizdeki 9 parça legoyu (vektör),
# 3x3'lük bir kare (matris) yapmak istiyoruz.


a = np.arange(1, 10) # 1'den 9'a kadar sayılar
print("Düz Hali:", a)

matris = a.reshape(3, 3)
print("Kare Hali (3x3):", matris)


###############################################
# 5. INDEX VE SLICING (VERİYE ERİŞİM)
###############################################
# Verinin içinden istediğimiz parçayı çekmek.


a = np.array([10, 20, 30, 40, 50])

# İlk elemanı ver
print(a[0])

# 1. indexten 4. indexe kadar
print(a[1:4])

# Veri Güncelleme
a[0] = 999
print(a)


###############################################
# 6. KOŞULLU İŞLEMLER (FİLTRELEME)
###############################################
# Sınıfta notu 50'den düşük olanları bul.
# Veri analizinde en çok kullandığımız kısımdır.


notlar = np.array([20, 40, 60, 80, 10])

# NumPy'a soru soruyoruz: "Kimler 50'den küçük?"
print("Durum:", notlar < 50)

# Bu maskeyi veriye giydirip sadece True olanları alalım:
kalanlar = notlar[notlar < 50]
print("Kalanlar:", kalanlar)



###############################################
# 7. MATEMATİKSEL İŞLEMLER
###############################################
# Tüm veriye aynı anda işlem yapmak.
# Öğretmen herkese +10 puan kanaat notu verdi.

puanlar = np.array([50, 60, 70])

print("Herkesin yeni notu:", puanlar + 10)

# İstatistikler
print("Sınıf Ortalaması:", np.mean(puanlar))
print("En Yüksek Not:", np.max(puanlar))
print("En Düşük Not:", np.min(puanlar))


#############################################
# PYTHON İLE VERİ ANALİZİ - PANDAS
#############################################

import pandas as pd
import seaborn as sns

#############################################
# 1. PANDAS SERIES (TEK SÜTUNLU LİSTE)
#############################################
# DataFrame bir tablodur, Series ise o tablonun tek bir sütunudur.
# NumPy array'inden farkı: Her verinin bir "Etiketi" (Index) vardır.

puanlar = np.array([50, 60, 70])
type(puanlar)

s = pd.Series([10, 77, 12, 4, 5])

print("Tip:", type(s))

print("Index Bilgisi:", s.index)

print("Veri Tipi:", s.dtype)

print("Boyut:", s.size)

print("Değerler (NumPy hali):", s.values)

print("İlk 3 kayıt:", s.head(3))
s.head(3)

#############################################
# 2. VERİ OKUMA (READING DATA)
#############################################
# Veriler genelde dışarıdan gelir (CSV, Excel, SQL).
# pd.read_csv("dosya_yolu") komutu ile dosyayı içeri çekeriz.

df = pd.read_csv("breast_cancer.csv")
df.head()

df = sns.load_dataset("titanic")
df.head()


#############################################
# 3. VERİYE HIZLI BAKIŞ (CHECK-UP)
#############################################

print("İlk 5 Satır:", df.head())
print("Son 5 Satır:", df.tail())

print("Boyut (Satır, Sütun):", df.shape)

df.info()

print("Sütun İsimleri:", df.columns)

print(df.describe().T)

print("Hiç boş (Null) değer var mı?:", df.isnull().values.any())

print(df.isnull().sum())

print(df["sex"].value_counts())


#############################################
# 4. PANDAS'TA SEÇİM İŞLEMLERİ
#############################################
# Tablonun içinden istediğimiz satırı veya sütunu çekmek.
df.head()
# İndexlerde gezinme
print(df.index)
print(df[0:5])

# Silme İşlemi (Drop)
# axis=0 -> Satır siler
# axis=1 -> Sütun siler
print(df.drop(0, axis=0).head())

delete_indexes = [1, 3, 5, 7]
print(df.drop(delete_indexes, axis=0).head(2))

# KALICI SİLME (inplace=True)
df.drop(delete_indexes, axis=0, inplace=True)
# "inplace=True" demezsek değişiklik sadece ekranda görünür, veriye işlenmez!


##################################################
# 5. INDEX MANİPÜLASYONU (ETİKETLERİ DEĞİŞTİRME)
##################################################
# Bazen bir sütunu (mesela "age") satır etiketi yapmak isteriz.

# Yaş sütununu Index yapalım:
df.index = df["age"]
df.head()
# Age sütunu artık indexte olduğu için, normal sütunlardan silebiliriz.
df.drop("age", axis=1, inplace=True)
print(df.head())

# İndex'i tekrar değişkene (Sütuna) çevirmek:
# "Yaşları indexte tutmaktan vazgeçtim, geri tabloya al."
df["age"] = df.index
print(df.head())

# İkinci Yol: reset_index()
# Indexi sıfırlar ve eski indexi sütun olarak ekler.
df.drop("age", axis=1, inplace=True) # Önce temizleyelim
df = df.reset_index()
print("Resetlenmiş Hali:", df.head())


#############################################
# 6. DEĞİŞKENLER ÜZERİNDE İŞLEMLER
#############################################
#
# Sütun seçerken dikkat edilmesi gereken bir detay: Series mi, DataFrame mi?

# "age" sütunu var mı?
print("age" in df)

# DİKKAT:
type(df["age"])   # pandas.Series (Tek boyutlu)
type(df[["age"]]) # pandas.DataFrame (İki boyutlu - Tablo formatında)

# Birden fazla sütun seçme
print(df[["age", "alive"]].head())

col_names = ["age", "adult_male", "alive"]
print(df[col_names].head())

# YENİ SÜTUN OLUŞTURMA (Feature Engineering 101)
# Mevcut veriden yeni bilgi türetme.
df["age2"] = df["age"] ** 2            # Yaşın karesi
df["age3"] = df["age"] / df["age2"]    # Matematiksel işlem
print(df.head())

# Sütun Silme
df.drop("age3", axis=1).head()
df.drop(col_names, axis=1).head()



#############################################
# 6. SEÇİM İŞLEMLERİ
#############################################
# iloc (index location): GPS koordinatı gibidir. (0, 1, 2...)
# loc (location): Adres tarifi gibidir. (Etiket isimleri)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Tüm sütunları görebilmek için ayar
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")

df.head()

# iloc: "Bana 0'dan 3'e kadar olan satırları ver" (3 dahil DEĞİL)
print(df.iloc[0:3])

# loc: "Bana 0 ve 3 arasındaki etiketleri ver" (3 DAHİL!)
# loc ayrıca sütun ismiyle çalışmayı sever.
print(df.loc[0:3, "age"])

# Karma Seçim: "0-3 arası satırların, 'age' ve 'alive' sütunlarını getir"
col_names = ["age", "alive"]
print(df.loc[0:3, col_names])


#############################################
# 7. KOŞULLU SEÇİM (CONDITIONAL SELECTION)
#############################################
# "Yaşı 50'den büyük OLAN VE Erkek OLAN yolcuları bul."

# Adım Adım Filtreleme:
criteria = (df["age"] > 50) & (df["sex"] == "male")

# Bu kriterlere uyanların sadece yaş ve sınıf bilgisini getir:
filtered_df = df.loc[criteria, ["age", "class"]]
print(filtered_df.head())

# Yeni bir değişkene atayabiliriz:
print("Bulunan Kişi Sayısı:", filtered_df.shape[0])


#############################################
# 3. TOPLULAŞTIRMA (AGGREGATION & GROUPING)
#############################################
# "Hangi kategorinin hayatta kalma oranı daha yüksek?"
# Tek tek sayamayız. Gruplamamız lazım.

# Basit Ortalama
print("Tüm Yolcuların Yaş Ortalaması:", df["age"].mean())

# Gruplayarak Bakma (Cinsiyete göre yaş ortalaması)
print(df.groupby("sex")["age"].mean())


# Gelişmiş Rapor (Aggregation)
# "Cinsiyete göre grupla; Yaşın ortalamasını, Hayatta kalma durumunun ortalamasını al"
print(df.groupby("sex").agg({"age": "mean",
                             "survived": "mean"}))


# Pivot Table (Excel'in en sevilen özelliği)
# Satırda Cinsiyet, Sütunda Gemi Sınıfı olsun, Değerler Hayatta Kalma oranı olsun.
summary = df.pivot_table("survived",
                         index="sex",
                         columns="class")
print(summary)


#############################################
# 4. BİRLEŞTİRME (JOINS: MERGE & CONCAT)
#############################################
# İK departmanında veri bilimci olarak çalıştığınızı düşünelim.
# Bir dosyada çalışan isimleri, diğer dosyada işe giriş tarihleri var.
# Bunları eşleştirmeniz lazım.

# Tablo 1: Çalışanlar ve Departmanları
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

# Tablo 2: Çalışanlar ve İşe Giriş Yılları
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

merged_df = pd.merge(df1, df2, on="employees")
print(merged_df)


#############################################
# 5. VERİ GÖRSELLEŞTİRME (MATPLOTLIB & SEABORN)
#############################################
# "Bir resim bin satıra bedeldir."
# Veriyi anlamanın en hızlı yolu onu çizmektir.

# Sütun Grafik (Kategorik Değişkenler İçin)
# Gemide kaç kadın kaç erkek var?
df["sex"].value_counts().plot(kind='bar')
plt.title("Cinsiyet Dağılımı (Matplotlib)")
plt.show(block=True)

# Seaborn ile daha şık hali:
sns.countplot(x=df["sex"], data=df)
plt.title("Cinsiyet Dağılımı (Seaborn)")
plt.show(block=True)

# Histogram (Sayısal Değişkenler İçin)
# Yaş dağılımı nasıl? Genç mi yaşlı mı çok?
plt.hist(df["age"])
plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Kişi Sayısı")
plt.show(block=True)

# Boxplot (Kutu Grafiği)
# Bilet fiyatlarında uçuk kaçık değerler (Aykırı Değer) var mı?
sns.boxplot(x=df["fare"])
plt.title("Bilet Fiyatları Aykırı Değer Analizi")
plt.show(block=True)


#############################################
# GELİŞMİŞ KEŞİFÇİ VERİ ANALİZİ (EDA)
#############################################
# Elimize ham bir veri geldiğinde hemen model kurmaya başlamayız. Önce şu soruları sorarız:

# 1. Veri ne kadar büyük? Eksik var mı?
# 2. Hangi sütun sayı, hangi sütun kategori?
# 3. Kadın/Erkek oranı ne? Yaş ortalaması ne?
# 4. Bu özellikler hayatta kalmayı etkiledi mi?

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df = pd.read_csv("pythonProgramlama/python_for_data_science/data_analysis_with_python/datasets/application_train.csv")

#############################################
# 1. GENEL RESİM
#############################################
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)


#############################################
# 2. DEĞİŞKENLERİ AYRIŞTIRMA (GRAB COL NAMES)
#############################################
# - "Survived" (0-1) sayı gibi görünür ama aslında Kategoriktir (Öldü/Kaldı).
# - "Name" kategorik görünür ama Kardinaldir (Her satırda değişir, bilgi taşımaz).
#
# Bu fonksiyon elmaları (Sayısal) ve armutları (Kategorik) doğru sepetlere ayırır.

def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Gözlem Sayısı: {dataframe.shape[0]}")
    print(f"Değişken Sayısı: {dataframe.shape[1]}")
    print(f'cat_cols (Kategorik): {len(cat_cols)} -> {cat_cols}')
    print(f'num_cols (Sayısal): {len(num_cols)} -> {num_cols}')
    print(f'cat_but_car (Kardinal): {len(cat_but_car)} -> {cat_but_car}')

    return cat_cols, num_cols, cat_but_car

# Fonksiyonu çalıştırıp listeleri alalım
cat_cols, num_cols, cat_but_car = grab_col_names(df)


#############################################
# 3. KATEGORİK DEĞİŞKEN ANALİZİ
#############################################
# Sınıfların dağılımı nedir? (Kaç kadın, kaç erkek?)


def cat_summary(dataframe, col_name, plot=False):
    """
    Kategorik değişkenin sınıflarını ve yüzdelerini gösterir.
    İstenirse grafiğini çizer.
    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


print("\n--- KATEGORİK DEĞİŞKEN ANALİZİ BAŞLIYOR ---")
for col in cat_cols:
    # Bool tipindeyse grafikte hata vermemesi için int'e çevirip analiz et
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=False)
    else:
        cat_summary(df, col, plot=False)


#############################################
# 4. SAYISAL DEĞİŞKEN ANALİZİ
#############################################
# Sayıların dağılımı nedir? (Yaş ortalaması, min, max?)

def num_summary(dataframe, numerical_col, plot=False):
    """
    Sayısal değişkenin istatistiksel özetini verir.
    İstenirse Histogram grafiğini çizer.
    """
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


# Tüm sayısal değişkenleri inceleyelim
print("\n--- SAYISAL DEĞİŞKEN ANALİZİ BAŞLIYOR ---")
for col in num_cols:
    num_summary(df, col, plot=False)


#############################################
# 5. HEDEF DEĞİŞKEN ANALİZİ (TARGET ANALYSIS)
#############################################
# "Bu değişkenler sonucu (Survived) nasıl etkiledi?"
# Kadınların hayatta kalma oranı ne? 1. sınıf yolcuların oranı ne?

def target_summary_with_cat(dataframe, target, categorical_col):
    """
    Kategorik değişkenin kırılımında hedef değişkenin ortalamasını verir.
    """
    print(dataframe.groupby(categorical_col).agg({target: "mean"}), end="\n\n\n")


def target_summary_with_num(dataframe, target, numerical_col):
    """
    Hedef değişkenin kırılımında sayısal değişkenin ortalamasını verir.
    (Örn: Ölenlerin yaş ortalaması vs Hayatta kalanların yaş ortalaması)
    """
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


print("\n--- HEDEF DEĞİŞKEN (SURVIVED) ANALİZİ ---")

# 1. Kategorik değişkenlere göre hayatta kalma oranları
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)

# 2. Hayatta kalma durumuna göre sayısal değerlerin ortalaması
for col in num_cols:
    target_summary_with_num(df, "survived", col)




