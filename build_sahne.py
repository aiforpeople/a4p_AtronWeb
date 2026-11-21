#!/usr/bin/env python3
"""Builds public/yeni/index.html: the scene-driven home page (video frame sequences scrubbed by scroll).
Text lives in the HTML so it reads without JS and for AI crawlers. Run: python3 build_sahne.py"""
import html, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

# side = where the text sits (the picture's calm area); fx = where the subject sits (0..1), used to crop on phones.
LIGHT = dict(red="#ff5a47", ink="#f3efe6", dim="rgba(243,239,230,.62)", line="rgba(243,239,230,.2)")
DARK = dict(red="#ca0013", ink="#0d0e11", dim="#5b5e66", line="rgba(13,14,17,.22)")
ACTS = [
    dict(id="ses", n=2, more=('Örnek: bir sağlık turizmi şirketi', [('23:40', "İtalya'dan bir hasta arıyor. Ekip uyuyor."), ('ATRON', "Telefonu açar, İtalyanca konuşur, hangi tedaviyi ve ne zaman istediğini sorar. Talebi CRM'e yazar."), ('09:00', 'Kayıt satış ekibinin önünde.')]), iris=(.429, .586, .022), w="narrow", dir="/sahne/s2/ses", tag="01 / SES", label="SES AJANI", side="R", fx=.22, bg="#030d1e", scrim=.0, **LIGHT,
         intro=("Sürecinizi söyleyin. Gelecek hafta çalışsın.",
                "ATRON, ekibinizin her gün tekrar ettiği işi yapan yapay zekâ çalışanlarıdır. Gece gelen aramayı açar, yüzlerce WhatsApp konuşmasını okur, Excel'de unutulmuş listeyi arar. Sonucu sabah CRM'inizde bulursunuz."),
         mid=("23:40", "TELEFON ÇALIYOR · EKİP UYUYOR"),
         say="Gece gelen aramayı açar.",
         sub="Arayanın dilinde konuşur, ne istediğini sorar, talebi CRM'inize yazar. Sabah kayıt ekibinizin önündedir.",
         cta=("AJANLA ŞİMDİ KONUŞ", "/#canli"),
         alt="Gece, masa lambasının altında ATRON kuklası telefonu açmış, bir koluyla not alıyor"),
    dict(id="whatsapp", n=2, more=('Örnek: aynı şirket, ertesi sabah', [('DÜN', 'Yüzlerce WhatsApp konuşması yapıldı. Kimse hepsini okuyamaz.'), ('ATRON', 'Hepsini okudu. Fiyat sorusu cevapsız kalan konuşmaları ve iki kez dönüp cevap alamayan müşterileri ayrı bir listeye koydu.'), ('10:20', 'Liste satış müdürünün ekranında.')]), iris=(.84, .36, .055), dir="/sahne/s2/wa", tag="02 / WHATSAPP", label="WHATSAPP KALİTE KONTROL", side="L", fx=.78, bg="#f1dcc7", scrim=.0, **DARK,
         mid=("09:00", "DÜNKÜ YAZIŞMALARI KİM OKUDU?"),
         say="Her yazışmayı okur.",
         sub="Ekibinizin WhatsApp görüşmelerini tek tek okur; geç kalan cevabı, yanlış bilgiyi, kaçan satışı işaretler. Yönetici sabah özetini görür.",
         cta=("NASIL ÇALIŞIYOR", "/ajanlar/whatsapp-kalite-kontrol/"),
         alt="ATRON kuklası çok yakından: büyüteçle telefondaki yazışmaya bakıyor, gözü mercekte kocaman"),
    dict(id="outbound", n=2, more=('Örnek: aynı gün, öğleden sonra', [('EXCEL', 'Geçen yıl ilgilenip vazgeçen binlerce kişi bir listede duruyor.'), ('ATRON', 'Herkesi kendi dilinde ve kendi saatinde arar. Aranmak istemeyenleri bir daha aramaz.'), ('18:00', "Hâlâ ilgilenenler CRM'de, sırada.")]), iris=(.118, .303, .006), w="narrow", dir="/sahne/s2/out", tag="03 / OUTBOUND", label="OUTBOUND GERİ KAZANIM", side="R", fx=.36, bg="#2e371e", scrim=.0, **LIGHT,
         mid=("6 HAT", "ESKİ LİSTE ARANMAYI BEKLİYOR"),
         say="Aramadığınız listeyi arar.",
         sub="Cevap vermemiş eski başvuruları kendi dillerinde arar, ilgileneni ekibinize sıcak devreder. Aynı anda birden çok hat.",
         cta=("NASIL ÇALIŞIYOR", "/ajanlar/outbound-geri-kazanim/"),
         alt="Dev bir telefon santralinin önünde küçük ATRON kuklası altı koluyla altı kabloyu takmış, lambalar yanıyor"),
    dict(id="brain", n=2, more=('Dört katman, tek hafıza', [('EKİBİNİZ', 'Satış, operasyon, yönetim. Soru sorar, karar verir.'), ('BRAIN', 'Kim ne konuştu, ne karar verildi, hangi iş nerede.'), ('AJANLAR', "Telefonu açar, WhatsApp'ı okur, listeyi arar. Yaptığını beyne yazar."), ('SİSTEMLER', 'CRM, ERP, Drive, santral. Veri yerinde kalır; beyin nerede olduğunu bilir.')]), iris=(.31, .068, .028), w="tight", dir="/sahne/s2/brain", tag="04 / ATRON BRAIN", label="ATRON BRAIN", side="R", fx=.30, bg="#4a2210", scrim=.55, **LIGHT,
         mid=("TEK YER", "BİLGİ ON AYRI YERDE DURUYORDU"),
         say="Hepsi tek hafızada.",
         sub="Kim ne konuştu, ne karar verildi, hangi iş nerede. İnsan da ajan da aynı yerden okur. Biz kendi şirketimizi böyle yönetiyoruz; aynısının sizde kurulduğunu düşünün.",
         cta=("MİMARİYİ GÖR", "/#mimari"),
         alt="Tepeden görünüm: ATRON kuklası ortada, her kolu masadaki ayrı bir nesneye uzanmış, hepsi kırmızı iple ona bağlı"),
    dict(id="derin", n=2, more=('Dört proje', [('PROSEM', 'Sesten duyguyu, cümle bitmeden okuyan model. Global shortlist.'), ('VOICE4FIC', 'Teknisyen konuşur, arıza raporu kendini doldurur. Global shortlist.'), ('MIND WANDERING', 'Sürücünün aklının yoldan ayrıldığını fark eder, güvenli anı bekleyip sorar.'), ('READY CHECK', 'Yola çıkmadan üç dakikalık ısınma; sürücünün o gün ne kadar hazır olduğunu ölçer.')]), dir="/sahne/s2/oto", tag="05 / DERİN TEKNOLOJİ", label="RENAULT", side="L", fx=.80, bg="#27304f", scrim=.62, **LIGHT,
         mid=("4 PROJE", "RENAULT INNOVATION HUB · GLOBAL SHORTLIST"),
         say="Renault bizden dört proje istedi.",
         sub="Renault'nun inovasyon programına geliştirdiğimiz iki proje dünya çapındaki kısa listeye girdi; Renault iki proje daha istedi: PROSEM, VOICE4FIC, Mind Wandering, Ready Check.",
         cta=("DÖRT PROJEYİ GÖR", "/#derin"),
         alt="Alacakaranlıkta eski bir otomobilin sürücü koltuğunda ATRON kuklası, kolları direksiyonda, gösterge paneli yanıyor"),
]

