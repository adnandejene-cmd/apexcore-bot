"""
╔══════════════════════════════════════════╗
║   APEX BUSINESS BOT — by Adnan          ║
║   AI Agents • Web Creation • Editing    ║
║   Languages: English | አማርኛ | Afan Oromo ║
╚══════════════════════════════════════════╝
"""

import logging
import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    filters, ContextTypes, CallbackQueryHandler,
)

# ─────────────────────────────────────────────
# 🔧 CONFIG
# ─────────────────────────────────────────────
BOT_TOKEN   = os.environ.get("BOT_TOKEN")
ADMIN_CHAT  = os.environ.get("ADMIN_CHAT_ID")

# ─────────────────────────────────────────────
# 🌐 CONTENT — All 3 Languages
# ─────────────────────────────────────────────

CONTENT = {

    # ══════════════ ENGLISH ══════════════
    "en": {
        "welcome": (
            "⚡ *Welcome to Apex Elite Services!* ⚡\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👋 Hello! I'm *Adnan*'s business assistant.\n\n"
            "🤖 AI Agents  •  🌐 Web Creation  •  🎬 Editing\n\n"
            "✅ _Professional service. Rapid response._\n"
            "_All messages replied to in minutes._\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👇 *Choose a service below:*"
        ),
        "ai": (
            "🤖 *AI Agent Creation*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "We build *intelligent bots* that work for your business *24/7* — no breaks, no delays.\n\n"
            "💡 *What our AI Agents do:*\n"
            "• ✅ Automate customer service replies\n"
            "• ✅ Handle sales conversations\n"
            "• ✅ Take orders automatically\n"
            "• ✅ Send reminders & follow-ups\n"
            "• ✅ Connect to Telegram, WhatsApp & web\n\n"
            "📊 *Result:* Save hours daily. Earn while you sleep.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Ready to start? Message *Adnan* for a quote.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "web": (
            "🌐 *Web Creation*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "We build *high-speed, mobile-first* premium websites that turn visitors into paying customers.\n\n"
            "💡 *What we deliver:*\n"
            "• ✅ Fast-loading, modern design\n"
            "• ✅ Mobile & desktop optimized\n"
            "• ✅ SEO-ready from day one\n"
            "• ✅ E-commerce & booking systems\n"
            "• ✅ Landing pages that convert\n\n"
            "📊 *Result:* A website that works as hard as you do.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Ready to start? Message *Adnan* for a quote.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "edit": (
            "🎬 *Media Editing*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "We provide *high-tier video & photo editing* that makes your brand look elite, trusted, and unforgettable.\n\n"
            "💡 *What we create:*\n"
            "• ✅ Professional video editing\n"
            "• ✅ Brand photo retouching\n"
            "• ✅ Social media content\n"
            "• ✅ Reels, shorts & ads\n"
            "• ✅ Thumbnails & graphics\n\n"
            "📊 *Result:* Content that stops the scroll.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Ready to start? Message *Adnan* for a quote.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "join": (
            "🤝 *Join the Apex Team*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Are you skilled in any of these?\n\n"
            "• 🤖 AI Bot Development\n"
            "• 🌐 Web Design & Development\n"
            "• 🎬 Video / Photo Editing\n"
            "• 📣 Social Media Management\n"
            "• 📝 Content Writing\n\n"
            "We're looking for *talented freelancers* to join our growing team!\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📩 Send your portfolio & skills to *Adnan*:\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "contact": (
            "📞 *Contact Adnan*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 *Phone:*    0906139339\n"
            "💬 *Telegram:* @ApexOTC\\_Global1\n"
            "👥 *Group:*    @ApexOTC\\_Global\n\n"
            "⏱ _Professional service. Rapid response._\n"
            "_All messages replied to in minutes._\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🕐 Available: Mon–Sat, 9AM–9PM"
        ),
        "menu_label": "🇬🇧 English menu active",
        "btn_ai":      "🤖 AI Solutions",
        "btn_web":     "🌐 Web Mastery",
        "btn_edit":    "🎬 Media Editing",
        "btn_portfolio":"💎 Portfolio & Proof",
        "btn_join":    "🤝 Join the Team",
        "btn_contact": "📞 Contact Adnan",
        "btn_lang":    "🌐 Change Language",
    },

    # ══════════════ AMHARIC ══════════════
    "am": {
        "welcome": (
            "⚡ *እንኳን ደህና መጡ — Apex Elite!* ⚡\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👋 ሰላም! እኔ *Adnan* ን ንግድ ረዳት ነኝ።\n\n"
            "🤖 AI ወኪሎች  •  🌐 ድር ፈጠራ  •  🎬 አርትዖት\n\n"
            "✅ _ፕሮፌሽናል አገልግሎት። ፈጣን ምላሽ።_\n"
            "_ሁሉም መልዕክቶች በደቂቃዎች ይመለሳሉ።_\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👇 *ከታች አንድ አገልግሎት ይምረጡ:*"
        ),
        "ai": (
            "🤖 *AI ወኪል ፈጠራ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "ለእርስዎ ንግድ *24/7* የሚሰሩ ዘመናዊ *AI ቦቶች* እንሰራለን።\n\n"
            "💡 *AI ወኪሎቻችን የሚያደርጉት:*\n"
            "• ✅ የደንበኞች አጠቃቀምን ራሱ ይመልሳሉ\n"
            "• ✅ ሽያጮችን ያስተዳድራሉ\n"
            "• ✅ ትዕዛዞችን ራሱ ይቀበላሉ\n"
            "• ✅ ማስታወሻዎችን ይልካሉ\n"
            "• ✅ ቴሌግራም፣ WhatsApp እና ድርን ያገናኛሉ\n\n"
            "📊 *ውጤት:* ጊዜ ቆጥቡ። በእንቅልፍ ጊዜ ያግኙ።\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 ለመጀመር ዝግጁ ነዎት? *Adnan* ን ያናግሩ።\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "web": (
            "🌐 *ድር ፈጠራ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "ጎብኝዎቹን ወደ ደንበኞች የሚቀይሩ *ፈጣን፣ ሞባይል-ፈርስት* ዌብሳይቶችን እንሰራለን።\n\n"
            "💡 *የምናቀርበው:*\n"
            "• ✅ ዘመናዊ፣ ፈጣን ዲዛይን\n"
            "• ✅ ሞባይልና ዴስክቶፕ ተስማሚ\n"
            "• ✅ SEO ዝግጁ\n"
            "• ✅ ኢ-ኮሜርስ እና የቅጥያ ስርዓቶች\n"
            "• ✅ ሽያጭ የሚያስፋፉ ገፆች\n\n"
            "📊 *ውጤት:* ለእርስዎ ንግድ እንደሚሰራ ዌብሳይት።\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 ለመጀመር ዝግጁ ነዎት? *Adnan* ን ያናግሩ።\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "edit": (
            "🎬 *ሚዲያ አርትዖት*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "ብራንድዎን ልዩ፣ ታማኝ እና የማይረሳ የሚያደርጉ *ከፍተኛ ደረጃ ቪዲዮ እና ፎቶ አርትዖት* እናቀርባለን።\n\n"
            "💡 *የምንሰጠው:*\n"
            "• ✅ ፕሮፌሽናል ቪዲዮ አርትዖት\n"
            "• ✅ የብራንድ ፎቶ ማሻሻያ\n"
            "• ✅ ሶሻል ሚዲያ ይዘቶች\n"
            "• ✅ Reels፣ Shorts እና ማስታወቂያዎች\n"
            "• ✅ Thumbnails እና ግራፊክስ\n\n"
            "📊 *ውጤት:* ሰዎችን ያቆማሉ — ያሳምናሉ።\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 ለመጀመር ዝግጁ ነዎት? *Adnan* ን ያናግሩ።\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "join": (
            "🤝 *ቡድናችንን ይቀላቀሉ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "በእነዚህ ውስጥ ክህሎት አለዎት?\n\n"
            "• 🤖 AI Bot ልማት\n"
            "• 🌐 ድር ዲዛይን እና ልማት\n"
            "• 🎬 ቪዲዮ / ፎቶ አርትዖት\n"
            "• 📣 ሶሻል ሚዲያ አስተዳደር\n"
            "• 📝 ይዘት ጽሁፍ\n\n"
            "ወደ ቡድናችን *ተሰጥኦ ያላቸው ፍሪላንሰሮች* እንፈልጋለን!\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📩 ፖርትፎሊዮዎን ወደ *Adnan* ይላኩ:\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "contact": (
            "📞 *Adnan ን አግኙ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 *ስልክ:*      0906139339\n"
            "💬 *ቴሌግራም:*  @ApexOTC\\_Global1\n"
            "👥 *ቡድን:*     @ApexOTC\\_Global\n\n"
            "⏱ _ፕሮፌሽናል አገልግሎት። ፈጣን ምላሽ።_\n"
            "_ሁሉም መልዕክቶች በደቂቃዎች ይመለሳሉ።_\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🕐 ሰኞ–ቅዳሜ፣ ጠዋት 9 — ማታ 9"
        ),
        "menu_label": "🇪🇹 አማርኛ ምናሌ ንቁ ነው",
        "btn_ai":      "🤖 AI መፍትሔዎች",
        "btn_web":     "🌐 ድር ጌትነት",
        "btn_edit":    "🎬 ሚዲያ አርትዖት",
        "btn_portfolio":"💎 ስራዎቻችን",
        "btn_join":    "🤝 ቡድን ተቀላቀሉ",
        "btn_contact": "📞 Adnan ን አግኙ",
        "btn_lang":    "🌐 ቋንቋ ቀይር",
    },

    # ══════════════ OROMO ══════════════
    "or": {
        "welcome": (
            "⚡ *Baga Nagaan Dhuftan — Apex Elite!* ⚡\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👋 Akkam! Ani gargaaraa daldala *Adnan* dha.\n\n"
            "🤖 AI Agents  •  🌐 Web  •  🎬 Editing\n\n"
            "✅ _Tajaajila ogummaa. Deebii ariifataa._\n"
            "_Ergaan hunduu daqiiqaadhaan deebifama._\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👇 *Tajaajila filadhu:*"
        ),
        "ai": (
            "🤖 *Uumama AI Agent*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Bot *AI* cimoo *sa'aatii 24/7* hojjetan daldalaadhaf ijaaraa jirra.\n\n"
            "💡 *AI Agents keenya maal hojjetan:*\n"
            "• ✅ Deebii gaafattoota ofumaan kennu\n"
            "• ✅ Gurgurtaa too'atu\n"
            "• ✅ Ajaja ofumaan fudhatu\n"
            "• ✅ Yaadachiisaafi hordoffii erguu\n"
            "• ✅ Telegram, WhatsApp fi web walqabsiisu\n\n"
            "📊 *Bu'aa:* Sa'aatii qusadhu. Rafee kasbi.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Jalqabuuf qophaahee? *Adnan* dubbisi.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "web": (
            "🌐 *Uumama Web*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Daawwattoota gara maamiloota jijjiiran weebsaayitii *ariifataa, mobaayila-dursa* ijaaraa jirra.\n\n"
            "💡 *Maal kennina:*\n"
            "• ✅ Dizaayinii ammayyaa, saffisaa\n"
            "• ✅ Mobaayilii fi kompuutaraa mijataa\n"
            "• ✅ SEO qophaahaa\n"
            "• ✅ Sirna gurgurtaa fi galmeessuu\n"
            "• ✅ Fuuloota jijjiirraa guddisan\n\n"
            "📊 *Bu'aa:* Weebsaayitii daldalaaf hojjetu.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Jalqabuuf qophaahee? *Adnan* dubbisi.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "edit": (
            "🎬 *Gulantaa Miidiyaa*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Braandii keessan addaa, amanamaa fi dagatamuu hin dandeenye godhuuf *gulantaa viidiyoo fi suuraa sadarkaa olaanaa* dhiyeessina.\n\n"
            "💡 *Maal uumna:*\n"
            "• ✅ Gulantaa viidiyoo ogummaa\n"
            "• ✅ Suura braandii fooyyessuu\n"
            "• ✅ Qabiyyee miidiyaa hawaasaa\n"
            "• ✅ Reels, Shorts fi beeksisa\n"
            "• ✅ Thumbnails fi graafiiksii\n\n"
            "📊 *Bu'aa:* Namoota dhaabu — amansiisu.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💬 Jalqabuuf qophaahee? *Adnan* dubbisi.\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "join": (
            "🤝 *Garee Keenyatti Makamu*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Ogummaa kanaa qabdaa?\n\n"
            "• 🤖 Guddinsa Bot AI\n"
            "• 🌐 Dizaayinii fi guddinsa Web\n"
            "• 🎬 Gulantaa viidiyoo / suuraa\n"
            "• 📣 Bulchiinsa miidiyaa hawaasaa\n"
            "• 📝 Barreeffama qabiyyee\n\n"
            "Garee guddinaa keenyaaf *firilaansaroonni dandeettii qaban* barbaachisa!\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📩 Porfaayilii keessan gara *Adnan* ergi:\n"
            "📱 0906139339  |  @ApexOTC\\_Global1"
        ),
        "contact": (
            "📞 *Adnan Dubbisi*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 *Bilbila:*    0906139339\n"
            "💬 *Telegram:*  @ApexOTC\\_Global1\n"
            "👥 *Garee:*     @ApexOTC\\_Global\n\n"
            "⏱ _Tajaajila ogummaa. Deebii ariifataa._\n"
            "_Ergaan hunduu daqiiqaadhaan deebifama._\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🕐 Wiixata–Sanbata, ganama 9 — galgala 9"
        ),
        "menu_label": "🇪🇹 Afan Oromo filatameera",
        "btn_ai":      "🤖 Furmaata AI",
        "btn_web":     "🌐 Ogeessa Web",
        "btn_edit":    "🎬 Gulantaa Miidiyaa",
        "btn_portfolio":"💎 Hojii Keenya",
        "btn_join":    "🤝 Garee Makamu",
        "btn_contact": "📞 Adnan Dubbisi",
        "btn_lang":    "🌐 Afaan Jijjiiri",
    },
}

