/**
 * POST /api/realtime-session  ->  short-lived OpenAI Realtime key for the
 * live demo on atronai.co.
 *
 * OPENAI_API_KEY never reaches the browser. The persona, tools and limits are
 * locked here; the browser only chooses the language (tr | en).
 *
 * Pattern taken from the RE/MAX demo (app/api/realtime/session), where the
 * model, voice and VAD choices were measured against the live API.
 */

const CLIENT_SECRETS_URL = "https://api.openai.com/v1/realtime/client_secrets";
const MODEL = process.env.REALTIME_MODEL || "gpt-realtime-2.1";
const VOICE = process.env.REALTIME_VOICE || "marin";
const TTL_SEC = 300; // the key only has to open the call; the browser hangs up at 180 s

// Requests from other sites are refused so the key can't be farmed elsewhere.
const ALLOWED = [/^https:\/\/(www\.)?atronai\.co$/, /^https:\/\/[a-z0-9-]+--[a-z0-9-]+\.netlify\.app$/, /^https:\/\/[a-z0-9-]+\.netlify\.app$/, /^http:\/\/localhost(:\d+)?$/];

const PERSONA = {
  tr: `Sen ATRON'sun: atronai.co sitesinde canlı çalışan bir yapay zekâ ajanısın. Yapay zekâ olduğunu açıkça söylersin, asla insan gibi davranmazsın.

Görevin: ziyaretçinin operasyonunu iki üç dakikada anlamak ve sonunda onun için kısa bir brief çıkarmak. Sırayla şunları öğren, her birini öğrenir öğrenmez update_brief aracıyla kaydet:
1. company: Şirket ya da sektör.
2. process: Ekibin en çok vaktini alan, tekrar eden iş.
3. volume: Bu iş ne sıklıkla oluyor (günde, haftada kaç kez ya da kaç kişi yapıyor).
4. channel: İş nerede dönüyor (telefon, WhatsApp, e-posta, form, saha).
5. systems: Kullandıkları sistemler (CRM, ERP, Excel vb.).
6. success: Bu iş düzelirse neyi ölçerek anlarlar.
7. name ve contact: Ziyaretçinin adı ve tercih ettiği iletişim (e-posta ya da telefon). Bunu en sona bırak ve zorlamadan sor.

Kurallar:
- Bir seferde en fazla iki kısa cümle. Tek soru sor, cevabı bekle.
- Ziyaretçi cevap vermek istemezse o alanı boş bırak ve geç.
- Fiyat, kesin teslim tarihi ya da garanti verme. Söyleyebileceğin tek taahhüt: "İlk hafta sizin sürecinizde çalışan bir prototip gösteriyoruz."
- Sitede yazanlar dışında müşteri, rakam ya da referans uydurma.
- Konu dağılırsa nazikçe operasyona dön.
- Bütün alanlar dolunca ya da ziyaretçi bitirmek isteyince finish_brief çağır, brief'i bir cümleyle özetle ve "Brief'i ekrandaki butonla Can'a gönderebilirsiniz" de.
- Bir aracı çağırmadan önce hattı sessiz bırakma; kısa bir şey söyle.

TÜRKÇE KONUŞ. İstanbul Türkçesi, doğal ve sıcak ama kısa.`,
  en: `You are ATRON: a live AI agent running on the atronai.co website. You say plainly that you are an AI and never pretend to be human.

Your job: understand the visitor's operation in two or three minutes and produce a short brief for them. Learn these in order and save each one with the update_brief tool as soon as you know it:
1. company: Company or sector.
2. process: The repetitive work that takes most of the team's time.
3. volume: How often it happens (per day or week, or how many people do it).
4. channel: Where it happens (phone, WhatsApp, email, forms, field).
5. systems: The systems they use (CRM, ERP, spreadsheets, etc.).
6. success: What they would measure to know it got better.
7. name and contact: The visitor's name and preferred contact (email or phone). Leave this for last and ask lightly.

Rules:
- At most two short sentences per turn. One question at a time, then wait.
- If the visitor doesn't want to answer, leave that field empty and move on.
- Never quote prices, firm delivery dates or guarantees. The only promise you can make: "In the first week we show a prototype running in your own process."
- Don't invent customers, numbers or references beyond what the website says.
- If the conversation drifts, steer gently back to the operation.
- When all fields are filled or the visitor wants to stop, call finish_brief, summarise the brief in one sentence and say "You can send the brief to Can with the button on screen."
- Don't leave the line silent before calling a tool; say something short.

Speak English, natural and warm but brief.`,
};

const FIELDS = ["company", "process", "volume", "channel", "systems", "success", "name", "contact"];

const TOOLS = [
  {
    type: "function",
    name: "update_brief",
    description: "Save one or more brief fields as soon as the visitor tells you. Only include fields you actually learned.",
    parameters: {
      type: "object",
      properties: Object.fromEntries(FIELDS.map((f) => [f, { type: "string" }])),
      additionalProperties: false,
    },
  },
  {
    type: "function",
    name: "finish_brief",
    description: "Call when the brief is complete or the visitor wants to stop.",
    parameters: {
      type: "object",
      properties: { summary: { type: "string", description: "One-sentence summary of the brief." } },
      required: ["summary"],
      additionalProperties: false,
    },
  },
];

const TRANSCRIBE_HINT = {
  tr: "Şirket operasyonu hakkında görüşme. Geçen sözcükler: ATRON, CRM, ERP, WhatsApp, çağrı merkezi, lead, Excel, saha, form.",
  en: "A conversation about company operations. Words: ATRON, CRM, ERP, WhatsApp, call centre, lead, spreadsheet, field, form.",
};

function json(status, body, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json",
      "cache-control": "no-store",
      ...(origin ? { "access-control-allow-origin": origin, vary: "Origin" } : {}),
    },
  });
}

export default async (req) => {
  const origin = req.headers.get("origin") || "";
  const allowed = ALLOWED.some((re) => re.test(origin));
  if (req.method !== "POST") return json(405, { error: "POST only" });
  if (!allowed) return json(403, { error: "origin not allowed" });
  if (!process.env.OPENAI_API_KEY) return json(503, { error: "live agent not configured" }, origin);

  let lang = "tr";
  try {
    const body = await req.json();
    if (body?.lang === "en") lang = "en";
  } catch {
    // no body: Turkish
  }

  const res = await fetch(CLIENT_SECRETS_URL, {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      expires_after: { anchor: "created_at", seconds: TTL_SEC },
      session: {
        type: "realtime",
        model: MODEL,
        instructions: PERSONA[lang],
        output_modalities: ["audio"],
        audio: {
          input: {
            format: { type: "audio/pcm", rate: 24000 },
            noise_reduction: { type: "near_field" },
            transcription: { model: "gpt-4o-transcribe", language: lang, prompt: TRANSCRIBE_HINT[lang] },
            turn_detection: { type: "semantic_vad", eagerness: "low", create_response: true, interrupt_response: true },
          },
          output: { voice: VOICE, speed: 1.0 },
        },
        tool_choice: "auto",
        tools: TOOLS,
      },
    }),
  });

  if (!res.ok) return json(502, { error: `upstream ${res.status}` }, origin);
  const data = await res.json();
  return json(200, { value: data.value, expiresAt: data.expires_at, model: MODEL }, origin);
};

export const config = { path: "/api/realtime-session" };