e = html.escape


NAVN = {"ses": "SES", "whatsapp": "WHATSAPP", "outbound": "OUTBOUND", "brain": "BRAIN", "derin": "RENAULT"}


def nav(a):
    out = []
    for i, b in enumerate(ACTS):
        cur = b["id"] == a["id"]
        out.append(f'<a href="#{b["id"]}"{' class="on" aria-current="true"' if cur else ''}><b>{i + 1:02d}</b> {NAVN[b["id"]]}</a>')
    return "".join(out)


def act_html(a, first):
    last = "%02d" % a["n"]
    intro = ""
    if a.get("intro"):
        intro = f'''
      <div class="beat b1">
        <h1>{e(a["intro"][0])}</h1>
        <p class="sub">{e(a["intro"][1])}</p>
      </div>'''
    hint = '<p class="hint mono"><span>↓</span><span>KAYDIRIN</span></p>' if first else ""
    tag = "p" if a.get("intro") else "h2"
    style = f'--bg:{a["bg"]};--ink:{a["ink"]};--dim:{a["dim"]};--line:{a["line"]};--scrim:{a["scrim"]};--red:{a["red"]}'
    return f'''<section class="act {a["side"]} {a.get("w","")}" id="{a["id"]}" aria-label="{e(a["label"].title())}" data-n="{a["n"]}" data-dir="{a["dir"]}" data-fx="{a["fx"]}" data-bg="{a["bg"]}" data-scrim="{a["scrim"]}"{' data-ax="%s" data-ay="%s" data-ar="%s"' % a["iris"] if a.get("iris") else ''} style="{style}">
  <div class="stage">
    <img class="fallback" src="{a["dir"]}/{last}.webp" alt="{e(a["alt"])}" loading="{'eager' if first else 'lazy'}" style="object-position:{int(a["fx"]*100)}% 50%">
    <canvas aria-hidden="true"></canvas>
    <header class="top"><a href="/"><img src="/logo.png" alt="ATRON" width="1037" height="266"></a><nav class="mono r" aria-label="Bölümler">{nav(a)}</nav></header>
    <div class="copy">{intro}
      <p class="beat clock"><b>{e(a["mid"][0])}</b><span class="mono">{e(a["mid"][1])}</span></p>
      <div class="beat b2">
        <p class="mono k"><i></i>{e(a["label"])}</p>
        <{tag} class="say">{e(a["say"])}</{tag}>
        <p class="sub">{e(a["sub"])}</p>
      </div>
      <div class="beat b3">
        <h3 class="mh">{e(a["more"][0])}</h3>
        <dl class="rows">{"".join('<div class="row"><dt class="mono">%s</dt><dd>%s</dd></div>' % (e(k), e(v)) for k, v in a["more"][1])}</dl>
        <a class="go mono" href="{a["cta"][1]}"><span>{e(a["cta"][0])}</span><span>→</span></a>
      </div>
    </div>
    {hint}
  </div>
</section>'''


