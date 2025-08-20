Kütüphane Yönetim Sistemi 📚
Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirilen, nesne yönelimli programlama (OOP) prensiplerini, harici API entegrasyonunu ve FastAPI ile kendi API'nizi oluşturmayı birleştiren üç aşamalı bir uygulamadır.

Amacımız, basit bir komut satırı uygulamasından başlayarak, onu harici verilerle zenginleştirmek ve son olarak bir web servisi haline getirmektir.

Özellikler ve Aşamalar ✨
Aşama 1: OOP ile Terminalde Çalışan Kütüphane
Book ve Library Sınıfları: Kitapları ve kütüphane operasyonlarını yöneten nesne tabanlı bir yapı.

Kalıcı Veri Depolama: Kitap verileri, library.json dosyasına kaydedilerek kalıcılık sağlanır.

Aşama 2: Harici API ile Veri Zenginleştirme
Open Library API Entegrasyonu: Kullanıcıdan sadece ISBN alarak kitap başlığı ve yazar bilgilerini otomatik olarak çeker.

Hata Yönetimi: Geçersiz ISBN veya API bağlantı sorunları gibi durumlarda programın çökmesi engellenir.

Aşama 3: FastAPI ile Kendi API'nizi Oluşturma
Web Servisi: Uygulamanın mantığına, web üzerinden erişilebilen bir API katmanı eklenir.

API Endpoint'leri: Kitapları listeleme, ekleme ve silme işlemleri için özel API uç noktaları (/books) oluşturulmuştur.

Pydantic Veri Modelleri: API veri giriş ve çıkışları, güvenli ve düzenli bir şekilde yönetilir.

Kurulum ⚙️
Projeyi yerel makinenize kurmak ve çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

git clone https://github.com/gulnihal-arslan/PythonProject4
cd python-bootcamp-kutuphane


Bağımlılıkları Kurun:
Gerekli tüm kütüphaneler requirements.txt dosyasında listelenmiştir.

pip install -r requirements.txt

Kullanım 
Terminal Uygulaması (Aşama 1 & 2)
Terminal uygulamasını başlatmak için main.py dosyasını çalıştırın:

Bash

python main.py
Uygulama, size interaktif bir menü sunacak ve buradan kitap yönetimi işlemlerini yapabilirsiniz.

FastAPI Uygulaması (Aşama 3)
API sunucusunu başlatmak için uvicorn komutunu kullanın:

Bash

uvicorn api:app --reload
API, varsayılan olarak http://127.0.0.1:8000 adresinde çalışacaktır. Tarayıcınızdan http://127.0.0.1:8000/docs adresine giderek otomatik olarak oluşturulan interaktif API dokümantasyonunu görüntüleyebilirsiniz.

API Dokümantasyonu 
Proje API'si, aşağıdaki endpoint'leri sunar:

GET /books: Kütüphanedeki tüm kitapların listesini JSON formatında döndürür.

POST /books: İstek gövdesinde bir ISBN alır ({"isbn": "..."}) ve Open Library API'den kitap bilgilerini çekerek kütüphaneye yeni bir kitap ekler.

DELETE /books/{isbn}: Belirtilen ISBN'e sahip kitabı kütüphaneden siler.

Testler
Projedeki tüm fonksiyonların ve API endpoint'lerinin doğru çalıştığından emin olmak için pytest ile test senaryoları yazılmıştır. Testleri çalıştırmak için:

Bash

pytest
