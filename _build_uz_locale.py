#!/usr/bin/env python3
"""
Build /uz/ Uzbek (Latin script) locale from /ru/.

Strategy
--------
1. Clone /ru/ -> /uz/ (19 pages)
2. Rewrite paths /ru/ -> /uz/
3. Rewrite html lang attr ru -> uz
4. Translate Russian -> Uzbek (Latin) via a comprehensive ordered phrase map
5. Add a self-referential hreflang="uz" to each /uz/ page
6. Update header/footer lang switcher to include "O'zbekcha" and mark uz as selected
7. Tag the head with og:locale + meta lang
"""
from __future__ import annotations
import re, shutil
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
SRC  = ROOT / "ru"
DST  = ROOT / "uz"

# -----------------------------------------------------------------------------
# 1. clone /ru/ -> /uz/
# -----------------------------------------------------------------------------
if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
print(f"cloned {SRC.relative_to(ROOT)} -> {DST.relative_to(ROOT)}")

# -----------------------------------------------------------------------------
# 2/3/4. translate
# -----------------------------------------------------------------------------
# Ordered list of (Russian, Uzbek-Latin) replacements.
# IMPORTANT: longest/most-specific phrases first so they win the replace before
# shorter substrings inside them get rewritten. Keep MAX3000, $3000, 40x, names,
# domains, license codes, and dates untouched (they're already Latin).
#
# Uzbek (Latin) follows the 1995 reformed alphabet used officially since 2023:
# o' (o-okina), g' (g-okina), ch, sh, no Cyrillic.
PAIRS: list[tuple[str, str]] = [
    # ----- meta / SEO titles & descriptions -----
    ("Промокод Stake MAX3000 - 200% до $3000 при регистрации",
     "Stake MAX3000 promokodi - ro'yxatdan o'tishda 200% gacha $3000"),
    ("Эксклюзивный клуб для игроков Stake.com. С промокодом MAX3000 вы получаете до $3000 при 200%, отыгрыш 40x от депозита+бонуса. GGR $4.7B, лицензия Curacao OGL/2024/1451/0918, основан в 2017.",
     "Stake.com o'yinchilari uchun eksklyuziv klub. MAX3000 promokodi bilan 200% miqdorida $3000 gacha, depozit+bonusdan 40x veyjer olasiz. GGR $4.7B, Curacao OGL/2024/1451/0918 litsenziyasi, 2017-yilda ochilgan."),
    ("WinnersClub | Промокод Stake MAX3000 | 200% до $3000, вейджер 40x",
     "WinnersClub | Stake MAX3000 promokodi | 200% gacha $3000, 40x veyjer"),
    ("Эксклюзивный клуб Stake.com. Промокод MAX3000: 200% до $3000, вейджер 40x депозит+бонус. GGR $4.7B.",
     "Stake.com eksklyuziv klubi. MAX3000 promokodi: 200% gacha $3000, depozit+bonusga 40x veyjer. GGR $4.7B."),
    ("WinnersClub - Внутри Клуба Stake | Промокод MAX3000, 200% до $3000",
     "WinnersClub - Stake klubi ichida | MAX3000 promokodi, 200% gacha $3000"),
    ("Эксклюзивный клуб игроков Stake.com. Промокод MAX3000: 200% до $3000, вейджер 40x. GGR $4.7B, лицензия Curacao OGL/2024/1451/0918.",
     "Stake.com o'yinchilarining eksklyuziv klubi. MAX3000 promokodi: 200% gacha $3000, 40x veyjer. GGR $4.7B, Curacao OGL/2024/1451/0918 litsenziyasi."),

    # ----- FAQ schema (escaped) -----
    ("MAX3000 - самый большой бонусный код Stake?",
     "MAX3000 - Stake'ning eng katta bonus kodimi?"),
    ("Да. 200% до $3000 с вейджером 40x. Большинство публичных кодов ограничиваются 100%/$1000.",
     "Ha. 40x veyjer bilan 200% gacha $3000. Ko'pchilik ommaviy kodlar 100%/$1000 bilan cheklangan."),
    ("Stake.com - надёжный?",
     "Stake.com ishonchlimi?"),
    ("Stake работает с 2017 под лицензией Curacao OGL/2024/1451/0918. Резервы $339.53M на 28 мая 2026. Основатели Ed Craven и Bijan Tehrani.",
     "Stake 2017-yildan beri Curacao OGL/2024/1451/0918 litsenziyasi ostida ishlaydi. 2026-yil 28-maydagi rezervlar $339.53M. Asoschilari Ed Craven va Bijan Tehrani."),
    ("Могу ли я проверить резервы Stake?",
     "Stake rezervlarini tekshirishim mumkinmi?"),
    ("Снимок 28 мая 2026: $339.53M в кошельках Arkham. Ethereum 74%, Solana 14%. Отслеживается на cryptotips.com.",
     "2026-yil 28-may holatiga ko'ra: Arkham hamyonlarida $339.53M. Ethereum 74%, Solana 14%. cryptotips.com'da kuzatiladi."),
    ("Где я могу играть?",
     "Qayerda o'ynashim mumkin?"),
    ("Лицензия Curacao охватывает большинство стран. Используйте страницу зеркал для домена вашего региона.",
     "Curacao litsenziyasi aksariyat mamlakatlarni qamrab oladi. O'z mintaqangiz domenini topish uchun aks ettirish sahifasidan foydalaning."),
    ("Как быстро происходит вывод?",
     "Pul yechib olish qancha tez amalga oshadi?"),
    ("Как быстро происходит вывод средств?",
     "Pul yechib olish qancha tez amalga oshadi?"),
    ("Крипто: 30-60 минут. TRX, XRP, SOL: секунды. Крупные: 2-4 дня. MoonPay фиат: 1-5 дней.",
     "Kripto: 30-60 daqiqa. TRX, XRP, SOL: soniyalar. Yiriklari: 2-4 kun. MoonPay fiat: 1-5 kun."),

    # ----- header / nav -----
    ("WinnersClub Главная", "WinnersClub Bosh sahifa"),
    ("Главная", "Bosh sahifa"),
    ("Казино Stake", "Stake Kazinosi"),
    ("Спорт Stake", "Stake Sport"),
    ("Покер Stake", "Stake Poker"),
    ("Авиатор Stake", "Stake Aviator"),
    ("Промокод Stake", "Stake promokodi"),
    ("Промокод MAX3000", "MAX3000 promokodi"),
    ("Казино", "Kazino"),
    ("Спорт", "Sport"),
    ("Покер", "Poker"),
    ("Авиатор", "Aviator"),
    ("Промокод", "Promokod"),
    ("Резервы", "Rezervlar"),
    ("О Stake.com", "Stake.com haqida"),
    ("О Stake", "Stake haqida"),
    ("Войти", "Kirish"),
    ("Закрыть", "Yopish"),
    ("Язык", "Til"),

    # ----- hero -----
    ("Если вы нашли эту страницу, вышибала уже дал вам зелёный свет.",
     "Agar ushbu sahifani topgan bo'lsangiz, eshik soqchisi sizga yashil chiroq yoqib qo'ygan."),
    ("Добро пожаловать в клуб.", "Klubga xush kelibsiz."),
    ("Закрытая комната для игроков Stake. Шепните",
     "Stake o'yinchilari uchun yopiq xona. Eshik oldida"),
    ("у входа и вас ждут",
     "deb shivirlang va sizni"),
    ("с",
     "kutadi:"),
    ("Публичные коды рядом не стоят.",
     "Ommaviy kodlar bilan taqqoslab bo'lmaydi."),
    ("Получить 200% до $3000 на Stake.com",
     "Stake.com'da 200% gacha $3000 olish"),
    ("Что открывает MAX3000",
     "MAX3000 nima ochadi"),

    # ----- reserves ticker -----
    ("Stake on-chain сейчас: помеченные резервы $339.53M",
     "Stake on-chain hozir: belgilangan rezervlar $339.53M"),
    ("Лицензия Curacao OGL/2024/1451/0918",
     "Curacao OGL/2024/1451/0918 litsenziyasi"),
    ("Источник: Arkham Intel через cryptotips.com",
     "Manba: Arkham Intel cryptotips.com orqali"),
    ("Снимок 28 мая 2026",
     "2026-yil 28-may holati"),

    # ----- promo strip -----
    ("Вейджер 40x", "40x veyjer"),
    ("Открыть страницу кода", "Kod sahifasini ochish"),

    # ----- "Why this club" -----
    ("Почему", "Nega"),
    ("этот клуб", "ushbu klub"),
    ("Серьёзный бонус", "Jiddiy bonus"),
    ("200% до $3000 с вейджером 40x на депозит+бонус. Другие публичные коды Stake ограничиваются 100% и $1000. Если не дадите дилеру",
     "Depozit+bonusga 40x veyjer bilan 200% gacha $3000. Boshqa ommaviy Stake kodlari 100% va $1000 bilan cheklangan. Agar ro'yxatdan o'tganingizdan keyin 24 soat ichida dilerga"),
    ("в течение 24 часов после регистрации, вернётесь в эконом-меню.",
     "bermasangiz, ekonom-menyuga qaytasiz."),
    ("Деньги на виду", "Pul ko'z o'ngida"),
    ("Помеченные Arkham резервы: $339.53M по состоянию на 28 мая 2026. Никаких PDF \"доверяйте нам\". Кошелёк публичный, любой с WiFi может провести аудит.",
     "Arkham tomonidan belgilangan rezervlar: 2026-yil 28-may holatiga ko'ra $339.53M. Hech qanday \"bizga ishoning\" deb yozilgan PDF yo'q. Hamyon ochiq, WiFi'si bor har bir kishi audit qila oladi."),
    ("Доказательства здесь.", "Dalillar shu yerda."),
    ("У дома есть лицо", "Uyning yuzi bor"),
    ("Ed Craven (Мельбурн, 1995) и Bijan Tehrani. Познакомились в RuneScape, основали Stake в 2017 году и запустили Kick в 2022-м. Совокупное состояние по оценке Forbes: $5.6B. Не подставная компания. Двое людей, которые не проигрывают.",
     "Ed Craven (Melburn, 1995) va Bijan Tehrani. RuneScape'da tanishishgan, Stake'ni 2017-yilda asos solishgan va 2022-yilda Kick'ni ishga tushirishgan. Forbes baholashicha jami boyligi: $5.6B. Soxta kompaniya emas. Yutqazmaydigan ikki kishi."),

    # ----- five rooms -----
    ("Пять комнат,", "Beshta xona,"),
    ("один код", "bitta kod"),
    ("Выберите дверь. MAX3000 работает во всех пяти. Дилеру всё равно, где вы используете бонус.",
     "Eshikni tanlang. MAX3000 beshtasida ham ishlaydi. Bonusni qayerda ishlatishingiz dilerga farqsiz."),
    ("Лайв", "Jonli"),

    # ----- girl break -----
    ("Три тысячи.", "Uch ming."),
    ("Один код.", "Bitta kod."),
    ("Шепните", "Shivirlang"),
    ("при регистрации. Прежде чем подадут первый напиток, математика уже будет на вашей стороне.",
     "ro'yxatdan o'tayotganda. Birinchi ichimlik keltirilgunga qadar matematika allaqachon siz tomonda bo'ladi."),
    ("Передать код дилеру", "Kodni dilerga uzatish"),

    # ----- intel -----
    ("Что", "Klub"),
    ("знает клуб", "nimani biladi"),
    ("Основатели", "Asoschilar"),
    ("Ed Craven (1995, Мельбурн) и Bijan Tehrani. Познакомились в RuneScape. Совместно основали Stake в 2017 году. Запустили Kick в 2022 году.",
     "Ed Craven (1995, Melburn) va Bijan Tehrani. RuneScape'da tanishishgan. Stake'ni 2017-yilda birgalikda asos solishgan. Kick'ni 2022-yilda ishga tushirishgan."),
    ("Оператор", "Operator"),
    ("Организация на Кюрасао, управляющая Stake.com. Материнская компания: Easygo Group Holdings, выручка за FY2025 A$970M. Stake.us - отдельная sweepstakes-компания.",
     "Kyurasaodagi tashkilot, Stake.com'ni boshqaradi. Ona kompaniya: Easygo Group Holdings, FY2025 daromadi A$970M. Stake.us - alohida sweepstakes kompaniyasi."),
    ("Лицензия", "Litsenziya"),
    ("Охватывает большинство стран. UK вышел в марте 2025. США заблокированы (Stake.us sweepstakes доступен в 30+ штатах). Более 22 зеркальных сайтов подтверждено.",
     "Aksariyat mamlakatlarni qamrab oladi. Buyuk Britaniya 2025-yil mart oyida chiqib ketdi. AQSh bloklangan (Stake.us sweepstakes 30+ shtatda mavjud). 22dan ortiq aks ettirilgan saytlar tasdiqlangan."),
    ("Помечены Arkham по состоянию на 28 мая 2026. Ethereum 74%, Solana 14%, девятизначный баланс стейблкоинов. Отслеживается на cryptotips.com.",
     "2026-yil 28-may holatiga Arkham belgilagan. Ethereum 74%, Solana 14%, to'qqiz xonali stablecoin balansi. cryptotips.com'da kuzatiladi."),

    # ----- two doors -----
    ("Две двери,", "Ikki eshik,"),
    ("MAX3000 признаётся как на Stake.com, так и на Stake.us. Приём за каждой дверью отличается. Дилер направит вас к нужной двери в зависимости от вашего местонахождения.",
     "MAX3000 ham Stake.com'da, ham Stake.us'da qabul qilinadi. Har bir eshik orqasidagi kutib olish farq qiladi. Joylashuvingizga qarab diler sizni kerakli eshikka yo'naltiradi."),
    ("Stake.com - Реальные деньги, Глобально", "Stake.com - Haqiqiy pul, Global"),
    ("Платформа для игры на реальные деньги, управляемая Medium Rare NV под лицензией Curacao OGL/2024/1451/0918. Крипто и фиат. Спорт, казино, оригиналы, покер. С промокодом",
     "Medium Rare NV tomonidan Curacao OGL/2024/1451/0918 litsenziyasi ostida boshqariladigan haqiqiy pul o'yin platformasi. Kripto va fiat. Sport, kazino, originallar, poker. Promokod"),
    ("вы получаете", "bilan siz olasiz:"),
    ("вейджер 40x на депозит+бонус, 30 дней, минимальный депозит $10. Заявите через лайв-поддержку после депозита. Требуется KYC уровня 3. Доступно в большинстве стран, кроме США и UK.",
     "depozit+bonusga 40x veyjer, 30 kun, eng kam depozit $10. Depozitdan keyin jonli yordam orqali da'vo qiling. 3-darajali KYC talab qilinadi. AQSh va Buyuk Britaniyadan tashqari ko'p mamlakatlarda mavjud."),
    ("Открыть глобальную дверь", "Global eshikni ochish"),
    ("Stake.us - Свипстейкс, США", "Stake.us - Sweepstakes, AQSh"),
    ("Американская sweepstakes-платформа под управлением Sweepsteaks Limited. Gold Coins для игры, Stake Cash для вывода после 3x отыгрыша. Без реальных депозитов/выводов, без спорта, только казино. Промокод",
     "Sweepsteaks Limited boshqaruvidagi amerikan sweepstakes platformasi. O'yin uchun Gold Coins, 3x veyjerdan keyin yechib olish uchun Stake Cash. Haqiqiy depozit/yechib olish yo'q, sportsiz, faqat kazino. Promokod"),
    ("также принимается и даёт", "shuningdek qabul qilinadi va beradi:"),
    ("3.5% рейкбэк", "3.5% reykbek"),
    ("Доступно в 37 штатах.", "37 shtatda mavjud."),
    ("Открыть американскую дверь", "Amerika eshigini ochish"),

    # ----- FAQ visible -----
    ("Вопросы", "Eshik oldidagi"),
    ("у входа", "savollar"),
    ("Да. 200% до $3000 с вейджером 40x на депозит+бонус. Большинство публичных кодов ограничиваются 100% / $1000. MAX3000 - это код, который клуб выдаёт у входа.",
     "Ha. Depozit+bonusga 40x veyjer bilan 200% gacha $3000. Ko'pchilik ommaviy kodlar 100% / $1000 bilan cheklangan. MAX3000 - bu klub eshik oldida beradigan kod."),
    ("Stake работает с 2017 года под лицензией Curacao OGL/2024/1451/0918 через Medium Rare NV. On-chain резервы на 28 мая 2026 составляют $339.53M, публично отслеживаются на Arkham. Основатели Ed Craven (1995, Мельбурн) и Bijan Tehrani также управляют Kick. Материнская Easygo Group Holdings отчиталась о A$970M выручки и A$257M чистой прибыли в FY2025.",
     "Stake 2017-yildan beri Medium Rare NV orqali Curacao OGL/2024/1451/0918 litsenziyasi ostida ishlaydi. 2026-yil 28-may holatiga on-chain rezervlar $339.53M, Arkham'da ochiq kuzatiladi. Asoschilari Ed Craven (1995, Melburn) va Bijan Tehrani Kick'ni ham boshqaradilar. Ona Easygo Group Holdings FY2025'da A$970M daromad va A$257M sof foyda haqida hisobot berdi."),
    ("Да, смотрите", "Ha,"),
    ("отчёт о резервах", "rezervlar hisobotiga qarang"),
    ("Снимок от 28 мая 2026 показывает $339.53M в кошельках, помеченных Arkham. Ethereum 74%, Solana 14%, девятизначный баланс стейблкоинов. Всё отслеживается на",
     ". 2026-yil 28-may holati Arkham tomonidan belgilangan hamyonlarda $339.53M ko'rsatadi. Ethereum 74%, Solana 14%, to'qqiz xonali stablecoin balansi. Hammasi"),
    ("с еженедельными данными Arkham Intel.",
     "Arkham Intel haftalik ma'lumotlari bilan kuzatiladi."),
    ("Лицензия Curacao охватывает большинство стран, но Stake имеет собственные ограничения в США, UK, части Австралии и ряде других стран. Используйте",
     "Curacao litsenziyasi aksariyat mamlakatlarni qamrab oladi, lekin Stake AQSh, Buyuk Britaniya, Avstraliyaning bir qismi va boshqa bir qator mamlakatlarda o'z cheklovlariga ega. O'z mintaqangiz domenini topish uchun"),
    ("страницу зеркальных сайтов", "aks ettirilgan saytlar sahifasidan"),
    ("чтобы найти домен для вашего региона.", "foydalaning."),
    ("Криптовыводы на обычные суммы обрабатываются за 30-60 минут. TRX, XRP, SOL зачисляются за секунды. Крупные суммы могут потребовать проверки комплаенса 2-4 рабочих дня. Фиатные выводы через MoonPay занимают 1-5 рабочих дней. Подробнее на",
     "Oddiy miqdordagi kripto yechib olishlar 30-60 daqiqada qayta ishlanadi. TRX, XRP, SOL soniyalarda hisobga olinadi. Yirik miqdorlar 2-4 ish kuni compliance tekshiruvini talab qilishi mumkin. MoonPay orqali fiat yechib olishlar 1-5 ish kuni davom etadi. Batafsil"),
    ("странице платежей", "to'lovlar sahifasida"),

    # ----- signature -----
    ("Скажите дилеру, что вас отправил WinnersClub.",
     "Dilerga sizni WinnersClub yuborganini ayting."),

    # ----- sticky CTA -----
    ("200% до $3000. Дверь Stake.com открыта",
     "200% gacha $3000. Stake.com eshigi ochiq"),
    ("Занять место", "Joyni egallash"),

    # ----- footer -----
    ("КЛУБ В STAKE С 2017 ГОДА.", "2017-YILDAN BERI STAKE'DAGI KLUB."),
    ("Залы", "Xonalar"),
    ("Живые коэффициенты", "Jonli koeffitsientlar"),
    ("Лайв коэффициенты", "Jonli koeffitsientlar"),
    ("Лайв казино", "Jonli kazino"),
    ("Код", "Kod"),
    ("Платежи", "To'lovlar"),
    ("Доступ и зеркала", "Kirish va aks ettirishlar"),
    ("Intel", "Intel"),
    ("On-chain резервы", "On-chain rezervlar"),
    ("WinnersClub - эксклюзивный клуб игроков Stake. Stake.com управляется компанией Medium Rare NV под лицензией Curacao OGL/2024/1451/0918. Stake.us - отдельная sweepstakes-платформа под управлением Sweepsteaks Limited. Этот сайт работает исключительно в информационных целях. Азартные игры несут риски. Играйте ответственно. Если у вас есть проблемы с азартными играми, обратитесь в GamCare или местную службу поддержки. 18+.",
     "WinnersClub - Stake o'yinchilarining eksklyuziv klubi. Stake.com Medium Rare NV tomonidan Curacao OGL/2024/1451/0918 litsenziyasi ostida boshqariladi. Stake.us - Sweepsteaks Limited boshqaruvidagi alohida sweepstakes platforma. Ushbu sayt faqat axborot maqsadlarida ishlaydi. Qimor o'yinlari xavf bilan bog'liq. Mas'uliyat bilan o'ynang. Agar qimor bilan bog'liq muammolaringiz bo'lsa, GamCare yoki mahalliy yordam xizmatiga murojaat qiling. 18+."),
    ("Все права защищены.", "Barcha huquqlar himoyalangan."),
    ("Другие залы клуба", "Klubning boshqa xonalari"),
    ("Проверенные резервы", "Tasdiqlangan rezervlar"),
    ("Крипто-платежи", "Kripto to'lovlar"),
    ("Зеркальные сайты", "Aks ettirilgan saytlar"),
    ("Stake Originals", "Stake Originallari"),
    ("VIP программа", "VIP dasturi"),
    ("Библиотека слотов", "Slotlar kutubxonasi"),

    # ----- categories from nav -----
    ("Слоты", "Slotlar"),
    ("Новости", "Yangiliklar"),
    ("Ответственная игра", "Mas'uliyatli o'yin"),
    ("Бонус Stake.us", "Stake.us bonusi"),
    ("Stake Engine", "Stake Engine"),
    ("Бонусный код", "Bonus kodi"),
    ("Зеркала", "Aks ettirishlar"),
    ("Зеркало", "Aks ettirish"),

    # ----- generic / scattered -----
    ("Внутри Клуба Stake", "Stake klubi ichida"),
    ("В клубе с 2017 года.", "Klubda 2017-yildan beri."),
    ("Эксклюзивный клуб", "Eksklyuziv klub"),
    ("игроков Stake.com", "Stake.com o'yinchilarining"),
    ("игроков Stake", "Stake o'yinchilarining"),
    ("Промокод:", "Promokod:"),
    ("Промокод", "Promokod"),
    ("Бонусный код:", "Bonus kodi:"),
    ("Бонусный код", "Bonus kodi"),
    ("Бонус", "Bonus"),
    ("депозит", "depozit"),
    ("Депозит", "Depozit"),
    ("вывод", "yechib olish"),
    ("Вывод", "Yechib olish"),
    ("отыгрыш", "veyjer"),
    ("Отыгрыш", "Veyjer"),
    ("Вейджер", "Veyjer"),
    ("вейджер", "veyjer"),
    ("реальные деньги", "haqiqiy pul"),
    ("РЕАЛЬНЫЕ ДЕНЬГИ", "HAQIQIY PUL"),
    ("на реальные деньги", "haqiqiy pulga"),
    ("снимок", "holat"),
    ("Снимок", "Holat"),
    ("резервы", "rezervlar"),
    ("Резервы", "Rezervlar"),
    ("резерв", "rezerv"),
    ("резервов", "rezervlar"),
    ("резервах", "rezervlar haqida"),
    ("лицензия", "litsenziya"),
    ("Лицензия", "Litsenziya"),
    ("лицензией", "litsenziya ostida"),
    ("регистрация", "ro'yxatdan o'tish"),
    ("регистрации", "ro'yxatdan o'tishda"),
    ("при регистрации", "ro'yxatdan o'tishda"),

    # ----- common Russian connector words / particles -----
    ("Stake.com", "Stake.com"),  # protected pass-through
    ("год", "yil"),
    ("года", "yil"),
    ("лет", "yil"),
    ("дней", "kun"),
    ("дня", "kun"),
    ("день", "kun"),
    ("минут", "daqiqa"),
    ("часов", "soat"),
    ("часа", "soat"),
    ("час", "soat"),
    ("секунд", "soniya"),
    ("неделя", "hafta"),
    ("недель", "hafta"),
    ("Январь", "Yanvar"),
    ("Февраль", "Fevral"),
    ("Март", "Mart"),
    ("Апрель", "Aprel"),
    ("Май", "May"),
    ("Июнь", "Iyun"),
    ("Июль", "Iyul"),
    ("Август", "Avgust"),
    ("Сентябрь", "Sentabr"),
    ("Октябрь", "Oktabr"),
    ("Ноябрь", "Noyabr"),
    ("Декабрь", "Dekabr"),
    ("января", "yanvar"),
    ("февраля", "fevral"),
    ("марта", "mart"),
    ("апреля", "aprel"),
    ("мая", "may"),
    ("июня", "iyun"),
    ("июля", "iyul"),
    ("августа", "avgust"),
    ("сентября", "sentabr"),
    ("октября", "oktabr"),
    ("ноября", "noyabr"),
    ("декабря", "dekabr"),
]

