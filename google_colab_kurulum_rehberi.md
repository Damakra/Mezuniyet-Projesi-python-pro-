# 📦 Gerekli Kütüphaneler (Google Colab için)

Bu projeyi **Google Colab** üzerinde çalıştırmak istiyorsanız, aşağıdaki kütüphaneleri yüklemeniz gerekmektedir.  

🔸 **UYARI:** Lütfen her komutu ayrı bir hücreye yazın. Google Colab’ın çalışma yapısı bu şekilde daha sağlıklı çalışacaktır.

---

# 📸 Görüntü işleme için gerekli kütüphane
!pip install Pillow==9.1.0

Pillow, Python'da resim dosyalarını açmak, düzenlemek ve kaydetmek için kullanılır. Modelinize gönderilen görsellerin yeniden boyutlandırılması bu kütüphane ile yapılır.

---

# 💾 Model dosyasını zip'ten çıkarmak için
!unzip ./converted_keras.zip

converted_keras.zip dosyası içinde eğitimli makine öğrenmesi modeli (keras_model.h5) ve etiket dosyası (labels.txt) yer alır. Bu komutla bu dosyalar açılır.

---

# 🧠 Derin öğrenme modelleri için Keras
!pip install keras==2.12.0

Keras, TensorFlow ile çalışan, kullanıcı dostu bir yapay sinir ağı kütüphanesidir. Modeliniz bu yapı ile oluşturulmuşsa, bu kütüphane olmazsa çalışmaz.

---

# 🔧 Makine öğrenimi için temel kütüphane
!pip install tensorflow==2.12.0

TensorFlow, derin öğrenme projelerinin temelini oluşturan kütüphanedir. Modeli çalıştırmak ve tahmin almak için gereklidir.

---

# 🔄 Asenkron işlemlerin Google Colab'da çalışması için
!pip install nest-asyncio

nest_asyncio, Google Colab gibi ortamlarda asyncio tabanlı kütüphanelerin düzgün çalışmasını sağlar. Discord botu asenkron çalıştığı için gereklidir.

---

# 💬 Discord botu için gerekli ana kütüphaneler
!pip install discord
!pip install discord.py

Bu iki kütüphane, Python ile Discord botları geliştirmeni sağlar. discord.py aktif geliştirilen kütüphanedir, diğer discord paketi ise ek destek içerebilir.

---
