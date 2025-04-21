#Eklediğim kütüphaneler:
import discord
from discord.ext import commands
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow import keras
import nest_asyncio
import os
nest_asyncio.apply()


#Modelin yüklendiği kısım:
  #Eğitimini önceden yaptığım yapay zeka modelini buradan yüklüyoruz. 
  #Bu model, gönderilen görselin cam, kağıt veya plastik olup olmadığını % doğrulukla tahmin eder.
model = tf.keras.models.load_model("keras_model.h5")


#Etiketlerin Yüklenmesi:
  #Her tahmin edilen sınıfın karşılığında bir etiket var.
  #(örneğin: "Plastik", "Cam", "Kağıt") Bunları bu dosyadan okuyoruz.
with open("/content/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]


#tensorflow sürümünü kontrol edildiği yer. (isteğe bağlı)
print(tf.__version__)


#Görsellerin Kaydedileceği Klasör:
  #Kullanıcıdan gelen görseller geçici olarak bu klasöre kaydediliyor, analiz ediliyor. Sonra silinebilir.
image_save_dir = '/content/gonderilmis_resimler'
os.makedirs(image_save_dir, exist_ok=True)


#get_class Fonksiyonu:
  #Bu fonksiyon görseli işler, modele gönderir ve sonucunda hangi atık türü olduğunu bize verir.
def get_class(model, labels_path, image_path):
    with open(labels_path, 'r') as f:
        labels = f.read().splitlines()

    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    class_index = np.argmax(predictions, axis=1)[0]
    return class_index, labels[class_index]

#Discord Botunun Tanımlanması:
  #Botumuz burada tanımlanıyor. Gerekli izinlerle birlikte on_ready ve on_message gibi olaylara tepki veriyor.
ayricaliklar = discord.Intents.default()
ayricaliklar.message_content = True
istemci = discord.Client(intents=ayricaliklar)


@istemci.event
async def on_ready():
    print(f'{istemci.user} olarak giriş yaptık')


@istemci.event
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(image_save_dir, file_name)  #Resmin kaydedildiği yer.
            await attachment.save(file_path)
            class_index, class_label = get_class(model, "labels.txt", file_path)
            
            if class_index == 0:
                await message.channel.send(
                    "**Bu bir cam atıktır.**\n"
                    "Cam doğada yok olması milyonlarca yıl sürebilen bir materyaldir. Ancak iyi haber şu ki, cam %100 oranında geri dönüştürülebilir.\n"
                    "♻️ Bu camı atmak yerine, temizleyip dekoratif bir obje, mumluk ya da saklama kabı olarak değerlendirebilirsin.\n"
                    "⚠️ **Eğer cam kırılmışsa**, güvenlik için iki kat poşete sararak veya sağlam bir kutuya koyarak geri dönüşüm kutusuna atmalısın.\n"
                    "👉 Eğer geri dönüşüme göndermek istersen, cam atık kutularına bırakmayı unutma!"
                )

            elif class_index == 1:
                await message.channel.send(
                    "**Bu bir kağıt atıktır.**\n"
                    "Kağıtlar doğada daha hızlı çözülebilir ancak ağaç kesimi nedeniyle doğaya ciddi zararlar verebilir.\n"
                    "📚 Bu kağıdı not kağıdı olarak tekrar kullanabilir ya da çocuklar için origami/karton oyuncaklar yapabilirsin.\n"
                    "⚠️ **Yağlı, kirli veya ıslak kağıtlar geri dönüştürülemez!** Bu türleri çöpe atmalısın.\n"
                    "👉 Kirlenmemişse mutlaka geri dönüşüm kutusuna at!"
                )

            elif class_index == 2:
                await message.channel.send(
                    "**Bu bir plastik atıktır.**\n"
                    "Plastik, doğada çözülmesi binlerce yıl süren ve çevreye ciddi zararlar verebilen bir materyaldir.\n"
                    "🌱 Tekrar kullanabileceğin şişeleri sulama kabı, kalemlik ya da saksı haline getirebilirsin.\n"
                    "⚠️ **Etiketli, kirli veya içinde sıvı kalan plastikler geri dönüşüm sürecini bozar!** Lütfen temizle ve kurut.\n"
                    "👉 Geri dönüştürülemeyecek plastikleri doğaya bırakma, ilgili atık kutularına yönlendir!"
                )

    if message.author == istemci.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Selam!')

    elif message.content.startswith("$bye"):
        await message.channel.send("Hoşçakal! :slight_smile:")

    elif message.content.startswith("$help"):
        await message.channel.send(
            "Merhaba! Beni kullanmaya başlamak için aşağıdaki komutları kullanabilirsin:\n\n"
            "🖐 **Genel Komutlar:**\n"
            "$hello: Selam ver!\n"
            "$bye: Hoşça kal!\n"
            "$help: Yardım al!\n\n"

            "♻️ **Atık Değerlendirme Komutları:**\n"
            "$karton değerlendirme: Karton kutularını nasıl değerlendirebileceğinle ilgili bilgi al!\n"
            "$cam değerlendirme: Cam atıklarını nasıl değerlendirebileceğinle ilgili bilgi al!\n"
            "$plastikleri değerlendirme: Plastik atıkları nasıl değerlendirebileceğinle ilgili bilgi al!\n\n"

            "🔄 **Geri Dönüşüm Bilgisi Komutları:**\n"
            "$kağıt geri dönüşüm: Kağıtların geri dönüşümünü öğren!\n"
            "$cam geri dönüşüm: Cam atıkların geri dönüşümünü öğren!\n"
            "$plastik geri dönüşüm: Plastiklerin geri dönüşümünü öğren!\n\n"

            "İhtiyacın olduğunda sadece komutları yazman yeterli!"
        )

    elif message.content.startswith('$karton değerlendirme'):
        await message.channel.send(
            "Karton kutularını değerlendirmek için pek çok yaratıcı fikrin var! 📦\n\n"
            "🔄 **Değerlendirme Fikirleri:**\n"
            "- Karton kutu içerisine eşyalarını yerleştirip kullanabilirsin.\n"
            "- Yaratıcı projeler için kartonları kesip, boyayarak dekoratif objeler yapabilirsin.\n"
            "- Kartonları birleştirerek kalemlik, telefon tutacağı veya küçük bir sehpa yapabilirsin.\n"
            "Pinterest'teki fikirlerden ilham almak istersen, işte sana bir liste: "
            "[Karton Kutu Değerlendirme Fikirleri](https://tr.pinterest.com/semrayilmazoglu/karton-kutu-de%C4%9Ferlendirme/)"
        )

    elif message.content.startswith("$cam değerlendirme"):
        await message.channel.send(
            "Cam atıkları geri dönüştürülebilir ama güvenli şekilde değerlendirilmesi çok önemli! 🔨\n\n"
            "🔄 **Cam Değerlendirme İpuçları:**\n"
            "- Kırık camı güvenli bir şekilde atmalısın. Camı iki poşet veya bir kutuya koyarak, geri dönüşüm kutusuna atabilirsin.\n"
            "- Cam şişeleri veya kutuları dekoratif objelere dönüştürebilirsin. İçine mum yerleştirerek dekoratif bir obje yaratabilirsin.\n\n"
            "Eğer camın geri dönüşümü ile ilgili daha fazla bilgi almak istersen, '$cam geri dönüşüm' komutunu kullanabilirsin."
        )

    elif message.content.startswith("$plastikleri değerlendirme"):
        await message.channel.send(
            "Plastik atıklar geri dönüşüme uygun olabilir, ama onları doğru bir şekilde değerlendirmek önemlidir! 🌍\n\n"
            "🔄 **Plastik Değerlendirme İpuçları:**\n"
            "- Şişeleri, kutuları tekrar kullanabilirsin. Örneğin, eski plastik şişeleri saksı veya sulama kabı olarak kullanabilirsin.\n"
            "- Etiketli, kirli veya sıvı içeren plastikleri temizlemelisin. Aksi takdirde geri dönüşüm sürecini bozabilirler.\n\n"
            "Plastiklerin geri dönüşümü ile ilgili bilgi almak için '$plastik geri dönüşüm' komutunu kullanabilirsin."
        )

    elif message.content.startswith('$kağıt geri dönüşüm'):
        await message.channel.send(
            "Kağıtların çoğu geri dönüştürülebilir! 📄\n\n"
            "🔄 **Kağıt Geri Dönüşüm İpuçları:**\n"
            "- Temiz kağıtlar geri dönüştürülebilir. Ancak yağlı, kirli veya ıslak kağıtlar geri dönüştürülemez.\n"
            "- Kahverengi zarflar, kraft zarflar, karbon kağıtları gibi bazı kağıt türleri geri dönüştürülemez.\n"
            "- Pizza kutuları, şeker ambalajları ve kağıt havlular da geri dönüşümde kabul edilmez.\n"
            "Kağıtların geri dönüşüm süreci hakkında daha fazla bilgi almak istersen, bana soru sorabilirsin."
        )

    elif message.content.startswith('$cam geri dönüşüm'):
        await message.channel.send(
            "Cam atıklar her zaman geri dönüştürülebilir! 🏺\n\n"
            "🔄 **Cam Geri Dönüşüm İpuçları:**\n"
            "- Cam şişeler, kavanozlar ve içecek şişeleri geri dönüştürülebilir.\n"
            "- Ancak bazı camlar, örneğin florasanlar, ampuller veya tıbbi camlar, özel geri dönüşüm süreçlerine tabidir.\n"
            "Bunlar için geri dönüşüm merkezlerinde özel işleme yapılmalıdır.\n\n"
            "Camın geri dönüşümü ile ilgili daha fazla bilgi almak için bana soru sorabilirsin!"
        )

    elif message.content.startswith('$plastik geri dönüşüm'):
        await message.channel.send(
            "Plastikler, doğada çözülmesi yıllar sürebilen bir malzemedir, bu yüzden geri dönüşümleri çok önemlidir! ♻️\n\n"
            "🔄 **Plastik Geri Dönüşüm İpuçları:**\n"
            "- Bazı plastik türleri geri dönüştürülemez. Örneğin, kurşun geçirmez plastikler veya bazı su şişeleri geri dönüştürülemez.\n"
            "- Geri dönüştürülemeyen plastikleri doğru şekilde atmalısın. Bunlar, doğada uzun süre kalabilir ve çevreye zarar verebilir.\n\n"
            "Plastiklerin geri dönüşüm süreci hakkında daha fazla bilgi almak istersen, '$plastik geri dönüşüm' komutunu kullanabilirsin."
        )

istemci.run("BOT TOKEN")