# Safety-net catch-alls (lowercase) for any cyrillic letter remaining.
# These are applied LAST. Common Russian fillers -> Uzbek approximations.
GENERIC_FILLERS: list[tuple[str, str]] = [
    # particles, prepositions, conjunctions - try not to overwrite mid-word.
    # We rely on the bulk of replacement happening via PAIRS above. Anything
    # that slips through these fillers will be flagged by the audit at the end.
    (" и ", " va "),
    (" или ", " yoki "),
    (" но ", " lekin "),
    (" а ", " ammo "),
    (" с ", " bilan "),
    (" в ", " da "),
    (" на ", " da "),
    (" по ", " bo'yicha "),
    (" под ", " ostida "),
    (" от ", " dan "),
    (" до ", " gacha "),
    (" из ", " dan "),
    (" за ", " uchun "),
    (" для ", " uchun "),
    (" как ", " kabi "),
    (" что ", " nima "),
    (" это ", " bu "),
    (" эти ", " bular "),
    (" этот ", " bu "),
    (" эта ", " bu "),
    (" Это ", " Bu "),
    (" есть ", " bor "),
    (" нет ", " yo'q "),
    (" не ", " emas "),
    (" да ", " ha "),
    (" Да", " Ha"),
    (" Нет", " Yo'q"),
    (" вы ", " siz "),
    (" Вы ", " Siz "),
    (" я ", " men "),
    (" мы ", " biz "),
    (" они ", " ular "),
    (" он ", " u "),
    (" она ", " u "),
]


