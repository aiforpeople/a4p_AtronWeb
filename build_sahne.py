#!/usr/bin/env python3
"""Builds public/yeni/index.html: the scene-driven home page (video frame sequences scrubbed by scroll).
Text lives in the HTML so it reads without JS and for AI crawlers. Run: python3 build_sahne.py"""
import html, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
PAPER = "#cfd0d3"

# anchor = where the red leader line starts, as a fraction of the frame (final pose). None = no line.
ACTS = [
    dict(id="ses", n=65, dir="/sahne/v/f", tag="01 / SES", label="SES AJANI",
         intro=("Sürecinizi söyleyin. Gelecek hafta çalışsın.",
                "ATRON, ekibinizin her gün tekrar ettiği işi yapan yapay zekâ çalışanlarıdır."),
         mid=("23:40", "TELEFON ÇALIYOR · EKİP UYUYOR"),
         say="Gece gelen aramayı açar.",
         sub="Arayanın dilinde konuşur, ne istediğini sorar, talebi CRM'inize yazar. Sabah kayıt ekibinizin önündedir.",
         cta=("AJANLA ŞİMDİ KONUŞ", "/#canli"), anchor=(0.372, 0.395),
         alt="ATRON kuklası bir koluyla telefon ahizesini kulağına tutuyor"),
    dict(id="whatsapp", n=65, dir="/sahne/s/wa", tag="02 / WHATSAPP", label="WHATSAPP KALİTE KONTROL",
         mid=("09:00", "DÜNKÜ YAZIŞMALARI KİM OKUDU?"),
         say="Her yazışmayı okur.",
         sub="Ekibinizin WhatsApp görüşmelerini tek tek okur; geç kalan cevabı, yanlış bilgiyi, kaçan satışı işaretler. Yönetici sabah özetini görür.",
         cta=("NASIL ÇALIŞIYOR", "/ajanlar/whatsapp-kalite-kontrol/"), anchor=(0.415, 0.36),
         alt="ATRON kuklası bir koluyla telefonu kaldırmış, büyüteçle ekrandaki yazışmayı inceliyor"),
    dict(id="outbound", n=2, dir="/sahne/s/out", tag="03 / OUTBOUND", label="OUTBOUND GERİ KAZANIM",
         mid=("3 HAT", "ESKİ LİSTE ARANMAYI BEKLİYOR"),
         say="Aramadığınız listeyi arar.",
         sub="Cevap vermemiş eski başvuruları kendi dillerinde arar, ilgileneni ekibinize sıcak devreder. Aynı anda birden çok hat.",
         cta=("NASIL ÇALIŞIYOR", "/ajanlar/outbound-geri-kazanim/"), anchor=(0.385, 0.40),
         alt="ATRON kuklası üç koluyla üç telefon ahizesini aynı anda tutuyor"),
    dict(id="brain", n=2, narrow="tight", dir="/sahne/s/brain", tag="04 / ATRON BRAIN", label="ATRON BRAIN",
         mid=("TEK YER", "BİLGİ ON AYRI YERDE DURUYORDU"),
         say="Hepsi tek hafızada.",
         sub="Kim ne konuştu, ne karar verildi, hangi iş nerede. İnsan da ajan da aynı yerden okur. Biz kendi şirketimizi böyle yönetiyoruz; aynısının sizde kurulduğunu düşünün.",
         cta=("MİMARİYİ GÖR", "/#mimari"), anchor=(0.545, 0.58),
         alt="ATRON kuklası kartların düzenle iğnelendiği mantar panoyu gösteriyor"),
    dict(id="derin", n=2, narrow=True, dir="/sahne/s/oto", tag="05 / DERİN TEKNOLOJİ", label="RENAULT",
         mid=("4 PROJE", "RENAULT INNOVATION HUB · GLOBAL SHORTLIST"),
         say="Renault bizden dört proje istedi.",
         sub="Renault'nun inovasyon programına geliştirdiğimiz iki proje dünya çapındaki kısa listeye girdi; Renault iki proje daha istedi: PROSEM, VOICE4FIC, Mind Wandering, Ready Check.",
         cta=("DÖRT PROJEYİ GÖR", "/#derin"), anchor=(0.53, 0.47),
         alt="ATRON kuklası iki koluyla bir direksiyonu tutuyor, pirinç bir boruyla dinliyor"),
]

e = html.escape


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
    return f'''<section class="act{(' tight' if a.get('narrow')=='tight' else ' narrow') if a.get('narrow') else ''}" id="{a["id"]}" aria-label="{e(a["label"].title())}" data-n="{a["n"]}" data-dir="{a["dir"]}"{' data-ax="%s" data-ay="%s"' % a["anchor"] if a.get("anchor") else ''}>
  <div class="stage">
    <img class="fallback" src="{a["dir"]}/{last}.webp" alt="{e(a["alt"])}" loading="{'eager' if first else 'lazy'}">
    <canvas aria-hidden="true"></canvas>
    <svg class="lead" aria-hidden="true"><path/><circle r="4"/></svg>
    <header class="top"><a href="/"><img src="/logo.png" alt="ATRON" width="1037" height="266"></a><span class="mono r">OPERASYON KATMANI · {e(a["tag"])}</span></header>
    <div class="copy">{intro}
      <p class="beat clock"><b>{e(a["mid"][0])}</b><span class="mono">{e(a["mid"][1])}</span></p>
      <div class="beat b2">
        <p class="mono k"><i></i>{e(a["label"])}</p>
        <{'p' if a.get('intro') else 'h2'} class="say">{e(a["say"])}</{'p' if a.get('intro') else 'h2'}>
        <p class="sub">{e(a["sub"])}</p>
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
<section class="end">
  <p class="mono k"><i></i>SIRADAKİ ADIM</p>
  <h2 class="say">Tekrar eden işinizi anlatın.</h2>
  <p class="sub">Hangi işin ajana devredilebileceğini ilk görüşmede söyleriz. ATRON; ses, WhatsApp ve form kanallarında çalışan ajanlar ile hepsinin ortak hafızası ATRON Brain'den oluşan bir operasyon katmanıdır.</p>
  <p class="links mono"><a class="go" href="/#iletisim"><span>GÖRÜŞME AYARLA</span><span>→</span></a>
  <a class="go" href="/ajanlar/sesli-ajan/"><span>SES AJANI</span><span>→</span></a>
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