# ─────────────────────────────────────────────
# ⌨️ KEYBOARDS
# ─────────────────────────────────────────────
def lang_keyboard():
    """Language selection screen."""
    buttons = [
        [KeyboardButton("🇬🇧 English")],
        [KeyboardButton("🇪🇹 አማርኛ")],
        [KeyboardButton("🇪🇹 Afan Oromo")],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def main_menu(lang: str):
    c = CONTENT[lang]
    buttons = [
        [KeyboardButton(c["btn_ai"]),        KeyboardButton(c["btn_web"])],
        [KeyboardButton(c["btn_edit"]),      KeyboardButton(c["btn_portfolio"])],
        [KeyboardButton(c["btn_join"]),      KeyboardButton(c["btn_contact"])],
        [KeyboardButton(c["btn_lang"])],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def portfolio_inline():
    """Inline button for group link."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👥 Visit @ApexOTC_Global", url="https://t.me/ApexOTC_Global")]
    ])

def contact_inline():
    """Inline button for direct DM."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Message Adnan on Telegram", url="https://t.me/ApexOTC_Global1")]
    ])

# ─────────────────────────────────────────────
# 🛠 HELPERS
# ─────────────────────────────────────────────
def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", "en")

# ─────────────────────────────────────────────
# 🏁 HANDLERS
# ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 *Choose your language / ቋንቋ ይምረጡ / Afaan filadhu:*",
        parse_mode="Markdown",
        reply_markup=lang_keyboard()
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    lang = get_lang(context)
    c    = CONTENT[lang]

    # ── Language selection ──
    if text == "🇬🇧 English":
        context.user_data["lang"] = "en"
        lang = "en"
        c    = CONTENT["en"]
        await update.message.reply_text(
            CONTENT["en"]["welcome"],
            parse_mode="Markdown",
            reply_markup=main_menu("en")
        )
        return

    if text == "🇪🇹 አማርኛ":
        context.user_data["lang"] = "am"
        lang = "am"
        c    = CONTENT["am"]
        await update.message.reply_text(
            CONTENT["am"]["welcome"],
            parse_mode="Markdown",
            reply_markup=main_menu("am")
        )
        return

    if text == "🇪🇹 Afan Oromo":
        context.user_data["lang"] = "or"
        lang = "or"
        c    = CONTENT["or"]
        await update.message.reply_text(
            CONTENT["or"]["welcome"],
            parse_mode="Markdown",
            reply_markup=main_menu("or")
        )
        return

    # ── Language change button ──
    if text == c["btn_lang"]:
        await update.message.reply_text(
            "🌐 *Choose your language / ቋንቋ ይምረጡ / Afaan filadhu:*",
            parse_mode="Markdown",
            reply_markup=lang_keyboard()
        )
        return

    # ── AI ──
    if text == c["btn_ai"]:
        await update.message.reply_text(
            c["ai"], parse_mode="Markdown",
            reply_markup=contact_inline()
        )
        return

    # ── Web ──
    if text == c["btn_web"]:
        await update.message.reply_text(
            c["web"], parse_mode="Markdown",
            reply_markup=contact_inline()
        )
        return

    # ── Editing ──
    if text == c["btn_edit"]:
        await update.message.reply_text(
            c["edit"], parse_mode="Markdown",
            reply_markup=contact_inline()
        )
        return

    # ── Portfolio ──
    if text == c["btn_portfolio"]:
        await update.message.reply_text(
            "💎 *Portfolio & Proof*\n\n"
            "See Adnan's real work and client results in our group 👇",
            parse_mode="Markdown",
            reply_markup=portfolio_inline()
        )
        return

    # ── Join team ──
    if text == c["btn_join"]:
        await update.message.reply_text(
            c["join"], parse_mode="Markdown",
            reply_markup=contact_inline()
        )
        return

    # ── Contact ──
    if text == c["btn_contact"]:
        await update.message.reply_text(
            c["contact"], parse_mode="Markdown",
            reply_markup=contact_inline()
        )
        return

    # ── Default (no language set yet) ──
    await update.message.reply_text(
        "🌐 *Choose your language / ቋንቋ ይምረጡ / Afaan filadhu:*",
        parse_mode="Markdown",
        reply_markup=lang_keyboard()
    )

# ─────────────────────────────────────────────
# 🚀 MAIN
# ─────────────────────────────────────────────
def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Apex Business Bot is live — Adnan's system running!")
    app.run_polling()

if __name__ == "__main__":
    main()
