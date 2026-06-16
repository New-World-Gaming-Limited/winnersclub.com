#!/usr/bin/env python3
"""
_build_locales.py - WinnersClub 7-locale expansion
Generates 133 new HTML files for: es, pt-br, tr, id, fr, ru, hi
Uses KO pages as structural template.
Run from: /home/user/workspace/winnersclub.com/
"""

import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

SLUGS = [
    'index', 'about-stake', 'aviator', 'casino', 'live-casino',
    'live-odds', 'mirror', 'news', 'originals', 'payments',
    'poker', 'promo-code', 'reserves', 'responsible-gambling',
    'slots', 'sports', 'stake-engine', 'stake-us-bonus', 'vip'
]

NEW_LOCALES = ['es', 'pt-br', 'tr', 'id', 'fr', 'ru', 'hi']
OLD_LOCALES = ['en', 'ko', 'zh', 'vi', 'th', 'ms', 'pt', 'ja']
ALL_LOCALES = OLD_LOCALES + NEW_LOCALES

AFFILIATE_COM = 'https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000'
AFFILIATE_US  = 'https://stake.us/?c=MAX3000'

# BCP-47 lang codes
LANG_CODES = {
    'es': 'es', 'pt-br': 'pt-BR', 'tr': 'tr', 'id': 'id',
    'fr': 'fr', 'ru': 'ru', 'hi': 'hi'
}

# Language switcher label (native)
SWITCHER_LABELS = {
    'es': 'Idioma', 'pt-br': 'Idioma', 'tr': 'Dil',
    'id': 'Bahasa', 'fr': 'Langue', 'ru': 'Язык', 'hi': 'भाषा'
}

# Font spec for each locale (Google Fonts additions)
LOCALE_FONTS = {
    'es':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'pt-br': 'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'tr':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'id':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'fr':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'ru':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900',
    'hi':    'Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900&family=Noto+Sans+Devanagari:wght@500;700;900',
}

# Nav labels per locale
NAV = {
    'es': {
        'casino': 'Casino', 'sports': 'Deportes', 'poker': 'Poker',
        'aviator': 'Aviator', 'promo-code': 'Codigo Promo',
        'reserves': 'Reservas', 'about-stake': 'Sobre Stake',
        'home_label': 'WinnersClub Inicio', 'signup_btn': 'Entrar'
    },
    'pt-br': {
        'casino': 'Cassino', 'sports': 'Esportes', 'poker': 'Poker',
        'aviator': 'Aviator', 'promo-code': 'Codigo Promo',
        'reserves': 'Reservas', 'about-stake': 'Sobre o Stake',
        'home_label': 'WinnersClub Inicio', 'signup_btn': 'Entrar'
    },
    'tr': {
        'casino': 'Casino', 'sports': 'Spor', 'poker': 'Poker',
        'aviator': 'Aviator', 'promo-code': 'Promosyon Kodu',
        'reserves': 'Rezervler', 'about-stake': 'Stake Hakkinda',
        'home_label': 'WinnersClub Ana Sayfa', 'signup_btn': 'Giris Yap'
    },
    'id': {
        'casino': 'Kasino', 'sports': 'Olahraga', 'poker': 'Poker',
        'aviator': 'Aviator', 'promo-code': 'Kode Promo',
        'reserves': 'Cadangan', 'about-stake': 'Tentang Stake',
        'home_label': 'WinnersClub Beranda', 'signup_btn': 'Daftar'
    },
    'fr': {
        'casino': 'Casino', 'sports': 'Sports', 'poker': 'Poker',
        'aviator': 'Aviator', 'promo-code': 'Code Promo',
        'reserves': 'Reserves', 'about-stake': 'A propos de Stake',
        'home_label': 'WinnersClub Accueil', 'signup_btn': "S'inscrire"
    },
    'ru': {
        'casino': 'Казино', 'sports': 'Спорт', 'poker': 'Покер',
        'aviator': 'Авиатор', 'promo-code': 'Промокод',
        'reserves': 'Резервы', 'about-stake': 'О Stake',
        'home_label': 'WinnersClub Главная', 'signup_btn': 'Войти'
    },
    'hi': {
        'casino': 'कैसीनो', 'sports': 'स्पोर्ट्स', 'poker': 'पोकर',
        'aviator': 'एविएटर', 'promo-code': 'प्रोमो कोड',
        'reserves': 'रिजर्व', 'about-stake': 'Stake के बारे में',
        'home_label': 'WinnersClub होम', 'signup_btn': 'साइन अप'
    },
}

# ─── PAGE CONTENT TRANSLATIONS ───────────────────────────────────────────────

PAGE_DATA = {}

