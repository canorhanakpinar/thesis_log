Since I want to translate my work to Turkish and French, I might use them in parallel

-----
## **Takip edilen plan**

### **Yaz Programı:**

**Haziran:**

**10-30 Haziran:**
- Literatür Taraması: Ön taramayı yap, makalelerin tema dökümünü özetle. (alternatif olarak yer bilgisini de ekle)
- NLP (resmi gazete) kodlarının taşınması ve geçmiş senelere dönük tarama için kod yazmak, yapıya göz at.
- NLP kodları için 1 güne yönelik tüm içerik indirmeyi dene, nasıl özetleyebilirsin? Summarize
- GPU ile analiz için CUDA yükle. CUDA testi için 1 parsel Hatay bölgesi uydu görüntüsü indir. Bir kere segmentation ile analiz dene, ama hata çıkarsa çok vakit harcama.

**Temmuz:**

**1-15 Temmuz:**
- CUDA testi devam, ilk parseli annotate et. Hata oranı nedir? sırayla parsel parsel 5 parsele çık. Önce tek parseli annotate edip test etmeyi tamamladan sayı artırmaya çalışma.
- Literatür Taraması: Ön taramayı grupla, ekstra keywordler ile taramalı mıyız? Başka index'e (WebofScience vs. bakmalı mıyız?)
- Ekonometrik Analiz: Okumalara göre Variable selection listeni güncelle, ilk taslağı tamamla.
- NLP: Resmi gazeteleri indir, 1 hafta için tüm içerik indir, annotation'ı kontrol et, LLM ile kullanmayı dene.
- NLP: Öncelik başlıkları taramak. Tüm resmi gazeteleri tamamlayınca başlık annotationa başla. Tüm kategorilere bak, kararlar, yürütmelikler vs.

**16-31 Temmuz:**
- Literatür Taraması: Bir önceki bölümde çıkan grup sayısına ve tekrar eden tema sayısına bak. Neler çok? Neler az?
- Literatür Taraması: Citation network incelemesi yap. Citationlara göre cluster analizi yap. Grupların bu clusterlarla ne kadar uyumlu?
- Ekonometrik Analiz: TÜİK verilerini indir. Eksik verilerini sapta. İlk verilerle DID ve PSM taslağını çıkar.
- Ekonometrik Analiz: Kurumlara mail at. Hatta İstanbul'da olan varsa ziyaret et. İstanbul'daki tarım, çiftçi, vs kooperatifler ve kurumsal organizasyonlar varsa onları ziyaret et. (Ay sonuna kaldıysa diğer aya ayarla)
- Harita analizi çalıştı mı? Bu noktada olduysa son kararını ver. İlerlemenle ilgili harita analizi kullanan uzmanlara ulaşıp destek talep et.

**Ağustos:**

**1-15 Ağustos:**
- Literatür Taraması: Sonuçları yazmaya başla, hipotezi kesinleştir. Bu noktada çoğunluğu tamamlanmış olmalı.
- Ekonometrik Analiz: Daha çok okuma yap. Modellerinin denklemlerini kesinleştir, kodların matematiksel-istatiksel arka planını anla. Assumptionların ve biaslarını belirle.
- NLP: Validation okuması yap. Bu kadar seneyi elle ayıramazsın. Bir kısım golden corpus oluşturdun. Kalanını anlamak için matematiksel mantığını öğrenmen gerekli. LLM ile golden corpus testi yap. Buna göre ek validation modeli geliştir.
- Harita analizi: İlk sonuçları özetle ve destek aldığın insanlarla paylaş.

**15-31 Ağustos:**
- İlk sonuçlarını özetle. Araştırma konusu ile hipotezi sonuçlandır. 



-----


Verileri bulmak - Ne kadar erişilebilir?

Verileri işlemek - Ne kadar maliyetli?

Verileri depolamak - Ne kadar yer, ne kadar süre?

Verileri korumak - Ne seviyede gizlemeliyiz ve korumalıyız?

Verilerin insanları - Kimler etkileniyor, ne şekilde (Belmont Raporu prensipleri) ?


Açık Bilim - Open Science

- Önce tüm verileri topla, teknik kısmını da örnek pratikleriyle dene. Analizi yapacağın araçların metodlarını önceden çalışmaya başla. 
- Metodolojide yazdığın bölümlerin eğitim paketlerini uygula. Daha sonra incelemeye başlamadan önce verinle ne yapacağını söyle. 
- Daha sonrasında değişecek her metod için bir referans bildirisi olacak.

Image recognition - paketleri indir ve örnekleri dene

Dil işleme - paketleri indir ve örnekleri dene

Regresyon - modellerini belirle ve değişkenlerini denklemleştir.

Resmi gazetenin tamamını kaydet.

TÜİK'ten belirlediğin teorideki değişkenlerin verilerine ulaş.

Coğrafi analiz için verileri belirleyip kaydet, bunun öncesinde bir örneklem alanı belirlemen lazım.

Toprak kullanımı ve parsel transferleri verilerini bir tabloya kaydet.

Alan belirlemek için de propensity score(or CEM oscore) matching (PSM) için oluşturacağın verilerin doğruluğunu ispatla. Coğrafi özellikler, yapılaşma vs. dahil olacaksa yeniden işlemeyi gerekebilir.

Difference-in-differences (DID) için belirleyeceğin bölümlerin coğrafi, ekonomik, ve etnik özelliklerini açıkla.

Türkiye Cumhuriyetinde tarım ve gıda ile ilgili tüm birimlerin ayrıntılı bir listesini oluştur

Saha gezisi için oluşturacağın grupları berlirle. PCA ve clustering analizleri grup sayısı belirlemede yardımcı olabilir.
