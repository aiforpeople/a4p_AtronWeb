"""Page copy that isn't in src/copy.json: head meta, FAQ and the agent pages.

Rule for everything here: only claims that are true today. No invented
customers or numbers. Anything unconfirmed stays out until Can says so.
"""

SITE = "https://atronai.co"

HEAD = {
    "tr": {
        "title": "ATRON · Sürecinizi söyleyin, gelecek hafta çalışsın",
        "desc": "ATRON ajanları ekibinizin telefonda, WhatsApp'ta ve formlarda her gün tekrar ettiği işi devralır. İlk hafta sizin sürecinizde çalışan bir prototip.",
        "og_title": "ATRON · Sürecinizi söyleyin, gelecek hafta çalışsın",
        "locale": "tr_TR",
    },
    "en": {
        "title": "ATRON · Name the process. Watch it run next week.",
        "desc": "AI agents that take over the work your team repeats on the phone, on WhatsApp and in forms. A working prototype in your own process in week one.",
        "og_title": "ATRON · Name the process. Watch it run next week.",
        "locale": "en_GB",
    },
}

FAQ = {
    "tr": {
        "label": "06 · Sık sorulanlar",
        "h": "Kısa cevaplar.",
        "items": [
            ("ATRON nedir?",
             "ATRON, şirketlerin telefonda, WhatsApp'ta ve formlarda tekrar eden operasyon işlerini devralan yapay zekâ ajanlarının çalıştığı bir operasyon katmanıdır. Ortak bir çekirdek (hafıza, kurallar, kalite kontrol, entegrasyonlar) ve her biri tek bir işi üstlenen ajanlardan oluşur. AI for People Teknoloji A.Ş. tarafından İstanbul'da geliştirilir."),
            ("Kurulum ne kadar sürer?",
             "İlk hafta sizin sürecinizde çalışan bir prototip gösteriyoruz. Ardından ajan gerçek verinizle, baştan birlikte seçtiğimiz tek bir ölçüte göre pilot olarak çalışır. Ölçüt tutunca canlıya geçer."),
            ("Hangi sistemlere bağlanır?",
             "CRM'inize (örneğin Zoho), santralinize ya da SIP hattınıza ve WhatsApp kanallarınıza bağlanır. Türkiye'deki telefon numaraları için Verimor, Netgsm gibi SIP operatörleri ya da kendi bulut santraliniz kullanılır."),
            ("Hangi dillerde konuşur?",
             "Türkçe ve İngilizce konuşur. Canlıdaki outbound kampanyalarında Portekizce, Bulgarca, İtalyanca, Rumence, İspanyolca, Sırpça, Fransızca, Rusça, Felemenkçe ve Almanca arama yapıyor. Her kişiyi, geldiği listenin dilinde arar."),
            ("Bir chatbot'tan farkı ne?",
             "Ajanlar yalnızca cevap vermez, işi bitirir: arar, niteler, sonucu CRM'e yazar, gerektiğinde insana devreder. Her adım kayıt altındadır ve tek bir başarı ölçütüne göre değerlendirilir."),
        ],
    },
    "en": {
        "label": "06 · FAQ",
        "h": "Short answers.",
        "items": [
            ("What is ATRON?",
             "ATRON is an operations layer where AI agents take over the repetitive work companies do on the phone, on WhatsApp and in forms. It is one shared core (memory, rules, quality control, integrations) plus agents that each own one job. It is built in Istanbul by AI for People Teknoloji A.Ş."),
            ("How long does setup take?",
             "In the first week we show a prototype running in your own process. Then the agent runs as a pilot on your real data, judged against one metric we agree on up front. When it meets the metric, it goes live."),
            ("Which systems does it connect to?",
             "Your CRM (for example Zoho), your phone system or SIP trunk, and your WhatsApp channels. For Turkish phone numbers it uses SIP operators such as Verimor or Netgsm, or your own cloud PBX."),
            ("Which languages does it speak?",
             "Turkish and English. Its live outbound campaigns call in Portuguese, Bulgarian, Italian, Romanian, Spanish, Serbian, French, Russian, Dutch and German. Each contact is called in the language of the list they came from."),
            ("How is this different from a chatbot?",
             "The agents don't just answer, they finish the job: they call, qualify, write the outcome to the CRM and hand over to a person when needed. Every step is logged and judged against a single success metric."),
        ],
    },
}