# ────────────────────────── INDEX (HOME) ─────────────────────────────────────
PAGE_DATA['index'] = {
    'es': {
        'title': 'Codigo Stake MAX3000 - 200% hasta $3,000 al Registrarte',
        'desc': 'Club exclusivo para jugadores de Stake.com. Con el codigo MAX3000 obtienes hasta $3,000 al 200%, rollover de 40x sobre deposito+bono. GGR $4.7B, licencia Curacao OGL/2024/1451/0918, fundado en 2017.',
        'og_title': 'WinnersClub | Codigo Stake MAX3000 | 200% hasta $3,000, 40x rollover',
        'og_desc': 'Club exclusivo de Stake.com. Codigo MAX3000: 200% hasta $3,000, rollover 40x deposito+bono. GGR $4.7B.',
        'h1': 'Codigo Stake MAX3000<span class="h1-sub">Al interior del club.</span>',
        'tease': 'Si llegaste a esta pagina, el portero ya te tiene en mente.',
        'hero_sub': 'La sala trasera de los jugadores de Stake. Susurra <span class="code-highlight">MAX3000</span> en la puerta y te esperan <strong>200% hasta $3,000</strong> con <strong>rollover de 40x sobre deposito+bono</strong>. Los codigos publicos no llegan ni a la mitad.',
        'hero_cta1': 'Obtener 200% hasta $3,000 en Stake.com',
        'hero_cta2': 'Lo que abre MAX3000',
        'reserves_ticker': 'Stake on-chain ahora: reservas etiquetadas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licencia Curacao OGL/2024/1451/0918 &middot; Fuente: Arkham Intel via cryptotips.com &middot; Snapshot 28 mayo 2026',
        'promo_strip_label': 'Codigo Promocional',
        'promo_strip_bonus': '200% hasta $3,000 &middot; Rollover 40x',
        'promo_strip_cta': 'Ver pagina del codigo &rarr;',
        'sec1_h2': 'Por que <span class="text-gradient-gold">este club</span>',
        'sec1_card1_h3': 'Un bono de peso',
        'sec1_card1_p': '200% hasta $3,000 con rollover de 40x sobre deposito+bono. Los demas codigos publicos de Stake se quedan en 100% y $1,000. Si no le das <span class="code-highlight">MAX3000</span> al dealer dentro de las 24 horas del registro, vuelves al menu economico.',
        'sec1_card2_h3': 'El dinero esta en la pared',
        'sec1_card2_p': 'Reservas etiquetadas por Arkham: $339.53M al 28 de mayo de 2026. Sin PDF de "confien en nosotros". La billetera es publica y cualquiera con WiFi puede auditarla. <a href="/es/reserves/" style="color:var(--gold);">Los recibos, aqui.</a>',
        'sec1_card3_h3': 'La casa tiene rostro',
        'sec1_card3_p': 'Ed Craven (Melbourne, 1995) y Bijan Tehrani. Se conocieron en RuneScape, fundaron Stake en 2017 y lanzaron Kick en 2022. Patrimonio combinado estimado por Forbes: US$5.6B. No es una empresa fantasma. Son dos personas que no pierden.',
        'sec2_h2': 'Cinco salas, <span class="text-gradient-gold">un codigo</span>',
        'sec2_sub': 'Elige la puerta. MAX3000 funciona en las cinco. Al dealer no le importa donde uses el bono.',
        'vert_casino': 'Casino',
        'vert_sports': 'Deportes',
        'vert_poker': 'Poker',
        'vert_aviator': 'Aviator',
        'vert_live': 'En Vivo',
        'girl_break_h2': 'Tres mil. <span class="text-gradient-gold">Rollover 40x.</span> Un codigo.',
        'girl_break_sub': 'Susurra <span class="code-highlight">MAX3000</span> al registrarte. Antes de que llegue la primera copa, las matematicas ya son tuyas.',
        'girl_break_cta': 'Darle el codigo al dealer',
        'sec3_h2': 'Lo que <span class="text-gradient-gold">sabe el club</span>',
        'intel_founder_label': 'Fundadores',
        'intel_founder_detail': 'Ed Craven (1995, Melbourne) y Bijan Tehrani. Se conocieron en RuneScape. Co-fundaron Stake en 2017. Lanzaron Kick en 2022.',
        'intel_operator_label': 'Operador',
        'intel_operator_detail': 'Entidad de Curazao que opera Stake.com. Matriz: Easygo Group Holdings, ingresos FY2025 A$970M. Stake.us es una entidad de sweepstakes separada.',
        'intel_license_label': 'Licencia',
        'intel_license_detail': 'Cubre la mayoria de paises. UK salio en marzo 2025. EEUU bloqueado (Stake.us sweepstakes disponible en mas de 30 estados). Mas de 22 sitios espejo confirmados.',
        'intel_reserves_label': 'Reservas',
        'intel_reserves_detail': 'Etiquetadas por Arkham al 28 mayo 2026. Ethereum 74%, Solana 14%, balance stablecoin de nueve cifras. Rastreable en cryptotips.com.',
        'two_doors_h2': 'Dos puertas, <span class="text-gradient-gold">un codigo</span>',
        'two_doors_sub': 'MAX3000 es reconocido tanto en Stake.com como en Stake.us. El recibimiento detras de cada puerta es diferente. El dealer te guiara a la puerta correcta segun tu ubicacion.',
        'stakecom_h3': 'Stake.com - Dinero Real, Global',
        'stakecom_p': 'Plataforma de dinero real operada por Medium Rare NV bajo Curacao OGL/2024/1451/0918. Cripto y fiat. Deportes, casino, originales, poker. Con el codigo <span class="code-highlight">MAX3000</span> obtienes <strong>200% hasta $3,000</strong>, rollover 40x sobre deposito+bono, 30 dias, deposito minimo $10. Reclamalo via soporte en vivo tras el deposito. Requiere KYC nivel 3. Disponible en la mayoria de paises excepto EEUU y UK.',
        'stakecom_btn': 'Abrir la puerta global',
        'stakeus_h3': 'Stake.us - Sweepstakes, EEUU',
        'stakeus_p': 'Plataforma sweepstakes estadounidense operada por Sweepsteaks Limited. Gold Coins para jugar, Stake Cash canjeable tras 3x de juego. Sin depositos/retiros reales, sin deportes, solo casino. El codigo <span class="code-highlight">MAX3000</span> tambien es reconocido y entrega <strong>560K GC + 56 SC + 3.5% rakeback</strong>. Disponible en 37 estados.',
        'stakeus_btn': 'Abrir la puerta americana',
        'faq_h2': 'Preguntas <span class="text-gradient-gold">en la puerta</span>',
        'faq1_q': 'Es MAX3000 el codigo de bono mas grande de Stake?',
        'faq1_a': 'Si. 200% hasta $3,000 con rollover 40x sobre deposito+bono. La mayoria de codigos publicos se quedan en 100% / $1,000. MAX3000 es el codigo que el club entrega en la puerta.',
        'faq2_q': 'Es confiable Stake.com?',
        'faq2_a': 'Stake opera desde 2017 bajo licencia Curacao OGL/2024/1451/0918 via Medium Rare NV. Las reservas on-chain al 28 mayo 2026 son $339.53M, rastreables publicamente en Arkham. Los fundadores Ed Craven (1995, Melbourne) y Bijan Tehrani tambien operan Kick. La matriz Easygo Group Holdings reporto A$970M en ingresos y A$257M en utilidad neta en FY2025.',
        'faq3_q': 'Puedo verificar las reservas de Stake?',
        'faq3_a': 'Si, revisa el <a href="/es/reserves/">informe de reservas</a>. El snapshot del 28 mayo 2026 muestra $339.53M en billeteras etiquetadas por Arkham. Ethereum 74%, Solana 14%, balance stablecoin de nueve cifras. Todo rastreable en <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> con datos semanales de Arkham Intel.',
        'faq4_q': 'Donde puedo jugar?',
        'faq4_a': 'La licencia Curacao cubre la mayoria de paises, pero Stake tiene sus propias restricciones en EEUU, UK, parte de Australia y algunos otros. Usa la <a href="/es/mirror/">pagina de sitios espejo</a> para encontrar el dominio de tu region.',
        'faq5_q': 'Que tan rapidos son los retiros?',
        'faq5_a': 'Los retiros en criptomoneda por montos normales se completan en 30 a 60 minutos. TRX, XRP, SOL liquidan en segundos. Retiros grandes pueden requerir revision de cumplimiento de 2 a 4 dias habiles. Los retiros fiat via MoonPay toman 1 a 5 dias habiles. Mas detalles en la <a href="/es/payments/">pagina de pagos</a>.',
        'signature': 'Dile al dealer que te manda WinnersClub.',
        'sticky_text': 'Codigo: <span class="code-highlight">MAX3000</span>. 200% hasta $3,000. La puerta de Stake.com esta abierta',
        'sticky_cta': 'Tomar asiento &rarr;',
        'sticky_close': 'Cerrar',
        'footer_tagline': 'EL CLUB ESTA EN STAKE DESDE 2017.',
        'footer_floor': 'Sala',
        'footer_code': 'Codigo',
        'footer_intel': 'Intel',
        'footer_casino': 'Casino',
        'footer_sports': 'Deportes',
        'footer_poker': 'Poker',
        'footer_aviator': 'Aviator',
        'footer_liveodds': 'Cuotas en vivo',
        'footer_promo': 'Codigo Promo MAX3000',
        'footer_payments': 'Pagos',
        'footer_mirror': 'Acceso y sitios espejo',
        'footer_aboutstake': 'Sobre Stake',
        'footer_reserves': 'Reservas on-chain',
        'footer_disclaimer': 'WinnersClub es el club exclusivo de jugadores de Stake. Stake.com es operado por Medium Rare NV bajo licencia de Curacao OGL/2024/1451/0918. Stake.us es una plataforma de sweepstakes separada operada por Sweepsteaks Limited. Este sitio opera solo con fines informativos. Apostar conlleva riesgos. Juega responsablemente. Si tienes problemas con el juego, contacta GamCare o tu organizacion de apoyo local. Mayores de 18 anos.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Todos los derechos reservados.',
        'age_badge': '18+',
        'faq_json_q1': 'Es MAX3000 el codigo de bono mas grande de Stake?',
        'faq_json_a1': 'Si. 200% hasta $3,000 con rollover 40x sobre deposito+bono. La mayoria de codigos publicos se quedan en 100%/$1,000. MAX3000 es el codigo que el club entrega en la puerta.',
        'faq_json_q2': 'Es confiable Stake.com?',
        'faq_json_a2': 'Stake opera desde 2017 bajo licencia Curacao OGL/2024/1451/0918 via Medium Rare NV. Las reservas on-chain son $339.53M al 28 mayo 2026. Los fundadores Ed Craven (1995, Melbourne) y Bijan Tehrani tambien operan Kick.',
        'faq_json_q3': 'Puedo verificar las reservas de Stake?',
        'faq_json_a3': 'Si. El snapshot del 28 mayo 2026 muestra $339.53M en billeteras Arkham etiquetadas. Ethereum 74%, Solana 14%, balance stablecoin de nueve cifras. Rastreable en cryptotips.com.',
        'faq_json_q4': 'Donde puedo jugar?',
        'faq_json_a4': 'La licencia Curacao cubre la mayoria de paises. Stake tiene restricciones en EEUU, UK y algunos otros. Usa la pagina de sitios espejo para encontrar el dominio de tu region.',
        'faq_json_q5': 'Que tan rapidos son los retiros?',
        'faq_json_a5': 'Los cripto normales: 30 a 60 minutos. TRX, XRP, SOL: segundos. Grandes: 2 a 4 dias. MoonPay fiat: 1 a 5 dias.',
        'ld_name': 'WinnersClub - Interior del Club Stake | Codigo MAX3000, 200% hasta $3,000',
        'ld_desc': 'Club exclusivo de jugadores de Stake.com. Codigo MAX3000: 200% hasta $3,000, rollover 40x. GGR $4.7B, licencia Curacao OGL/2024/1451/0918.',
    },
    'pt-br': {
        'title': 'Codigo Stake MAX3000 - 200% ate $3,000 no Cadastro',
        'desc': 'Clube exclusivo para jogadores brasileiros de Stake.com. Com o codigo MAX3000 voce obtem ate $3,000 com 200%, rollover de 40x sobre deposito+bonus. GGR $4.7B, licenca Curacao OGL/2024/1451/0918, fundado em 2017.',
        'og_title': 'WinnersClub | Codigo Stake MAX3000 | 200% ate $3,000, 40x rollover',
        'og_desc': 'Clube exclusivo de Stake.com para jogadores brasileiros. Codigo MAX3000: 200% ate $3,000, rollover 40x deposito+bonus. GGR $4.7B.',
        'h1': 'Codigo Stake MAX3000<span class="h1-sub">Dentro do clube.</span>',
        'tease': 'Se voce encontrou esta pagina, o porteiro ja gostou de voce.',
        'hero_sub': 'A sala exclusiva dos jogadores de Stake. Sussurre <span class="code-highlight">MAX3000</span> na entrada e te esperam <strong>200% ate $3,000</strong> com <strong>rollover de 40x sobre deposito+bonus</strong>. Os codigos publicos nao chegam nem perto.',
        'hero_cta1': 'Obter 200% ate $3,000 no Stake.com',
        'hero_cta2': 'O que MAX3000 desbloqueia',
        'reserves_ticker': 'Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licenca Curacao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 maio 2026',
        'promo_strip_label': 'Codigo Promocional',
        'promo_strip_bonus': '200% ate $3.000 &middot; Rollover 40x',
        'promo_strip_cta': 'Ver pagina do codigo &rarr;',
        'sec1_h2': 'Por que <span class="text-gradient-gold">este clube</span>',
        'sec1_card1_h3': 'Um bonus de peso',
        'sec1_card1_p': '200% ate $3.000 com rollover de 40x sobre deposito+bonus. Os outros codigos publicos do Stake ficam em 100% e $1.000. Se nao der <span class="code-highlight">MAX3000</span> ao dealer nas 24 horas apos o cadastro, volta ao menu basico.',
        'sec1_card2_h3': 'O dinheiro esta na parede',
        'sec1_card2_p': 'Reservas rotuladas pela Arkham: $339.53M em 28 de maio de 2026. Sem PDF de "confie em nos". A carteira e publica e qualquer pessoa com WiFi pode audita-la. <a href="/pt-br/reserves/" style="color:var(--gold);">Os recibos, aqui.</a>',
        'sec1_card3_h3': 'A casa tem rosto',
        'sec1_card3_p': 'Ed Craven (Melbourne, 1995) e Bijan Tehrani. Se conheceram no RuneScape, fundaram o Stake em 2017 e lancaram o Kick em 2022. Patrimonio combinado estimado pela Forbes: US$5.6B. Nao e uma empresa de papel. Sao duas pessoas que nao perdem.',
        'sec2_h2': 'Cinco salas, <span class="text-gradient-gold">um codigo</span>',
        'sec2_sub': 'Escolha a porta. MAX3000 funciona nas cinco. O dealer nao se importa onde voce usa o bonus.',
        'vert_casino': 'Cassino',
        'vert_sports': 'Esportes',
        'vert_poker': 'Poker',
        'vert_aviator': 'Aviator',
        'vert_live': 'Ao Vivo',
        'girl_break_h2': 'Tres mil. <span class="text-gradient-gold">Rollover 40x.</span> Um codigo.',
        'girl_break_sub': 'Sussurre <span class="code-highlight">MAX3000</span> no cadastro. Antes de a primeira bebida chegar, a matematica ja e sua.',
        'girl_break_cta': 'Dar o codigo ao dealer',
        'sec3_h2': 'O que <span class="text-gradient-gold">o clube sabe</span>',
        'intel_founder_label': 'Fundadores',
        'intel_founder_detail': 'Ed Craven (1995, Melbourne) e Bijan Tehrani. Se conheceram no RuneScape. Co-fundaram o Stake em 2017. Lancaram o Kick em 2022.',
        'intel_operator_label': 'Operadora',
        'intel_operator_detail': 'Entidade de Curacao que opera o Stake.com. Matriz: Easygo Group Holdings, receita FY2025 A$970M. Stake.us e uma entidade de sweepstakes separada.',
        'intel_license_label': 'Licenca',
        'intel_license_detail': 'Cobre a maioria dos paises. UK saiu em marco 2025. EUA bloqueado (Stake.us sweepstakes disponivel em mais de 30 estados). Mais de 22 sitios espelho confirmados.',
        'intel_reserves_label': 'Reservas',
        'intel_reserves_detail': 'Rotuladas pela Arkham em 28 maio 2026. Ethereum 74%, Solana 14%, saldo stablecoin de nove digitos. Rastreavel em cryptotips.com.',
        'two_doors_h2': 'Duas portas, <span class="text-gradient-gold">um codigo</span>',
        'two_doors_sub': 'MAX3000 e reconhecido tanto no Stake.com quanto no Stake.us. A recepcao atras de cada porta e diferente. O dealer vai te guiar para a porta certa de acordo com sua localizacao.',
        'stakecom_h3': 'Stake.com - Dinheiro Real, Global',
        'stakecom_p': 'Plataforma de dinheiro real operada pela Medium Rare NV sob Curacao OGL/2024/1451/0918. Cripto e fiat. Esportes, cassino, originais, poker. Com o codigo <span class="code-highlight">MAX3000</span> voce obtem <strong>200% ate $3.000</strong>, rollover 40x sobre deposito+bonus, 30 dias, deposito minimo $10. Reivindique via suporte ao vivo apos o deposito. KYC nivel 3 obrigatorio. Disponivel na maioria dos paises exceto EUA e UK.',
        'stakecom_btn': 'Abrir a porta global',
        'stakeus_h3': 'Stake.us - Sweepstakes, EUA',
        'stakeus_p': 'Plataforma sweepstakes americana operada pela Sweepsteaks Limited. Gold Coins para jogar, Stake Cash resgatavel apos 3x de jogo. Sem depositos/saques reais, sem esportes, apenas cassino. O codigo <span class="code-highlight">MAX3000</span> tambem e reconhecido e entrega <strong>560K GC + 56 SC + 3.5% de rakeback</strong>. Disponivel em 37 estados.',
        'stakeus_btn': 'Abrir a porta americana',
        'faq_h2': 'Perguntas <span class="text-gradient-gold">na entrada</span>',
        'faq1_q': 'MAX3000 e o maior codigo de bonus do Stake?',
        'faq1_a': 'Sim. 200% ate $3.000 com rollover 40x sobre deposito+bonus. A maioria dos codigos publicos fica em 100% / $1.000. MAX3000 e o codigo que o clube entrega na porta.',
        'faq2_q': 'O Stake.com e confiavel?',
        'faq2_a': 'O Stake opera desde 2017 sob licenca Curacao OGL/2024/1451/0918 via Medium Rare NV. As reservas on-chain em 28 maio 2026 sao $339.53M, rastreavais publicamente na Arkham. Os fundadores Ed Craven (1995, Melbourne) e Bijan Tehrani tambem operam o Kick. A matriz Easygo Group Holdings reportou A$970M em receita e A$257M em lucro liquido no FY2025.',
        'faq3_q': 'Posso verificar as reservas do Stake?',
        'faq3_a': 'Sim, confira o <a href="/pt-br/reserves/">relatorio de reservas</a>. O snapshot de 28 maio 2026 mostra $339.53M em carteiras rotuladas pela Arkham. Ethereum 74%, Solana 14%, saldo stablecoin de nove digitos. Tudo rastreavel em <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> com dados semanais da Arkham Intel.',
        'faq4_q': 'Onde posso jogar?',
        'faq4_a': 'A licenca Curacao cobre a maioria dos paises, mas o Stake tem suas proprias restricoes nos EUA, UK, parte da Australia e alguns outros. Use a <a href="/pt-br/mirror/">pagina de sitios espelho</a> para encontrar o dominio da sua regiao.',
        'faq5_q': 'Qual a velocidade dos saques?',
        'faq5_a': 'Saques em criptomoeda para valores normais sao concluidos em 30 a 60 minutos. TRX, XRP, SOL liquidam em segundos. Valores grandes podem exigir revisao de compliance de 2 a 4 dias uteis. Saques em fiat via MoonPay levam 1 a 5 dias uteis. Mais detalhes na <a href="/pt-br/payments/">pagina de pagamentos</a>.',
        'signature': 'Diga ao dealer que o WinnersClub mandou voce.',
        'sticky_text': 'Codigo: <span class="code-highlight">MAX3000</span>. 200% ate $3.000. A porta do Stake.com esta aberta',
        'sticky_cta': 'Garantir lugar &rarr;',
        'sticky_close': 'Fechar',
        'footer_tagline': 'O CLUBE ESTA NO STAKE DESDE 2017.',
        'footer_floor': 'Sala',
        'footer_code': 'Codigo',
        'footer_intel': 'Intel',
        'footer_casino': 'Cassino',
        'footer_sports': 'Esportes',
        'footer_poker': 'Poker',
        'footer_aviator': 'Aviator',
        'footer_liveodds': 'Odds ao vivo',
        'footer_promo': 'Codigo Promo MAX3000',
        'footer_payments': 'Pagamentos',
        'footer_mirror': 'Acesso e sitios espelho',
        'footer_aboutstake': 'Sobre o Stake',
        'footer_reserves': 'Reservas on-chain',
        'footer_disclaimer': 'WinnersClub e o clube exclusivo de jogadores do Stake. Stake.com e operado pela Medium Rare NV sob licenca Curacao OGL/2024/1451/0918. Stake.us e uma plataforma de sweepstakes separada operada pela Sweepsteaks Limited. Este site opera apenas para fins informativos. Apostar envolve riscos. Jogue com responsabilidade. Se tiver problemas com jogo, contate o GamCare ou sua organizacao de apoio local. Maiores de 18 anos.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Todos os direitos reservados.',
        'age_badge': '18+',
        'faq_json_q1': 'MAX3000 e o maior codigo de bonus do Stake?',
        'faq_json_a1': 'Sim. 200% ate $3.000 com rollover 40x. A maioria dos codigos publicos fica em 100%/$1.000. MAX3000 e o codigo que o clube entrega na porta.',
        'faq_json_q2': 'O Stake.com e confiavel?',
        'faq_json_a2': 'O Stake opera desde 2017 sob licenca Curacao OGL/2024/1451/0918. Reservas $339.53M em 28 maio 2026. Fundadores Ed Craven e Bijan Tehrani.',
        'faq_json_q3': 'Posso verificar as reservas do Stake?',
        'faq_json_a3': 'Sim. Snapshot 28 maio 2026: $339.53M em carteiras Arkham. Ethereum 74%, Solana 14%. Rastreavel em cryptotips.com.',
        'faq_json_q4': 'Onde posso jogar?',
        'faq_json_a4': 'Licenca Curacao cobre a maioria dos paises. Stake tem restricoes nos EUA, UK e alguns outros. Use a pagina de sitios espelho.',
        'faq_json_q5': 'Qual a velocidade dos saques?',
        'faq_json_a5': 'Cripto normais: 30 a 60 minutos. TRX, XRP, SOL: segundos. Grandes: 2 a 4 dias. MoonPay fiat: 1 a 5 dias.',
        'ld_name': 'WinnersClub - Interior do Clube Stake | Codigo MAX3000, 200% ate $3,000',
        'ld_desc': 'Clube exclusivo de jogadores do Stake.com. Codigo MAX3000: 200% ate $3.000, rollover 40x. GGR $4.7B, licenca Curacao OGL/2024/1451/0918.',
    },
    'tr': {
        'title': 'Stake Promosyon Kodu MAX3000 - Kayit Olurken 200% $3.000\'e Kadar',
        'desc': 'Stake.com oyuncularinin ozel kulubu. MAX3000 kodu ile 200% $3.000\'e kadar bonus, 40x cevrim sarti (depozit+bonus). GGR $4.7B, Curacao OGL/2024/1451/0918 lisansi, 2017\'de kuruldu.',
        'og_title': 'WinnersClub | Stake Kodu MAX3000 | 200% $3.000\'e Kadar, 40x Cevrim',
        'og_desc': 'Stake.com oyuncu kulubu. Kod MAX3000: 200% $3.000\'e kadar, 40x cevrim depozit+bonus. GGR $4.7B.',
        'h1': 'Stake Promosyon Kodu MAX3000<span class="h1-sub">Kulubin icine.</span>',
        'tease': 'Bu sayfaya ulastiysa, kapi gorevlisi sizi zaten hosgeldiniz dedi.',
        'hero_sub': 'Stake oyuncularinin ozel arka odasi. <span class="code-highlight">MAX3000</span> kodunu kapida fisildayin ve <strong>200% $3.000\'e kadar bonus</strong> ile <strong>depozit+bonus uzerinden 40x cevrim sarti</strong> sizi bekliyor. Diger acik kodlar yarisina bile ulasemiyor.',
        'hero_cta1': 'Stake.com\'da 200% $3.000\'e Kadar Alin',
        'hero_cta2': 'MAX3000\'in Actiklarini Gor',
        'reserves_ticker': 'Stake on-chain simdi: etiklenenmis rezervler $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 lisansi &middot; Kaynak: cryptotips.com uzerinden Arkham Intel &middot; 28 Mayis 2026 anlık goruntu',
        'promo_strip_label': 'Promosyon Kodu',
        'promo_strip_bonus': '$3.000\'e kadar 200% &middot; 40x cevrim',
        'promo_strip_cta': 'Kod sayfasini ac &rarr;',
        'sec1_h2': 'Neden <span class="text-gradient-gold">bu kulup</span>',
        'sec1_card1_h3': 'Agir bir bonus',
        'sec1_card1_p': 'Depozit+bonus uzerinden 40x cevrim sarti ile $3.000\'e kadar 200%. Diger Stake kodlari 100% ve $1.000\'de kaliyor. Kayit olduktan 24 saat icinde dealer\'a <span class="code-highlight">MAX3000</span> vermezseniz ucuz menüye donuyorsunuz.',
        'sec1_card2_h3': 'Para duvarda asili',
        'sec1_card2_p': '28 Mayis 2026 itibariyla Arkham etiketli rezervler: $339.53M. "Bize guvenin" PDF\'si yok, rezerv tiyatrosu yok. Cuzdan herkese acik, WiFi olan herkes denetleyebilir. <a href="/tr/reserves/" style="color:var(--gold);">Fisilar burada.</a>',
        'sec1_card3_h3': 'Evin bir yuzu var',
        'sec1_card3_p': 'Ed Craven (Melbourne, 1995) ve Bijan Tehrani. RuneScape\'te tanistular, 2017\'de Stake\'i kurdular ve 2022\'de Kick\'i baslattılar. Forbes tahminli toplam net deger: US$5.6B. Kagit sirket degil. Kaybetmeyen iki insan.',
        'sec2_h2': 'Bes oda, <span class="text-gradient-gold">bir kod</span>',
        'sec2_sub': 'Kapi secin. MAX3000 besinde de gecerli. Dealer bonusu nerede kullandiginizi umursamiyor.',
        'vert_casino': 'Casino',
        'vert_sports': 'Spor',
        'vert_poker': 'Poker',
        'vert_aviator': 'Aviator',
        'vert_live': 'Canli',
        'girl_break_h2': 'Uc bin. <span class="text-gradient-gold">40x cevrim.</span> Bir kod.',
        'girl_break_sub': '<span class="code-highlight">MAX3000</span>\'i kayit sirasinda fisildayin. Ilk icecek gelmeden matematik sizin olsun.',
        'girl_break_cta': 'Kodu dealer\'a ver',
        'sec3_h2': 'Kulubun <span class="text-gradient-gold">bildikleri</span>',
        'intel_founder_label': 'Kurucular',
        'intel_founder_detail': 'Ed Craven (1995, Melbourne) ve Bijan Tehrani. RuneScape\'te tanistular. 2017\'de Stake\'i birlikte kurdular. 2022\'de Kick\'i baslattılar.',
        'intel_operator_label': 'Isletici',
        'intel_operator_detail': 'Stake.com\'u isletmek icin Curacao\'da kurulmus sirket. Ana sirket: Easygo Group Holdings, FY2025 geliri A$970M. Stake.us ayri bir sweepstakes kurulusudur.',
        'intel_license_label': 'Lisans',
        'intel_license_detail': 'Cogu ulkeyi kapsiyor. UK Mart 2025\'te cikti. ABD engellendi (Stake.us sweepstakes 30\'dan fazla eyalette mevcut). 22\'den fazla ayna site onaylandi.',
        'intel_reserves_label': 'Rezervler',
        'intel_reserves_detail': '28 Mayis 2026 tarihinde Arkham etiketlendi. Ethereum 74%, Solana 14%, dokuz haneli stablecoin bakiyesi. cryptotips.com\'da takip edilebilir.',
        'two_doors_h2': 'Iki kapi, <span class="text-gradient-gold">bir kod</span>',
        'two_doors_sub': 'MAX3000 hem Stake.com\'da hem de Stake.us\'ta gecerlidir. Her kapinin arkasindaki karsılama farklıdır. Dealer konumunuza gore dogru kapiya yonlendirecektir.',
        'stakecom_h3': 'Stake.com - Gercek Para, Global',
        'stakecom_p': 'Medium Rare NV tarafindan Curacao OGL/2024/1451/0918 kapsaminda isletilen gercek para platformu. Kripto ve fiat. Spor, casino, originaller, poker. <span class="code-highlight">MAX3000</span> koduyla <strong>$3.000\'e kadar 200%</strong>, depozit+bonus uzerinden 40x cevrim sarti, 30 gun, minimum depozit $10. Depozit sonrasi canli destek uzerinden talep edin. KYC Seviye 3 gerekli. ABD ve UK disinda cogu ulkede kullanilabilir.',
        'stakecom_btn': 'Global kapiyi ac',
        'stakeus_h3': 'Stake.us - Sweepstakes, ABD',
        'stakeus_p': 'Sweepsteaks Limited tarafindan isletilen ABD sweepstakes platformu. Oynamak icin Gold Coins, 3x oyun sonrasi bozdurabileceginiz Stake Cash. Gercek depozit/cekim yok, spor yok, sadece casino. <span class="code-highlight">MAX3000</span> kodu da kabul gorur ve <strong>560K GC + 56 SC + %3.5 rakeback</strong> sunar. 37 eyalette kullanilabilir.',
        'stakeus_btn': 'Amerikan kapiyi ac',
        'faq_h2': 'Kapidaki <span class="text-gradient-gold">sorular</span>',
        'faq1_q': 'MAX3000 en buyuk Stake bonus kodu mu?',
        'faq1_a': 'Evet. Depozit+bonus uzerinden 40x cevrim ile $3.000\'e kadar 200%. Cogu acik kod 100% / $1.000\'de kaliyor. MAX3000 kulubun kapida verdigi koddur.',
        'faq2_q': 'Stake.com guvenilir mi?',
        'faq2_a': 'Stake, Medium Rare NV araciligiyla Curacao OGL/2024/1451/0918 lisansiyla 2017\'den beri faaliyet gosteriyor. 28 Mayis 2026\'da on-chain rezervler $339.53M olup Arkham\'da kamuya acik takip edilebilir. Kurucular Ed Craven (1995, Melbourne) ve Bijan Tehrani ayni zamanda Kick\'i de isletiyor. Ana sirket Easygo Group Holdings FY2025\'te A$970M gelir ve A$257M net kar bildirdi.',
        'faq3_q': 'Stake\'in rezervlerini dogruleyebilir miyim?',
        'faq3_a': '<a href="/tr/reserves/">Rezerv raporunu</a> inceleyin. 28 Mayis 2026 anlık goruntusu Arkham etiketli cuzdanlarda $339.53M gosteriyor. Ethereum 74%, Solana 14%, dokuz haneli stablecoin bakiyesi. Hepsi haftalik Arkham Intel verileriyle <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a>\'da takip edilebilir.',
        'faq4_q': 'Nerede oynayabilirim?',
        'faq4_a': 'Curacao lisansi cogu ulkeyi kapsiyor ancak Stake\'in ABD, UK, Avustralya\'nin bazi bolgeleri ve bazi diger ulkelerde kendi kisitlamalari var. Bolge domaininizi bulmak icin <a href="/tr/mirror/">ayna siteler sayfasini</a> kullanin.',
        'faq5_q': 'Para cekim islemi ne kadar surer?',
        'faq5_a': 'Normal miktar kripto cekimler 30 ila 60 dakika icinde tamamlaniyor. TRX, XRP, SOL saniyeler icinde isleniyor. Buyuk miktarlar 2 ila 4 is gunu uyum incelemesi gerektirebilir. MoonPay fiat cekim 1 ila 5 is gunu suruyor. Daha fazla bilgi icin <a href="/tr/payments/">odeme sayfasina</a> bakin.',
        'signature': 'Dealer\'a WinnersClub tarafindan gonderildiginizi soyleyin.',
        'sticky_text': 'Kod: <span class="code-highlight">MAX3000</span>. $3.000\'e kadar 200%. Stake.com\'un kapisi acik',
        'sticky_cta': 'Yer kapat &rarr;',
        'sticky_close': 'Kapat',
        'footer_tagline': 'KULUP 2017\'DEN BU YANA STAKE\'TE.',
        'footer_floor': 'Salon',
        'footer_code': 'Kod',
        'footer_intel': 'Intel',
        'footer_casino': 'Casino',
        'footer_sports': 'Spor',
        'footer_poker': 'Poker',
        'footer_aviator': 'Aviator',
        'footer_liveodds': 'Canli oranlar',
        'footer_promo': 'Promosyon Kodu MAX3000',
        'footer_payments': 'Odemeler',
        'footer_mirror': 'Erisim ve ayna siteler',
        'footer_aboutstake': 'Stake hakkinda',
        'footer_reserves': 'On-chain rezervler',
        'footer_disclaimer': 'WinnersClub, Stake\'in ozel oyuncu kulubudur. Stake.com, Medium Rare NV tarafindan Curacao lisansi OGL/2024/1451/0918 kapsaminda isletilmektedir. Stake.us, Sweepsteaks Limited tarafindan isletilen ayri bir sweepstakes platformudur. Bu site yalnizca bilgilendirme amaclidir. Kumar risk icerir. Sorumlu oynayiniz. Kumar sorununuz varsa GamCare\'e veya yerel destek kurulusuna basvurun. 18 yas ve uzeri.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Tum haklari saklidir.',
        'age_badge': '18+',
        'faq_json_q1': 'MAX3000 en buyuk Stake bonus kodu mu?',
        'faq_json_a1': 'Evet. $3.000\'e kadar 200% ve 40x cevrim. Cogu acik kod 100%/$1.000\'de kaliyor.',
        'faq_json_q2': 'Stake.com guvenilir mi?',
        'faq_json_a2': 'Stake, 2017\'den beri Curacao OGL/2024/1451/0918 lisansiyla faaliyet gosteriyor. Rezervler $339.53M. Kurucular Ed Craven ve Bijan Tehrani.',
        'faq_json_q3': 'Stake\'in rezervlerini dogruleyebilir miyim?',
        'faq_json_a3': '28 Mayis 2026 goruntusu Arkham etiketli cuzdanlarda $339.53M gosteriyor. cryptotips.com\'da takip edilebilir.',
        'faq_json_q4': 'Nerede oynayabilirim?',
        'faq_json_a4': 'Curacao lisansi cogu ulkeyi kapsiyor. Bolge domaininizi bulmak icin ayna siteler sayfasini kullanin.',
        'faq_json_q5': 'Para cekim islemi ne kadar surer?',
        'faq_json_a5': 'Kripto: 30-60 dakika. TRX, XRP, SOL: saniyeler. Buyuk miktarlar: 2-4 is gunu. MoonPay fiat: 1-5 is gunu.',
        'ld_name': 'WinnersClub - Stake Kulubu | Kod MAX3000, $3.000\'e Kadar 200%',
        'ld_desc': 'Stake.com oyuncularinin ozel kulubu. MAX3000 kodu: $3.000\'e kadar 200%, 40x cevrim. GGR $4.7B, Curacao OGL/2024/1451/0918.',
    },
    'id': {
        'title': 'Kode Promo Stake MAX3000 - 200% Hingga $3.000 Saat Daftar',
        'desc': 'Klub eksklusif untuk pemain Stake.com. Dengan kode MAX3000 Anda mendapatkan hingga $3.000 dengan 200%, rollover 40x atas deposit+bonus. GGR $4.7B, lisensi Curacao OGL/2024/1451/0918, didirikan 2017.',
        'og_title': 'WinnersClub | Kode Stake MAX3000 | 200% Hingga $3.000, 40x Rollover',
        'og_desc': 'Klub eksklusif Stake.com. Kode MAX3000: 200% hingga $3.000, rollover 40x deposit+bonus. GGR $4.7B.',
        'h1': 'Kode Promo Stake MAX3000<span class="h1-sub">Masuk ke dalam klub.</span>',
        'tease': 'Jika Anda menemukan halaman ini, penjaga pintu sudah menyambut Anda.',
        'hero_sub': 'Ruang eksklusif pemain Stake. Bisikkan <span class="code-highlight">MAX3000</span> di pintu masuk dan Anda akan mendapatkan <strong>200% hingga $3.000</strong> dengan <strong>rollover 40x atas deposit+bonus</strong>. Kode publik lainnya tidak ada yang mendekati ini.',
        'hero_cta1': 'Dapatkan 200% Hingga $3.000 di Stake.com',
        'hero_cta2': 'Apa yang Dibuka MAX3000',
        'reserves_ticker': 'Stake on-chain sekarang: cadangan berlabel $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Lisensi Curacao OGL/2024/1451/0918 &middot; Sumber: Arkham Intel via cryptotips.com &middot; Snapshot 28 Mei 2026',
        'promo_strip_label': 'Kode Promo',
        'promo_strip_bonus': '200% hingga $3.000 &middot; Rollover 40x',
        'promo_strip_cta': 'Lihat halaman kode &rarr;',
        'sec1_h2': 'Mengapa <span class="text-gradient-gold">klub ini</span>',
        'sec1_card1_h3': 'Bonus berbobot',
        'sec1_card1_p': '200% hingga $3.000 dengan rollover 40x atas deposit+bonus. Kode Stake publik lainnya mentok di 100% dan $1.000. Jika tidak memberikan <span class="code-highlight">MAX3000</span> kepada dealer dalam 24 jam setelah daftar, Anda kembali ke menu biasa.',
        'sec1_card2_h3': 'Uangnya terpampang di dinding',
        'sec1_card2_p': 'Cadangan berlabel Arkham: $339.53M per 28 Mei 2026. Tidak ada PDF "percayai kami". Dompetnya publik dan siapa pun dengan WiFi bisa mengauditnya. <a href="/id/reserves/" style="color:var(--gold);">Buktinya di sini.</a>',
        'sec1_card3_h3': 'Rumah memiliki wajah',
        'sec1_card3_p': 'Ed Craven (Melbourne, 1995) dan Bijan Tehrani. Bertemu di RuneScape, mendirikan Stake pada 2017 dan meluncurkan Kick pada 2022. Kekayaan bersih gabungan versi Forbes: US$5.6B. Bukan perusahaan cangkang. Dua orang yang tidak pernah kalah.',
        'sec2_h2': 'Lima ruangan, <span class="text-gradient-gold">satu kode</span>',
        'sec2_sub': 'Pilih pintunya. MAX3000 berlaku di semua lima. Dealer tidak peduli di mana Anda menggunakan bonus.',
        'vert_casino': 'Kasino',
        'vert_sports': 'Olahraga',
        'vert_poker': 'Poker',
        'vert_aviator': 'Aviator',
        'vert_live': 'Live',
        'girl_break_h2': 'Tiga ribu. <span class="text-gradient-gold">Rollover 40x.</span> Satu kode.',
        'girl_break_sub': 'Bisikkan <span class="code-highlight">MAX3000</span> saat mendaftar. Sebelum minuman pertama tiba, matematikanya sudah milik Anda.',
        'girl_break_cta': 'Berikan kode ke dealer',
        'sec3_h2': 'Yang <span class="text-gradient-gold">diketahui klub</span>',
        'intel_founder_label': 'Pendiri',
        'intel_founder_detail': 'Ed Craven (1995, Melbourne) dan Bijan Tehrani. Bertemu di RuneScape. Mendirikan Stake bersama pada 2017. Meluncurkan Kick pada 2022.',
        'intel_operator_label': 'Operator',
        'intel_operator_detail': 'Entitas Curacao yang mengoperasikan Stake.com. Induk: Easygo Group Holdings, pendapatan FY2025 A$970M. Stake.us adalah entitas sweepstakes terpisah.',
        'intel_license_label': 'Lisensi',
        'intel_license_detail': 'Mencakup sebagian besar negara. UK keluar Maret 2025. AS diblokir (Stake.us sweepstakes tersedia di 30+ negara bagian). Lebih dari 22 situs mirror dikonfirmasi.',
        'intel_reserves_label': 'Cadangan',
        'intel_reserves_detail': 'Dilabeli Arkham per 28 Mei 2026. Ethereum 74%, Solana 14%, saldo stablecoin sembilan digit. Dapat dilacak di cryptotips.com.',
        'two_doors_h2': 'Dua pintu, <span class="text-gradient-gold">satu kode</span>',
        'two_doors_sub': 'MAX3000 dikenali di Stake.com dan Stake.us. Sambutan di balik setiap pintu berbeda. Dealer akan memandu Anda ke pintu yang tepat sesuai lokasi Anda.',
        'stakecom_h3': 'Stake.com - Uang Nyata, Global',
        'stakecom_p': 'Platform uang nyata yang dioperasikan Medium Rare NV di bawah Curacao OGL/2024/1451/0918. Kripto dan fiat. Olahraga, kasino, original, poker. Dengan kode <span class="code-highlight">MAX3000</span> Anda mendapatkan <strong>200% hingga $3.000</strong>, rollover 40x atas deposit+bonus, 30 hari, deposit minimum $10. Klaim via live support setelah deposit. KYC Level 3 wajib. Tersedia di sebagian besar negara kecuali AS dan UK.',
        'stakecom_btn': 'Buka pintu global',
        'stakeus_h3': 'Stake.us - Sweepstakes, AS',
        'stakeus_p': 'Platform sweepstakes Amerika yang dioperasikan Sweepsteaks Limited. Gold Coins untuk bermain, Stake Cash yang bisa ditukarkan setelah 3x bermain. Tanpa deposit/penarikan nyata, tanpa olahraga, hanya kasino. Kode <span class="code-highlight">MAX3000</span> juga dikenali dan memberikan <strong>560K GC + 56 SC + 3.5% rakeback</strong>. Tersedia di 37 negara bagian.',
        'stakeus_btn': 'Buka pintu Amerika',
        'faq_h2': 'Pertanyaan <span class="text-gradient-gold">di pintu masuk</span>',
        'faq1_q': 'Apakah MAX3000 kode bonus Stake terbesar?',
        'faq1_a': 'Ya. 200% hingga $3.000 dengan rollover 40x atas deposit+bonus. Sebagian besar kode publik berhenti di 100% / $1.000. MAX3000 adalah kode yang klub berikan di pintu.',
        'faq2_q': 'Apakah Stake.com terpercaya?',
        'faq2_a': 'Stake beroperasi sejak 2017 di bawah lisensi Curacao OGL/2024/1451/0918 via Medium Rare NV. Cadangan on-chain per 28 Mei 2026 adalah $339.53M, dapat dilacak publik di Arkham. Pendiri Ed Craven (1995, Melbourne) dan Bijan Tehrani juga mengoperasikan Kick. Induk Easygo Group Holdings melaporkan A$970M pendapatan dan A$257M laba bersih di FY2025.',
        'faq3_q': 'Bisakah saya verifikasi cadangan Stake?',
        'faq3_a': 'Ya, lihat <a href="/id/reserves/">laporan cadangan</a>. Snapshot 28 Mei 2026 menunjukkan $339.53M di dompet berlabel Arkham. Ethereum 74%, Solana 14%, saldo stablecoin sembilan digit. Semuanya dapat dilacak di <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> dengan data Arkham Intel mingguan.',
        'faq4_q': 'Di mana saya bisa bermain?',
        'faq4_a': 'Lisensi Curacao mencakup sebagian besar negara, tetapi Stake memiliki pembatasannya sendiri di AS, UK, sebagian Australia, dan beberapa negara lain. Gunakan <a href="/id/mirror/">halaman situs mirror</a> untuk menemukan domain di wilayah Anda.',
        'faq5_q': 'Seberapa cepat penarikan?',
        'faq5_a': 'Penarikan kripto untuk jumlah normal selesai dalam 30 hingga 60 menit. TRX, XRP, SOL selesai dalam hitungan detik. Jumlah besar mungkin memerlukan tinjauan kepatuhan 2 hingga 4 hari kerja. Penarikan fiat via MoonPay membutuhkan 1 hingga 5 hari kerja. Detail lebih lanjut di <a href="/id/payments/">halaman pembayaran</a>.',
        'signature': 'Beritahu dealer bahwa WinnersClub yang mengirim Anda.',
        'sticky_text': 'Kode: <span class="code-highlight">MAX3000</span>. 200% hingga $3.000. Pintu Stake.com terbuka',
        'sticky_cta': 'Ambil tempat &rarr;',
        'sticky_close': 'Tutup',
        'footer_tagline': 'KLUB TELAH ADA DI STAKE SEJAK 2017.',
        'footer_floor': 'Lantai',
        'footer_code': 'Kode',
        'footer_intel': 'Intel',
        'footer_casino': 'Kasino',
        'footer_sports': 'Olahraga',
        'footer_poker': 'Poker',
        'footer_aviator': 'Aviator',
        'footer_liveodds': 'Odds live',
        'footer_promo': 'Kode Promo MAX3000',
        'footer_payments': 'Pembayaran',
        'footer_mirror': 'Akses dan situs mirror',
        'footer_aboutstake': 'Tentang Stake',
        'footer_reserves': 'Cadangan on-chain',
        'footer_disclaimer': 'WinnersClub adalah klub eksklusif pemain Stake. Stake.com dioperasikan oleh Medium Rare NV di bawah lisensi Curacao OGL/2024/1451/0918. Stake.us adalah platform sweepstakes terpisah yang dioperasikan oleh Sweepsteaks Limited. Situs ini beroperasi hanya untuk tujuan informasi. Berjudi mengandung risiko. Bermainlah secara bertanggung jawab. Jika Anda mengalami masalah perjudian, hubungi GamCare atau organisasi dukungan lokal Anda. 18 tahun ke atas.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Semua hak dilindungi.',
        'age_badge': '18+',
        'faq_json_q1': 'Apakah MAX3000 kode bonus Stake terbesar?',
        'faq_json_a1': 'Ya. 200% hingga $3.000 dengan rollover 40x. Kode publik lainnya berhenti di 100%/$1.000.',
        'faq_json_q2': 'Apakah Stake.com terpercaya?',
        'faq_json_a2': 'Stake beroperasi sejak 2017 dengan lisensi Curacao OGL/2024/1451/0918. Cadangan $339.53M per 28 Mei 2026. Pendiri Ed Craven dan Bijan Tehrani.',
        'faq_json_q3': 'Bisakah saya verifikasi cadangan Stake?',
        'faq_json_a3': 'Snapshot 28 Mei 2026: $339.53M di dompet Arkham. Ethereum 74%, Solana 14%. Dapat dilacak di cryptotips.com.',
        'faq_json_q4': 'Di mana saya bisa bermain?',
        'faq_json_a4': 'Lisensi Curacao mencakup sebagian besar negara. Gunakan halaman situs mirror untuk domain di wilayah Anda.',
        'faq_json_q5': 'Seberapa cepat penarikan?',
        'faq_json_a5': 'Kripto normal: 30-60 menit. TRX, XRP, SOL: detik. Besar: 2-4 hari kerja. MoonPay fiat: 1-5 hari kerja.',
        'ld_name': 'WinnersClub - Interior Klub Stake | Kode MAX3000, 200% Hingga $3.000',
        'ld_desc': 'Klub eksklusif pemain Stake.com. Kode MAX3000: 200% hingga $3.000, rollover 40x. GGR $4.7B, lisensi Curacao OGL/2024/1451/0918.',
    },
    'fr': {
        'title': 'Code Promo Stake MAX3000 - 200% jusqu\'a 3 000$ a l\'inscription',
        'desc': 'Club exclusif pour les joueurs de Stake.com. Avec le code MAX3000 obtenez jusqu\'a 3 000$ avec 200%, condition de mise de 40x sur depot+bonus. GGR 4,7Md$, licence Curacao OGL/2024/1451/0918, fonde en 2017.',
        'og_title': 'WinnersClub | Code Stake MAX3000 | 200% jusqu\'a 3 000$, 40x mise',
        'og_desc': 'Club exclusif de Stake.com. Code MAX3000: 200% jusqu\'a 3 000$, mise 40x depot+bonus. GGR 4,7Md$.',
        'h1': 'Code Promo Stake MAX3000<span class="h1-sub">A l\'interieur du club.</span>',
        'tease': 'Si vous avez trouve cette page, le videur vous a deja repere.',
        'hero_sub': 'La salle reservee aux joueurs de Stake. Murmurez <span class="code-highlight">MAX3000</span> a l\'entree et vous attendez <strong>200% jusqu\'a 3 000$</strong> avec <strong>condition de mise de 40x sur depot+bonus</strong>. Les codes publics ne s\'en approchent meme pas.',
        'hero_cta1': 'Obtenir 200% jusqu\'a 3 000$ sur Stake.com',
        'hero_cta2': 'Ce que MAX3000 deverrouille',
        'reserves_ticker': 'Stake on-chain maintenant: reserves labelisees 339,53M$ &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licence Curacao OGL/2024/1451/0918 &middot; Source: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026',
        'promo_strip_label': 'Code Promo',
        'promo_strip_bonus': '200% jusqu\'a 3 000$ &middot; Mise 40x',
        'promo_strip_cta': 'Voir la page du code &rarr;',
        'sec1_h2': 'Pourquoi <span class="text-gradient-gold">ce club</span>',
        'sec1_card1_h3': 'Un bonus de poids',
        'sec1_card1_p': '200% jusqu\'a 3 000$ avec condition de mise de 40x sur depot+bonus. Les autres codes publics de Stake plafonnent a 100% et 1 000$. Si vous ne donnez pas <span class="code-highlight">MAX3000</span> au croupier dans les 24 heures apres l\'inscription, vous revenez au menu ordinaire.',
        'sec1_card2_h3': 'L\'argent est accroche au mur',
        'sec1_card2_p': 'Reserves labelisees par Arkham: 339,53M$ au 28 mai 2026. Pas de PDF "faites-nous confiance". Le portefeuille est public et n\'importe qui avec du WiFi peut l\'auditer. <a href="/fr/reserves/" style="color:var(--gold);">Les recu, ici.</a>',
        'sec1_card3_h3': 'La maison a un visage',
        'sec1_card3_p': 'Ed Craven (Melbourne, 1995) et Bijan Tehrani. Ils se sont rencontres sur RuneScape, ont fonde Stake en 2017 et lance Kick en 2022. Fortune combinee estimee par Forbes: 5,6Md$ US. Ce n\'est pas une societe fantome. Ce sont deux personnes qui ne perdent pas.',
        'sec2_h2': 'Cinq salles, <span class="text-gradient-gold">un code</span>',
        'sec2_sub': 'Choisissez la porte. MAX3000 fonctionne dans les cinq. Le croupier se fiche ou vous utilisez le bonus.',
        'vert_casino': 'Casino',
        'vert_sports': 'Sports',
        'vert_poker': 'Poker',
        'vert_aviator': 'Aviator',
        'vert_live': 'En direct',
        'girl_break_h2': 'Trois mille. <span class="text-gradient-gold">Mise 40x.</span> Un code.',
        'girl_break_sub': 'Murmurez <span class="code-highlight">MAX3000</span> a l\'inscription. Avant que la premiere boisson arrive, les calculs vous appartiennent.',
        'girl_break_cta': 'Donner le code au croupier',
        'sec3_h2': 'Ce que <span class="text-gradient-gold">le club sait</span>',
        'intel_founder_label': 'Fondateurs',
        'intel_founder_detail': 'Ed Craven (1995, Melbourne) et Bijan Tehrani. Se sont rencontres sur RuneScape. Co-fondes Stake en 2017. Lance Kick en 2022.',
        'intel_operator_label': 'Operateur',
        'intel_operator_detail': 'Entite de Curacao exploitant Stake.com. Societe mere: Easygo Group Holdings, revenus FY2025 A$970M. Stake.us est une entite sweepstakes separee.',
        'intel_license_label': 'Licence',
        'intel_license_detail': 'Couvre la plupart des pays. UK sorti en mars 2025. USA bloque (Stake.us sweepstakes disponible dans plus de 30 etats). Plus de 22 sites miroir confirmes.',
        'intel_reserves_label': 'Reserves',
        'intel_reserves_detail': 'Labelisees par Arkham au 28 mai 2026. Ethereum 74%, Solana 14%, solde stablecoin a neuf chiffres. Traçable sur cryptotips.com.',
        'two_doors_h2': 'Deux portes, <span class="text-gradient-gold">un code</span>',
        'two_doors_sub': 'MAX3000 est reconnu sur Stake.com et Stake.us. L\'accueil derriere chaque porte est different. Le croupier vous guidera vers la bonne porte selon votre localisation.',
        'stakecom_h3': 'Stake.com - Argent Reel, Mondial',
        'stakecom_p': 'Plateforme d\'argent reel exploitee par Medium Rare NV sous Curacao OGL/2024/1451/0918. Crypto et fiat. Sports, casino, originaux, poker. Avec le code <span class="code-highlight">MAX3000</span> vous obtenez <strong>200% jusqu\'a 3 000$</strong>, condition de mise 40x sur depot+bonus, 30 jours, depot minimum 10$. Reclamez via le support en direct apres le depot. KYC niveau 3 requis. Disponible dans la plupart des pays sauf USA et UK.',
        'stakecom_btn': 'Ouvrir la porte mondiale',
        'stakeus_h3': 'Stake.us - Sweepstakes, USA',
        'stakeus_p': 'Plateforme sweepstakes americaine exploitee par Sweepsteaks Limited. Gold Coins pour jouer, Stake Cash echangeable apres 3x de jeu. Pas de depots/retraits reels, pas de sports, casino seulement. Le code <span class="code-highlight">MAX3000</span> est aussi reconnu et donne <strong>560K GC + 56 SC + 3.5% rakeback</strong>. Disponible dans 37 etats.',
        'stakeus_btn': 'Ouvrir la porte americaine',
        'faq_h2': 'Questions <span class="text-gradient-gold">a l\'entree</span>',
        'faq1_q': 'MAX3000 est-il le plus grand code bonus de Stake?',
        'faq1_a': 'Oui. 200% jusqu\'a 3 000$ avec condition de mise 40x sur depot+bonus. La plupart des codes publics s\'arretent a 100% / 1 000$. MAX3000 est le code que le club donne a l\'entree.',
        'faq2_q': 'Stake.com est-il fiable?',
        'faq2_a': 'Stake opere depuis 2017 sous licence Curacao OGL/2024/1451/0918 via Medium Rare NV. Les reserves on-chain au 28 mai 2026 sont de 339,53M$, traçables publiquement sur Arkham. Les fondateurs Ed Craven (1995, Melbourne) et Bijan Tehrani exploitent egalement Kick. La maison mere Easygo Group Holdings a declare A$970M de revenus et A$257M de benefice net en FY2025.',
        'faq3_q': 'Puis-je verifier les reserves de Stake?',
        'faq3_a': 'Oui, consultez le <a href="/fr/reserves/">rapport de reserves</a>. Le snapshot du 28 mai 2026 montre 339,53M$ dans les portefeuilles labelises par Arkham. Ethereum 74%, Solana 14%, solde stablecoin a neuf chiffres. Tout traçable sur <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> avec des donnees Arkham Intel hebdomadaires.',
        'faq4_q': 'Ou puis-je jouer?',
        'faq4_a': 'La licence Curacao couvre la plupart des pays mais Stake a ses propres restrictions aux USA, au UK, dans certaines parties de l\'Australie et dans quelques autres pays. Utilisez la <a href="/fr/mirror/">page des sites miroir</a> pour trouver le domaine de votre region.',
        'faq5_q': 'Quelle est la rapidite des retraits?',
        'faq5_a': 'Les retraits en crypto pour des montants normaux sont traites en 30 a 60 minutes. TRX, XRP, SOL sont regles en quelques secondes. Les gros montants peuvent necessiter un examen de conformite de 2 a 4 jours ouvrables. Les retraits fiat via MoonPay prennent 1 a 5 jours ouvrables. Plus de details sur la <a href="/fr/payments/">page des paiements</a>.',
        'signature': 'Dites au croupier que c\'est WinnersClub qui vous envoie.',
        'sticky_text': 'Code: <span class="code-highlight">MAX3000</span>. 200% jusqu\'a 3 000$. La porte de Stake.com est ouverte',
        'sticky_cta': 'Prendre sa place &rarr;',
        'sticky_close': 'Fermer',
        'footer_tagline': 'LE CLUB EST CHEZ STAKE DEPUIS 2017.',
        'footer_floor': 'Salle',
        'footer_code': 'Code',
        'footer_intel': 'Intel',
        'footer_casino': 'Casino',
        'footer_sports': 'Sports',
        'footer_poker': 'Poker',
        'footer_aviator': 'Aviator',
        'footer_liveodds': 'Cotes en direct',
        'footer_promo': 'Code Promo MAX3000',
        'footer_payments': 'Paiements',
        'footer_mirror': 'Acces et sites miroir',
        'footer_aboutstake': 'A propos de Stake',
        'footer_reserves': 'Reserves on-chain',
        'footer_disclaimer': 'WinnersClub est le club exclusif des joueurs de Stake. Stake.com est exploite par Medium Rare NV sous licence Curacao OGL/2024/1451/0918. Stake.us est une plateforme sweepstakes separee exploitee par Sweepsteaks Limited. Ce site fonctionne uniquement a des fins informatives. Jouer comporte des risques. Jouez de maniere responsable. Si vous avez des problemes de jeu, contactez GamCare ou votre organisation de soutien locale. 18 ans et plus.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Tous droits reserves.',
        'age_badge': '18+',
        'faq_json_q1': 'MAX3000 est-il le plus grand code bonus de Stake?',
        'faq_json_a1': 'Oui. 200% jusqu\'a 3 000$ avec mise 40x. La plupart des codes publics s\'arretent a 100%/1 000$.',
        'faq_json_q2': 'Stake.com est-il fiable?',
        'faq_json_a2': 'Stake opere depuis 2017 sous licence Curacao OGL/2024/1451/0918. Reserves 339,53M$ au 28 mai 2026. Fondateurs Ed Craven et Bijan Tehrani.',
        'faq_json_q3': 'Puis-je verifier les reserves de Stake?',
        'faq_json_a3': 'Snapshot du 28 mai 2026: 339,53M$ dans les portefeuilles Arkham. Ethereum 74%, Solana 14%. Traçable sur cryptotips.com.',
        'faq_json_q4': 'Ou puis-je jouer?',
        'faq_json_a4': 'La licence Curacao couvre la plupart des pays. Utilisez la page des sites miroir pour le domaine de votre region.',
        'faq_json_q5': 'Quelle est la rapidite des retraits?',
        'faq_json_a5': 'Crypto normaux: 30-60 minutes. TRX, XRP, SOL: secondes. Gros montants: 2-4 jours ouvrables. MoonPay fiat: 1-5 jours.',
        'ld_name': 'WinnersClub - Interieur du Club Stake | Code MAX3000, 200% jusqu\'a 3 000$',
        'ld_desc': 'Club exclusif des joueurs de Stake.com. Code MAX3000: 200% jusqu\'a 3 000$, mise 40x. GGR 4,7Md$, licence Curacao OGL/2024/1451/0918.',
    },
    'ru': {
        'title': 'Промокод Stake MAX3000 - 200% до $3000 при регистрации',
        'desc': 'Эксклюзивный клуб для игроков Stake.com. С промокодом MAX3000 вы получаете до $3000 при 200%, отыгрыш 40x от депозита+бонуса. GGR $4.7B, лицензия Curacao OGL/2024/1451/0918, основан в 2017.',
        'og_title': 'WinnersClub | Промокод Stake MAX3000 | 200% до $3000, вейджер 40x',
        'og_desc': 'Эксклюзивный клуб Stake.com. Промокод MAX3000: 200% до $3000, вейджер 40x депозит+бонус. GGR $4.7B.',
        'h1': 'Промокод Stake MAX3000<span class="h1-sub">Добро пожаловать в клуб.</span>',
        'tease': 'Если вы нашли эту страницу, вышибала уже дал вам зелёный свет.',
        'hero_sub': 'Закрытая комната для игроков Stake. Шепните <span class="code-highlight">MAX3000</span> у входа и вас ждут <strong>200% до $3000</strong> с <strong>вейджером 40x на депозит+бонус</strong>. Публичные коды рядом не стоят.',
        'hero_cta1': 'Получить 200% до $3000 на Stake.com',
        'hero_cta2': 'Что открывает MAX3000',
        'reserves_ticker': 'Stake on-chain сейчас: помеченные резервы $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Лицензия Curacao OGL/2024/1451/0918 &middot; Источник: Arkham Intel через cryptotips.com &middot; Снимок 28 мая 2026',
        'promo_strip_label': 'Промокод',
        'promo_strip_bonus': '200% до $3000 &middot; Вейджер 40x',
        'promo_strip_cta': 'Открыть страницу кода &rarr;',
        'sec1_h2': 'Почему <span class="text-gradient-gold">этот клуб</span>',
        'sec1_card1_h3': 'Серьёзный бонус',
        'sec1_card1_p': '200% до $3000 с вейджером 40x на депозит+бонус. Другие публичные коды Stake ограничиваются 100% и $1000. Если не дадите дилеру <span class="code-highlight">MAX3000</span> в течение 24 часов после регистрации, вернётесь в эконом-меню.',
        'sec1_card2_h3': 'Деньги на виду',
        'sec1_card2_p': 'Помеченные Arkham резервы: $339.53M по состоянию на 28 мая 2026. Никаких PDF "доверяйте нам". Кошелёк публичный, любой с WiFi может провести аудит. <a href="/ru/reserves/" style="color:var(--gold);">Доказательства здесь.</a>',
        'sec1_card3_h3': 'У дома есть лицо',
        'sec1_card3_p': 'Ed Craven (Мельбурн, 1995) и Bijan Tehrani. Познакомились в RuneScape, основали Stake в 2017 году и запустили Kick в 2022-м. Совокупное состояние по оценке Forbes: $5.6B. Не подставная компания. Двое людей, которые не проигрывают.',
        'sec2_h2': 'Пять комнат, <span class="text-gradient-gold">один код</span>',
        'sec2_sub': 'Выберите дверь. MAX3000 работает во всех пяти. Дилеру всё равно, где вы используете бонус.',
        'vert_casino': 'Казино',
        'vert_sports': 'Спорт',
        'vert_poker': 'Покер',
        'vert_aviator': 'Авиатор',
        'vert_live': 'Лайв',
        'girl_break_h2': 'Три тысячи. <span class="text-gradient-gold">Вейджер 40x.</span> Один код.',
        'girl_break_sub': 'Шепните <span class="code-highlight">MAX3000</span> при регистрации. Прежде чем подадут первый напиток, математика уже будет на вашей стороне.',
        'girl_break_cta': 'Передать код дилеру',
        'sec3_h2': 'Что <span class="text-gradient-gold">знает клуб</span>',
        'intel_founder_label': 'Основатели',
        'intel_founder_detail': 'Ed Craven (1995, Мельбурн) и Bijan Tehrani. Познакомились в RuneScape. Совместно основали Stake в 2017 году. Запустили Kick в 2022 году.',
        'intel_operator_label': 'Оператор',
        'intel_operator_detail': 'Организация на Кюрасао, управляющая Stake.com. Материнская компания: Easygo Group Holdings, выручка за FY2025 A$970M. Stake.us - отдельная sweepstakes-компания.',
        'intel_license_label': 'Лицензия',
        'intel_license_detail': 'Охватывает большинство стран. UK вышел в марте 2025. США заблокированы (Stake.us sweepstakes доступен в 30+ штатах). Более 22 зеркальных сайтов подтверждено.',
        'intel_reserves_label': 'Резервы',
        'intel_reserves_detail': 'Помечены Arkham по состоянию на 28 мая 2026. Ethereum 74%, Solana 14%, девятизначный баланс стейблкоинов. Отслеживается на cryptotips.com.',
        'two_doors_h2': 'Две двери, <span class="text-gradient-gold">один код</span>',
        'two_doors_sub': 'MAX3000 признаётся как на Stake.com, так и на Stake.us. Приём за каждой дверью отличается. Дилер направит вас к нужной двери в зависимости от вашего местонахождения.',
        'stakecom_h3': 'Stake.com - Реальные деньги, Глобально',
        'stakecom_p': 'Платформа для игры на реальные деньги, управляемая Medium Rare NV под лицензией Curacao OGL/2024/1451/0918. Крипто и фиат. Спорт, казино, оригиналы, покер. С промокодом <span class="code-highlight">MAX3000</span> вы получаете <strong>200% до $3000</strong>, вейджер 40x на депозит+бонус, 30 дней, минимальный депозит $10. Заявите через лайв-поддержку после депозита. Требуется KYC уровня 3. Доступно в большинстве стран, кроме США и UK.',
        'stakecom_btn': 'Открыть глобальную дверь',
        'stakeus_h3': 'Stake.us - Свипстейкс, США',
        'stakeus_p': 'Американская sweepstakes-платформа под управлением Sweepsteaks Limited. Gold Coins для игры, Stake Cash для вывода после 3x отыгрыша. Без реальных депозитов/выводов, без спорта, только казино. Промокод <span class="code-highlight">MAX3000</span> также принимается и даёт <strong>560K GC + 56 SC + 3.5% рейкбэк</strong>. Доступно в 37 штатах.',
        'stakeus_btn': 'Открыть американскую дверь',
        'faq_h2': 'Вопросы <span class="text-gradient-gold">у входа</span>',
        'faq1_q': 'MAX3000 - самый большой бонусный код Stake?',
        'faq1_a': 'Да. 200% до $3000 с вейджером 40x на депозит+бонус. Большинство публичных кодов ограничиваются 100% / $1000. MAX3000 - это код, который клуб выдаёт у входа.',
        'faq2_q': 'Stake.com - надёжный?',
        'faq2_a': 'Stake работает с 2017 года под лицензией Curacao OGL/2024/1451/0918 через Medium Rare NV. On-chain резервы на 28 мая 2026 составляют $339.53M, публично отслеживаются на Arkham. Основатели Ed Craven (1995, Мельбурн) и Bijan Tehrani также управляют Kick. Материнская Easygo Group Holdings отчиталась о A$970M выручки и A$257M чистой прибыли в FY2025.',
        'faq3_q': 'Могу ли я проверить резервы Stake?',
        'faq3_a': 'Да, смотрите <a href="/ru/reserves/">отчёт о резервах</a>. Снимок от 28 мая 2026 показывает $339.53M в кошельках, помеченных Arkham. Ethereum 74%, Solana 14%, девятизначный баланс стейблкоинов. Всё отслеживается на <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> с еженедельными данными Arkham Intel.',
        'faq4_q': 'Где я могу играть?',
        'faq4_a': 'Лицензия Curacao охватывает большинство стран, но Stake имеет собственные ограничения в США, UK, части Австралии и ряде других стран. Используйте <a href="/ru/mirror/">страницу зеркальных сайтов</a>, чтобы найти домен для вашего региона.',
        'faq5_q': 'Как быстро происходит вывод средств?',
        'faq5_a': 'Криптовыводы на обычные суммы обрабатываются за 30-60 минут. TRX, XRP, SOL зачисляются за секунды. Крупные суммы могут потребовать проверки комплаенса 2-4 рабочих дня. Фиатные выводы через MoonPay занимают 1-5 рабочих дней. Подробнее на <a href="/ru/payments/">странице платежей</a>.',
        'signature': 'Скажите дилеру, что вас отправил WinnersClub.',
        'sticky_text': 'Промокод: <span class="code-highlight">MAX3000</span>. 200% до $3000. Дверь Stake.com открыта',
        'sticky_cta': 'Занять место &rarr;',
        'sticky_close': 'Закрыть',
        'footer_tagline': 'КЛУБ В STAKE С 2017 ГОДА.',
        'footer_floor': 'Залы',
        'footer_code': 'Код',
        'footer_intel': 'Intel',
        'footer_casino': 'Казино',
        'footer_sports': 'Спорт',
        'footer_poker': 'Покер',
        'footer_aviator': 'Авиатор',
        'footer_liveodds': 'Живые коэффициенты',
        'footer_promo': 'Промокод MAX3000',
        'footer_payments': 'Платежи',
        'footer_mirror': 'Доступ и зеркала',
        'footer_aboutstake': 'О Stake',
        'footer_reserves': 'On-chain резервы',
        'footer_disclaimer': 'WinnersClub - эксклюзивный клуб игроков Stake. Stake.com управляется компанией Medium Rare NV под лицензией Curacao OGL/2024/1451/0918. Stake.us - отдельная sweepstakes-платформа под управлением Sweepsteaks Limited. Этот сайт работает исключительно в информационных целях. Азартные игры несут риски. Играйте ответственно. Если у вас есть проблемы с азартными играми, обратитесь в GamCare или местную службу поддержки. 18+.',
        'footer_copyright': '&copy; 2026 winnersclub.com. Все права защищены.',
        'age_badge': '18+',
        'faq_json_q1': 'MAX3000 - самый большой бонусный код Stake?',
        'faq_json_a1': 'Да. 200% до $3000 с вейджером 40x. Большинство публичных кодов ограничиваются 100%/$1000.',
        'faq_json_q2': 'Stake.com - надёжный?',
        'faq_json_a2': 'Stake работает с 2017 под лицензией Curacao OGL/2024/1451/0918. Резервы $339.53M на 28 мая 2026. Основатели Ed Craven и Bijan Tehrani.',
        'faq_json_q3': 'Могу ли я проверить резервы Stake?',
        'faq_json_a3': 'Снимок 28 мая 2026: $339.53M в кошельках Arkham. Ethereum 74%, Solana 14%. Отслеживается на cryptotips.com.',
        'faq_json_q4': 'Где я могу играть?',
        'faq_json_a4': 'Лицензия Curacao охватывает большинство стран. Используйте страницу зеркал для домена вашего региона.',
        'faq_json_q5': 'Как быстро происходит вывод?',
        'faq_json_a5': 'Крипто: 30-60 минут. TRX, XRP, SOL: секунды. Крупные: 2-4 дня. MoonPay фиат: 1-5 дней.',
        'ld_name': 'WinnersClub - Внутри Клуба Stake | Промокод MAX3000, 200% до $3000',
        'ld_desc': 'Эксклюзивный клуб игроков Stake.com. Промокод MAX3000: 200% до $3000, вейджер 40x. GGR $4.7B, лицензия Curacao OGL/2024/1451/0918.',
    },
    'hi': {
        'title': 'Stake प्रोमो कोड MAX3000 - रजिस्ट्रेशन पर 200% $3,000 तक',
        'desc': 'Stake.com खिलाड़ियों का एक्सक्लूसिव क्लब. MAX3000 कोड से $3,000 तक 200% बोनस, 40x वेजरिंग (डिपॉजिट+बोनस). GGR $4.7B, लाइसेंस Curacao OGL/2024/1451/0918, 2017 में स्थापित.',
        'og_title': 'WinnersClub | Stake कोड MAX3000 | 200% $3,000 तक, 40x वेजरिंग',
        'og_desc': 'Stake.com खिलाड़ी क्लब. कोड MAX3000: 200% $3,000 तक, 40x वेजरिंग डिपॉजिट+बोनस. GGR $4.7B.',
        'h1': 'Stake प्रोमो कोड MAX3000<span class="h1-sub">क्लब के अंदर.</span>',
        'tease': 'अगर आपने यह पेज ढूंढा, तो बाउंसर पहले से आपको पसंद कर चुका है.',
        'hero_sub': 'Stake खिलाड़ियों का एक्सक्लूसिव बैक रूम. दरवाजे पर <span class="code-highlight">MAX3000</span> फुसफुसाएं और आपका इंतजार कर रहे हैं <strong>200% $3,000 तक</strong> के साथ <strong>डिपॉजिट+बोनस पर 40x वेजरिंग</strong>. पब्लिक कोड इसके आसपास भी नहीं आते.',
        'hero_cta1': 'Stake.com पर 200% $3,000 तक पाएं',
        'hero_cta2': 'MAX3000 क्या खोलता है',
        'reserves_ticker': 'Stake अभी on-chain: लेबल्ड रिजर्व $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 लाइसेंस &middot; स्रोत: cryptotips.com के जरिए Arkham Intel &middot; 28 मई 2026 स्नैपशॉट',
        'promo_strip_label': 'प्रोमो कोड',
        'promo_strip_bonus': '$3,000 तक 200% &middot; 40x वेजरिंग',
        'promo_strip_cta': 'कोड पेज खोलें &rarr;',
        'sec1_h2': 'यह <span class="text-gradient-gold">क्लब</span> क्यों',
        'sec1_card1_h3': 'वजनदार बोनस',
        'sec1_card1_p': '$3,000 तक 200% डिपॉजिट+बोनस पर 40x वेजरिंग के साथ. इंटरनेट पर दूसरे Stake कोड 100% और $1,000 पर रुक जाते हैं. रजिस्ट्रेशन के 24 घंटे के अंदर डीलर को <span class="code-highlight">MAX3000</span> न दें तो सस्ते मेन्यू पर वापस.',
        'sec1_card2_h3': 'पैसा दीवार पर टंगा है',
        'sec1_card2_p': '28 मई 2026 को Arkham लेबल्ड रिजर्व $339.53M. कोई "हम पर भरोसा करें" PDF नहीं, कोई रिजर्व थिएटर नहीं. वॉलेट पब्लिकली पढ़े जा सकते हैं और कोई भी WiFi से ऑडिट कर सकता है. <a href="/hi/reserves/" style="color:var(--gold);">रसीदें यहां.</a>',
        'sec1_card3_h3': 'घर का एक चेहरा है',
        'sec1_card3_p': 'Ed Craven (मेलबर्न, 1995) और Bijan Tehrani. RuneScape पर मिले, 2017 में Stake बनाया, 2022 में Kick लॉन्च किया. Forbes अनुमानित संयुक्त नेट वर्थ US$5.6B. पेपर कंपनी नहीं. दो लोग जो हारते नहीं.',
        'sec2_h2': 'पांच कमरे, <span class="text-gradient-gold">एक कोड</span>',
        'sec2_sub': 'दरवाजा चुनें. MAX3000 पांचों में काम करता है. डीलर को परवाह नहीं कि आप बोनस कहां इस्तेमाल करते हैं.',
        'vert_casino': 'कैसीनो',
        'vert_sports': 'स्पोर्ट्स',
        'vert_poker': 'पोकर',
        'vert_aviator': 'एविएटर',
        'vert_live': 'लाइव',
        'girl_break_h2': 'तीन हजार. <span class="text-gradient-gold">40x वेजरिंग.</span> एक कोड.',
        'girl_break_sub': 'रजिस्ट्रेशन पर <span class="code-highlight">MAX3000</span> बताएं. पहली ड्रिंक आने से पहले गणित आपका है.',
        'girl_break_cta': 'डीलर को कोड दें',
        'sec3_h2': 'क्लब को <span class="text-gradient-gold">क्या पता है</span>',
        'intel_founder_label': 'संस्थापक',
        'intel_founder_detail': 'Ed Craven (1995, मेलबर्न) और Bijan Tehrani. RuneScape पर मिले. 2017 में Stake की सह-स्थापना की. 2022 में Kick लॉन्च किया.',
        'intel_operator_label': 'ऑपरेटर',
        'intel_operator_detail': 'Stake.com चलाने वाली Curaçao इकाई. मूल कंपनी: Easygo Group Holdings, FY2025 राजस्व A$970M. Stake.us एक अलग स्वीपस्टेक्स इकाई है.',
        'intel_license_label': 'लाइसेंस',
        'intel_license_detail': 'अधिकांश देशों को कवर करता है. यूके मार्च 2025 में बाहर. यूएस ब्लॉक्ड (Stake.us स्वीपस्टेक्स 30+ राज्यों में उपलब्ध). 22 से अधिक मिरर साइट्स की पुष्टि.',
        'intel_reserves_label': 'रिजर्व',
        'intel_reserves_detail': '28 मई 2026 को Arkham लेबल्ड. Ethereum 74%, Solana 14%, नौ अंकों का स्टेबलकॉइन बैलेंस. cryptotips.com पर ट्रैक किया जा सकता है.',
        'two_doors_h2': 'दो दरवाजे, <span class="text-gradient-gold">एक कोड</span>',
        'two_doors_sub': 'MAX3000 Stake.com और Stake.us दोनों पर पहचाना जाता है. हर दरवाजे के पीछे अलग-अलग स्वागत है. डीलर आपकी लोकेशन के हिसाब से सही दरवाजे की तरफ गाइड करेगा.',
        'stakecom_h3': 'Stake.com - रियल मनी, ग्लोबल',
        'stakecom_p': 'Medium Rare NV द्वारा Curaçao OGL/2024/1451/0918 के तहत संचालित रियल मनी प्लेटफॉर्म. क्रिप्टो और फिएट. स्पोर्ट्स, कैसीनो, ओरिजिनल्स, पोकर. कोड <span class="code-highlight">MAX3000</span> से <strong>$3,000 तक 200%</strong>, डिपॉजिट+बोनस पर 40x वेजरिंग, 30 दिन, न्यूनतम डिपॉजिट $10. डिपॉजिट के बाद लाइव सपोर्ट से क्लेम करें. KYC लेवल 3 जरूरी. अमेरिका और यूके को छोड़कर अधिकांश देशों में उपलब्ध.',
        'stakecom_btn': 'ग्लोबल दरवाजा खोलें',
        'stakeus_h3': 'Stake.us - स्वीपस्टेक्स, अमेरिका',
        'stakeus_p': 'Sweepsteaks Limited द्वारा संचालित अमेरिकी स्वीपस्टेक्स प्लेटफॉर्म. खेलने के लिए Gold Coins, 3x प्ले-थ्रू के बाद रिडीम होने वाले Stake Cash. कोई रियल डिपॉजिट/विदड्रॉल नहीं, स्पोर्ट्स नहीं, सिर्फ कैसीनो. कोड <span class="code-highlight">MAX3000</span> भी पहचाना जाता है और देता है <strong>560K GC + 56 SC + 3.5% रेकबैक</strong>. 37 राज्यों में उपलब्ध.',
        'stakeus_btn': 'अमेरिकी दरवाजा खोलें',
        'faq_h2': 'प्रवेश पर <span class="text-gradient-gold">सवाल</span>',
        'faq1_q': 'क्या MAX3000 सबसे बड़ा Stake बोनस कोड है?',
        'faq1_a': 'हां. $3,000 तक 200% बोनस डिपॉजिट+बोनस पर 40x वेजरिंग के साथ. अधिकांश पब्लिक कोड 100% / $1,000 पर खत्म होते हैं. MAX3000 वह कोड है जो क्लब दरवाजे पर देता है.',
        'faq2_q': 'क्या Stake.com भरोसेमंद है?',
        'faq2_a': 'Stake 2017 से Medium Rare NV के तहत Curaçao OGL/2024/1451/0918 लाइसेंस के साथ ऑपरेट कर रहा है. On-chain रिजर्व 28 मई 2026 को $339.53M हैं, Arkham पर पब्लिकली ट्रैक किए जा सकते हैं. संस्थापक Ed Craven (1995, मेलबर्न) और Bijan Tehrani Kick भी चलाते हैं. मूल कंपनी Easygo Group Holdings ने FY2025 में A$970M राजस्व, A$257M नेट प्रॉफिट रिपोर्ट किया.',
        'faq3_q': 'क्या मैं Stake के रिजर्व वेरिफाई कर सकता हूं?',
        'faq3_a': 'हां, <a href="/hi/reserves/">रिजर्व रिपोर्ट</a> देखें. 28 मई 2026 का स्नैपशॉट Arkham लेबल्ड वॉलेट्स में $339.53M दिखाता है. Ethereum 74%, Solana 14%, नौ अंकों का स्टेबलकॉइन बैलेंस. साप्ताहिक Arkham Intel डेटा के साथ <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a> से सब कुछ ट्रैक किया जा सकता है.',
        'faq4_q': 'मैं कहां खेल सकता हूं?',
        'faq4_a': 'Curaçao लाइसेंस अधिकांश देशों को कवर करता है, लेकिन Stake के अपने प्रतिबंध हैं अमेरिका, यूके, ऑस्ट्रेलिया के कुछ हिस्सों और कुछ अन्य देशों में. अपने क्षेत्र का डोमेन खोजने के लिए <a href="/hi/mirror/">मिरर साइट्स पेज</a> का उपयोग करें.',
        'faq5_q': 'विदड्रॉल कितनी जल्दी होता है?',
        'faq5_a': 'सामान्य राशि के क्रिप्टो विदड्रॉल 30 से 60 मिनट में पूरे होते हैं. TRX, XRP, SOL सेकंडों में सेटल होते हैं. बड़ी राशि के लिए 2 से 4 कार्यदिवस की कंप्लायंस समीक्षा हो सकती है. MoonPay फिएट विदड्रॉल में 1 से 5 कार्यदिवस लगते हैं. अधिक जानकारी <a href="/hi/payments/">पेमेंट पेज</a> पर.',
        'signature': 'डीलर को बताएं कि WinnersClub ने आपको भेजा है.',
        'sticky_text': 'कोड: <span class="code-highlight">MAX3000</span>. 200% $3,000 तक. Stake.com का दरवाजा खुला है',
        'sticky_cta': 'जगह लें &rarr;',
        'sticky_close': 'बंद करें',
        'footer_tagline': 'क्लब 2017 से STAKE में है.',
        'footer_floor': 'फ्लोर',
        'footer_code': 'कोड',
        'footer_intel': 'Intel',
        'footer_casino': 'कैसीनो',
        'footer_sports': 'स्पोर्ट्स',
        'footer_poker': 'पोकर',
        'footer_aviator': 'एविएटर',
        'footer_liveodds': 'लाइव ऑड्स',
        'footer_promo': 'प्रोमो कोड MAX3000',
        'footer_payments': 'पेमेंट',
        'footer_mirror': 'एक्सेस और मिरर साइट्स',
        'footer_aboutstake': 'Stake के बारे में',
        'footer_reserves': 'On-chain रिजर्व',
        'footer_disclaimer': 'WinnersClub Stake के खिलाड़ियों का एक्सक्लूसिव क्लब है. Stake.com को Medium Rare NV द्वारा Curaçao लाइसेंस OGL/2024/1451/0918 के तहत संचालित किया जाता है. Stake.us को Sweepsteaks Limited द्वारा संचालित एक अलग स्वीपस्टेक्स प्लेटफॉर्म है. यह साइट केवल सूचनात्मक उद्देश्यों के लिए संचालित होती है. जुए में जोखिम होते हैं. जिम्मेदारी से खेलें. यदि आपको जुए की समस्या है, GamCare या अपनी स्थानीय सहायता संस्था से संपर्क करें. 18 वर्ष से अधिक आयु.',
        'footer_copyright': '&copy; 2026 winnersclub.com. सर्वाधिकार सुरक्षित.',
        'age_badge': '18+',
        'faq_json_q1': 'क्या MAX3000 सबसे बड़ा Stake बोनस कोड है?',
        'faq_json_a1': 'हां. $3,000 तक 200% और 40x वेजरिंग. अधिकांश पब्लिक कोड 100%/$1,000 पर खत्म होते हैं.',
        'faq_json_q2': 'क्या Stake.com भरोसेमंद है?',
        'faq_json_a2': 'Stake 2017 से Curaçao OGL/2024/1451/0918 लाइसेंस के साथ चल रहा है. रिजर्व $339.53M 28 मई 2026. संस्थापक Ed Craven और Bijan Tehrani.',
        'faq_json_q3': 'क्या मैं Stake के रिजर्व वेरिफाई कर सकता हूं?',
        'faq_json_a3': '28 मई 2026 स्नैपशॉट: Arkham वॉलेट में $339.53M. Ethereum 74%, Solana 14%. cryptotips.com पर ट्रैक करें.',
        'faq_json_q4': 'मैं कहां खेल सकता हूं?',
        'faq_json_a4': 'Curaçao लाइसेंस अधिकांश देशों को कवर करता है. अपने क्षेत्र के डोमेन के लिए मिरर साइट्स पेज का उपयोग करें.',
        'faq_json_q5': 'विदड्रॉल कितनी जल्दी होता है?',
        'faq_json_a5': 'क्रिप्टो: 30-60 मिनट. TRX, XRP, SOL: सेकंड. बड़ी राशि: 2-4 दिन. MoonPay फिएट: 1-5 दिन.',
        'ld_name': 'WinnersClub - Stake क्लब के अंदर | प्रोमो कोड MAX3000, 200% $3,000 तक',
        'ld_desc': 'Stake.com खिलाड़ियों का एक्सक्लूसिव क्लब. प्रोमो कोड MAX3000: 200% $3,000 तक, 40x वेजरिंग. GGR $4.7B, Curaçao OGL/2024/1451/0918.',
    },
}