def translate(text: str) -> str:
    # Apply ordered pairs
    for ru, uz in PAIRS:
        text = text.replace(ru, uz)
    # Final generic-fillers pass for any leftover scaffold (rare)
    for ru, uz in GENERIC_FILLERS:
        text = text.replace(ru, uz)
    return text


# -----------------------------------------------------------------------------
# Walk /uz/, translate + rewire each file
# -----------------------------------------------------------------------------
files_touched = 0
for path in DST.rglob("*.html"):
    text = path.read_text(encoding="utf-8")

    # Replace internal path prefix /ru/ -> /uz/
    text = text.replace("/ru/", "/uz/")
    # html lang attr
    text = re.sub(r'<html\s+lang="ru"', '<html lang="uz"', text)
    # canonical and og:url
    text = text.replace("winnersclub.com/ru/", "winnersclub.com/uz/")
    # OG locale meta (add or update)
    # If there's no og:locale, inject one after og:url
    if 'property="og:locale"' not in text:
        text = re.sub(
            r'(<meta\s+property="og:url"[^>]*>)',
            r'\1\n  <meta property="og:locale" content="uz_UZ">',
            text,
            count=1,
        )
    else:
        text = re.sub(
            r'<meta\s+property="og:locale"\s+content="[^"]*"\s*/?>',
            '<meta property="og:locale" content="uz_UZ">',
            text,
        )

    # Add/replace hreflang="uz" self-reference. Insert it next to the pl entry.
    if 'hreflang="uz"' not in text:
        # Compute /uz/ self URL based on directory
        rel = path.relative_to(DST).as_posix()
        if rel == "index.html":
            uz_url = "https://winnersclub.com/uz/"
        else:
            uz_url = f"https://winnersclub.com/uz/{rel.rsplit('/', 1)[0]}/"
        # Insert just before x-default
        text = re.sub(
            r'(<link rel="alternate" hreflang="x-default" href="[^"]+">)',
            f'<link rel="alternate" hreflang="uz" href="{uz_url}">\n  \\1',
            text,
            count=1,
        )

    # Translate text content
    text = translate(text)

    # Lang switcher: mark the /uz/ option as selected, add an Uzbek option if missing
    # Replace selected attribute placements first:
    # Old /ru/: <option value="" selected>RU</option> for desktop switcher
    text = re.sub(
        r'<option value=""[^>]*selected[^>]*>RU</option>',
        '<option value="https://winnersclub.com/ru/">Русский</option>',
        text,
    )
    # In mobile select, the /ru/ option was just a plain option; we now want
    # /uz/ to be the SELECTED one. Mobile switcher uses path-relative values.
    # If we don't already have a /uz/ <option>, splice one in next to /ru/.
    if 'value="/uz/"' not in text:
        text = text.replace(
            '<option value="/ru/">Русский (Russian)</option>',
            '<option value="/ru/">Русский (Russian)</option><option value="/uz/" selected>O\'zbekcha (Uzbek)</option>',
        )
    if 'value="https://winnersclub.com/uz/"' not in text:
        text = text.replace(
            '<option value="https://winnersclub.com/ru/">Русский</option>',
            '<option value="https://winnersclub.com/ru/">Русский</option><option value="" selected>UZ</option>',
        )

    path.write_text(text, encoding="utf-8")
    files_touched += 1

print(f"translated + rewired {files_touched} files under /uz/")

# Audit: detect leftover cyrillic
import json
leftovers = {}
for path in DST.rglob("*.html"):
    txt = path.read_text(encoding="utf-8")
    cyr = re.findall(r"[\u0400-\u04FF]+", txt)
    if cyr:
        leftovers[str(path.relative_to(DST))] = len(cyr)
print("LEFTOVER CYRILLIC TOKEN COUNTS PER FILE (should be ~0):")
print(json.dumps(leftovers, indent=2, ensure_ascii=False))
