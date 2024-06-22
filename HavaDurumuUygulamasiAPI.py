# API yapısı, bir uygulamanın içerisindeki işlevlerden bazılarını veya tamamını, başka bir uygulama tarafından kullanılabilmesidir.

import requests # type: ignore
import json

while True:

    Sehir = input("\nLütfen Hava Durumunu Öğrenmek İstediğiniz Şehri Giriniz: ")
    apikey = "9c5b53f9db32bd0b8b69adb91339e832"
    adres = f"https://api.openweathermap.org/data/2.5/weather?q={Sehir}&appid={apikey}&lang=tr&units=metric" #&lang api olarakta veriliyormuş, TR olarak seçtim. Kullanıcının seçmesinide isteyebilirdim.
    # units=metric ile santigrad olarak veriyi çekiyorum Apiden.
    baglan = requests.get(adres) # Siteye bağlanma talebini, requests.get metoduyla yapıyoruz.
    # Verileri liste halinde görmek için json formatına dönüştürmem lazım.
    sorgu = baglan.json() # Hizmet sağlayıcının verdiği bilgiler str yapısında, json ile kendi istediğim bir liste yapısına çevirmiş oldum.
    # print(type(sorgu)) # sorgu bir liste formatında oldu artık.
    # print(sorgu) # Hizmet sağlayıcının verdiği değerleri çekmiş oldum.
    # Tüm verileri istemiyorum artık, istediğim verileri bir değişkene atıyorum.
    
    HavaDurumu = sorgu["weather"][0]["description"] # weather içinde bir listede, onun için [0] indekse gittim.
    HavaSicaklik = sorgu["main"]["temp"]
    HissedilenHavaSicaklik = sorgu["main"]["feels_like"]
    MinSicaklik = sorgu["main"]["temp_min"]
    MaxSicaklik = sorgu["main"]["temp_max"]
    Basinc = sorgu["main"]["pressure"]
    Nem = sorgu["main"]["humidity"]
    
    print(f"\n{Sehir.capitalize()} İçin Hava Durumu Bilgileri Aşağıdaki Gibidir...\n\nSıcaklık: {HavaSicaklik}°\nHava Durumu: {HavaDurumu.title()}\nHissedilen Sıcaklık: {HissedilenHavaSicaklik}°\nEn Düşük Sıcaklık: {MinSicaklik}°\nEn Yüksek Sıcaklık: {MaxSicaklik}°\nBasınç: {Basinc} hpa\nNem: {Nem}%")
    
    