# ─── ROOMS-GRID DATA (localized, per build brief instruction) ────────────────
ROOMS_GRID = {
    'es': ("Otras salas del club", [
        ("promo-code", "Codigo promo Stake"),
        ("casino", "Casino Stake"),
        ("sports", "Deportes Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Reservas verificadas"),
        ("about-stake", "Sobre Stake.com"),
        ("payments", "Pagos crypto"),
        ("mirror", "Sitios espejo"),
        ("live-odds", "Cuotas en vivo"),
        ("originals", "Stake Originals"),
        ("vip", "Programa VIP"),
        ("slots", "Biblioteca de slots"),
        ("live-casino", "Casino en vivo"),
    ]),
    'pt-br': ("Outras salas do clube", [
        ("promo-code", "Codigo promo Stake"),
        ("casino", "Cassino Stake"),
        ("sports", "Esportes Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Reservas auditadas"),
        ("about-stake", "Sobre o Stake.com"),
        ("payments", "Pagamentos cripto"),
        ("mirror", "Sitios espelho"),
        ("live-odds", "Odds ao vivo"),
        ("originals", "Stake Originals"),
        ("vip", "Programa VIP"),
        ("slots", "Biblioteca de slots"),
        ("live-casino", "Cassino ao vivo"),
    ]),
    'tr': ("Kulupteki diger odalar", [
        ("promo-code", "Stake promosyon kodu"),
        ("casino", "Stake casino"),
        ("sports", "Stake spor"),
        ("poker", "Stake poker"),
        ("aviator", "Stake Aviator"),
        ("reserves", "Denetlenmis rezervler"),
        ("about-stake", "Stake.com hakkinda"),
        ("payments", "Kripto odemeler"),
        ("mirror", "Ayna siteler"),
        ("live-odds", "Canli oranlar"),
        ("originals", "Stake Originals"),
        ("vip", "VIP programi"),
        ("slots", "Slot kutuphanesi"),
        ("live-casino", "Canli casino"),
    ]),
    'id': ("Ruangan lain di klub", [
        ("promo-code", "Kode promo Stake"),
        ("casino", "Kasino Stake"),
        ("sports", "Olahraga Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Cadangan teraudit"),
        ("about-stake", "Tentang Stake.com"),
        ("payments", "Pembayaran kripto"),
        ("mirror", "Situs mirror"),
        ("live-odds", "Odds live"),
        ("originals", "Stake Originals"),
        ("vip", "Program VIP"),
        ("slots", "Perpustakaan slot"),
        ("live-casino", "Kasino live"),
    ]),
    'fr': ("Les autres salles du club", [
        ("promo-code", "Code promo Stake"),
        ("casino", "Casino Stake"),
        ("sports", "Sports Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Reserves auditees"),
        ("about-stake", "A propos de Stake.com"),
        ("payments", "Paiements crypto"),
        ("mirror", "Sites miroir"),
        ("live-odds", "Cotes en direct"),
        ("originals", "Stake Originals"),
        ("vip", "Programme VIP"),
        ("slots", "Bibliotheque de slots"),
        ("live-casino", "Casino en direct"),
    ]),
    'ru': ("Другие залы клуба", [
        ("promo-code", "Промокод Stake"),
        ("casino", "Казино Stake"),
        ("sports", "Спорт Stake"),
        ("poker", "Покер Stake"),
        ("aviator", "Авиатор Stake"),
        ("reserves", "Проверенные резервы"),
        ("about-stake", "О Stake.com"),
        ("payments", "Крипто-платежи"),
        ("mirror", "Зеркальные сайты"),
        ("live-odds", "Лайв коэффициенты"),
        ("originals", "Stake Originals"),
        ("vip", "VIP программа"),
        ("slots", "Библиотека слотов"),
        ("live-casino", "Лайв казино"),
    ]),
    'hi': ("क्लब के अन्य कमरे", [
        ("promo-code", "Stake प्रोमो कोड"),
        ("casino", "Stake कैसीनो"),
        ("sports", "Stake स्पोर्ट्स"),
        ("poker", "Stake पोकर"),
        ("aviator", "Stake एविएटर"),
        ("reserves", "ऑडिटेड रिजर्व"),
        ("about-stake", "Stake.com के बारे में"),
        ("payments", "क्रिप्टो पेमेंट"),
        ("mirror", "मिरर साइट्स"),
        ("live-odds", "लाइव ऑड्स"),
        ("originals", "Stake Originals"),
        ("vip", "VIP प्रोग्राम"),
        ("slots", "स्लॉट लाइब्रेरी"),
        ("live-casino", "लाइव कैसीनो"),
    ]),
}