# Agent pages. Each one answers one buyer query in plain words.
AGENTS = [
    {
        "arm": 0,
        "img": "voice",
        "slug": {"tr": "sesli-ajan", "en": "voice-agent"},
        "tr": {
            "title": "Sesli yapay zekâ ajanı · Gelen aramaları karşılar, niteler, aktarır · ATRON",
            "desc": "ATRON sesli ajanı gelen aramaları arayanın dilinde karşılar, niteler, sonucu CRM'e yazar ve gerektiğinde ekibinize aktarır. Türkiye'deki SIP hatlarıyla çalışır.",
            "label": "Ajan · 01 · Ses",
            "h1": "Telefonu açan, niteleyen ve <em>doğru yere aktaran</em> sesli ajan.",
            "intro": "ATRON sesli ajanı gelen aramaları karşılar, arayanın ne istediğini anlar, gereken bilgileri toplar ve görüşmeyi doğru kişiye ya da sisteme aktarır. Her görüşme CRM'inize yapılandırılmış bir kayıt olarak düşer.",
            "does_h": "Ne yapar",
            "does": [
                ("Karşılar", "Aramayı bekletmeden açar ve arayanın dilinde konuşur. Menü tuşlatmaz."),
                ("Niteler", "Sizin belirlediğiniz soruları sorar; boş bıraktığı alanı tahminle doldurmaz."),
                ("Kaydeder", "Görüşmenin sonucunu ve toplanan bilgileri CRM'inize yazar."),
                ("Devreder", "Cevaplayamadığı bir soru kaldığında ya da arayan isterse görüşmeyi ekibinize aktarır."),
            ],
            "connect_h": "Nasıl bağlanır",
            "connect": "Türkiye'deki numaralar için Verimor, Netgsm gibi SIP operatörleri ya da kendi bulut santraliniz üzerinden çalışır. CRM tarafında mevcut kayıt yapınıza uyar.",
            "where": "Kurumsal bir sağlık turizmi operatöründe canlıda çalışıyor.",
            "faq": [
                ("Türkçe konuşabiliyor mu?", "Evet. Türkçe ve İngilizce konuşur; operasyonunuzda gereken başka diller de eklenebilir."),
                ("Mevcut santralime bağlanır mı?", "Evet. SIP hattınız ya da bulut santraliniz üzerinden bağlanır, numaranızı değiştirmeniz gerekmez."),
                ("Ne kadar sürede kurulur?", "İlk hafta sizin akışınızda çalışan bir prototip gösteriyoruz."),
            ],
        },
        "en": {
            "title": "AI voice agent · Answers, qualifies and routes inbound calls · ATRON",
            "desc": "The ATRON voice agent answers inbound calls in the caller's language, qualifies them, writes the outcome to your CRM and hands over to your team when needed.",
            "label": "Agent · 01 · Voice",
            "h1": "A voice agent that answers, qualifies and <em>routes the call.</em>",
            "intro": "The ATRON voice agent answers inbound calls, understands what the caller wants, collects the details you need and routes the call to the right person or system. Every call lands in your CRM as a structured record.",
            "does_h": "What it does",
            "does": [
                ("Answers", "Picks up without a queue and speaks the caller's language. No phone menus."),
                ("Qualifies", "Asks the questions you set; it never fills a blank with a guess."),
                ("Records", "Writes the outcome and the details it collected to your CRM."),
                ("Hands over", "Routes the call to your team when a question is left open or the caller asks for a person."),
            ],
            "connect_h": "How it connects",
            "connect": "For Turkish numbers it works through SIP operators such as Verimor or Netgsm, or through your own cloud PBX. On the CRM side it follows your existing record structure.",
            "where": "Running in production at an enterprise health-tourism operator.",
            "faq": [
                ("Does it speak Turkish?", "Yes. It speaks Turkish and English; other languages your operation needs can be added."),
                ("Will it work with my existing phone system?", "Yes. It connects through your SIP trunk or cloud PBX; you keep your number."),
                ("How long does setup take?", "In the first week we show a prototype running in your own flow."),
            ],
        },
    },
    {
        "arm": 1,
        "img": "record",
        "slug": {"tr": "whatsapp-kalite-kontrol", "en": "whatsapp-qa"},
        "tr": {
            "title": "WhatsApp satış kalite kontrolü · Konuşmaların tamamını okuyan ajan · ATRON",
            "desc": "ATRON WhatsApp kalite kontrol ajanı satış ekibinizin WhatsApp konuşmalarının tamamını okur, puanlar, şüpheli davranışları ve kaçan fırsatları işaretler, haftanın tahminini çıkarır.",
            "label": "Ajan · 02 · WhatsApp",
            "h1": "Satış konuşmalarının <em>tamamını</em> okuyan kalite kontrol.",
            "intro": "Satış ekibinizin WhatsApp konuşmalarını örneklemle değil, tamamını okur. Belirlediğiniz kriterlere göre puanlar, şüpheli davranışları ve kaçan fırsatları işaretler, haftanın tahminini çıkarır.",
            "does_h": "Ne yapar",
            "does": [
                ("Okur", "Bütün konuşmaları okur; kimseyi rastgele seçmez."),
                ("Puanlar", "Sizin kalite kriterlerinize göre her konuşmaya puan verir ve gerekçesini yazar."),
                ("İşaretler", "Şüpheli davranışları ve takip edilmeyen fırsatları ayrı bir listede toplar."),
                ("Tahmin eder", "Konuşmalardan haftanın satış tahminini çıkarır."),
            ],
            "connect_h": "Nasıl bağlanır",
            "connect": "Ekibinizin kullandığı WhatsApp kanallarından konuşmaları alır, sonuçları CRM'inize ya da size özel bir panele yazar.",
            "where": "Kurumsal bir sağlık turizmi operatöründe canlıda çalışıyor.",
            "faq": [
                ("Konuşmaların hepsini mi okuyor?", "Evet. Örneklem almaz, bütün konuşmaları okur."),
                ("Kriterleri kim belirliyor?", "Siz. Kalite kriterleri sizin satış sürecinize göre birlikte yazılır."),
                ("Ne kadar sürede kurulur?", "İlk hafta sizin konuşmalarınız üzerinde çalışan bir prototip gösteriyoruz."),
            ],
        },
        "en": {
            "title": "WhatsApp sales QA · An agent that reads every conversation · ATRON",
            "desc": "The ATRON WhatsApp QA agent reads every WhatsApp conversation your sales team has, scores them, flags suspicious behaviour and missed opportunities, and produces the week's forecast.",
            "label": "Agent · 02 · WhatsApp",
            "h1": "Quality control that reads <em>every</em> sales conversation.",
            "intro": "It reads all of your sales team's WhatsApp conversations, not a sample. It scores them against your criteria, flags suspicious behaviour and missed opportunities, and produces the week's forecast.",
            "does_h": "What it does",
            "does": [
                ("Reads", "Reads every conversation; nobody is picked at random."),
                ("Scores", "Scores each conversation against your quality criteria and writes down why."),
                ("Flags", "Collects suspicious behaviour and unfollowed opportunities in a separate list."),
                ("Forecasts", "Produces the week's sales forecast from the conversations."),
            ],
            "connect_h": "How it connects",
            "connect": "It takes conversations from the WhatsApp channels your team uses and writes results to your CRM or a dedicated panel.",
            "where": "Running in production at an enterprise health-tourism operator.",
            "faq": [
                ("Does it really read every conversation?", "Yes. No sampling; it reads all of them."),
                ("Who sets the criteria?", "You do. We write the quality criteria together, based on your sales process."),
                ("How long does setup take?", "In the first week we show a prototype running on your own conversations."),
            ],
        },
    },
    {
        "arm": 2,
        "img": "core",
        "slug": {"tr": "outbound-geri-kazanim", "en": "outbound-win-back"},
        "tr": {
            "title": "Outbound arama ajanı · Soğumuş lead'leri geri kazanma · ATRON",
            "desc": "ATRON outbound ajanı soğumuş ve kaybedilmiş lead'leri listenin dilinde arar, ilgiyi yeniden ölçer, ilgilenenleri ekibinize aktarır ve her sonucu CRM'e yazar.",
            "label": "Ajan · 03 · Outbound",
            "h1": "Soğumuş lead'leri arayan, <em>sonucu CRM'e yazan</em> ajan.",
            "intro": "Kaybedilmiş ya da soğumuş lead listelerinizi arar, ilgiyi yeniden ölçer, ilgilenenleri ekibinize aktarır ve her aramanın sonucunu CRM durumlarıyla yazar. Kampanyayı siz başlatırsınız; ajan sizin belirlediğiniz saat aralığında çalışır.",
            "does_h": "Ne yapar",
            "does": [
                ("Arar", "Her kişiyi, geldiği listenin dilinde ve kendi saat diliminde arar."),
                ("Ölçer", "İlgiyi yeniden ölçer; ilgilenenleri, geri aranmak isteyenleri ve ilgilenmeyenleri ayırır."),
                ("Yazar", "Her aramanın sonucunu CRM'inizdeki durumlarla birebir yazar."),
                ("Dener", "Ulaşılamayanları belirlediğiniz sayıda yeniden dener, aranmak istemeyenleri bir daha aramaz."),
            ],
            "connect_h": "Nasıl bağlanır",
            "connect": "Kişi listelerinizi alır, sonuçları CRM'inize (örneğin Zoho) yazar. Kampanyalar dil ve ülkeye göre otomatik bölünür, siz onaylamadan başlamaz.",
            "where": "Kurumsal bir sağlık turizmi operatöründe on bir dilde canlıda arama yapıyor.",
            "faq": [
                ("Hangi dillerde arıyor?", "Canlıda Portekizce, Bulgarca, İtalyanca, Rumence, İspanyolca, Sırpça, Fransızca, Rusça, Felemenkçe, Almanca ve İngilizce arama yapıyor."),
                ("Aranmak istemeyenler ne oluyor?", "Aranmak istemediğini söyleyen kişi aranmayacaklar listesine alınır ve bir daha aranmaz."),
                ("Kampanyayı kim başlatıyor?", "Siz. Ajan taslak kampanya hazırlar, sizin onayınız olmadan arama başlamaz."),
            ],
        },
        "en": {
            "title": "Outbound calling agent · Win back cold leads · ATRON",
            "desc": "The ATRON outbound agent calls cold and lost leads in the language of their list, re-measures interest, hands interested leads to your team and writes every outcome to your CRM.",
            "label": "Agent · 03 · Outbound",
            "h1": "An agent that calls cold leads and <em>writes the outcome to the CRM.</em>",
            "intro": "It calls your lost or cold lead lists, re-measures interest, hands interested leads to your team and writes the outcome of every call with your CRM statuses. You start the campaign; the agent works inside the calling window you set.",
            "does_h": "What it does",
            "does": [
                ("Calls", "Calls each contact in the language of their list and in their own time zone."),
                ("Measures", "Re-measures interest and separates interested, call-back and not-interested contacts."),
                ("Writes", "Writes the outcome of every call with the exact statuses in your CRM."),
                ("Retries", "Retries unreached contacts as many times as you set, and never calls people who opted out."),
            ],
            "connect_h": "How it connects",
            "connect": "It takes your contact lists and writes outcomes to your CRM (for example Zoho). Campaigns are split by language and country automatically and never start without your approval.",
            "where": "Calling live in eleven languages for an enterprise health-tourism operator.",
            "faq": [
                ("Which languages does it call in?", "It calls live in Portuguese, Bulgarian, Italian, Romanian, Spanish, Serbian, French, Russian, Dutch, German and English."),
                ("What happens to people who don't want calls?", "Anyone who says they don't want to be called goes on the do-not-call list and is never called again."),
                ("Who starts a campaign?", "You do. The agent prepares draft campaigns; no calls start without your approval."),
            ],
        },
    },
]
