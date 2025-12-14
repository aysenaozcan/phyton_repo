#1
import numpy as np
import pandas as pd
df = pd.read_csv('weather_data.csv', encoding='latin1')

#2
print("İlk 5 veriyi listeleyiniz:")
print(df.head())
print("Son 5 veriyi listeleyiniz:")
print(df.tail( ))
print("İstatiksel hesaplamaları listeleyiniz:")
print(df.describe())

#3
print("Date, City ve Temperature sütunları ile yeni bir görünüm elde ediniz;")
new_view=df[['Date', 'City', 'Temperature']]
print(new_view)
print("City ve Temperature kolonlarını birlikte listeleyiniz;")
print(df[['City', 'Temperature']])

#4
print("3o derece sıcaklığın üstündeki değerleri listeleyiniz:")
print(df[df['Temperature']>30 ])
print("City kolonu Bursa olan kayıtları listeleyiniz:")
print(df[df['City']=='Bursa'])

#5
print("Şehri İstanbul olan ve nem oranı (Humidity) 60'tan büyük olan kayıtları filtreleyiniz:")
print(df[(df['City'] == 'Istanbul') & (df['Humidity'] > 60)])
print("Şehri Ankara olan veya sıcaklığı 5 dereceden küçük olan kayıtları filtreleyiniz:")
print(df[(df['City']=='Ankara') | (df['Temperature']<5)])
print("Sıcaklığı 10°C altında veya nemi (Humidity) %70 üzerinde olan verileri filtreleyiniz:")
print(df[(df['Temperature']<10) | (df['Humidity']>70)])

#6
print("Veri setini Temperature (Sıcaklık) değerine göre büyükten küçüğe (azalan) sıralayın ve ilk 10 kaydı gösteriniz:")
print(df.sort_values('Temperature', ascending=False).head(10))
print("Veriyi neme göre azalan şekilde sıralayınız:")
print(df.sort_values('Humidity', ascending=False))
print("Veriyi Şehir alanına göre Artan şekilde sıralayanız.")
print(df.sort_values('City'))

#7
print("Veri setine Temperature_F adında yeni bir sütun ekleyiniz. Bu sütun, sıcaklığın Fahrenheit cinsinden değerini taşımalıdır:")
print(df.assign(Temperature_F = df['Temperature'] * 9/5 + 32))
print("FeelsLike isminde yeni bir kolon oluşturunuz:")
print(df.assign(FeelsLike = df['Temperature']-(df['Humidity']/100)))

#8
print("Her şehirde (City) kaç adet veri kaydı olduğunu hesaplayın:")
print(df.groupby('City')['City'].count())
print("Şehirlere göre ortalama sıcaklık (Temperature) değerlerini hesaplayın:")
print(df.groupby('City')['Temperature'].mean())

#9
print("En yüksek sıcaklığın olduğu satırı (tüm bilgilerini) bulun ve yazdırın:")
print(df.loc[df['Temperature'].idxmax()])
print("En düşük nem oranının olduğu satırı bulun ve yazdırın:")
print(df.loc[df['Humidity'].idxmin()])

#10
print("En yüksek sıcaklığın olduğu satırı (tüm bilgilerini) bulun ve yazdırın:")
ort_sicaklik = df.groupby('City')['Temperature'].mean()
ort_sicaklik.to_csv("sehir_sicakliklari.csv")
print("CSV dosyası kaydedildi.")