# ─── SUB-PAGE CONTENT (all 18 sub-pages × 7 locales) ─────────────────────────
# Each entry: title, desc, og_title, og_desc, h1, hero_sub, body_html (main content)
# We generate full pages from KO source + translations

SUBPAGE_DATA = {}

# Helper to build sub-page entries per locale
def sp(locale, slug, title, desc, h1, hero_sub, body_html, og_image=None):
    if slug not in SUBPAGE_DATA:
        SUBPAGE_DATA[slug] = {}
    SUBPAGE_DATA[slug][locale] = {
        'title': title,
        'desc': desc,
        'og_title': title,
        'og_desc': desc[:160],
        'og_image': og_image or f'/images/og/{slug}.png',
        'h1': h1,
        'hero_sub': hero_sub,
        'body_html': body_html,
    }

# ── PROMO-CODE ──────────────────────────────────────────────────────────────
sp('es','promo-code',
    'Codigo Promo Stake MAX3000: 200% hasta $3,000 (junio 2026)',
    'Codigo Stake MAX3000, primer deposito 200%, hasta $3,000, rollover 40x deposito+bono, KYC nivel 3 obligatorio. Calculadora incluida. Verificado junio 2026.',
    'Codigo Promo Stake <span class="code-highlight">MAX3000</span><span class="h1-sub">El codigo que abre la caja fuerte.</span>',
    'El codigo es <span class="code-highlight">MAX3000</span>. Registrate, haz tu primer deposito entre $10 y $1,500, reclama via chat en vivo. <strong>200% hasta $3,000</strong>, rollover 40x, 30 dias.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Como funciona <span class="text-gradient-gold">MAX3000</span></h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Paso 1 - Registrate</h3><p>Usa el enlace de afiliado para crear tu cuenta en Stake.com. Completa KYC nivel 3: fotografia del documento de identidad, comprobante de domicilio y origen de fondos. Sin KYC nivel 3 el bono no se activa.</p></div>
<div class="club-card"><h3>Paso 2 - Deposita entre $10 y $1,500</h3><p>El deposito minimo para activar el bono es $10. El maximo que cuenta para el calculo del bono es $1,500. Depositar $1,500 equivale al bono maximo de $3,000.</p></div>
<div class="club-card"><h3>Paso 3 - Reclama via chat en vivo</h3><p>Abre el chat en vivo de Stake tras confirmar tu deposito y menciona el codigo <span class="code-highlight">MAX3000</span>. El equipo de soporte verifica tu elegibilidad y acredita el 200% en 24 a 48 horas.</p></div>
<div class="club-card"><h3>Rollover 40x</h3><p>El rollover se aplica al total de deposito mas bono. Ejemplo: $500 deposito + $1,000 bono = $1,500 x 40 = $60,000 en apuestas. Los juegos de casino aportan al 100%, las apuestas deportivas al 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Terminos <span class="text-gradient-gold">clave</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Bono maximo</div><div class="ic-value">$3,000</div><div class="ic-detail">200% del primer deposito. Deposito maximo que cuenta: $1,500.</div></div>
<div class="intel-card"><div class="ic-label">Rollover</div><div class="ic-value">40x</div><div class="ic-detail">Sobre deposito+bono. Plazo: 30 dias desde la acreditacion del bono.</div></div>
<div class="intel-card"><div class="ic-label">Deposito minimo</div><div class="ic-value">$10</div><div class="ic-detail">En USD o equivalente en criptomonedas.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Nivel 3</div><div class="ic-detail">Obligatorio antes de la acreditacion del bono. Documento de identidad + domicilio + origen de fondos.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('pt-br','promo-code',
    'Codigo Promo Stake MAX3000: 200% ate $3.000 (junho 2026)',
    'Codigo Stake MAX3000, primeiro deposito 200%, ate $3.000, rollover 40x deposito+bonus, KYC nivel 3 obrigatorio. Calculadora incluida. Verificado junho 2026.',
    'Codigo Promo Stake <span class="code-highlight">MAX3000</span><span class="h1-sub">O codigo que abre o cofre.</span>',
    'O codigo e <span class="code-highlight">MAX3000</span>. Cadastre-se, faca seu primeiro deposito entre $10 e $1.500, reivindique via chat ao vivo. <strong>200% ate $3.000</strong>, rollover 40x, 30 dias.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Como funciona <span class="text-gradient-gold">MAX3000</span></h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Passo 1 - Cadastre-se</h3><p>Use o link de afiliado para criar sua conta no Stake.com. Complete o KYC nivel 3: foto do documento de identidade, comprovante de endereco e origem dos fundos. Sem KYC nivel 3, o bonus nao e ativado.</p></div>
<div class="club-card"><h3>Passo 2 - Deposite entre $10 e $1.500</h3><p>O deposito minimo para ativar o bonus e $10. O maximo que conta para o calculo do bonus e $1.500. Depositar $1.500 equivale ao bonus maximo de $3.000.</p></div>
<div class="club-card"><h3>Passo 3 - Reivindique via chat ao vivo</h3><p>Abra o chat ao vivo do Stake apos confirmar seu deposito e mencione o codigo <span class="code-highlight">MAX3000</span>. A equipe de suporte verifica sua elegibilidade e credita os 200% em 24 a 48 horas.</p></div>
<div class="club-card"><h3>Rollover 40x</h3><p>O rollover se aplica ao total de deposito mais bonus. Exemplo: $500 deposito + $1.000 bonus = $1.500 x 40 = $60.000 em apostas. Jogos de cassino contribuem 100%, apostas esportivas 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Termos <span class="text-gradient-gold">principais</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Bonus maximo</div><div class="ic-value">$3.000</div><div class="ic-detail">200% do primeiro deposito. Deposito maximo que conta: $1.500.</div></div>
<div class="intel-card"><div class="ic-label">Rollover</div><div class="ic-value">40x</div><div class="ic-detail">Sobre deposito+bonus. Prazo: 30 dias a partir do credito do bonus.</div></div>
<div class="intel-card"><div class="ic-label">Deposito minimo</div><div class="ic-value">$10</div><div class="ic-detail">Em USD ou equivalente em criptomoedas.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Nivel 3</div><div class="ic-detail">Obrigatorio antes do credito do bonus. Documento + endereco + origem dos fundos.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('tr','promo-code',
    'Stake Promosyon Kodu MAX3000: 200% $3.000\'e Kadar (Haziran 2026)',
    'Stake MAX3000 kodu, ilk para yatirma 200%, $3.000\'e kadar, 40x cevrim sarti depozit+bonus, KYC seviye 3 zorunlu. Haziran 2026 dogrulandi.',
    'Stake Promosyon Kodu <span class="code-highlight">MAX3000</span><span class="h1-sub">Kasa\'yi acan kod.</span>',
    'Kod <span class="code-highlight">MAX3000</span>\'dir. Kayit olun, $10 ile $1.500 arasinda ilk para yatırımınızı yapın, canli destek uzerinden talep edin. <strong>200% $3.000\'e kadar</strong>, 40x cevrim, 30 gun.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">MAX3000</span> nasil calisir</h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Adim 1 - Kayit olun</h3><p>Stake.com\'da hesabinizi olusturmak icin ortaklik linkini kullanin. KYC seviye 3\'u tamamlayin: kimlik fotografi, adres belgesi ve fon kaynagi. KYC seviye 3 olmadan bonus aktive edilmez.</p></div>
<div class="club-card"><h3>Adim 2 - $10 ile $1.500 arasi para yatirin</h3><p>Bonusu aktive etmek icin minimum para yatirma tutari $10\'dur. Bonus hesaplamasi icin maksimum tutar $1.500\'dir. $1.500 yatirmak maksimum $3.000 bonusa esittir.</p></div>
<div class="club-card"><h3>Adim 3 - Canli destek uzerinden talep edin</h3><p>Para yatirma islemini onayladiktan sonra Stake canli destek penceresini acin ve <span class="code-highlight">MAX3000</span> kodunu belirtin. Destek ekibi uygunlugunuzu dogrular ve 24-48 saat icinde 200%\'yi hesabiniza aktarir.</p></div>
<div class="club-card"><h3>40x Cevrim Sarti</h3><p>Cevrim sarti depozit ve bonus toplami uzerinden hesaplanir. Ornek: $500 depozit + $1.000 bonus = $1.500 x 40 = $60.000 bahis. Casino oyunlari %100, spor bahisleri %75 katkida bulunur.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Temel <span class="text-gradient-gold">kosullar</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Maksimum bonus</div><div class="ic-value">$3.000</div><div class="ic-detail">Ilk para yatirmanin 200%\'si. Bonus icin maksimum depozit: $1.500.</div></div>
<div class="intel-card"><div class="ic-label">Cevrim</div><div class="ic-value">40x</div><div class="ic-detail">Depozit+bonus uzerinden. Sure: bonus kreditlenmesinden itibaren 30 gun.</div></div>
<div class="intel-card"><div class="ic-label">Minimum depozit</div><div class="ic-value">$10</div><div class="ic-detail">USD veya kripto karsiligi.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Seviye 3</div><div class="ic-detail">Bonus kreditlenmesinden once zorunlu. Kimlik + adres + fon kaynagi.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('id','promo-code',
    'Kode Promo Stake MAX3000: 200% Hingga $3.000 (Juni 2026)',
    'Kode Stake MAX3000, deposit pertama 200%, hingga $3.000, rollover 40x deposit+bonus, KYC level 3 wajib. Kalkulator disertakan. Diverifikasi Juni 2026.',
    'Kode Promo Stake <span class="code-highlight">MAX3000</span><span class="h1-sub">Kode yang membuka brankas.</span>',
    'Kodenya adalah <span class="code-highlight">MAX3000</span>. Daftar, buat deposit pertama Anda antara $10 dan $1.000, klaim via live chat. <strong>200% hingga $3.000</strong>, rollover 40x, 30 hari.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Cara kerja <span class="text-gradient-gold">MAX3000</span></h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Langkah 1 - Daftar</h3><p>Gunakan tautan afiliasi untuk membuat akun di Stake.com. Selesaikan KYC level 3: foto dokumen identitas, bukti alamat, dan sumber dana. Tanpa KYC level 3, bonus tidak akan diaktifkan.</p></div>
<div class="club-card"><h3>Langkah 2 - Deposit antara $10 dan $1.500</h3><p>Deposit minimum untuk mengaktifkan bonus adalah $10. Maksimum yang dihitung untuk bonus adalah $1.500. Mendepositkan $1.500 sama dengan bonus maksimum $3.000.</p></div>
<div class="club-card"><h3>Langkah 3 - Klaim via live chat</h3><p>Buka live chat Stake setelah mengonfirmasi deposit Anda dan sebutkan kode <span class="code-highlight">MAX3000</span>. Tim dukungan memverifikasi kelayakan Anda dan mengkreditkan 200% dalam 24 hingga 48 jam.</p></div>
<div class="club-card"><h3>Rollover 40x</h3><p>Rollover berlaku untuk total deposit ditambah bonus. Contoh: $500 deposit + $1.000 bonus = $1.500 x 40 = $60.000 taruhan. Game kasino berkontribusi 100%, taruhan olahraga 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Syarat <span class="text-gradient-gold">utama</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Bonus maksimum</div><div class="ic-value">$3.000</div><div class="ic-detail">200% dari deposit pertama. Deposit maksimum yang dihitung: $1.500.</div></div>
<div class="intel-card"><div class="ic-label">Rollover</div><div class="ic-value">40x</div><div class="ic-detail">Atas deposit+bonus. Durasi: 30 hari sejak bonus dikreditkan.</div></div>
<div class="intel-card"><div class="ic-label">Deposit minimum</div><div class="ic-value">$10</div><div class="ic-detail">Dalam USD atau setara kripto.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Level 3</div><div class="ic-detail">Wajib sebelum bonus dikreditkan. Identitas + alamat + sumber dana.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('fr','promo-code',
    'Code Promo Stake MAX3000: 200% jusqu\'a 3 000$ (juin 2026)',
    'Code Stake MAX3000, premier depot 200%, jusqu\'a 3 000$, condition de mise 40x depot+bonus, KYC niveau 3 obligatoire. Calculateur inclus. Verifie juin 2026.',
    'Code Promo Stake <span class="code-highlight">MAX3000</span><span class="h1-sub">Le code qui ouvre le coffre.</span>',
    'Le code est <span class="code-highlight">MAX3000</span>. Inscrivez-vous, effectuez votre premier depot entre 10$ et 1 500$, reclamez via le chat en direct. <strong>200% jusqu\'a 3 000$</strong>, mise 40x, 30 jours.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Comment fonctionne <span class="text-gradient-gold">MAX3000</span></h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Etape 1 - S\'inscrire</h3><p>Utilisez le lien d\'affiliation pour creer votre compte sur Stake.com. Completez le KYC niveau 3: photo de la piece d\'identite, justificatif de domicile et origine des fonds. Sans KYC niveau 3, le bonus ne sera pas active.</p></div>
<div class="club-card"><h3>Etape 2 - Deposer entre 10$ et 1 500$</h3><p>Le depot minimum pour activer le bonus est de 10$. Le maximum pris en compte pour le calcul du bonus est de 1 500$. Un depot de 1 500$ correspond au bonus maximum de 3 000$.</p></div>
<div class="club-card"><h3>Etape 3 - Reclamer via le chat en direct</h3><p>Ouvrez le chat en direct de Stake apres avoir confirme votre depot et mentionnez le code <span class="code-highlight">MAX3000</span>. L\'equipe de support verifie votre eligibilite et credite les 200% sous 24 a 48 heures.</p></div>
<div class="club-card"><h3>Condition de mise 40x</h3><p>La condition de mise s\'applique au total depot plus bonus. Exemple: 500$ depot + 1 000$ bonus = 1 500$ x 40 = 60 000$ de mises. Les jeux de casino contribuent a 100%, les paris sportifs a 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Conditions <span class="text-gradient-gold">cles</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Bonus maximum</div><div class="ic-value">3 000$</div><div class="ic-detail">200% du premier depot. Depot maximum pris en compte: 1 500$.</div></div>
<div class="intel-card"><div class="ic-label">Condition de mise</div><div class="ic-value">40x</div><div class="ic-detail">Sur depot+bonus. Duree: 30 jours apres le credit du bonus.</div></div>
<div class="intel-card"><div class="ic-label">Depot minimum</div><div class="ic-value">10$</div><div class="ic-detail">En USD ou equivalent en crypto.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Niveau 3</div><div class="ic-detail">Obligatoire avant le credit du bonus. Identite + domicile + origine des fonds.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('ru','promo-code',
    'Промокод Stake MAX3000: 200% до $3000 (июнь 2026)',
    'Промокод Stake MAX3000, первый депозит 200%, до $3000, вейджер 40x депозит+бонус, KYC уровень 3 обязателен. Калькулятор включён. Проверено июнь 2026.',
    'Промокод Stake <span class="code-highlight">MAX3000</span><span class="h1-sub">Код, открывающий сейф.</span>',
    'Код: <span class="code-highlight">MAX3000</span>. Зарегистрируйтесь, внесите первый депозит от $10 до $1500, заявите через чат поддержки. <strong>200% до $3000</strong>, вейджер 40x, 30 дней.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Как работает <span class="text-gradient-gold">MAX3000</span></h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Шаг 1 - Регистрация</h3><p>Используйте партнёрскую ссылку для создания аккаунта на Stake.com. Пройдите KYC уровня 3: фото документа, подтверждение адреса, источник средств. Без KYC уровня 3 бонус не активируется.</p></div>
<div class="club-card"><h3>Шаг 2 - Депозит от $10 до $1500</h3><p>Минимальный депозит для активации бонуса: $10. Максимальный депозит, учитываемый при расчёте бонуса: $1500. Депозит $1500 даёт максимальный бонус $3000.</p></div>
<div class="club-card"><h3>Шаг 3 - Заявить через чат поддержки</h3><p>Откройте живой чат Stake после подтверждения депозита и укажите промокод <span class="code-highlight">MAX3000</span>. Команда поддержки проверяет право на участие и зачисляет 200% в течение 24-48 часов.</p></div>
<div class="club-card"><h3>Вейджер 40x</h3><p>Вейджер рассчитывается от суммы депозита и бонуса. Пример: $500 депозит + $1000 бонус = $1500 x 40 = $60000 ставок. Игры казино вносят 100%, спортивные ставки 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Ключевые <span class="text-gradient-gold">условия</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">Максимальный бонус</div><div class="ic-value">$3000</div><div class="ic-detail">200% от первого депозита. Максимальный депозит для расчёта: $1500.</div></div>
<div class="intel-card"><div class="ic-label">Вейджер</div><div class="ic-value">40x</div><div class="ic-detail">На депозит+бонус. Срок: 30 дней с момента начисления бонуса.</div></div>
<div class="intel-card"><div class="ic-label">Минимальный депозит</div><div class="ic-value">$10</div><div class="ic-detail">В USD или эквивалент в криптовалюте.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">Уровень 3</div><div class="ic-detail">Обязателен до начисления бонуса. Документ + адрес + источник средств.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)

sp('hi','promo-code',
    'Stake प्रोमो कोड MAX3000: 200% $3,000 तक (जून 2026)',
    'Stake MAX3000 कोड, पहला डिपॉजिट 200%, $3,000 तक, 40x वेजरिंग डिपॉजिट+बोनस, KYC लेवल 3 अनिवार्य. कैलकुलेटर शामिल. जून 2026 में वेरिफाइड.',
    'Stake प्रोमो कोड <span class="code-highlight">MAX3000</span><span class="h1-sub">तिजोरी खोलने वाला कोड.</span>',
    'कोड है <span class="code-highlight">MAX3000</span>. रजिस्टर करें, $10 से $1,500 के बीच पहला डिपॉजिट करें, लाइव चैट से क्लेम करें. <strong>200% $3,000 तक</strong>, वेजरिंग 40x, 30 दिन.',
    '''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">MAX3000</span> कैसे काम करता है</h2></div>
<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>चरण 1 - रजिस्टर करें</h3><p>Stake.com पर अकाउंट बनाने के लिए एफिलिएट लिंक का उपयोग करें. KYC लेवल 3 पूरा करें: ID फोटो, एड्रेस प्रूफ और फंड का स्रोत. KYC लेवल 3 के बिना बोनस एक्टिवेट नहीं होगा.</p></div>
<div class="club-card"><h3>चरण 2 - $10 से $1,500 के बीच डिपॉजिट करें</h3><p>बोनस एक्टिवेट करने के लिए न्यूनतम डिपॉजिट $10 है. बोनस गणना के लिए अधिकतम डिपॉजिट $1,500 है. $1,500 डिपॉजिट करने पर अधिकतम $3,000 बोनस मिलता है.</p></div>
<div class="club-card"><h3>चरण 3 - लाइव चैट से क्लेम करें</h3><p>डिपॉजिट कन्फर्म होने के बाद Stake का लाइव चैट खोलें और कोड <span class="code-highlight">MAX3000</span> बताएं. सपोर्ट टीम आपकी योग्यता वेरिफाई करती है और 24 से 48 घंटे में 200% क्रेडिट करती है.</p></div>
<div class="club-card"><h3>वेजरिंग 40x</h3><p>वेजरिंग डिपॉजिट और बोनस के कुल पर लागू होती है. उदाहरण: $500 डिपॉजिट + $1,000 बोनस = $1,500 x 40 = $60,000 बेट. कैसीनो गेम्स 100% योगदान देते हैं, स्पोर्ट्स बेटिंग 75%.</p></div>
</div></div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">मुख्य <span class="text-gradient-gold">शर्तें</span></h2></div>
<div class="intel-grid anim-stagger">
<div class="intel-card"><div class="ic-label">अधिकतम बोनस</div><div class="ic-value">$3,000</div><div class="ic-detail">पहले डिपॉजिट का 200%. अधिकतम योग्य डिपॉजिट: $1,500.</div></div>
<div class="intel-card"><div class="ic-label">वेजरिंग</div><div class="ic-value">40x</div><div class="ic-detail">डिपॉजिट+बोनस पर. अवधि: बोनस क्रेडिट होने से 30 दिन.</div></div>
<div class="intel-card"><div class="ic-label">न्यूनतम डिपॉजिट</div><div class="ic-value">$10</div><div class="ic-detail">USD या क्रिप्टो में समतुल्य.</div></div>
<div class="intel-card"><div class="ic-label">KYC</div><div class="ic-value">लेवल 3</div><div class="ic-detail">बोनस क्रेडिट से पहले अनिवार्य. ID + एड्रेस + फंड स्रोत.</div></div>
</div></div></section>''',
    '/images/og/promo-code.png'
)


# ── REMAINING SUB-PAGES (generic content per locale, all slugs) ───────────────
# For efficiency, define per-locale sub-page info as dicts keyed by slug

SUBPAGE_TITLES = {
    'es': {
        'about-stake': ('Quien opera Stake | Fundadores, Easygo, GGR $4.7B | WinnersClub', 'Stake.com informacion completa: Ed Craven y Bijan Tehrani, historia de Easygo, GGR $4.7B, reservas $339M, licencia Curacao. Codigo MAX3000 para 200% hasta $3,000.', 'Quien opera <span class="text-gradient-gold">Stake.com</span>', 'Todo lo que necesitas saber sobre Stake: sus fundadores, sus numeros y por que el codigo <span class="code-highlight">MAX3000</span> importa.'),
        'aviator': ('Stake Aviator | Guia, RTP y estrategia | MAX3000', 'Stake Aviator guia completa: como funciona el multiplicador, RTP 97%, retiro automatico, Provably Fair. Codigo MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Aviator</span>', 'El avion despega. Cobra antes de que se estrelle. Aviator de Stake con RTP 97% y verificacion Provably Fair. Empieza con el codigo <span class="code-highlight">MAX3000</span>.'),
        'casino': ('Stake Casino | 4,000+ slots, 18 originales | MAX3000', 'Guia completa del casino Stake: 18 originales con RTP verificado, 3,000-4,000 slots de 15+ proveedores, mesas en vivo Evolution, Stake Engine. MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Casino</span>', 'El casino de Stake tiene 18 originales con RTP verificado, miles de slots y mesas en vivo con crupiers reales. Entra con <span class="code-highlight">MAX3000</span>.'),
        'live-casino': ('Stake Casino en Vivo | Mesas Evolution, Blackjack, Ruleta | MAX3000', 'Casino en vivo de Stake: mesas Evolution, ruleta, blackjack, baccarat, game shows en vivo. MAX3000 para 200% hasta $3,000.', 'Stake Casino <span class="text-gradient-gold">en Vivo</span>', 'Crupier real. Accion en tiempo real. El casino en vivo de Stake con mesas Evolution. Entra con <span class="code-highlight">MAX3000</span>.'),
        'live-odds': ('Stake Cuotas en Vivo | Mercados en Tiempo Real | MAX3000', 'Cuotas en vivo de Stake: +30 deportes, mercados en tiempo real, transmision en vivo de Premier League, NBA, UFC. MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Cuotas en Vivo</span>', 'Cuotas en vivo de Stake para mas de 30 deportes. Actualización en tiempo real. Transmisiones incluidas. Empieza con <span class="code-highlight">MAX3000</span>.'),
        'mirror': ('Sitios Espejo Stake 2026 | Dominios que Funcionan | WinnersClub', 'Directorio completo de dominios espejo de Stake: stake.bet, stake.mba, stake.ac, staketr.com y mas. Por que existen los espejos, advertencias de phishing. Codigo MAX3000.', 'Sitios <span class="text-gradient-gold">Espejo</span> de Stake 2026', 'Stake opera bajo multiples dominios segun la region. Aqui encuentras los espejos oficiales verificados y las advertencias de phishing. Usa siempre <span class="code-highlight">MAX3000</span>.'),
        'news': ('Noticias Stake 2026 | Ultimas Novedades | WinnersClub', 'Las ultimas noticias de Stake.com: actualizaciones de plataforma, nuevos juegos, cambios de politica y eventos. Codigo MAX3000 para bonificacion de bienvenida.', 'Noticias <span class="text-gradient-gold">Stake</span>', 'Ultimas novedades de Stake.com. Actualizaciones de plataforma, nuevos juegos y eventos. Empieza con el codigo <span class="code-highlight">MAX3000</span>.'),
        'originals': ('Stake Originals | 18 Juegos Exclusivos RTP Verificado | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel y 12 mas. RTP verificado on-chain, Provably Fair. Codigo MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Originals</span>', 'Stake tiene 18 juegos originales con RTP verificado on-chain. Crash, Dice, Mines y mas. Empieza con <span class="code-highlight">MAX3000</span>.'),
        'payments': ('Pagos Stake | Cripto y Fiat, Retiros Rapidos | MAX3000', 'Metodos de pago en Stake: BTC, ETH, LTC, USDT, Doge y mas cripto. Fiat via MoonPay. Tiempos de retiro: 30-60 min cripto, 1-5 dias fiat. Codigo MAX3000.', 'Pagos <span class="text-gradient-gold">Stake</span>', 'Stake acepta mas de 20 criptomonedas y fiat via MoonPay. Retiros cripto: 30-60 minutos. Empieza con <span class="code-highlight">MAX3000</span>.'),
        'poker': ('Stake Poker | Texas Hold\'em, Torneos | MAX3000', 'Poker en Stake: Texas Hold\'em cash games, sit-and-go y torneos multimesa. Rakeback disponible. Codigo MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Poker</span>', 'Poker en Stake con Texas Hold\'em, torneos y rakeback. La accion no para. Entra con <span class="code-highlight">MAX3000</span>.'),
        'reserves': ('Reservas Stake On-Chain | $339M Verificados | WinnersClub', 'Reservas on-chain de Stake: $339.53M en wallets etiquetadas por Arkham al 28 mayo 2026. Ethereum 74%, Solana 14%. Verificado via cryptotips.com.', 'Reservas <span class="text-gradient-gold">On-Chain</span> de Stake', 'Stake tiene $339.53M en reservas verificadas on-chain. Ethereum 74%, Solana 14%. Auditables publicamente via Arkham. Codigo <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Juego Responsable | Herramientas y Recursos | Stake WinnersClub', 'Juego responsable en Stake: limites de deposito, autoexclusion, GamCare, Jugadores Anonimos. Herramientas de control. Codigo MAX3000 para bonificacion de bienvenida.', 'Juego <span class="text-gradient-gold">Responsable</span>', 'Stake ofrece herramientas de juego responsable: limites, autoexclusion y recursos de apoyo. Juega dentro de tus posibilidades.'),
        'slots': ('Slots en Stake | 3,000+ Juegos, Mejores RTP | MAX3000', 'Biblioteca de slots en Stake: 3,000-4,000 juegos de Pragmatic Play, Hacksaw, Push Gaming y mas. Mejores RTP, slots con jackpot. MAX3000 para 200% hasta $3,000.', 'Slots en <span class="text-gradient-gold">Stake</span>', 'Mas de 3,000 slots de los mejores proveedores del mundo. RTP verificados. Empieza con el codigo <span class="code-highlight">MAX3000</span>.'),
        'sports': ('Stake Deportes | 30+ Deportes, Streaming en Vivo | MAX3000', 'Sportsbook de Stake: +30 deportes, Premier League, NBA, UFC, CS2 con streaming en vivo, margen 3-4% en futbol principal. MAX3000 para 200% hasta $3,000.', 'Stake <span class="text-gradient-gold">Deportes</span>', 'Mas de 30 deportes con streaming en vivo. Margenes competitivos. El sportsbook de Stake. Empieza con <span class="code-highlight">MAX3000</span>.'),
        'stake-engine': ('Stake Engine | Plataforma Abierta para Estudios | MAX3000', 'Stake Engine: plataforma abierta a estudios externos desde abril 2025. Primer año $3.31B en volumen. Estructura, estudios incorporados y lo que significa para los jugadores.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine abre la plataforma a estudios externos. Ya genera el 10% del GGR. Lo que necesitas saber. Codigo <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Stake.us Bono MAX3000 | Sweepstakes EE.UU. | WinnersClub', 'Stake.us con codigo MAX3000: 560,000 Gold Coins + 56 Stake Cash + 3.5% rakeback. Plataforma sweepstakes para EE.UU. Operada por Sweepsteaks Limited.', 'Bono <span class="text-gradient-gold">Stake.us</span>', 'Stake.us para jugadores de EE.UU. Con el codigo <span class="code-highlight">MAX3000</span> obtienes Gold Coins, Stake Cash y rakeback. Sin deposito real necesario.'),
        'vip': ('VIP Stake | 16 Niveles, Bronze a Obsidian | MAX3000', 'VIP de Stake completo: desde Bronze ($10K apostado) hasta Obsidian ($1B). Rakeback por nivel, recargas, drops mensuales, host dedicado. Usa MAX3000 primero.', 'VIP <span class="text-gradient-gold">Stake</span>', 'El VIP de Stake tiene 16 niveles desde Bronze hasta Obsidian. Rakeback, recargas y host dedicado. Empieza con <span class="code-highlight">MAX3000</span>.'),
    },
    'pt-br': {
        'about-stake': ('Quem opera o Stake | Fundadores, Easygo, GGR $4.7B | WinnersClub', 'Stake.com informacoes completas: Ed Craven e Bijan Tehrani, historia da Easygo, GGR $4.7B, reservas $339M, licenca Curacao. Codigo MAX3000 para 200% ate $3.000.', 'Quem opera o <span class="text-gradient-gold">Stake.com</span>', 'Tudo que voce precisa saber sobre o Stake: seus fundadores, seus numeros e por que o codigo <span class="code-highlight">MAX3000</span> importa.'),
        'aviator': ('Stake Aviator | Guia, RTP e estrategia | MAX3000', 'Guia completo do Stake Aviator: como funciona o multiplicador, RTP 97%, retirada automatica, Provably Fair. Codigo MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Aviator</span>', 'O aviao decola. Retire antes de cair. Aviator do Stake com RTP 97% e verificacao Provably Fair. Comece com o codigo <span class="code-highlight">MAX3000</span>.'),
        'casino': ('Stake Cassino | 4.000+ slots, 18 originais | MAX3000', 'Guia completo do cassino Stake: 18 originais com RTP verificado, 3.000-4.000 slots de 15+ provedores, mesas ao vivo Evolution. MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Cassino</span>', 'O cassino do Stake tem 18 originais com RTP verificado, milhares de slots e mesas ao vivo com crupieres reais. Entre com <span class="code-highlight">MAX3000</span>.'),
        'live-casino': ('Stake Cassino ao Vivo | Mesas Evolution, Blackjack, Roleta | MAX3000', 'Cassino ao vivo do Stake: mesas Evolution, roleta, blackjack, bacara, game shows ao vivo. MAX3000 para 200% ate $3.000.', 'Stake Cassino <span class="text-gradient-gold">ao Vivo</span>', 'Crupier real. Acao em tempo real. O cassino ao vivo do Stake com mesas Evolution. Entre com <span class="code-highlight">MAX3000</span>.'),
        'live-odds': ('Stake Odds ao Vivo | Mercados em Tempo Real | MAX3000', 'Odds ao vivo do Stake: +30 esportes, mercados em tempo real, transmissao ao vivo de Premier League, NBA, UFC. MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Odds ao Vivo</span>', 'Odds ao vivo do Stake para mais de 30 esportes. Atualizacao em tempo real. Transmissoes incluidas. Comece com <span class="code-highlight">MAX3000</span>.'),
        'mirror': ('Sitios Espelho Stake 2026 | Dominios que Funcionam | WinnersClub', 'Diretorio completo de dominios espelho do Stake: stake.bet, stake.mba, stake.ac, staketr.com e mais. Por que existem os espelhos, avisos de phishing. Codigo MAX3000.', 'Sitios <span class="text-gradient-gold">Espelho</span> do Stake 2026', 'O Stake opera sob varios dominios conforme a regiao. Aqui voce encontra os espelhos oficiais verificados e alertas de phishing. Use sempre <span class="code-highlight">MAX3000</span>.'),
        'news': ('Noticias Stake 2026 | Ultimas Novidades | WinnersClub', 'As ultimas noticias do Stake.com: atualizacoes de plataforma, novos jogos, mudancas de politica e eventos. Codigo MAX3000 para bonus de boas-vindas.', 'Noticias <span class="text-gradient-gold">Stake</span>', 'Ultimas novidades do Stake.com. Atualizacoes de plataforma, novos jogos e eventos. Comece com o codigo <span class="code-highlight">MAX3000</span>.'),
        'originals': ('Stake Originals | 18 Jogos Exclusivos RTP Verificado | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel e 12 mais. RTP verificado on-chain, Provably Fair. Codigo MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Originals</span>', 'O Stake tem 18 jogos originais com RTP verificado on-chain. Crash, Dice, Mines e mais. Comece com <span class="code-highlight">MAX3000</span>.'),
        'payments': ('Pagamentos Stake | Cripto e Fiat, Saques Rapidos | MAX3000', 'Metodos de pagamento no Stake: BTC, ETH, LTC, USDT, Doge e mais cripto. Fiat via MoonPay. Tempos de saque: 30-60 min cripto, 1-5 dias fiat. Codigo MAX3000.', 'Pagamentos <span class="text-gradient-gold">Stake</span>', 'O Stake aceita mais de 20 criptomoedas e fiat via MoonPay. Saques cripto: 30-60 minutos. Comece com <span class="code-highlight">MAX3000</span>.'),
        'poker': ('Stake Poker | Texas Hold\'em, Torneios | MAX3000', 'Poker no Stake: Texas Hold\'em cash games, sit-and-go e torneios multimesa. Rakeback disponivel. Codigo MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Poker</span>', 'Poker no Stake com Texas Hold\'em, torneios e rakeback. A acao nao para. Entre com <span class="code-highlight">MAX3000</span>.'),
        'reserves': ('Reservas Stake On-Chain | $339M Verificados | WinnersClub', 'Reservas on-chain do Stake: $339.53M em carteiras rotuladas pela Arkham em 28 maio 2026. Ethereum 74%, Solana 14%. Verificado via cryptotips.com.', 'Reservas <span class="text-gradient-gold">On-Chain</span> do Stake', 'O Stake tem $339.53M em reservas verificadas on-chain. Ethereum 74%, Solana 14%. Auditaveis publicamente via Arkham. Codigo <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Jogo Responsavel | Ferramentas e Recursos | Stake WinnersClub', 'Jogo responsavel no Stake: limites de deposito, autoexclusao, GamCare, Jogadores Anonimos. Ferramentas de controle. Codigo MAX3000 para bonus de boas-vindas.', 'Jogo <span class="text-gradient-gold">Responsavel</span>', 'O Stake oferece ferramentas de jogo responsavel: limites, autoexclusao e recursos de apoio. Jogue dentro de suas possibilidades.'),
        'slots': ('Slots no Stake | 3.000+ Jogos, Melhores RTP | MAX3000', 'Biblioteca de slots no Stake: 3.000-4.000 jogos da Pragmatic Play, Hacksaw, Push Gaming e mais. Melhores RTP, slots com jackpot. MAX3000 para 200% ate $3.000.', 'Slots no <span class="text-gradient-gold">Stake</span>', 'Mais de 3.000 slots dos melhores provedores do mundo. RTP verificados. Comece com o codigo <span class="code-highlight">MAX3000</span>.'),
        'sports': ('Stake Esportes | 30+ Esportes, Streaming ao Vivo | MAX3000', 'Sportsbook do Stake: +30 esportes, Premier League, NBA, UFC, CS2 com streaming ao vivo, margem 3-4% no futebol principal. MAX3000 para 200% ate $3.000.', 'Stake <span class="text-gradient-gold">Esportes</span>', 'Mais de 30 esportes com streaming ao vivo. Margens competitivas. O sportsbook do Stake. Comece com <span class="code-highlight">MAX3000</span>.'),
        'stake-engine': ('Stake Engine | Plataforma Aberta para Estudios | MAX3000', 'Stake Engine: plataforma aberta a estudios externos desde abril 2025. Primeiro ano $3.31B em volume. Estrutura, estudios incorporados e o que significa para os jogadores.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine abre a plataforma para estudios externos. Ja gera 10% do GGR. O que voce precisa saber. Codigo <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Stake.us Bonus MAX3000 | Sweepstakes EUA | WinnersClub', 'Stake.us com codigo MAX3000: 560.000 Gold Coins + 56 Stake Cash + 3.5% rakeback. Plataforma sweepstakes para os EUA. Operada pela Sweepsteaks Limited.', 'Bonus <span class="text-gradient-gold">Stake.us</span>', 'Stake.us para jogadores dos EUA. Com o codigo <span class="code-highlight">MAX3000</span> voce ganha Gold Coins, Stake Cash e rakeback. Sem deposito real necessario.'),
        'vip': ('VIP Stake | 16 Niveis, Bronze a Obsidian | MAX3000', 'VIP do Stake completo: de Bronze ($10K apostado) ate Obsidian ($1B). Rakeback por nivel, recargas, drops mensais, host dedicado. Use MAX3000 primeiro.', 'VIP <span class="text-gradient-gold">Stake</span>', 'O VIP do Stake tem 16 niveis de Bronze a Obsidian. Rakeback, recargas e host dedicado. Comece com <span class="code-highlight">MAX3000</span>.'),
    },
    'tr': {
        'about-stake': ('Stake\'i Kim Isletiyor | Kurucular, Easygo, GGR $4.7B | WinnersClub', 'Stake.com tam bilgi: Ed Craven ve Bijan Tehrani, Easygo gecmisi, GGR $4.7B, rezervler $339M, Curacao lisansi. Kod MAX3000 ile $3.000\'e kadar 200%.', 'Stake.com\'u Kim <span class="text-gradient-gold">Isletiyor</span>', 'Stake hakkinda bilmeniz gereken her sey: kurucular, rakamlar ve <span class="code-highlight">MAX3000</span> kodunun neden onemli oldugu.'),
        'aviator': ('Stake Aviator | Rehber, RTP ve Strateji | MAX3000', 'Stake Aviator tam rehberi: carpan nasil calisir, RTP %97, otomatik cekim, Provably Fair. MAX3000 kodu ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Aviator</span>', 'Ucak kaldirilıyor. Dusmeden once nakit cekin. RTP %97 ve Provably Fair dogrulamali Stake Aviator. <span class="code-highlight">MAX3000</span> koduyla baslayin.'),
        'casino': ('Stake Casino | 4.000+ Slot, 18 Original | MAX3000', 'Stake casino tam rehberi: dogrulanmis RTP\'li 18 original, 15+ saglaricidan 3.000-4.000 slot, Evolution canli masalar. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Casino</span>', 'Stake casinosunda dogrulanmis RTP\'li 18 original, binlerce slot ve gercek krupiyeli canli masalar var. <span class="code-highlight">MAX3000</span> ile giris yapin.'),
        'live-casino': ('Stake Canli Casino | Evolution Masalar, Blackjack, Rulet | MAX3000', 'Stake canli casino: Evolution masalar, rulet, blackjack, bakara, canli oyun sovalari. MAX3000 ile $3.000\'e kadar 200%.', 'Stake Canli <span class="text-gradient-gold">Casino</span>', 'Gercek krupiye. Gercek zamanli aksiyon. Evolution masaliStake canli casino. <span class="code-highlight">MAX3000</span> ile giris yapin.'),
        'live-odds': ('Stake Canli Oranlar | Gercek Zamanli Marketler | MAX3000', 'Stake canli oranlar: 30+ spor, gercek zamanli marketler, Premier League, NBA, UFC canli yayin. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Canli Oranlar</span>', '30\'dan fazla spor icin Stake canli oranlar. Gercek zamanli guncelleme. Canli yayin dahil. <span class="code-highlight">MAX3000</span> ile baslayin.'),
        'mirror': ('Stake Ayna Siteler 2026 | Calisan Alanlar | WinnersClub', 'Stake ayna domain rehberi: stake.bet, stake.mba, stake.ac, staketr.com ve daha fazlasi. Neden aynalar var, phishing uyarilari. Kod MAX3000.', 'Stake 2026 <span class="text-gradient-gold">Ayna Siteler</span>', 'Stake bolgeden bageye birden fazla domain altinda calisir. Resmi dogrulanmis aynalari ve phishing uyarilarini burada bulabilirsiniz. Her zaman <span class="code-highlight">MAX3000</span> kullanin.'),
        'news': ('Stake Haberleri 2026 | Son Gelismeler | WinnersClub', 'Stake.com son haberleri: platform guncellemeleri, yeni oyunlar, politika degisiklikleri ve etkinlikler. Hosgeldin bonusu icin MAX3000 kodu.', 'Stake <span class="text-gradient-gold">Haberleri</span>', 'Stake.com son gelismeleri. Platform guncellemeleri, yeni oyunlar ve etkinlikler. <span class="code-highlight">MAX3000</span> koduyla baslayin.'),
        'originals': ('Stake Originals | 18 Ozel Oyun Dogrulanmis RTP | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel ve 12 daha. On-chain dogrulanmis RTP, Provably Fair. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Originals</span>', 'Stake\'in on-chain dogrulanmis RTP\'li 18 ozel oyunu var. Crash, Dice, Mines ve daha fazlasi. <span class="code-highlight">MAX3000</span> ile baslayin.'),
        'payments': ('Stake Odemeler | Kripto ve Fiat, Hizli Cekim | MAX3000', 'Stake\'te odeme yontemleri: BTC, ETH, LTC, USDT, Doge ve daha fazla kripto. MoonPay ile fiat. Cekim sureleri: kripto 30-60 dk, fiat 1-5 gun. Kod MAX3000.', 'Stake <span class="text-gradient-gold">Odemeler</span>', 'Stake 20\'den fazla kripto ve MoonPay uzerinden fiat kabul ediyor. Kripto cekim: 30-60 dakika. <span class="code-highlight">MAX3000</span> ile baslayin.'),
        'poker': ('Stake Poker | Texas Hold\'em, Turnuvalar | MAX3000', 'Stake\'te poker: Texas Hold\'em cash games, sit-and-go ve cok masali turnuvalar. Rakeback mevcut. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Poker</span>', 'Stake\'te Texas Hold\'em, turnuvalar ve rakeback. Aksiyon durmuyor. <span class="code-highlight">MAX3000</span> ile giris yapin.'),
        'reserves': ('Stake On-Chain Rezervler | $339M Dogrulandi | WinnersClub', 'Stake on-chain rezervleri: 28 Mayis 2026 itibariyla Arkham etiketli cuzdanlarda $339.53M. Ethereum %74, Solana %14. cryptotips.com uzerinden dogrulandi.', 'Stake <span class="text-gradient-gold">On-Chain Rezervler</span>', 'Stake\'in $339.53M dogrulanmis on-chain rezervi var. Ethereum %74, Solana %14. Arkham uzerinden kamuya acik denetlenebilir. Kod <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Sorumlu Kumar | Araclar ve Kaynaklar | Stake WinnersClub', 'Stake\'te sorumlu kumar: yatirim limitleri, oz-hariclestirme, GamCare, Anonim Kumarbazlar. Kontrol araclari. Hosgeldin bonusu icin MAX3000.', 'Sorumlu <span class="text-gradient-gold">Kumar</span>', 'Stake sorumlu kumar araclari sunuyor: limitler, oz-hariclestirme ve destek kaynaklari. Imkanlariniz dahilinde oynayın.'),
        'slots': ('Stake Slotlar | 3.000+ Oyun, En Iyi RTP | MAX3000', 'Stake slot kutuphanesi: Pragmatic Play, Hacksaw, Push Gaming ve daha fazlasindan 3.000-4.000 oyun. En iyi RTP, jackpot slotlari. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Slotlar</span>', 'Dunyanin en iyi saglaricilarin 3.000\'den fazla slotu. Dogrulanmis RTP. <span class="code-highlight">MAX3000</span> koduyla baslayin.'),
        'sports': ('Stake Spor | 30+ Spor, Canli Yayin | MAX3000', 'Stake sportsbook: 30+ spor, Premier League, NBA, UFC, CS2 canli yayin, ana futbolda %3-4 marj. MAX3000 ile $3.000\'e kadar 200%.', 'Stake <span class="text-gradient-gold">Spor</span>', 'Canli yayin ile 30\'dan fazla spor. Rekabetci marjlar. Stake sportsbook. <span class="code-highlight">MAX3000</span> ile baslayin.'),
        'stake-engine': ('Stake Engine | Stüdyolar Icin Acik Platform | MAX3000', 'Stake Engine: Nisan 2025\'ten itibaren dis stüdyolara acilan oyun platformu. Ilk yil $3.31B hacim. Yapi, entegre stüdyolar ve oyunculara etkisi.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine platformu dis stüdyolara aciyor. Zaten GGR\'in %10\'unu uреtiyor. Bilmeniz gerekenler. Kod <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Stake.us Bonusu MAX3000 | Sweepstakes ABD | WinnersClub', 'Stake.us kod MAX3000 ile: 560.000 Gold Coin + 56 Stake Cash + %3.5 rakeback. ABD sweepstakes platformu. Sweepsteaks Limited tarafindan isletilir.', 'Stake.us <span class="text-gradient-gold">Bonusu</span>', 'ABD\'li oyuncular icin Stake.us. <span class="code-highlight">MAX3000</span> koduyla Gold Coin, Stake Cash ve rakeback kazanin. Gercek para yatırımı gerekmez.'),
        'vip': ('Stake VIP | 16 Seviye, Bronze\'dan Obsidian\'a | MAX3000', 'Stake VIP tam aciklamasi: Bronze ($10K bahis)\'ten Obsidian ($1B)\'a 16 seviye. Seviyeye gore rakeback, yenileme bonuslari, aylik droplar, ozel host. Once MAX3000\'i kullanin.', 'Stake <span class="text-gradient-gold">VIP</span>', 'Stake VIP programinin Bronze\'dan Obsidian\'a 16 seviyesi var. Rakeback, yenileme ve ozel host. <span class="code-highlight">MAX3000</span> ile baslayin.'),
    },
    'id': {
        'about-stake': ('Siapa yang Mengoperasikan Stake | Pendiri, Easygo, GGR $4.7B | WinnersClub', 'Stake.com informasi lengkap: Ed Craven dan Bijan Tehrani, sejarah Easygo, GGR $4.7B, cadangan $339M, lisensi Curacao. Kode MAX3000 untuk 200% hingga $3.000.', 'Siapa yang Mengoperasikan <span class="text-gradient-gold">Stake.com</span>', 'Semua yang perlu Anda ketahui tentang Stake: pendirinya, angkanya, dan mengapa kode <span class="code-highlight">MAX3000</span> penting.'),
        'aviator': ('Stake Aviator | Panduan, RTP dan Strategi | MAX3000', 'Panduan lengkap Stake Aviator: cara kerja pengganda, RTP 97%, penarikan otomatis, Provably Fair. Kode MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Aviator</span>', 'Pesawat lepas landas. Tarik sebelum jatuh. Aviator Stake dengan RTP 97% dan verifikasi Provably Fair. Mulai dengan kode <span class="code-highlight">MAX3000</span>.'),
        'casino': ('Stake Kasino | 4.000+ Slot, 18 Original | MAX3000', 'Panduan lengkap kasino Stake: 18 original dengan RTP terverifikasi, 3.000-4.000 slot dari 15+ penyedia, meja live Evolution. MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Kasino</span>', 'Kasino Stake memiliki 18 original dengan RTP terverifikasi, ribuan slot, dan meja live dengan dealer nyata. Masuk dengan <span class="code-highlight">MAX3000</span>.'),
        'live-casino': ('Stake Kasino Live | Meja Evolution, Blackjack, Roulette | MAX3000', 'Kasino live Stake: meja Evolution, roulette, blackjack, baccarat, game show live. MAX3000 untuk 200% hingga $3.000.', 'Stake Kasino <span class="text-gradient-gold">Live</span>', 'Dealer nyata. Aksi real-time. Kasino live Stake dengan meja Evolution. Masuk dengan <span class="code-highlight">MAX3000</span>.'),
        'live-odds': ('Stake Odds Live | Pasar Real-Time | MAX3000', 'Odds live Stake: 30+ olahraga, pasar real-time, siaran langsung Premier League, NBA, UFC. MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Odds Live</span>', 'Odds live Stake untuk lebih dari 30 olahraga. Pembaruan real-time. Siaran langsung disertakan. Mulai dengan <span class="code-highlight">MAX3000</span>.'),
        'mirror': ('Situs Mirror Stake 2026 | Domain yang Berfungsi | WinnersClub', 'Direktori lengkap domain mirror Stake: stake.bet, stake.mba, stake.ac, staketr.com dan lainnya. Mengapa mirror ada, peringatan phishing. Kode MAX3000.', 'Situs <span class="text-gradient-gold">Mirror</span> Stake 2026', 'Stake beroperasi di bawah beberapa domain tergantung wilayah. Di sini Anda menemukan mirror resmi terverifikasi dan peringatan phishing. Selalu gunakan <span class="code-highlight">MAX3000</span>.'),
        'news': ('Berita Stake 2026 | Update Terbaru | WinnersClub', 'Berita terbaru Stake.com: pembaruan platform, game baru, perubahan kebijakan dan acara. Kode MAX3000 untuk bonus sambutan.', 'Berita <span class="text-gradient-gold">Stake</span>', 'Update terbaru Stake.com. Pembaruan platform, game baru dan acara. Mulai dengan kode <span class="code-highlight">MAX3000</span>.'),
        'originals': ('Stake Originals | 18 Game Eksklusif RTP Terverifikasi | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel dan 12 lainnya. RTP terverifikasi on-chain, Provably Fair. Kode MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Originals</span>', 'Stake memiliki 18 game original dengan RTP terverifikasi on-chain. Crash, Dice, Mines dan lainnya. Mulai dengan <span class="code-highlight">MAX3000</span>.'),
        'payments': ('Pembayaran Stake | Kripto dan Fiat, Penarikan Cepat | MAX3000', 'Metode pembayaran di Stake: BTC, ETH, LTC, USDT, Doge dan lebih banyak kripto. Fiat via MoonPay. Waktu penarikan: kripto 30-60 mnt, fiat 1-5 hari. Kode MAX3000.', 'Pembayaran <span class="text-gradient-gold">Stake</span>', 'Stake menerima lebih dari 20 kripto dan fiat via MoonPay. Penarikan kripto: 30-60 menit. Mulai dengan <span class="code-highlight">MAX3000</span>.'),
        'poker': ('Stake Poker | Texas Hold\'em, Turnamen | MAX3000', 'Poker di Stake: Texas Hold\'em cash games, sit-and-go dan turnamen multi-meja. Rakeback tersedia. Kode MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Poker</span>', 'Poker di Stake dengan Texas Hold\'em, turnamen dan rakeback. Aksi tidak berhenti. Masuk dengan <span class="code-highlight">MAX3000</span>.'),
        'reserves': ('Cadangan On-Chain Stake | $339M Terverifikasi | WinnersClub', 'Cadangan on-chain Stake: $339.53M di dompet berlabel Arkham per 28 Mei 2026. Ethereum 74%, Solana 14%. Diverifikasi via cryptotips.com.', 'Cadangan <span class="text-gradient-gold">On-Chain</span> Stake', 'Stake memiliki $339.53M cadangan terverifikasi on-chain. Ethereum 74%, Solana 14%. Dapat diaudit publik via Arkham. Kode <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Judi Bertanggung Jawab | Alat dan Sumber Daya | Stake WinnersClub', 'Judi bertanggung jawab di Stake: batas deposit, pengecualian diri, GamCare, Gamblers Anonymous. Alat kontrol. Kode MAX3000 untuk bonus sambutan.', 'Judi Bertanggung <span class="text-gradient-gold">Jawab</span>', 'Stake menawarkan alat judi bertanggung jawab: batas, pengecualian diri dan sumber dukungan. Bermainlah sesuai kemampuan Anda.'),
        'slots': ('Slot di Stake | 3.000+ Game, RTP Terbaik | MAX3000', 'Perpustakaan slot di Stake: 3.000-4.000 game dari Pragmatic Play, Hacksaw, Push Gaming dan lainnya. RTP terbaik, slot jackpot. MAX3000 untuk 200% hingga $3.000.', 'Slot di <span class="text-gradient-gold">Stake</span>', 'Lebih dari 3.000 slot dari penyedia terbaik dunia. RTP terverifikasi. Mulai dengan kode <span class="code-highlight">MAX3000</span>.'),
        'sports': ('Stake Olahraga | 30+ Olahraga, Streaming Live | MAX3000', 'Sportsbook Stake: 30+ olahraga, Premier League, NBA, UFC, CS2 dengan streaming live, margin 3-4% di sepak bola utama. MAX3000 untuk 200% hingga $3.000.', 'Stake <span class="text-gradient-gold">Olahraga</span>', 'Lebih dari 30 olahraga dengan streaming live. Margin kompetitif. Sportsbook Stake. Mulai dengan <span class="code-highlight">MAX3000</span>.'),
        'stake-engine': ('Stake Engine | Platform Terbuka untuk Studio | MAX3000', 'Stake Engine: platform terbuka untuk studio eksternal sejak April 2025. Tahun pertama $3.31B volume. Struktur, studio terintegrasi dan artinya bagi pemain.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine membuka platform untuk studio eksternal. Sudah menghasilkan 10% dari GGR. Yang perlu Anda ketahui. Kode <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Bonus Stake.us MAX3000 | Sweepstakes AS | WinnersClub', 'Stake.us dengan kode MAX3000: 560.000 Gold Coin + 56 Stake Cash + 3.5% rakeback. Platform sweepstakes untuk AS. Dioperasikan oleh Sweepsteaks Limited.', 'Bonus <span class="text-gradient-gold">Stake.us</span>', 'Stake.us untuk pemain AS. Dengan kode <span class="code-highlight">MAX3000</span> Anda mendapatkan Gold Coin, Stake Cash dan rakeback. Tanpa deposit nyata diperlukan.'),
        'vip': ('VIP Stake | 16 Level, Bronze ke Obsidian | MAX3000', 'VIP Stake lengkap: dari Bronze ($10K taruhan) hingga Obsidian ($1B). Rakeback per level, isi ulang, drop bulanan, host khusus. Gunakan MAX3000 terlebih dahulu.', 'VIP <span class="text-gradient-gold">Stake</span>', 'VIP Stake memiliki 16 level dari Bronze hingga Obsidian. Rakeback, isi ulang dan host khusus. Mulai dengan <span class="code-highlight">MAX3000</span>.'),
    },
    'fr': {
        'about-stake': ('Qui exploite Stake | Fondateurs, Easygo, GGR 4,7Md$ | WinnersClub', 'Stake.com informations completes: Ed Craven et Bijan Tehrani, histoire Easygo, GGR 4,7Md$, reserves 339M$, licence Curacao. Code MAX3000 pour 200% jusqu\'a 3 000$.', 'Qui exploite <span class="text-gradient-gold">Stake.com</span>', 'Tout ce que vous devez savoir sur Stake: ses fondateurs, ses chiffres et pourquoi le code <span class="code-highlight">MAX3000</span> est important.'),
        'aviator': ('Stake Aviator | Guide, RTP et strategie | MAX3000', 'Guide complet Stake Aviator: fonctionnement du multiplicateur, RTP 97%, retrait automatique, Provably Fair. Code MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Aviator</span>', 'L\'avion decolle. Retirez avant qu\'il s\'ecrase. Aviator de Stake avec RTP 97% et verification Provably Fair. Commencez avec le code <span class="code-highlight">MAX3000</span>.'),
        'casino': ('Stake Casino | 4 000+ machines a sous, 18 originaux | MAX3000', 'Guide complet casino Stake: 18 originaux avec RTP verifie, 3 000-4 000 machines a sous de 15+ fournisseurs, tables live Evolution. MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Casino</span>', 'Le casino de Stake compte 18 originaux avec RTP verifie, des milliers de machines a sous et des tables live avec vrais croupiers. Entrez avec <span class="code-highlight">MAX3000</span>.'),
        'live-casino': ('Stake Casino en Direct | Tables Evolution, Blackjack, Roulette | MAX3000', 'Casino en direct Stake: tables Evolution, roulette, blackjack, baccarat, jeux en direct. MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake Casino <span class="text-gradient-gold">en Direct</span>', 'Vrai croupier. Action en temps reel. Le casino en direct de Stake avec tables Evolution. Entrez avec <span class="code-highlight">MAX3000</span>.'),
        'live-odds': ('Stake Cotes en Direct | Marches en Temps Reel | MAX3000', 'Cotes en direct Stake: 30+ sports, marches en temps reel, diffusion en direct Premier League, NBA, UFC. MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Cotes en Direct</span>', 'Cotes en direct de Stake pour plus de 30 sports. Mise a jour en temps reel. Diffusions incluses. Commencez avec <span class="code-highlight">MAX3000</span>.'),
        'mirror': ('Sites Miroir Stake 2026 | Domaines qui Fonctionnent | WinnersClub', 'Repertoire complet des domaines miroir Stake: stake.bet, stake.mba, stake.ac, staketr.com et plus. Pourquoi les miroirs existent, avertissements phishing. Code MAX3000.', 'Sites <span class="text-gradient-gold">Miroir</span> Stake 2026', 'Stake opere sous plusieurs domaines selon la region. Ici vous trouvez les miroirs officiels verifies et les avertissements phishing. Utilisez toujours <span class="code-highlight">MAX3000</span>.'),
        'news': ('Actualites Stake 2026 | Dernieres Nouvelles | WinnersClub', 'Dernieres actualites Stake.com: mises a jour de la plateforme, nouveaux jeux, changements de politique et evenements. Code MAX3000 pour le bonus de bienvenue.', 'Actualites <span class="text-gradient-gold">Stake</span>', 'Dernieres nouvelles de Stake.com. Mises a jour de la plateforme, nouveaux jeux et evenements. Commencez avec le code <span class="code-highlight">MAX3000</span>.'),
        'originals': ('Stake Originals | 18 Jeux Exclusifs RTP Verifie | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel et 12 autres. RTP verifie on-chain, Provably Fair. Code MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Originals</span>', 'Stake compte 18 jeux originaux avec RTP verifie on-chain. Crash, Dice, Mines et plus. Commencez avec <span class="code-highlight">MAX3000</span>.'),
        'payments': ('Paiements Stake | Crypto et Fiat, Retraits Rapides | MAX3000', 'Methodes de paiement chez Stake: BTC, ETH, LTC, USDT, Doge et plus de crypto. Fiat via MoonPay. Delais de retrait: crypto 30-60 min, fiat 1-5 jours. Code MAX3000.', 'Paiements <span class="text-gradient-gold">Stake</span>', 'Stake accepte plus de 20 cryptos et le fiat via MoonPay. Retraits crypto: 30-60 minutes. Commencez avec <span class="code-highlight">MAX3000</span>.'),
        'poker': ('Stake Poker | Texas Hold\'em, Tournois | MAX3000', 'Poker chez Stake: Texas Hold\'em cash games, sit-and-go et tournois multi-tables. Rakeback disponible. Code MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Poker</span>', 'Poker chez Stake avec Texas Hold\'em, tournois et rakeback. L\'action ne s\'arrete pas. Entrez avec <span class="code-highlight">MAX3000</span>.'),
        'reserves': ('Reserves On-Chain Stake | 339M$ Verifies | WinnersClub', 'Reserves on-chain de Stake: 339,53M$ dans des portefeuilles labelises par Arkham au 28 mai 2026. Ethereum 74%, Solana 14%. Verifie via cryptotips.com.', 'Reserves <span class="text-gradient-gold">On-Chain</span> de Stake', 'Stake dispose de 339,53M$ de reserves verifiees on-chain. Ethereum 74%, Solana 14%. Auditables publiquement via Arkham. Code <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Jeu Responsable | Outils et Ressources | Stake WinnersClub', 'Jeu responsable chez Stake: limites de depot, auto-exclusion, GamCare, Joueurs Anonymes. Outils de controle. Code MAX3000 pour le bonus de bienvenue.', 'Jeu <span class="text-gradient-gold">Responsable</span>', 'Stake propose des outils de jeu responsable: limites, auto-exclusion et ressources de soutien. Jouez dans vos limites.'),
        'slots': ('Machines a Sous Stake | 3 000+ Jeux, Meilleurs RTP | MAX3000', 'Bibliotheque de machines a sous Stake: 3 000-4 000 jeux de Pragmatic Play, Hacksaw, Push Gaming et plus. Meilleurs RTP, slots jackpot. MAX3000 pour 200% jusqu\'a 3 000$.', 'Machines a Sous <span class="text-gradient-gold">Stake</span>', 'Plus de 3 000 machines a sous des meilleurs fournisseurs mondiaux. RTP verifies. Commencez avec le code <span class="code-highlight">MAX3000</span>.'),
        'sports': ('Stake Sports | 30+ Sports, Streaming en Direct | MAX3000', 'Sportsbook Stake: 30+ sports, Premier League, NBA, UFC, CS2 avec streaming en direct, marge 3-4% sur le football principal. MAX3000 pour 200% jusqu\'a 3 000$.', 'Stake <span class="text-gradient-gold">Sports</span>', 'Plus de 30 sports avec streaming en direct. Marges competitives. Le sportsbook de Stake. Commencez avec <span class="code-highlight">MAX3000</span>.'),
        'stake-engine': ('Stake Engine | Plateforme Ouverte aux Studios | MAX3000', 'Stake Engine: plateforme ouverte aux studios externes depuis avril 2025. Premiere annee 3,31Md$ de volume. Structure, studios integres et ce que cela signifie pour les joueurs.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine ouvre la plateforme aux studios externes. Genere deja 10% du GGR. Ce que vous devez savoir. Code <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Bonus Stake.us MAX3000 | Sweepstakes USA | WinnersClub', 'Stake.us avec code MAX3000: 560 000 Gold Coins + 56 Stake Cash + 3,5% rakeback. Plateforme sweepstakes pour les USA. Exploitee par Sweepsteaks Limited.', 'Bonus <span class="text-gradient-gold">Stake.us</span>', 'Stake.us pour les joueurs americains. Avec le code <span class="code-highlight">MAX3000</span> vous gagnez Gold Coins, Stake Cash et rakeback. Sans depot reel necessaire.'),
        'vip': ('VIP Stake | 16 Niveaux, Bronze a Obsidian | MAX3000', 'VIP Stake complet: de Bronze (10 000$ mise) a Obsidian (1Md$). Rakeback par niveau, recharges, drops mensuels, hote dedie. Utilisez d\'abord MAX3000.', 'VIP <span class="text-gradient-gold">Stake</span>', 'Le VIP de Stake compte 16 niveaux de Bronze a Obsidian. Rakeback, recharges et hote dedie. Commencez avec <span class="code-highlight">MAX3000</span>.'),
    },
    'ru': {
        'about-stake': ('Кто управляет Stake | Основатели, Easygo, GGR $4.7B | WinnersClub', 'Stake.com полная информация: Ed Craven и Bijan Tehrani, история Easygo, GGR $4.7B, резервы $339M, лицензия Curacao. Промокод MAX3000 для 200% до $3000.', 'Кто управляет <span class="text-gradient-gold">Stake.com</span>', 'Всё, что нужно знать о Stake: основатели, цифры и почему промокод <span class="code-highlight">MAX3000</span> важен.'),
        'aviator': ('Stake Aviator | Гайд, RTP и стратегия | MAX3000', 'Полный гайд по Stake Aviator: как работает мультипликатор, RTP 97%, автовывод, Provably Fair. Промокод MAX3000 для 200% до $3000.', 'Stake <span class="text-gradient-gold">Авиатор</span>', 'Самолёт взлетает. Выводите до крушения. Aviator от Stake с RTP 97% и Provably Fair верификацией. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'casino': ('Казино Stake | 4000+ слотов, 18 оригиналов | MAX3000', 'Полный гайд по казино Stake: 18 оригиналов с верифицированным RTP, 3000-4000 слотов от 15+ провайдеров, лайв-столы Evolution. MAX3000 для 200% до $3000.', 'Казино <span class="text-gradient-gold">Stake</span>', 'В казино Stake 18 оригиналов с верифицированным RTP, тысячи слотов и лайв-столы с настоящими дилерами. Войдите с промокодом <span class="code-highlight">MAX3000</span>.'),
        'live-casino': ('Лайв-казино Stake | Столы Evolution, Блэкджек, Рулетка | MAX3000', 'Лайв-казино Stake: столы Evolution, рулетка, блэкджек, баккара, живые игровые шоу. MAX3000 для 200% до $3000.', 'Лайв-казино <span class="text-gradient-gold">Stake</span>', 'Настоящий дилер. Экшн в реальном времени. Лайв-казино Stake со столами Evolution. Войдите с промокодом <span class="code-highlight">MAX3000</span>.'),
        'live-odds': ('Лайв-коэффициенты Stake | Рынки в реальном времени | MAX3000', 'Лайв-коэффициенты Stake: 30+ видов спорта, рынки в реальном времени, прямые трансляции Премьер-лиги, NBA, UFC. MAX3000 для 200% до $3000.', 'Лайв-коэффициенты <span class="text-gradient-gold">Stake</span>', 'Лайв-коэффициенты Stake для более чем 30 видов спорта. Обновление в реальном времени. Трансляции включены. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'mirror': ('Зеркала Stake 2026 | Работающие домены | WinnersClub', 'Полный каталог зеркальных доменов Stake: stake.bet, stake.mba, stake.ac, staketr.com и другие. Зачем нужны зеркала, предупреждения о фишинге. Промокод MAX3000.', 'Зеркала <span class="text-gradient-gold">Stake</span> 2026', 'Stake работает под несколькими доменами в зависимости от региона. Здесь вы найдёте проверенные официальные зеркала и предупреждения о фишинге. Всегда используйте <span class="code-highlight">MAX3000</span>.'),
        'news': ('Новости Stake 2026 | Последние события | WinnersClub', 'Последние новости Stake.com: обновления платформы, новые игры, изменения политики и события. Промокод MAX3000 для приветственного бонуса.', 'Новости <span class="text-gradient-gold">Stake</span>', 'Последние новости Stake.com. Обновления платформы, новые игры и события. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'originals': ('Stake Originals | 18 эксклюзивных игр с верифицированным RTP | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel и ещё 12. RTP верифицирован on-chain, Provably Fair. Промокод MAX3000 для 200% до $3000.', 'Stake <span class="text-gradient-gold">Originals</span>', 'У Stake 18 оригинальных игр с верифицированным on-chain RTP. Crash, Dice, Mines и другие. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'payments': ('Платежи Stake | Крипто и фиат, быстрые выводы | MAX3000', 'Методы оплаты на Stake: BTC, ETH, LTC, USDT, Doge и другая крипта. Фиат через MoonPay. Сроки вывода: крипто 30-60 мин, фиат 1-5 дней. Промокод MAX3000.', 'Платежи <span class="text-gradient-gold">Stake</span>', 'Stake принимает более 20 криптовалют и фиат через MoonPay. Вывод крипто: 30-60 минут. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'poker': ('Покер Stake | Texas Hold\'em, Турниры | MAX3000', 'Покер на Stake: Texas Hold\'em кэш-игры, sit-and-go и многостольные турниры. Рейкбэк доступен. Промокод MAX3000 для 200% до $3000.', 'Покер <span class="text-gradient-gold">Stake</span>', 'Покер на Stake с Texas Hold\'em, турнирами и рейкбэком. Экшн не останавливается. Войдите с промокодом <span class="code-highlight">MAX3000</span>.'),
        'reserves': ('On-chain резервы Stake | $339M верифицировано | WinnersClub', 'On-chain резервы Stake: $339.53M в кошельках, помеченных Arkham, по состоянию на 28 мая 2026. Ethereum 74%, Solana 14%. Верифицировано через cryptotips.com.', 'On-chain резервы <span class="text-gradient-gold">Stake</span>', 'У Stake $339.53M верифицированных on-chain резервов. Ethereum 74%, Solana 14%. Публично проверяемы через Arkham. Промокод <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('Ответственная игра | Инструменты и ресурсы | Stake WinnersClub', 'Ответственная игра на Stake: лимиты депозитов, самоисключение, GamCare, Анонимные игроки. Инструменты контроля. Промокод MAX3000 для приветственного бонуса.', 'Ответственная <span class="text-gradient-gold">игра</span>', 'Stake предлагает инструменты ответственной игры: лимиты, самоисключение и ресурсы поддержки. Играйте в пределах своих возможностей.'),
        'slots': ('Слоты на Stake | 3000+ игр, лучший RTP | MAX3000', 'Библиотека слотов Stake: 3000-4000 игр от Pragmatic Play, Hacksaw, Push Gaming и других. Лучший RTP, джекпот-слоты. MAX3000 для 200% до $3000.', 'Слоты <span class="text-gradient-gold">Stake</span>', 'Более 3000 слотов от лучших провайдеров мира. Верифицированный RTP. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'sports': ('Ставки на спорт Stake | 30+ видов спорта, прямые трансляции | MAX3000', 'Спортбук Stake: 30+ видов спорта, Премьер-лига, NBA, UFC, CS2 с прямыми трансляциями, маржа 3-4% на топ-футбол. MAX3000 для 200% до $3000.', 'Спорт <span class="text-gradient-gold">Stake</span>', 'Более 30 видов спорта с прямыми трансляциями. Конкурентная маржа. Спортбук Stake. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
        'stake-engine': ('Stake Engine | Открытая платформа для студий | MAX3000', 'Stake Engine: платформа, открытая для внешних студий с апреля 2025. Первый год - $3.31B оборот. Структура, интегрированные студии и что это значит для игроков.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine открывает платформу для внешних студий. Уже генерирует 10% GGR. Что нужно знать. Промокод <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Бонус Stake.us MAX3000 | Свипстейкс США | WinnersClub', 'Stake.us с промокодом MAX3000: 560 000 Gold Coins + 56 Stake Cash + 3.5% рейкбэк. Американская sweepstakes-платформа. Под управлением Sweepsteaks Limited.', 'Бонус <span class="text-gradient-gold">Stake.us</span>', 'Stake.us для американских игроков. С промокодом <span class="code-highlight">MAX3000</span> получаете Gold Coins, Stake Cash и рейкбэк. Реальный депозит не нужен.'),
        'vip': ('VIP Stake | 16 уровней, от Bronze до Obsidian | MAX3000', 'VIP Stake полный разбор: от Bronze ($10K ставок) до Obsidian ($1B). Рейкбэк по уровням, рекарджи, ежемесячные дропы, персональный хост. Сначала используйте MAX3000.', 'VIP <span class="text-gradient-gold">Stake</span>', 'VIP Stake имеет 16 уровней от Bronze до Obsidian. Рейкбэк, рекарджи и персональный хост. Начните с промокода <span class="code-highlight">MAX3000</span>.'),
    },
    'hi': {
        'about-stake': ('Stake को कौन चलाता है | संस्थापक, Easygo, GGR $4.7B | WinnersClub', 'Stake.com पूरी जानकारी: Ed Craven और Bijan Tehrani, Easygo इतिहास, GGR $4.7B, रिजर्व $339M, Curacao लाइसेंस. MAX3000 कोड से 200% $3,000 तक.', 'Stake.com को <span class="text-gradient-gold">कौन चलाता है</span>', 'Stake के बारे में जो जानना चाहिए: संस्थापक, आंकड़े और कोड <span class="code-highlight">MAX3000</span> क्यों मायने रखता है.'),
        'aviator': ('Stake Aviator | गाइड, RTP और रणनीति | MAX3000', 'Stake Aviator पूरी गाइड: मल्टीप्लायर कैसे काम करता है, RTP 97%, ऑटो-कैशआउट, Provably Fair. MAX3000 कोड से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">एविएटर</span>', 'विमान उड़ता है. क्रैश से पहले निकालें. Stake Aviator RTP 97% और Provably Fair वेरिफिकेशन के साथ. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'casino': ('Stake कैसीनो | 4,000+ स्लॉट, 18 ओरिजिनल | MAX3000', 'Stake कैसीनो पूरी गाइड: वेरिफाइड RTP वाले 18 ओरिजिनल, 15+ प्रोवाइडर्स के 3,000-4,000 स्लॉट, Evolution लाइव टेबल्स. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">कैसीनो</span>', 'Stake कैसीनो में वेरिफाइड RTP के 18 ओरिजिनल, हजारों स्लॉट और असली डीलर्स के साथ लाइव टेबल हैं. कोड <span class="code-highlight">MAX3000</span> से एंटर करें.'),
        'live-casino': ('Stake लाइव कैसीनो | Evolution टेबल, Blackjack, Roulette | MAX3000', 'Stake लाइव कैसीनो: Evolution टेबल, रूलेट, ब्लैकजैक, बैकारा, लाइव गेम शो. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">लाइव कैसीनो</span>', 'असली डीलर. रियल-टाइम एक्शन. Evolution टेबल के साथ Stake लाइव कैसीनो. कोड <span class="code-highlight">MAX3000</span> से एंटर करें.'),
        'live-odds': ('Stake लाइव ऑड्स | रियल-टाइम मार्केट | MAX3000', 'Stake लाइव ऑड्स: 30+ खेल, रियल-टाइम मार्केट, Premier League, NBA, UFC की लाइव स्ट्रीम. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">लाइव ऑड्स</span>', '30 से अधिक खेलों के लिए Stake लाइव ऑड्स. रियल-टाइम अपडेट. लाइव स्ट्रीम शामिल. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'mirror': ('Stake मिरर साइट्स 2026 | काम करने वाले डोमेन | WinnersClub', 'Stake मिरर डोमेन की पूरी डायरेक्टरी: stake.bet, stake.mba, stake.ac, staketr.com और अधिक. मिरर क्यों हैं, फिशिंग चेतावनियां. MAX3000 कोड.', 'Stake <span class="text-gradient-gold">मिरर साइट्स</span> 2026', 'Stake क्षेत्र के अनुसार कई डोमेन के तहत काम करता है. यहां आपको आधिकारिक वेरिफाइड मिरर और फिशिंग चेतावनियां मिलेंगी. हमेशा <span class="code-highlight">MAX3000</span> का उपयोग करें.'),
        'news': ('Stake समाचार 2026 | ताजा अपडेट | WinnersClub', 'Stake.com की ताजा खबरें: प्लेटफॉर्म अपडेट, नए गेम, पॉलिसी बदलाव और इवेंट. MAX3000 कोड से वेलकम बोनस.', 'Stake <span class="text-gradient-gold">समाचार</span>', 'Stake.com की ताजा खबरें. प्लेटफॉर्म अपडेट, नए गेम और इवेंट. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'originals': ('Stake Originals | 18 एक्सक्लूसिव गेम्स, वेरिफाइड RTP | MAX3000', 'Stake Originals: Crash, Dice, Mines, Limbo, Plinko, Wheel और 12 और. On-chain वेरिफाइड RTP, Provably Fair. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">Originals</span>', 'Stake में on-chain वेरिफाइड RTP के साथ 18 ओरिजिनल गेम्स हैं. Crash, Dice, Mines और अधिक. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'payments': ('Stake पेमेंट | क्रिप्टो और Fiat, तेज विदड्रॉल | MAX3000', 'Stake पर पेमेंट तरीके: BTC, ETH, LTC, USDT, Doge और अधिक क्रिप्टो. MoonPay से Fiat. विदड्रॉल समय: क्रिप्टो 30-60 मिनट, Fiat 1-5 दिन. MAX3000 कोड.', 'Stake <span class="text-gradient-gold">पेमेंट</span>', 'Stake 20 से अधिक क्रिप्टोकरेंसी और MoonPay के जरिए Fiat स्वीकार करता है. क्रिप्टो विदड्रॉल: 30-60 मिनट. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'poker': ('Stake पोकर | Texas Hold\'em, टूर्नामेंट | MAX3000', 'Stake पर पोकर: Texas Hold\'em कैश गेम, sit-and-go और मल्टी-टेबल टूर्नामेंट. Rakeback उपलब्ध. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">पोकर</span>', 'Stake पर Texas Hold\'em, टूर्नामेंट और Rakeback के साथ पोकर. एक्शन नहीं रुकता. कोड <span class="code-highlight">MAX3000</span> से एंटर करें.'),
        'reserves': ('Stake On-Chain रिजर्व | $339M वेरिफाइड | WinnersClub', 'Stake on-chain रिजर्व: 28 मई 2026 को Arkham लेबल्ड वॉलेट में $339.53M. Ethereum 74%, Solana 14%. cryptotips.com से वेरिफाइड.', 'Stake <span class="text-gradient-gold">On-Chain रिजर्व</span>', 'Stake के $339.53M वेरिफाइड on-chain रिजर्व हैं. Ethereum 74%, Solana 14%. Arkham के जरिए पब्लिकली ऑडिट किए जा सकते हैं. कोड <span class="code-highlight">MAX3000</span>.'),
        'responsible-gambling': ('जिम्मेदार जुआ | टूल्स और संसाधन | Stake WinnersClub', 'Stake पर जिम्मेदार जुआ: डिपॉजिट लिमिट, सेल्फ-एक्सक्लूजन, GamCare, Gamblers Anonymous. कंट्रोल टूल्स. MAX3000 कोड से वेलकम बोनस.', 'जिम्मेदार <span class="text-gradient-gold">जुआ</span>', 'Stake जिम्मेदार जुए के टूल्स प्रदान करता है: लिमिट, सेल्फ-एक्सक्लूजन और सपोर्ट संसाधन. अपनी क्षमता के भीतर खेलें.'),
        'slots': ('Stake पर स्लॉट | 3,000+ गेम, बेस्ट RTP | MAX3000', 'Stake स्लॉट लाइब्रेरी: Pragmatic Play, Hacksaw, Push Gaming और अधिक से 3,000-4,000 गेम. बेस्ट RTP, जैकपॉट स्लॉट. MAX3000 से 200% $3,000 तक.', 'Stake पर <span class="text-gradient-gold">स्लॉट</span>', 'दुनिया के सर्वश्रेष्ठ प्रोवाइडर्स के 3,000 से अधिक स्लॉट. वेरिफाइड RTP. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'sports': ('Stake स्पोर्ट्स | 30+ खेल, लाइव स्ट्रीम | MAX3000', 'Stake Sportsbook: 30+ खेल, Premier League, NBA, UFC, CS2 लाइव स्ट्रीम के साथ, मुख्य फुटबॉल में 3-4% मार्जिन. MAX3000 से 200% $3,000 तक.', 'Stake <span class="text-gradient-gold">स्पोर्ट्स</span>', 'लाइव स्ट्रीम के साथ 30 से अधिक खेल. प्रतिस्पर्धी मार्जिन. Stake Sportsbook. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
        'stake-engine': ('Stake Engine | स्टूडियो के लिए ओपन प्लेटफॉर्म | MAX3000', 'Stake Engine: अप्रैल 2025 से बाहरी स्टूडियो के लिए खुला प्लेटफॉर्म. पहले साल $3.31B वॉल्यूम. संरचना, एकीकृत स्टूडियो और खिलाड़ियों के लिए इसका मतलब.', 'Stake <span class="text-gradient-gold">Engine</span>', 'Stake Engine प्लेटफॉर्म को बाहरी स्टूडियो के लिए खोलता है. पहले से GGR का 10% जेनरेट कर रहा है. जो जानना चाहिए. कोड <span class="code-highlight">MAX3000</span>.'),
        'stake-us-bonus': ('Stake.us बोनस MAX3000 | Sweepstakes अमेरिका | WinnersClub', 'Stake.us कोड MAX3000 के साथ: 560,000 Gold Coins + 56 Stake Cash + 3.5% रेकबैक. अमेरिकी Sweepstakes प्लेटफॉर्म. Sweepsteaks Limited द्वारा संचालित.', 'Stake.us <span class="text-gradient-gold">बोनस</span>', 'अमेरिकी खिलाड़ियों के लिए Stake.us. कोड <span class="code-highlight">MAX3000</span> से Gold Coins, Stake Cash और Rakeback पाएं. कोई असली डिपॉजिट नहीं चाहिए.'),
        'vip': ('Stake VIP | 16 स्तर, Bronze से Obsidian | MAX3000', 'Stake VIP पूरी जानकारी: Bronze ($10K बेट) से Obsidian ($1B) तक 16 स्तर. प्रति स्तर Rakeback, रिलोड, मासिक ड्रॉप, डेडिकेटेड होस्ट. पहले MAX3000 का उपयोग करें.', 'Stake <span class="text-gradient-gold">VIP</span>', 'Stake VIP में Bronze से Obsidian तक 16 स्तर हैं. Rakeback, रिलोड और डेडिकेटेड होस्ट. कोड <span class="code-highlight">MAX3000</span> से शुरू करें.'),
    },
}

# Build SUBPAGE_DATA from SUBPAGE_TITLES for all non-promo-code slugs
for locale, slug_map in SUBPAGE_TITLES.items():
    for slug, (title, desc, h1, hero_sub) in slug_map.items():
        slug_to_img = {
            'about-stake': 'about-stake', 'aviator': 'aviator', 'casino': 'casino',
            'live-casino': 'live-casino', 'live-odds': 'live-odds', 'mirror': 'mirror',
            'news': 'default', 'originals': 'originals', 'payments': 'payments',
            'poker': 'poker', 'reserves': 'reserves', 'responsible-gambling': 'responsible-gambling',
            'slots': 'slots', 'sports': 'sports', 'stake-engine': 'stake-engine',
            'stake-us-bonus': 'stake-us-bonus', 'vip': 'vip',
        }
        img = f"/images/og/{slug_to_img.get(slug, 'default')}.png"
        # Generic body for non-promo-code pages
        body = f'''<section class="section"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{h1}</h2>
<p class="section-subtitle anim anim-fade-up anim-delay-1">{hero_sub}</p></div>
<div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Stake.com</h3><p>Curaçao OGL/2024/1451/0918 lisanslı Medium Rare NV tarafından işletilen gerçek para platformu. Kod <span class="code-highlight">MAX3000</span> ile 200% $3,000\'e kadar.</p></div>
<div class="club-card"><h3>MAX3000</h3><p>200% eşleştirme bonusu, $3,000\'e kadar, 40x veyjer (depozit+bonus üzerinden), 30 gün, minimum depozit $10. KYC seviye 3 gereklidir.</p></div>
</div></div></section>'''
        if slug not in SUBPAGE_DATA:
            SUBPAGE_DATA[slug] = {}
        SUBPAGE_DATA[slug][locale] = {
            'title': title,
            'desc': desc,
            'og_title': title,
            'og_desc': desc[:160],
            'og_image': img,
            'h1': h1,
            'hero_sub': hero_sub,
            'body_html': '',  # will use KO body as base
        }


# ─── FULL HREFLANG BLOCK ──────────────────────────────────────────────────────

def make_hreflang(slug):
    """Generate the full 15+1 hreflang block for a given slug."""
    lines = []
    slug_path = '' if slug == 'index' else f'{slug}/'
    lines.append(f'  <link rel="alternate" hreflang="en" href="https://winnersclub.com/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="ko" href="https://winnersclub.com/ko/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="zh-Hans" href="https://winnersclub.com/zh/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="vi" href="https://winnersclub.com/vi/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="th" href="https://winnersclub.com/th/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="ms" href="https://winnersclub.com/ms/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="pt" href="https://winnersclub.com/pt/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="ja" href="https://winnersclub.com/ja/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="es" href="https://winnersclub.com/es/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="pt-BR" href="https://winnersclub.com/pt-br/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="tr" href="https://winnersclub.com/tr/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="id" href="https://winnersclub.com/id/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="fr" href="https://winnersclub.com/fr/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="ru" href="https://winnersclub.com/ru/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="hi" href="https://winnersclub.com/hi/{slug_path}">')
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="https://winnersclub.com/{slug_path}">')
    return '\n'.join(lines)

# ─── LANGUAGE SWITCHER ────────────────────────────────────────────────────────

def make_mobile_lang_block(current_locale, label):
    """Build the mobile-lang-block select."""
    opts = [
        ('', 'English'),
        ('/ko/', '한국어 (Korean)'),
        ('/zh/', '中文 (Chinese)'),
        ('/vi/', 'Tiếng Việt (Vietnamese)'),
        ('/th/', 'ไทย (Thai)'),
        ('/ms/', 'Bahasa Melayu (Malay)'),
        ('/pt/', 'Português (Portuguese)'),
        ('/ja/', '日本語 (Japanese)'),
        ('/es/', 'Español (Spanish)'),
        ('/pt-br/', 'Português do Brasil (Portuguese - Brazil)'),
        ('/tr/', 'Türkçe (Turkish)'),
        ('/id/', 'Bahasa Indonesia (Indonesian)'),
        ('/fr/', 'Français (French)'),
        ('/ru/', 'Русский (Russian)'),
        ('/hi/', 'हिन्दी (Hindi)'),
    ]
    options_html = ''
    for val, txt in opts:
        options_html += f'<option value="{val}">{txt}</option>'
    return f'<div class="mobile-lang-block"><label>{label}</label><select onchange="if(this.value)window.location.href=this.value" aria-label="Language">{options_html}</select></div>'

def make_desktop_lang_switcher(current_locale):
    """Build the desktop lang-switcher select."""
    locale_labels = {
        '': ('https://winnersclub.com/', 'English'),
        'ko': ('https://winnersclub.com/ko/', 'KO'),
        'zh': ('https://winnersclub.com/zh/', '中文'),
        'vi': ('https://winnersclub.com/vi/', 'Tiếng Việt'),
        'th': ('https://winnersclub.com/th/', 'ไทย'),
        'ms': ('https://winnersclub.com/ms/', 'Bahasa Melayu'),
        'pt': ('https://winnersclub.com/pt/', 'Português'),
        'ja': ('https://winnersclub.com/ja/', '日本語'),
        'es': ('https://winnersclub.com/es/', 'ES'),
        'pt-br': ('https://winnersclub.com/pt-br/', 'PT-BR'),
        'tr': ('https://winnersclub.com/tr/', 'TR'),
        'id': ('https://winnersclub.com/id/', 'ID'),
        'fr': ('https://winnersclub.com/fr/', 'FR'),
        'ru': ('https://winnersclub.com/ru/', 'RU'),
        'hi': ('https://winnersclub.com/hi/', 'HI'),
    }
    opts_html = ''
    for loc_key, (url, label) in locale_labels.items():
        selected = ' selected' if loc_key == current_locale else ''
        val = '' if loc_key == current_locale else url
        opts_html += f'<option value="{val}"{selected}>{label}</option>'
    return f'<select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="Language">{opts_html}</select>'

# ─── ROOMS GRID BUILDER ───────────────────────────────────────────────────────

def build_rooms_grid(locale):
    heading, items = ROOMS_GRID[locale]
    lis = ''.join(f'<li><a href="/{locale}/{slug}/">{label}</a></li>' for slug, label in items)
    return (
        f'<aside class="rooms-grid" aria-label="{heading}" '
        f'style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);'
        f'border:1px solid rgba(255,215,0,.12);border-radius:14px;">'
        f'<h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;'
        f'color:#737378;margin:0 0 18px;font-weight:700;">{heading}</h3>'
        f'<ul style="list-style:none;margin:0;padding:0;display:grid;'
        f'grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;">'
        f'{lis}</ul></aside>'
    )

# ─── HTML GENERATOR ───────────────────────────────────────────────────────────

def make_font_link(locale):
    font_str = LOCALE_FONTS[locale]
    return f'<link href="https://fonts.googleapis.com/css2?family={font_str}&display=swap" rel="stylesheet">'

def build_home_page(locale):
    """Build the full home page HTML for a given locale."""
    lc = LANG_CODES[locale]
    d = PAGE_DATA['index'][locale]
    nav = NAV[locale]
    slug_path = ''
    slug = 'index'

    hreflang = make_hreflang(slug)
    mobile_lang = make_mobile_lang_block(locale, SWITCHER_LABELS[locale])
    desktop_lang = make_desktop_lang_switcher(locale)
    rooms_grid = build_rooms_grid(locale)
    font_link = make_font_link(locale)

    # Breadcrumb JSON-LD home label
    home_labels = {'es':'Inicio','pt-br':'Início','tr':'Ana Sayfa','id':'Beranda','fr':'Accueil','ru':'Главная','hi':'होम'}

    html = f'''<!DOCTYPE html>
<html lang="{lc}">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <link rel="canonical" href="https://winnersclub.com/{locale}/">
  <meta property="og:title" content="{d['og_title']}">
  <meta property="og:description" content="{d['og_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://winnersclub.com/{locale}/">
  <meta property="og:image" content="https://winnersclub.com/images/og/default.png">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#8b0a1a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {font_link}
  <link rel="stylesheet" href="/style.min.css?v=20260616d">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCFWWYWP7R"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-WCFWWYWP7R', {{anonymize_ip: true}});
  </script>
  <script src="/exit-tracker.js" defer></script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{d['ld_name']}",
  "description": "{d['ld_desc']}",
  "url": "https://winnersclub.com/{locale}/"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "{home_labels[locale]}",
      "item": "https://winnersclub.com/{locale}/"
    }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "{d['faq_json_q1']}", "acceptedAnswer": {{"@type": "Answer", "text": "{d['faq_json_a1']}"}}}},
    {{"@type": "Question", "name": "{d['faq_json_q2']}", "acceptedAnswer": {{"@type": "Answer", "text": "{d['faq_json_a2']}"}}}},
    {{"@type": "Question", "name": "{d['faq_json_q3']}", "acceptedAnswer": {{"@type": "Answer", "text": "{d['faq_json_a3']}"}}}},
    {{"@type": "Question", "name": "{d['faq_json_q4']}", "acceptedAnswer": {{"@type": "Answer", "text": "{d['faq_json_a4']}"}}}},
    {{"@type": "Question", "name": "{d['faq_json_q5']}", "acceptedAnswer": {{"@type": "Answer", "text": "{d['faq_json_a5']}"}}}}
  ]
}}
</script>
{hreflang}
  <script src="/lang-redirect.js" defer></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap"><link rel="preload" as="image" href="/images/girl-homepage-3.avif" type="image/avif" fetchpriority="high">
<script type="application/ld+json" data-ld="org">{{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players back room for Stake. Promo code MAX3000 unlocks a 200% match up to $3,000 with 40x wagering."}}</script>
<script type="application/ld+json" data-ld="website">{{"@context":"https://schema.org","@type":"WebSite","url":"https://winnersclub.com/","name":"WinnersClub","potentialAction":{{"@type":"SearchAction","target":{{"@type":"EntryPoint","urlTemplate":"https://winnersclub.com/?q={{search_term_string}}"}},"query-input":"required name=search_term_string"}}}}</script>
<meta name="twitter:image" content="https://winnersclub.com/images/og/default.png"><meta name="twitter:card" content="summary_large_image"></head>
<body>
  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/{locale}/" class="header-logo" aria-label="{nav['home_label']}">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        <a href="/{locale}/casino/" class="nav-link">{nav['casino']}</a>
        <a href="/{locale}/sports/" class="nav-link">{nav['sports']}</a>
        <a href="/{locale}/poker/" class="nav-link">{nav['poker']}</a>
        <a href="/{locale}/aviator/" class="nav-link">{nav['aviator']}</a>
        <a href="/{locale}/promo-code/" class="nav-link">{nav['promo-code']}</a>
        <a href="/{locale}/reserves/" class="nav-link">{nav['reserves']}</a>
        <a href="/{locale}/about-stake/" class="nav-link">{nav['about-stake']}</a>
      {mobile_lang}</nav>
      <div class="header-actions">{desktop_lang}
        <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup" aria-label="{nav['signup_btn']}">{nav['signup_btn']}</a>
        <button class="hamburger" id="hamburger" aria-label="{nav['signup_btn']}"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">{d['tease']}</p>
        <h1 class="ch-title text-gradient-gold">{d['h1']}</h1>
        <p class="ch-sub">{d['hero_sub']}</p>
        <div class="ch-actions">
          <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">{d['hero_cta1']}</a>
          <a href="/{locale}/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">{d['hero_cta2']}</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>{d['reserves_ticker']}</span><span>{d['reserves_ticker']}</span></div></div>
  <aside class="promo-strip" aria-label="MAX3000 {d['promo_strip_label']}"><div class="ps-inner"><span class="ps-label">{d['promo_strip_label']}</span><span class="ps-code">MAX3000</span><span class="ps-bonus">{d['promo_strip_bonus']}</span><a href="/{locale}/promo-code/" class="ps-cta">{d['promo_strip_cta']}</a></div></aside>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{d['sec1_h2']}</h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>{d['sec1_card1_h3']}</h3><p>{d['sec1_card1_p']}</p></div>
        <div class="club-card"><h3>{d['sec1_card2_h3']}</h3><p>{d['sec1_card2_p']}</p></div>
        <div class="club-card"><h3>{d['sec1_card3_h3']}</h3><p>{d['sec1_card3_p']}</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{d['sec2_h2']}</h2><p class="section-subtitle anim anim-fade-up anim-delay-1">{d['sec2_sub']}</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/{locale}/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">{d['vert_casino']}</div></a><a href="/{locale}/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">{d['vert_sports']}</div></a><a href="/{locale}/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">{d['vert_poker']}</div></a><a href="/{locale}/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">{d['vert_aviator']}</div></a><a href="/{locale}/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">{d['vert_live']}</div></a></div>
    </div>
  </section>
  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">{d['girl_break_h2']}</h2>
      <p class="girl-break-sub">{d['girl_break_sub']}</p>
      <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{d['girl_break_cta']}</a>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{d['sec3_h2']}</h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">{d['intel_founder_label']}</div><div class="ic-value">Craven &amp; Tehrani</div><div class="ic-detail">{d['intel_founder_detail']}</div></div>
        <div class="intel-card"><div class="ic-label">{d['intel_operator_label']}</div><div class="ic-value">Medium Rare NV</div><div class="ic-detail">{d['intel_operator_detail']}</div></div>
        <div class="intel-card"><div class="ic-label">{d['intel_license_label']}</div><div class="ic-value">Curaçao OGL/2024/1451/0918</div><div class="ic-detail">{d['intel_license_detail']}</div></div>
        <div class="intel-card"><div class="ic-label">{d['intel_reserves_label']}</div><div class="ic-value">$339.53M</div><div class="ic-detail">{d['intel_reserves_detail']}</div></div>
      </div>
    </div>
  </section>
  <!-- STAKE.COM vs STAKE.US -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">{d['two_doors_h2']}</h2>
        <p class="section-subtitle">{d['two_doors_sub']}</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>{d['stakecom_h3']}</h3>
          <p>{d['stakecom_p']}</p>
          <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">{d['stakecom_btn']}</a>
        </div>
        <div class="club-card">
          <h3>{d['stakeus_h3']}</h3>
          <p>{d['stakeus_p']}</p>
          <a href="{AFFILIATE_US}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">{d['stakeus_btn']}</a>
        </div>
      </div>
    </div>
  </section>
  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{d['faq_h2']}</h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{d['faq1_q']}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{d['faq1_a']}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{d['faq2_q']}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{d['faq2_a']}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{d['faq3_q']}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{d['faq3_a']}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{d['faq4_q']}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{d['faq4_a']}</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{d['faq5_q']}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{d['faq5_a']}</p></div>
        </div>
      </div>
    </div>
  </section>
  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">{d['signature']}</p>
    </div>
  </section>
  <!-- STICKY CTA -->
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">{d['sticky_text']}</div>
    <div class="sticky-cta-actions">
      <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{d['sticky_cta']}</a>
    </div>
    <button class="sticky-cta-close" aria-label="{d['sticky_close']}">&times;</button>
  </div>
  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">{d['footer_tagline']}</p>
          <div class="footer-badges">
            <span class="age-badge">{d['age_badge']}</span>
            <span class="cert-badge">GamCare</span>
            <span class="cert-badge">SSL</span>
          </div>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col">
            <h4>{d['footer_floor']}</h4>
            <a href="/{locale}/casino/">{d['footer_casino']}</a>
            <a href="/{locale}/sports/">{d['footer_sports']}</a>
            <a href="/{locale}/poker/">{d['footer_poker']}</a>
            <a href="/{locale}/aviator/">{d['footer_aviator']}</a>
            <a href="/{locale}/live-odds/">{d['footer_liveodds']}</a>
          </div>
          <div class="footer-col">
            <h4>{d['footer_code']}</h4>
            <a href="/{locale}/promo-code/">{d['footer_promo']}</a>
            <a href="/{locale}/payments/">{d['footer_payments']}</a>
            <a href="/{locale}/mirror/">{d['footer_mirror']}</a>
          </div>
          <div class="footer-col">
            <h4>{d['footer_intel']}</h4>
            <a href="/{locale}/about-stake/">{d['footer_aboutstake']}</a>
            <a href="/{locale}/reserves/">{d['footer_reserves']}</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">{d['footer_disclaimer']}</p>
        <p class="footer-copyright">{d['footer_copyright']}</p>
      </div>
    </div>
  </footer>

  <script src="/script.min.js?v=20260616a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script>{rooms_grid}</body>
</html>'''
    return html


def build_subpage(locale, slug):
    """Build a sub-page HTML by reading the KO template and adapting it."""
    lc = LANG_CODES[locale]
    nav = NAV[locale]

    # Get sub-page data
    if slug in SUBPAGE_DATA and locale in SUBPAGE_DATA[slug]:
        sd = SUBPAGE_DATA[slug][locale]
    else:
        # Fallback: derive from SUBPAGE_TITLES
        if locale in SUBPAGE_TITLES and slug in SUBPAGE_TITLES[locale]:
            title, desc, h1, hero_sub = SUBPAGE_TITLES[locale][slug]
        else:
            title = f'Stake {slug.replace("-"," ").title()} | MAX3000'
            desc = f'Stake {slug} guide with promo code MAX3000 for 200% up to $3,000.'
            h1 = f'Stake {slug.replace("-"," ").title()}'
            hero_sub = f'Use code <span class="code-highlight">MAX3000</span> for 200% up to $3,000.'
        sd = {
            'title': title, 'desc': desc, 'og_title': title, 'og_desc': desc[:160],
            'og_image': f'/images/og/{slug}.png',
            'h1': h1, 'hero_sub': hero_sub, 'body_html': ''
        }

    hreflang = make_hreflang(slug)
    mobile_lang = make_mobile_lang_block(locale, SWITCHER_LABELS[locale])
    desktop_lang = make_desktop_lang_switcher(locale)
    rooms_grid = build_rooms_grid(locale)
    font_link = make_font_link(locale)

    # Use body_html from promo-code page; for others, generate from KO template
    if sd.get('body_html'):
        body_content = sd['body_html']
    else:
        # Read KO version as body basis, then do minimal locale adaptation
        ko_path = os.path.join(BASE, 'ko', slug, 'index.html')
        if os.path.exists(ko_path):
            body_content = _extract_ko_body_content(ko_path, locale, slug, sd)
        else:
            body_content = _generic_body(locale, slug, sd)

    slug_path = f'{slug}/'
    # Breadcrumb
    home_labels = {'es':'Inicio','pt-br':'Início','tr':'Ana Sayfa','id':'Beranda','fr':'Accueil','ru':'Главная','hi':'होम'}

    html = f'''<!DOCTYPE html>
<html lang="{lc}">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{sd['title']}</title>
  <meta name="description" content="{sd['desc']}">
  <link rel="canonical" href="https://winnersclub.com/{locale}/{slug_path}">
  <meta property="og:title" content="{sd['og_title']}">
  <meta property="og:description" content="{sd['og_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://winnersclub.com/{locale}/{slug_path}">
  <meta property="og:image" content="https://winnersclub.com{sd['og_image']}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#8b0a1a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {font_link}
  <link rel="stylesheet" href="/style.min.css?v=20260616d">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCFWWYWP7R"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-WCFWWYWP7R', {{anonymize_ip: true}});
  </script>
  <script src="/exit-tracker.js" defer></script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{sd['title']}",
  "description": "{sd['desc']}",
  "url": "https://winnersclub.com/{locale}/{slug_path}"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "{home_labels[locale]}", "item": "https://winnersclub.com/{locale}/"}},
    {{"@type": "ListItem", "position": 2, "name": "{slug.replace('-',' ').title()}", "item": "https://winnersclub.com/{locale}/{slug_path}"}}
  ]
}}
</script>
{hreflang}
  <script src="/lang-redirect.js" defer></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">
<script type="application/ld+json" data-ld="org">{{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players back room for Stake. Promo code MAX3000 unlocks a 200% match up to $3,000 with 40x wagering."}}</script>
<script type="application/ld+json" data-ld="bc">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}},{{"@type":"ListItem","position":2,"name":"{locale.upper()}","item":"https://winnersclub.com/{locale}/"}},{{"@type":"ListItem","position":3,"name":"{slug.replace('-',' ').title()}","item":"https://winnersclub.com/{locale}/{slug_path}"}}]}}</script>
<meta name="twitter:image" content="https://winnersclub.com{sd['og_image']}"><meta name="twitter:card" content="summary_large_image"></head>
<body>
  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/{locale}/" class="header-logo" aria-label="{nav['home_label']}">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        <a href="/{locale}/casino/" class="nav-link">{nav['casino']}</a>
        <a href="/{locale}/sports/" class="nav-link">{nav['sports']}</a>
        <a href="/{locale}/poker/" class="nav-link">{nav['poker']}</a>
        <a href="/{locale}/aviator/" class="nav-link">{nav['aviator']}</a>
        <a href="/{locale}/promo-code/" class="nav-link">{nav['promo-code']}</a>
        <a href="/{locale}/reserves/" class="nav-link">{nav['reserves']}</a>
        <a href="/{locale}/about-stake/" class="nav-link">{nav['about-stake']}</a>
      {mobile_lang}</nav>
      <div class="header-actions">{desktop_lang}
        <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup" aria-label="{nav['signup_btn']}">{nav['signup_btn']}</a>
        <button class="hamburger" id="hamburger" aria-label="{nav['signup_btn']}"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-{slug}-3.avif') type('image/avif'), url('/images/girl-{slug}-3.webp') type('image/webp'));background-image:url('/images/girl-homepage-3.webp');background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">{sd['h1']}</h1>
        <p class="ch-sub">{sd['hero_sub']}</p>
        <div class="ch-actions">
          <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">MAX3000 &rarr;</a>
          <a href="/{locale}/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">{nav['promo-code']}</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain: $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Curaçao OGL/2024/1451/0918 &middot; Arkham Intel via cryptotips.com &middot; 28 May 2026</span><span>Stake on-chain: $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Curaçao OGL/2024/1451/0918 &middot; Arkham Intel via cryptotips.com &middot; 28 May 2026</span></div></div>

{body_content}

  <!-- STICKY CTA -->
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text"><span class="code-highlight">MAX3000</span> - 200% / $3,000 - Stake.com</div>
    <div class="sticky-cta-actions">
      <a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">MAX3000 &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="close">&times;</button>
  </div>
  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col">
            <h4>{PAGE_DATA['index'][locale]['footer_floor']}</h4>
            <a href="/{locale}/casino/">{PAGE_DATA['index'][locale]['footer_casino']}</a>
            <a href="/{locale}/sports/">{PAGE_DATA['index'][locale]['footer_sports']}</a>
            <a href="/{locale}/poker/">{PAGE_DATA['index'][locale]['footer_poker']}</a>
            <a href="/{locale}/aviator/">{PAGE_DATA['index'][locale]['footer_aviator']}</a>
            <a href="/{locale}/live-odds/">{PAGE_DATA['index'][locale]['footer_liveodds']}</a>
          </div>
          <div class="footer-col">
            <h4>{PAGE_DATA['index'][locale]['footer_code']}</h4>
            <a href="/{locale}/promo-code/">{PAGE_DATA['index'][locale]['footer_promo']}</a>
            <a href="/{locale}/payments/">{PAGE_DATA['index'][locale]['footer_payments']}</a>
            <a href="/{locale}/mirror/">{PAGE_DATA['index'][locale]['footer_mirror']}</a>
          </div>
          <div class="footer-col">
            <h4>{PAGE_DATA['index'][locale]['footer_intel']}</h4>
            <a href="/{locale}/about-stake/">{PAGE_DATA['index'][locale]['footer_aboutstake']}</a>
            <a href="/{locale}/reserves/">{PAGE_DATA['index'][locale]['footer_reserves']}</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">{PAGE_DATA['index'][locale]['footer_disclaimer']}</p>
        <p class="footer-copyright">{PAGE_DATA['index'][locale]['footer_copyright']}</p>
      </div>
    </div>
  </footer>

  <script src="/script.min.js?v=20260616a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script>{rooms_grid}</body>
</html>'''
    return html


def _extract_ko_body_content(ko_path, locale, slug, sd):
    """Extract the body content from KO page and adapt for new locale."""
    with open(ko_path, 'r', encoding='utf-8') as f:
        ko_html = f.read()

    # Extract everything between </section> after reserves-ticker and before sticky-cta
    # i.e., the main content sections
    body_match = re.search(
        r'((?:<section class="section".*?</section>\s*)+)',
        ko_html, re.S
    )
    if body_match:
        content = body_match.group(1)
        # Replace /ko/ links with /<locale>/
        content = content.replace(f'/ko/', f'/{locale}/')
        # Add MAX3000 highlight spans where plain MAX3000 appears (not already highlighted)
        content = re.sub(r'(?<!highlight">)MAX3000(?!</span>)', '<span class="code-highlight">MAX3000</span>', content)
        # Remove em-dashes and en-dashes
        content = content.replace('—', '-').replace('–', '-')
        return content
    else:
        return _generic_body(locale, slug, sd)


def _generic_body(locale, slug, sd):
    """Generate a generic body for pages without specific content."""
    d = PAGE_DATA['index'][locale]
    return f'''<section class="section"><div class="section-inner">
<div class="section-header">
<h2 class="section-title anim anim-rise gold-underline">{sd["h1"]}</h2>
<p class="section-subtitle anim anim-fade-up anim-delay-1">{sd["hero_sub"]}</p>
</div>
<div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
<div class="club-card"><h3>Stake.com</h3><p>Curaçao OGL/2024/1451/0918 under Medium Rare NV. Code <span class="code-highlight">MAX3000</span>: 200% up to $3,000, 40x wagering.</p></div>
<div class="club-card"><h3>MAX3000</h3><p>200% match, up to $3,000. 40x wagering on deposit+bonus. 30 days. Min deposit $10. KYC level 3 required.</p></div>
<div class="club-card"><h3>GGR $4.7B</h3><p>Ed Craven and Bijan Tehrani. Founded 2017. On-chain reserves $339.53M (Arkham Intel, 28 May 2026).</p></div>
</div>
</div></section>
<section class="section" style="background:var(--surface);"><div class="section-inner">
<div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{d["two_doors_h2"]}</h2></div>
<div class="club-grid anim-stagger">
<div class="club-card"><h3>{d["stakecom_h3"]}</h3><p>{d["stakecom_p"]}</p>
<a href="{AFFILIATE_COM}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">{d["stakecom_btn"]}</a></div>
<div class="club-card"><h3>{d["stakeus_h3"]}</h3><p>{d["stakeus_p"]}</p>
<a href="{AFFILIATE_US}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">{d["stakeus_btn"]}</a></div>
</div></div></section>'''


# ─── HREFLANG UPDATER FOR EXISTING PAGES ─────────────────────────────────────

OLD_HREFLANG_PATTERN = re.compile(
    r'(\s*<link rel="alternate" hreflang="en"[^>]*>\s*'
    r'<link rel="alternate" hreflang="ko"[^>]*>\s*'
    r'<link rel="alternate" hreflang="zh-Hans"[^>]*>\s*'
    r'<link rel="alternate" hreflang="vi"[^>]*>\s*'
    r'<link rel="alternate" hreflang="th"[^>]*>\s*'
    r'<link rel="alternate" hreflang="ms"[^>]*>\s*'
    r'<link rel="alternate" hreflang="pt"[^>]*>\s*'
    r'<link rel="alternate" hreflang="ja"[^>]*>\s*'
    r'<link rel="alternate" hreflang="x-default"[^>]*>)',
    re.S
)

# Full new switcher options HTML
NEW_SWITCHER_OPTIONS = (
    '<option value="">English</option>'
    '<option value="/ko/">한국어 (Korean)</option>'
    '<option value="/zh/">中文 (Chinese)</option>'
    '<option value="/vi/">Tiếng Việt (Vietnamese)</option>'
    '<option value="/th/">ไทย (Thai)</option>'
    '<option value="/ms/">Bahasa Melayu (Malay)</option>'
    '<option value="/pt/">Português (Portuguese)</option>'
    '<option value="/ja/">日本語 (Japanese)</option>'
    '<option value="/es/">Español (Spanish)</option>'
    '<option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option>'
    '<option value="/tr/">Türkçe (Turkish)</option>'
    '<option value="/id/">Bahasa Indonesia (Indonesian)</option>'
    '<option value="/fr/">Français (French)</option>'
    '<option value="/ru/">Русский (Russian)</option>'
    '<option value="/hi/">हिन्दी (Hindi)</option>'
)

# Pattern to match old mobile select options block (8 entries)
OLD_MOBILE_OPTIONS_PAT = re.compile(
    r'(<select onchange="if\(this\.value\)window\.location\.href=this\.value" aria-label="Language">)'
    r'(<option[^<]*</option>){8}'
    r'(</select>)',
    re.S
)

def update_existing_page(filepath):
    """Update hreflang + language switcher on an existing page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # 1. Update hreflang block - find and replace old 9-entry block
    # The old block has: en, ko, zh-Hans, vi, th, ms, pt, ja, x-default
    old_hreflang_re = re.compile(
        r'  <link rel="alternate" hreflang="en" href="https://winnersclub\.com/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="ko" href="https://winnersclub\.com/ko/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="zh-Hans" href="https://winnersclub\.com/zh/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="vi" href="https://winnersclub\.com/vi/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="th" href="https://winnersclub\.com/th/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="ms" href="https://winnersclub\.com/ms/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="pt" href="https://winnersclub\.com/pt/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="ja" href="https://winnersclub\.com/ja/[^"]*">\s*'
        r'  <link rel="alternate" hreflang="x-default" href="https://winnersclub\.com/[^"]*">',
        re.S
    )

    match = old_hreflang_re.search(html)
    if match:
        # Extract slug from canonical
        canonical_match = re.search(r'<link rel="canonical" href="https://winnersclub\.com/([^"]*)">', html)
        if canonical_match:
            path = canonical_match.group(1).strip('/')
            parts = path.split('/')
            # Determine slug
            if len(parts) == 0 or path == '':
                slug = 'index'
            elif len(parts) == 1:
                # Could be a locale dir (like /ko/) or a slug (like /promo-code/)
                if parts[0] in ['ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi']:
                    slug = 'index'
                else:
                    slug = parts[0] if parts[0] else 'index'
            elif len(parts) == 2:
                slug = parts[1] if parts[1] else 'index'
            else:
                slug = parts[-1] if parts[-1] else 'index'
        else:
            slug = 'index'

        new_hreflang = make_hreflang(slug)
        html = html[:match.start()] + new_hreflang + html[match.end():]
        changed = True

    # 2. Update mobile lang switcher - replace old options with new ones
    # Match the mobile-lang-block select
    old_mobile_re = re.compile(
        r'(<div class="mobile-lang-block"><label>[^<]*</label><select[^>]*>)'
        r'(.*?)'
        r'(</select></div>)',
        re.S
    )
    m2 = old_mobile_re.search(html)
    if m2:
        current_opts = m2.group(2)
        # Only update if it doesn't already have the new locales
        if '/es/' not in current_opts:
            html = html[:m2.start()] + m2.group(1) + NEW_SWITCHER_OPTIONS + m2.group(3) + html[m2.end():]
            changed = True

    # 3. Update desktop lang switcher
    old_desktop_re = re.compile(
        r'(<select class="lang-switcher"[^>]*>)(.*?)(</select>)',
        re.S
    )
    m3 = old_desktop_re.search(html)
    if m3:
        current_opts = m3.group(2)
        if 'winnersclub.com/es/' not in current_opts and '/es/' not in current_opts:
            # Build new desktop options preserving the 'selected' for current locale
            # Find which locale is selected
            selected_match = re.search(r'<option value="([^"]*)" selected>([^<]+)</option>', current_opts)
            if selected_match:
                sel_val = selected_match.group(1)
                # Keep the selected option in new build
                locale_map = {
                    'https://winnersclub.com/': ('','English'),
                    '': ('','KO/current'),  # will be determined by context
                }
                # Just rebuild with the same selected value
                new_desktop_opts = _build_desktop_opts_preserving_selected(current_opts)
                html = html[:m3.start()] + m3.group(1) + new_desktop_opts + m3.group(3) + html[m3.end():]
                changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    return changed


def _build_desktop_opts_preserving_selected(current_opts):
    """Rebuild desktop switcher options preserving the selected state."""
    # Extract what's currently selected
    sel_match = re.search(r'<option value="([^"]*)" selected>([^<]+)</option>', current_opts)
    sel_val = sel_match.group(1) if sel_match else ''
    sel_label = sel_match.group(2) if sel_match else 'Current'

    all_opts = [
        ('https://winnersclub.com/', 'English'),
        ('https://winnersclub.com/ko/', 'KO'),
        ('https://winnersclub.com/zh/', '中文'),
        ('https://winnersclub.com/vi/', 'Tiếng Việt'),
        ('https://winnersclub.com/th/', 'ไทย'),
        ('https://winnersclub.com/ms/', 'Bahasa Melayu'),
        ('https://winnersclub.com/pt/', 'Português'),
        ('https://winnersclub.com/ja/', '日本語'),
        ('https://winnersclub.com/es/', 'ES'),
        ('https://winnersclub.com/pt-br/', 'PT-BR'),
        ('https://winnersclub.com/tr/', 'TR'),
        ('https://winnersclub.com/id/', 'ID'),
        ('https://winnersclub.com/fr/', 'FR'),
        ('https://winnersclub.com/ru/', 'RU'),
        ('https://winnersclub.com/hi/', 'HI'),
    ]
    result = ''
    for url, label in all_opts:
        if url == sel_val or (sel_val == '' and label == sel_label):
            result += f'<option value="" selected>{sel_label}</option>'
        else:
            result += f'<option value="{url}">{label}</option>'
    return result


# ─── SITEMAP GENERATOR ────────────────────────────────────────────────────────

def generate_sitemap():
    """Regenerate sitemap.xml with all locale pages."""
    # Read existing sitemap to understand structure
    sitemap_path = os.path.join(BASE, 'sitemap.xml')

    # All slugs
    all_slug_paths = ['']  # home (root)
    for s in SLUGS:
        if s != 'index':
            all_slug_paths.append(f'{s}/')

    # All locales including existing
    all_locale_dirs = [''] + [f'{loc}/' for loc in ['ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi']]

    # Build full hreflang set for sitemap
    def sitemap_hreflang_links(url_path):
        lines = []
        slug = url_path.rstrip('/').split('/')[-1] if url_path.rstrip('/') else ''
        slug_for_href = slug + '/' if slug else ''

        for hreflang, loc_prefix in [
            ('en', ''), ('ko', 'ko/'), ('zh-Hans', 'zh/'), ('vi', 'vi/'), ('th', 'th/'),
            ('ms', 'ms/'), ('pt', 'pt/'), ('ja', 'ja/'), ('es', 'es/'), ('pt-BR', 'pt-br/'),
            ('tr', 'tr/'), ('id', 'id/'), ('fr', 'fr/'), ('ru', 'ru/'), ('hi', 'hi/'),
            ('x-default', '')
        ]:
            href = f'https://winnersclub.com/{loc_prefix}{slug_for_href}'
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{hreflang}" href="{href}"/>')
        return '\n'.join(lines)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']

    for loc_prefix in ['', 'ko/', 'zh/', 'vi/', 'th/', 'ms/', 'pt/', 'ja/', 'es/', 'pt-br/', 'tr/', 'id/', 'fr/', 'ru/', 'hi/']:
        for slug_path in [''] + [f'{s}/' for s in SLUGS if s != 'index']:
            full_path = f'{loc_prefix}{slug_path}'
            url = f'https://winnersclub.com/{full_path}'
            priority = '1.0' if not slug_path else '0.8'
            changefreq = 'weekly'

            # hreflang for this URL
            # The slug for hreflang lookup
            slug_clean = slug_path.rstrip('/')

            lines.append('  <url>')
            lines.append(f'    <loc>{url}</loc>')
            lines.append(f'    <changefreq>{changefreq}</changefreq>')
            lines.append(f'    <priority>{priority}</priority>')
            # Add xhtml:link alternates
            slug_for_href = (slug_clean + '/') if slug_clean else ''
            for hreflang, hloc_prefix in [
                ('en', ''), ('ko', 'ko/'), ('zh-Hans', 'zh/'), ('vi', 'vi/'), ('th', 'th/'),
                ('ms', 'ms/'), ('pt', 'pt/'), ('ja', 'ja/'), ('es', 'es/'), ('pt-BR', 'pt-br/'),
                ('tr', 'tr/'), ('id', 'id/'), ('fr', 'fr/'), ('ru', 'ru/'), ('hi', 'hi/'),
                ('x-default', '')
            ]:
                href = f'https://winnersclub.com/{hloc_prefix}{slug_for_href}'
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{hreflang}" href="{href}"/>')
            lines.append('  </url>')

    lines.append('</urlset>')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Sitemap written: {sitemap_path}')

# ─── LANG-REDIRECT.JS UPDATER ─────────────────────────────────────────────────

def update_lang_redirect():
    """Update lang-redirect.js with new locales and country mappings."""
    new_content = '''// Language detection and redirect for winnersclub.com
// Strategy: First-visit only. Cloudflare IP geolocation + browser language tiebreaker.
// Only redirects to languages the site actually ships.
(function() {
  'use strict';

  // Skip if user has already chosen a language
  if (document.cookie.indexOf('lang_set=') !== -1) return;
  if (localStorage.getItem('lang_set')) return;

  var path = window.location.pathname;

  // The 15 locales we actually have on disk.
  var supportedLangs = ['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi'];

  // If user is already on a language path, remember it and exit
  var pathLang = path.split('/')[1];
  if (supportedLangs.indexOf(pathLang) !== -1) {
    setLangCookie(pathLang);
    return;
  }

  // Skip on special files
  if (path.match(/\\.(xml|txt|json|html)$/) || path.indexOf('google') !== -1) return;

  // Country -> language mapping. Only languages we ship.
  // Countries that map to languages we don't have stay null -> fall through to English.
  var countryToLang = {
    // Korean
    'KR':'ko',
    // Chinese (Simplified target; we ship zh-Hans)
    'CN':'zh','HK':'zh','MO':'zh','TW':'zh',
    // Vietnamese
    'VN':'vi',
    // Thai
    'TH':'th',
    // Malay (Malaysia, Brunei, Singapore)
    'MY':'ms','BN':'ms','SG':'ms',
    // Portuguese (Portugal + lusophone Africa - NOT Brazil, which gets pt-br)
    'PT':'pt','AO':'pt','MZ':'pt','CV':'pt','GW':'pt','ST':'pt','TL':'pt',
    // Japanese
    'JP':'ja',
    // Spanish (LATAM)
    'MX':'es','AR':'es','CO':'es','CL':'es','PE':'es','BO':'es','EC':'es',
    'GT':'es','HN':'es','NI':'es','PA':'es','PY':'es','UY':'es','VE':'es',
    'CR':'es','DO':'es','SV':'es','CU':'es','PR':'es',
    // Brazilian Portuguese
    'BR':'pt-br',
    // Turkish
    'TR':'tr',
    // Indonesian (now gets id instead of ms)
    'ID':'id',
    // French (France + Francophone countries)
    'FR':'fr','BE':'fr','SN':'fr','CI':'fr','ML':'fr','BF':'fr','NE':'fr',
    'CD':'fr','GA':'fr','CM':'fr','TG':'fr','BJ':'fr','MG':'fr','GN':'fr',
    'CF':'fr','CG':'fr','DJ':'fr','KM':'fr','RE':'fr','MQ':'fr','GP':'fr',
    // Russian (CIS region)
    'RU':'ru','BY':'ru','KZ':'ru','KG':'ru','AM':'ru','AZ':'ru','TJ':'ru','UZ':'ru',
    // Hindi (India)
    'IN':'hi'
  };

  function setLangCookie(lang) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (365 * 24 * 60 * 60 * 1000));
    document.cookie = 'lang_set=' + lang + ';expires=' + expires.toUTCString() + ';path=/;SameSite=Lax';
    try { localStorage.setItem('lang_set', lang); } catch(e) {}
  }

  function browserLangToSupported() {
    var langs = navigator.languages || [navigator.language || navigator.userLanguage || 'en'];
    for (var i = 0; i < langs.length; i++) {
      var l = langs[i].toLowerCase();
      // Handle pt-BR specifically
      if (l === 'pt-br' || l === 'pt_br') return 'pt-br';
      var base = l.split('-')[0];
      if (supportedLangs.indexOf(base) !== -1) return base;
      if (supportedLangs.indexOf(l) !== -1) return l;
    }
    return 'en';
  }

  function redirectToLang(lang) {
    setLangCookie(lang);
    if (lang === 'en') return; // EN is at root
    var newPath = '/' + lang + (path === '/' ? '/' : path);
    newPath = newPath.replace(/\\/+/g, '/');
    // Sanity check: only redirect if target lang dir is known
    if (supportedLangs.indexOf(lang) === -1) return;
    window.location.replace(newPath);
  }

  // Use Cloudflare geolocation
  fetch('/cdn-cgi/trace', { cache: 'no-store' })
    .then(function(r) {
      if (!r.ok) throw new Error('CF unavailable');
      return r.text();
    })
    .then(function(text) {
      var match = text.match(/loc=([A-Z]{2})/);
      var country = match ? match[1] : null;
      var lang = null;

      if (country && country in countryToLang) {
        lang = countryToLang[country];
      }
      if (!lang) lang = browserLangToSupported();
      redirectToLang(lang);
    })
    .catch(function() {
      var lang = browserLangToSupported();
      redirectToLang(lang);
    });
})();
'''
    lr_path = os.path.join(BASE, 'lang-redirect.js')
    with open(lr_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'lang-redirect.js updated: {lr_path}')

# ─── MAIN BUILD ───────────────────────────────────────────────────────────────

def main():
    new_files = 0
    modified_files = 0

    # Step 1: Generate 133 new HTML files
    print('=== STEP 1: Generating new locale pages ===')
    for locale in NEW_LOCALES:
        locale_dir = os.path.join(BASE, locale)
        os.makedirs(locale_dir, exist_ok=True)
        print(f'  Building locale: {locale}')

        for slug in SLUGS:
            if slug == 'index':
                slug_dir = locale_dir
            else:
                slug_dir = os.path.join(locale_dir, slug)
                os.makedirs(slug_dir, exist_ok=True)

            out_path = os.path.join(slug_dir, 'index.html')

            if slug == 'index':
                html = build_home_page(locale)
            else:
                html = build_subpage(locale, slug)

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            new_files += 1

        print(f'    {locale}: 19 pages written')

    print(f'\nNew files created: {new_files}')

    # Step 2: Update existing 152 pages
    print('\n=== STEP 2: Updating existing pages (hreflang + switcher) ===')
    existing_pages = []
    for root, dirs, files in os.walk(BASE):
        # Skip new locale dirs and script dirs
        dirs[:] = [d for d in dirs if d not in NEW_LOCALES and not d.startswith('_') and d not in ['__pycache__','images','scripts','build_helpers','research','translations-wave2','skills']]
        for fname in files:
            if fname == 'index.html':
                fpath = os.path.join(root, fname)
                existing_pages.append(fpath)

    # Filter to only locale pages (existing 8 locales + root pages)
    locale_pages = [p for p in existing_pages if any(
        f'/{loc}/' in p or p.endswith(f'/{loc}/index.html')
        for loc in ['', 'ko', 'zh', 'vi', 'th', 'ms', 'pt', 'ja']
    )]

    # Actually get all existing pages (not in new locale dirs)
    all_existing = []
    for root, dirs, files in os.walk(BASE):
        # Exclude new locales and non-HTML dirs
        dirs[:] = [d for d in dirs if d not in NEW_LOCALES + ['__pycache__','images','scripts','build_helpers','research','translations-wave2','skills','node_modules','.git']]
        for fname in files:
            if fname == 'index.html':
                all_existing.append(os.path.join(root, fname))

    print(f'  Found {len(all_existing)} existing pages to update')
    for fpath in all_existing:
        if update_existing_page(fpath):
            modified_files += 1

    print(f'  Modified: {modified_files} existing pages')

    # Step 3: Regenerate sitemap
    print('\n=== STEP 3: Regenerating sitemap.xml ===')
    generate_sitemap()

    # Verify sitemap
    from xml.etree import ElementTree as ET
    try:
        ET.parse(os.path.join(BASE, 'sitemap.xml'))
        print('  Sitemap XML is valid')
    except Exception as e:
        print(f'  ERROR: Sitemap invalid: {e}')

    # Step 4: Update lang-redirect.js
    print('\n=== STEP 4: Updating lang-redirect.js ===')
    update_lang_redirect()

    # Step 5: Smoke tests
    print('\n=== STEP 5: Smoke tests ===')

    # Test 1: No em-dashes or en-dashes
    dash_count = 0
    for locale in NEW_LOCALES:
        locale_dir = os.path.join(BASE, locale)
        for root, dirs, files in os.walk(locale_dir):
            for fname in files:
                if fname.endswith('.html'):
                    content = open(os.path.join(root, fname), encoding='utf-8').read()
                    # Check for em-dash or en-dash NOT inside script/JSON blocks
                    # Simple check: look for these in visible text areas
                    if '—' in content or '–' in content:
                        dash_count += 1
                        print(f'  WARN: Dashes found in {os.path.join(root, fname)}')
    if dash_count == 0:
        print('  PASS: No em-dashes or en-dashes in new locales')
    else:
        print(f'  FAIL: {dash_count} files have dashes')

    # Test 2: MAX3000 count on home pages
    for locale in NEW_LOCALES:
        home_path = os.path.join(BASE, locale, 'index.html')
        content = open(home_path, encoding='utf-8').read()
        count = content.count('MAX3000')
        status = 'PASS' if count >= 3 else 'FAIL'
        print(f'  {status}: {locale}/index.html has {count} MAX3000 occurrences')

    # Test 3: Sitemap URL counts
    sitemap_content = open(os.path.join(BASE, 'sitemap.xml'), encoding='utf-8').read()
    for locale in NEW_LOCALES:
        count = sitemap_content.count(f'winnersclub.com/{locale}/')
        status = 'PASS' if count >= 19 else 'FAIL'
        print(f'  {status}: sitemap has {count} {locale}/ URLs (need >=19)')

    # Test 4: HTML tag closure check
    for locale in NEW_LOCALES:
        home_path = os.path.join(BASE, locale, 'index.html')
        content = open(home_path, encoding='utf-8').read()
        has_html = '</html>' in content and '</body>' in content and '</head>' in content
        print(f'  {"PASS" if has_html else "FAIL"}: {locale}/index.html has closing tags')

    print(f'\n=== BUILD COMPLETE ===')
    print(f'New files: {new_files}')
    print(f'Modified existing files: {modified_files}')
    print(f'Total: {new_files + modified_files} files changed')


if __name__ == '__main__':
    main()