CSS = open(os.path.join(ROOT, "src", "sahne.css")).read()
JS = open(os.path.join(ROOT, "src", "sahne.js")).read()

page = f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>ATRON · Sürecinizi söyleyin, gelecek hafta çalışsın</title>
<meta name="description" content="ATRON, şirketlerin telefonda, WhatsApp'ta ve formlarda tekrar eden operasyon işlerini devralan yapay zekâ ajanlarının çalıştığı operasyon katmanıdır.">
<meta name="robots" content="noindex">
<link rel="preload" href="/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{ACTS[0]["dir"]}/01.webp" as="image">
<style>
{CSS}
</style>
</head>
<body>
<script>document.documentElement.classList.add('js');</script>
<main>
{chr(10).join(act_html(a, i == 0) for i, a in enumerate(ACTS))}
<section class="how">
  <p class="mono k"><i></i>NASIL ÇALIŞIYORUZ · BİR HAFTA</p>
  <h2 class="say">Önce çalışan şey. Sonra gerçek veri.</h2>
  <dl class="steps">
    <div><dt class="mono">HAFTA 1 · PROTOTİP</dt><dd>Sürecinizi dışarıdan inceleriz, brief'i kendimize yazarız. Hafta sonunda kendi akışınızda çalışan bir ajan görürsünüz.</dd></div>
    <div><dt class="mono">PİLOT · GERÇEK VERİ, TEK ÖLÇÜT</dt><dd>Ajan gerçek verinizle, canlıya yakın bir ortamda çalışır. Başarıyı baştan birlikte seçtiğimiz tek bir ölçüte göre değerlendiririz.</dd></div>
    <div><dt class="mono">CANLI · SİZİN SİSTEMLERİNİZDE</dt><dd>CRM'inize, santralinize ve mesajlaşma kanallarınıza bağlanır, uyum kurallarınızın içinde çalışır. İzlemeyi ve iyileştirmeyi biz sürdürürüz.</dd></div>
  </dl>
</section>
<section class="end">
  <p class="mono k"><i></i>SIRA SİZDE</p>
  <h2 class="say">Hangi süreç sizi en çok yoruyor?</h2>
  <p class="sub">Bize o süreci anlatın. Google Meet'te yarım saat konuşalım, bir hafta sonra çalışır halini görün. ATRON; ses, WhatsApp ve form kanallarında çalışan ajanlar ile hepsinin ortak hafızası ATRON Brain'den oluşan bir operasyon katmanıdır.</p>
  <p class="links mono"><a class="go" href="/#iletisim"><span>GÖRÜŞME AYARLA</span><span>→</span></a>
  <a class="go" href="/#canli"><span>AJANLA ŞİMDİ KONUŞ</span><span>→</span></a>
  <a class="go" href="/#sss"><span>SIK SORULANLAR</span><span>→</span></a></p>
</section>
</main>
<script>
{JS}
</script>
</body>
</html>
'''
out = os.path.join(ROOT, "public", "yeni")
os.makedirs(out, exist_ok=True)
open(os.path.join(out, "index.html"), "w").write(page)
print("wrote public/yeni/index.html", len(page))
