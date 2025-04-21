# ♻️ Akıllı Geri Dönüşüm Discord Botu

Bu proje, yapay zeka destekli bir Discord botudur. Kullanıcılardan gelen **resimleri analiz ederek**, görseldeki atığın **cam, kağıt veya plastik** olduğunu tahmin eder ve buna göre **geri dönüşüm ve değerlendirme önerileri** sunar. Hem çevre bilincini artırmak hem de eğlenceli bir deneyim sunmak amaçlanmıştır. 🌍

# 📌 Bilgilendirme

⚠️ Bu proje Google Colab ortamında geliştirilmiştir.
Eğer siz de Google Colab kullanarak çalıştırmak isterseniz, proje dizininde yer alan `google_colab_kurulum_rehberi.md` dosyasını inceleyebilir ve gerekli pip komutlarını oradan alabilirsiniz.
Böylece kurulum süreci çok daha hızlı ve sorunsuz ilerleyecektir.

## 🔧 Kullanılan Teknolojiler
- **Python 3**
- **TensorFlow & Keras**: Görsel sınıflandırma modeli
- **discord.py**: Discord bot altyapısı
- **Pillow**: Görsel işleme
- **NumPy**: Görsel verilerle çalışma
- **nest_asyncio**: Google Colab uyumluluğu için

## 🚀 Botun Özellikleri
- 📷 Kullanıcıdan gelen görseli işler ve sınıflandırır.
- 🧠 Eğitimli makine öğrenmesi modeli ile tahmin yapar.
- 💬 Discord üzerinden bilgi verir:
  - Atık türüne göre **geri dönüşüm bilgilendirmesi**
  - Alternatif **değerlendirme fikirleri**
  - Komutlarla bilgi alma özelliği (örn. `$help`, `$cam değerlendirme`, `$plastik geri dönüşüm` vs.)

## 💬 Örnek Komutlar
| Komut | Açıklama |
|-------|----------|
| `$help` | Tüm komutları listeler |
| `$cam değerlendirme` | Camları nasıl değerlendirebileceğini söyler |
| `$plastik geri dönüşüm` | Plastiklerin geri dönüşüm süreçlerini anlatır |
| ... | Daha fazlası botta seni bekliyor! |

## 📁 Dosya Yapısı
- `keras_model.h5` → Görsel sınıflandırma için eğitilmiş model
- `labels.txt` → Modelin sınıflandırma etiketleri
- `main.py` → Discord bot kodları
- `/gonderilmis_resimler` → Kullanıcıdan gelen geçici resimler

## 🌱 Projenin Amacı
Bu proje ile bireylerin atıkları hakkında daha fazla bilgi edinmesini ve **geri dönüşüm kültürünü eğlenceli bir şekilde yaymayı** hedefliyorum. Çevre bilinci, teknolojiyle buluştuğunda gerçekten etkili çözümler ortaya çıkabiliyor.

## 📌 Kurulum & Kullanım
1. Gerekli kütüphaneleri yükleyin:
    ```
    pip install tensorflow==2.12.0 keras==2.12.0 Pillow==9.1.0 discord.py nest_asyncio
    ```
2. `main.py` dosyasına kendi Discord bot token’ınızı girin.
3. Botu çalıştırın ve Discord sunucunuzda keyfini çıkarın!

## 🔐 Uyarı
Lütfen kendi **Discord bot token'ınızı** `main.py` içinde `"BOT TOKEN"` yazan yere yerleştirmeyi unutmayın. Token’ı kimseyle paylaşmayın.

---
