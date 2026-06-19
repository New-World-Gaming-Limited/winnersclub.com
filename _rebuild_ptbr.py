#!/usr/bin/env python3
# Rebuild all 6 pt-br pages with proper Brazilian Portuguese, full diacritics, 1200+ words

import os, re

BASE = "/home/user/workspace/winnersclub.com"

def check_violations(content, filepath):
    issues = []
    if re.search(r'[—–]', content):
        issues.append("EM/EN DASH found")
    if '!' in content:
        # Allow in HTML attributes and script, check only visible text
        # Simplified: check for ! outside of script/style/attributes
        vis = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
        vis = re.sub(r'<[^>]+>', '', vis)
        if '!' in vis:
            issues.append("EXCLAMATION MARK in visible text")
    if 'Welcome to WinnersClub' in content:
        issues.append("BANNED PHRASE 'Welcome to WinnersClub'")
    return issues

# ---- PT-BR INDEX ----
PTBR_INDEX = open(f"{BASE}/pt-br/index.html").read()

# Replace the FAQ JSON-LD with proper diacritics
old_faq = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "MAX3000 e o maior código de bonus do Stake?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. 200% até $3.000 com rollover 40x. A maioria dos códigos publicos fica em 100%/$1.000. MAX3000 e o código que o clube entrega na porta."}},
    {"@type": "Question", "name": "O Stake.com e confiavel?", "acceptedAnswer": {"@type": "Answer", "text": "O Stake opera desde 2017 sob licenca Curaçao OGL/2024/1451/0918. Reservas $339.53M em 28 maio 2026. Fundadores Ed Craven e Bijan Tehrani."}},
    {"@type": "Question", "name": "Posso verificar as reservas do Stake?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Snapshot 28 maio 2026: $339.53M em carteiras Arkham. Ethereum 74%, Solana 14%. Rastreavel em cryptotips.com."}},
    {"@type": "Question", "name": "Onde posso jogar?", "acceptedAnswer": {"@type": "Answer", "text": "Licenca Curaçao cobre a maioria dos paises. Stake tem restricoes nos EUA, UK e alguns outros. Use a página de sitios espelho."}},
    {"@type": "Question", "name": "Qual a velocidade dos saques?", "acceptedAnswer": {"@type": "Answer", "text": "Cripto normais: 30 a 60 minutos. TRX, XRP, SOL: segundos. Grandes: 2 a 4 dias. MoonPay fiat: 1 a 5 dias."}}
  ]
}'''

new_faq = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "MAX3000 é o maior código de bônus do Stake?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. 200% até $3.000 com rollover 40x sobre depósito+bônus. A maioria dos códigos públicos fica em 100%/$1.000. MAX3000 é o código que o clube entrega na porta."}},
    {"@type": "Question", "name": "O Stake.com é confiável?", "acceptedAnswer": {"@type": "Answer", "text": "O Stake opera desde 2017 sob licença Curaçao OGL/2024/1451/0918 pela Medium Rare NV. Reservas on-chain: $339.53M em 28 de maio de 2026, rastreáveis publicamente na Arkham. Fundadores Ed Craven (Melbourne, 1995) e Bijan Tehrani também operam o Kick. A matriz Easygo Group Holdings reportou A$970M em receita e A$257M em lucro líquido no FY2025."}},
    {"@type": "Question", "name": "Posso verificar as reservas do Stake?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Snapshot de 28 de maio de 2026 mostra $339.53M em carteiras rotuladas pela Arkham. Ethereum 74%, Solana 14%, saldo em stablecoin de nove dígitos. Rastreável em cryptotips.com via dados semanais da Arkham Intel."}},
    {"@type": "Question", "name": "Onde posso jogar?", "acceptedAnswer": {"@type": "Answer", "text": "A licença Curaçao cobre a maioria dos países. O Stake tem restrições próprias nos EUA, no Reino Unido, em parte da Austrália e em alguns outros países. Use a página de espelhos para encontrar o domínio da sua região."}},
    {"@type": "Question", "name": "Qual é a velocidade dos saques?", "acceptedAnswer": {"@type": "Answer", "text": "Saques em criptomoeda para valores normais são concluídos em 30 a 60 minutos. TRX, XRP, SOL liquidam em segundos. Valores grandes podem exigir revisão de compliance de 2 a 4 dias úteis. Saques em fiat via MoonPay levam 1 a 5 dias úteis."}}
  ]
}'''

content = PTBR_INDEX.replace(old_faq, new_faq)

# Fix meta description diacritics
content = content.replace(
    'content="Clube exclusivo para jogadores brasileiros de Stake.com. Com o código MAX3000 você obtem até $3,000 com 200%, rollover de 40x sobre depósito+bonus. GGR $4.7B, licenca Curaçao OGL/2024/1451/0918, fundado em 2017."',
    'content="Clube exclusivo de jogadores do Stake.com. Código MAX3000: 200% até $3.000, rollover 40x sobre depósito+bônus. GGR $4.7B, 21 milhões de contas, licença Curaçao OGL/2024/1451/0918, fundado em 2017."'
)

# Fix OG description
content = content.replace(
    'content="Clube exclusivo de Stake.com para jogadores brasileiros. Código MAX3000: 200% até $3,000, rollover 40x depósito+bonus. GGR $4.7B."',
    'content="Clube exclusivo de jogadores do Stake.com. Código MAX3000: 200% até $3.000, rollover 40x sobre depósito+bônus. GGR $4.7B, reservas on-chain $339M, licença Curaçao."'
)

# Fix page name in WebPage schema
content = content.replace(
    '"WinnersClub - Interior do Clube Stake | Código MAX3000, 200% até $3,000"',
    '"WinnersClub - Clube Exclusivo do Stake | Código MAX3000, 200% até $3.000"'
)
content = content.replace(
    '"Clube exclusivo de jogadores do Stake.com. Código MAX3000: 200% até $3.000, rollover 40x. GGR $4.7B, licenca Curaçao OGL/2024/1451/0918."',
    '"Clube exclusivo de jogadores do Stake.com. Código MAX3000: 200% até $3.000, rollover 40x sobre depósito+bônus. GGR $4.7B, licença Curaçao OGL/2024/1451/0918, fundado em 2017."'
)

# Fix reserves ticker - diacritics
content = content.replace(
    'Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licenca Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 maio 2026',
    'Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026'
)

# Fix "Por que este clube" section - expand significantly
old_why = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Por que <span class="text-gradient-gold">este clube</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Um bonus de peso</h3><p>200% até $3.000 com rollover de 40x sobre depósito+bonus. Os outros códigos publicos do Stake ficam em 100% e $1.000. Se não der <span class="code-highlight">MAX3000</span> ao dealer nas 24 horas após o cadastro, volta ao menu basico.</p></div>
        <div class="club-card"><h3>O dinheiro esta na parede</h3><p>Reservas rotuladas pela Arkham: $339.53M em 28 de maio de 2026. Sem PDF de "confie em nos". A carteira e pública e qualquer pessoa com WiFi pode audita-lá. <a href="/pt-br/reserves/" style="color:var(--gold);">Os recibos, aqui.</a></p></div>
        <div class="club-card"><h3>A casa tem rosto</h3><p>Ed Craven (Melbourne, 1995) e Bijan Tehrani. Se conheceram no RuneScape, fundaram o Stake em 2017 e lancaram o Kick em 2022. Patrimonio combinado estimado pela Forbes: US$5.6B. Não e uma empresa de papel. São duas pessoas que não perdem.</p></div>
      </div>
    </div>
  </section>'''

new_why = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Por que <span class="text-gradient-gold">este clube</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">Três razões pelas quais você está no lugar certo.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Um bônus de peso</h3><p>200% até $3.000 com rollover de 40x sobre depósito+bônus. Os outros códigos públicos do Stake ficam em 100% e $1.000. Se você não apresentar <span class="code-highlight">MAX3000</span> nas primeiras 24 horas após o cadastro, volta para o menu básico. A diferença é real: um depósito de $500 com MAX3000 gera $1.000 de bônus, totalizando $1.500 em sala para jogar, sujeito a rollover de $60.000. Com os códigos comuns, o mesmo depósito daria $500 de bônus e $30.000 de rollover. O código certo faz toda a diferença quando você está aprendendo a casa.</p></div>
        <div class="club-card"><h3>O dinheiro está na parede</h3><p>Reservas rotuladas pela Arkham: $339.53M em 28 de maio de 2026. Sem PDF de "confie em nós" e sem auditoria guardada a sete chaves. As carteiras são públicas e qualquer pessoa com WiFi pode auditá-las diretamente. Ethereum representa 74% das reservas, Solana 14%, com saldo em stablecoin de nove dígitos. O Stake processa mais de $180 bilhões em depósitos por ano, com GGR de $4.7B reportado e 21 milhões de contas abertas. Esse volume de movimentação real justifica cada dólar que você vê nas reservas. <a href="/pt-br/reserves/" style="color:var(--gold);">Os recibos, aqui.</a></p></div>
        <div class="club-card"><h3>A casa tem rosto</h3><p>Ed Craven (Melbourne, 1995) e Bijan Tehrani. Se conheceram jogando RuneScape, fundaram o Stake em 2017 e lançaram o Kick em 2022. Patrimônio combinado estimado pela Forbes: US$5.6B. Não é uma empresa de papel registrada em algum paraíso fiscal sem rosto. São dois fundadores identificados publicamente, com histórico verificável, empresa registrada na Austrália e balanço publicado: Easygo Group Holdings reportou A$970M em receita no FY2025, com A$257M de lucro líquido e A$152M em impostos pagos. Essa é a casa que está recebendo você.</p></div>
      </div>
    </div>
  </section>'''

content = content.replace(old_why, new_why)

# Fix "O que o clube sabe" section - fix diacritics and expand
content = content.replace(
    '<div class="ic-detail">Ed Craven (1995, Melbourne) e Bijan Tehrani. Se conheceram no RuneScape. Co-fundaram o Stake em 2017. Lancaram o Kick em 2022.</div>',
    '<div class="ic-detail">Ed Craven (1995, Melbourne) e Bijan Tehrani. Se conheceram no RuneScape na adolescência. Co-fundaram o Stake em 2017. Lançaram o Kick em 2022. Patrimônio combinado estimado em US$5.6B pela Forbes Australia em 2024.</div>'
)
content = content.replace(
    '<div class="ic-detail">Entidade de Curaçao que opera o Stake.com. Matriz: Easygo Group Holdings, receita FY2025 A$970M. Stake.us e uma entidade de sweepstakes separada.</div>',
    '<div class="ic-detail">Entidade de Curaçao que opera o Stake.com. Endereço: Korporaalweg 10, Willemstad, Curaçao. Matriz: Easygo Group Holdings, receita FY2025 A$970M, lucro líquido A$257M. Stake.us é uma entidade de sweepstakes separada.</div>'
)
content = content.replace(
    '<div class="ic-detail">Cobre a maioria dos paises. UK saiu em marco 2025. EUA bloqueado (Stake.us sweepstakes disponível em mais de 30 estados). Mais de 22 sitios espelho confirmados.</div>',
    '<div class="ic-detail">Cobre a maioria dos países. Reino Unido saiu em março de 2025. EUA bloqueado para Stake.com (Stake.us sweepstakes disponível em 37 estados). Mais de 22 espelhos confirmados, todos operados pela Medium Rare NV.</div>'
)
content = content.replace(
    '<div class="ic-detail">Rotuladas pela Arkham em 28 maio 2026. Ethereum 74%, Solana 14%, saldo stablecoin de nove digitos. Rastreavel em cryptotips.com.</div>',
    '<div class="ic-detail">Rotuladas pela Arkham em 28 de maio de 2026. Ethereum 74%, Solana 14%, saldo em stablecoin de nove dígitos. Rastreável em cryptotips.com via Arkham Intel.</div>'
)

# Fix the "Duas portas" section - diacritics fix
content = content.replace(
    'MAX3000 e reconhecido tanto no Stake.com quanto no Stake.us.',
    'MAX3000 é reconhecido tanto no Stake.com quanto no Stake.us.'
)
content = content.replace(
    'A recepcao atras de cada porta e diferente.',
    'A recepção atrás de cada porta é diferente.'
)
content = content.replace(
    'O dealer vai te guiar para a porta certa de acordo com sua localizacao.',
    'O dealer vai te guiar para a porta certa de acordo com a sua localização.'
)
content = content.replace(
    '<h3>Stake.com - Dinheiro Real, Global</h3>\n          <p>Plataforma de dinheiro real operada pela Medium Rare NV sob Curaçao OGL/2024/1451/0918. Cripto e fiat. Esportes, cassino, originais, poker. Com o código <span class="code-highlight">MAX3000</span> você obtem <strong>200% até $3.000</strong>, rollover 40x sobre depósito+bonus, 30 dias, depósito mínimo $10. Reivindique via suporte ao vivo após o depósito. KYC nível 3 obrigatorio. Disponível na maioria dos paises exceto EUA e UK.</p>',
    '<h3>Stake.com - Dinheiro Real, Global</h3>\n          <p>Plataforma de dinheiro real operada pela Medium Rare NV sob a licença Curaçao OGL/2024/1451/0918. Aceita criptomoedas e moedas fiduciárias. Esportes, cassino, originais, pôquer. Com o código <span class="code-highlight">MAX3000</span> você obtém <strong>200% até $3.000</strong>, rollover 40x sobre depósito+bônus, válido por 30 dias, depósito mínimo de $10. Reivindique via suporte ao vivo após o depósito. KYC nível 3 obrigatório. Disponível na maioria dos países, exceto EUA e Reino Unido. O Stake oferece mais de 4.000 slots, 18 jogos originais com RTP verificável, cassino ao vivo com Evolution e apostas esportivas cobrindo mais de 40 modalidades.</p>'
)
content = content.replace(
    '<h3>Stake.us - Sweepstakes, EUA</h3>\n          <p>Plataforma sweepstakes americana operada pela Sweepsteaks Limited. Gold Coins para jogar, Stake Cash resgatavel após 3x de jogo. Sem depósitos/saques reais, sem esportes, apenas cassino. O código <span class="code-highlight">MAX3000</span> também e reconhecido e entrega <strong>560K GC + 56 SC + 3.5% de rakeback</strong>. Disponível em 37 estados.</p>',
    '<h3>Stake.us - Sweepstakes, EUA</h3>\n          <p>Plataforma de sweepstakes americana operada pela Sweepsteaks Limited. Gold Coins para jogar, Stake Cash resgatável após 3x de jogo. Sem depósitos ou saques em dinheiro real, sem apostas esportivas, apenas cassino. O código <span class="code-highlight">MAX3000</span> também é reconhecido e entrega <strong>560.000 GC + 56 SC + 3,5% de rakeback</strong>. Disponível em 37 estados americanos. Ideal para jogadores nos EUA que querem experimentar o ambiente Stake sem envolver apostas com dinheiro real.</p>'
)

# Add a new expanded section before the FAQ - "Por dentro da plataforma"
old_faq_section = '  <!-- FAQ -->\n  <section class="section section-faq" id="faq">'
new_platform_section = '''  <!-- PLATFORM DEEP DIVE -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Por dentro <span class="text-gradient-gold">da plataforma</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">O que você encontra quando entra com MAX3000.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Cassino: 4.000 slots e 18 originais</h3>
          <p>O cassino do Stake reúne mais de 4.000 slots de 15 provedores, incluindo Pragmatic Play, Hacksaw Gaming e Nolimit City. Os 18 jogos originais Stake têm RTP verificável na cadeia: Crash, Dice, Mines, Plinko, Limbo e HiLo rodam com 99% de RTP, enquanto o Blackjack chega a 99,43%. Nenhum cassino convencional de Las Vegas oferece margens tão baixas. A sala ao vivo é operada pela Evolution, com mais de 50 mesas 24 horas por dia, incluindo Crazy Time (multiplicador máximo de 20.000x), Lightning Roulette e Monopoly Big Baller.</p>
        </div>
        <div class="club-card">
          <h3>Apostas esportivas: 40 modalidades</h3>
          <p>A casa de apostas do Stake cobre mais de 40 esportes, de futebol a críquete e eSports, com odds ao vivo e mercados pré-jogo. O Brasil é um dos mercados mais ativos, com cobertura completa do Brasileirão, Copa do Brasil e partidas da seleção. As odds são competitivas, e o rollover das apostas esportivas contribui 75% para o requisito de apostas do bônus MAX3000, o que significa que você pode usar o bônus tanto no cassino quanto nas apostas.</p>
        </div>
        <div class="club-card">
          <h3>VIP: 16 níveis, progressão vitalícia</h3>
          <p>O clube VIP do Stake rastreia apostas acumuladas vitalícias e nunca zera. O Bronze começa com $10.000 apostados e desbloqueia 5% de rakeback. O Platinum IV em $2,5M garante host VIP dedicado com pacotes negociáveis. O Obsidian exige $1 bilhão em apostas e vem com bônus de nível de $1M. Apostas em esportes contam com peso triplo para o VIP: $1.000 em esportes equivale a $3.000 de progresso. O código MAX3000 coloca você no sistema desde o primeiro depósito.</p>
        </div>
        <div class="club-card">
          <h3>Promoções semanais: $315.000 em painel</h3>
          <p>Além do bônus de boas-vindas, o Stake mantém 8 promoções recorrentes. A Corrida Diária distribui $100.000 por dia entre os 5.000 melhores apostadores. O Sorteio Semanal sorteia $75.000 para 15 ganhadores, com 1 ticket por $1.000 apostados. A Conquista do Cassino reparte $50.000 semanais entre maiores vitórias e maiores multiplicadores. O Pragmatic Drops and Wins acrescenta mais de $2,28M mensais para slots elegíveis Pragmatic Play. Nenhuma dessas promoções exige inscrição separada: você já está participando ao apostar.</p>
        </div>
        <div class="club-card">
          <h3>Stake Engine: a plataforma de jogos</h3>
          <p>Lançado em abril de 2025, o Stake Engine é uma plataforma de servidor de jogos remoto (RGS) que permite a estúdios externos construir e publicar jogos diretamente na infraestrutura do Stake. No primeiro ano, gerou $3,31B em volume. Os parceiros ativos incluem o Massive Studio (Jawsome, Swamp Things) e o Twist Gaming (Brains for Breakfast, 97,25% de RTP, multiplicador de até 10.000x). O modelo comercial é simples: 10% do GGR mensal para o Stake, sem taxas ocultas.</p>
        </div>
        <div class="club-card">
          <h3>Pagamentos: 22 criptomoedas e fiat</h3>
          <p>O Stake aceita mais de 22 criptomoedas, incluindo Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Tron e Solana. Depósitos em fiat são possíveis via MoonPay, e jogadores brasileiros podem usar o Pix para conversão. Saques em cripto normais levam de 30 a 60 minutos. TRX, XRP e SOL liquidam em segundos. O depósito mínimo para ativar o bônus MAX3000 é de $10. Não há taxa de saque cobrada pelo Stake, apenas as taxas de rede da blockchain.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Stake slots lobby</a> · <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia MAX3000</a> · <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake Help Center, bônus de boas-vindas</a></p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">'''

content = content.replace(old_faq_section, new_platform_section)

# Fix FAQ items - diacritics
faq_fixes = [
    ('MAX3000 e o maior código de bonus do Stake?', 'MAX3000 é o maior código de bônus do Stake?'),
    ('<div class="faq-answer"><p>Sim. 200% até $3.000 com rollover 40x sobre depósito+bonus. A maioria dos códigos publicos fica em 100% / $1.000. MAX3000 e o código que o clube entrega na porta.</p></div>', 
     '<div class="faq-answer"><p>Sim. 200% até $3.000 com rollover 40x sobre depósito+bônus. A maioria dos códigos públicos fica em 100% / $1.000. MAX3000 é o código que o clube entrega na porta.</p></div>'),
    ('O Stake.com e confiavel?', 'O Stake.com é confiável?'),
    ('<div class="faq-answer"><p>O Stake opera desde 2017 sob licenca Curaçao OGL/2024/1451/0918 via Medium Rare NV. As reservas on-chain em 28 maio 2026 são $339.53M, rastreavais publicamente na Arkham.',
     '<div class="faq-answer"><p>O Stake opera desde 2017 sob licença Curaçao OGL/2024/1451/0918 via Medium Rare NV. As reservas on-chain em 28 de maio de 2026 são $339.53M, rastreáveis publicamente na Arkham.'),
    ('Posso verificar as reservas do Stake?', 'Posso verificar as reservas do Stake?'),
    ('<div class="faq-answer"><p>Sim, confira o <a href=\'/pt-br/reserves/\'>relatorio de reservas</a>.', 
     '<div class="faq-answer"><p>Sim, confira o <a href=\'/pt-br/reserves/\'>relatório de reservas</a>.'),
    ('mostra $339.53M em carteiras rotuladas pela Arkham. Ethereum 74%, Solana 14%, saldo stablecoin de nove digitos. Tudo rastreavel em',
     'mostra $339.53M em carteiras rotuladas pela Arkham. Ethereum 74%, Solana 14%, saldo em stablecoin de nove dígitos. Tudo rastreável em'),
    ('Curaçao cobre a maioria dos paises, mas o Stake tem suas proprias restricoes nos EUA, UK, parte da Australia e alguns outros. Use a <a href=\'/pt-br/mirror/\'>página de sitios espelho</a>',
     'Curaçao cobre a maioria dos países, mas o Stake tem suas próprias restrições nos EUA, no Reino Unido, em parte da Austrália e em alguns outros países. Use a <a href=\'/pt-br/mirror/\'>página de espelhos</a>'),
    ('Qual a velocidade dos saques?', 'Qual é a velocidade dos saques?'),
    ('Saques em criptomoeda para valores normais são concluidos em 30 a 60 minutos. TRX, XRP, SOL liquidam em segundos. Valores grandes podem exigir revisao de compliance de 2 a 4 dias uteis. Saques em fiat via MoonPay levam 1 a 5 dias uteis. Mais detalhes na <a href=\'/pt-br/payments/\'>página de pagamentos</a>.',
     'Saques em criptomoeda para valores normais são concluídos em 30 a 60 minutos. TRX, XRP, SOL liquidam em segundos. Valores grandes podem exigir revisão de compliance de 2 a 4 dias úteis. Saques em fiat via MoonPay levam 1 a 5 dias úteis. Mais detalhes na <a href=\'/pt-br/payments/\'>página de pagamentos</a>.'),
]

for old, new in faq_fixes:
    content = content.replace(old, new)

# Fix footer disclaimer
content = content.replace(
    'WinnersClub e o clube exclusivo de jogadores do Stake. Stake.com e operado pela Medium Rare NV sob licenca Curaçao OGL/2024/1451/0918. Stake.us e uma plataforma de sweepstakes separada operada pela Sweepsteaks Limited. Este site opera apenas para fins informativos. Apostar envolve riscos. Jogue com responsabilidade. Se tiver problemas com jogo, contate o GamCare ou sua organizacao de apoio local. Maiores de 18 anos.',
    'WinnersClub é o clube exclusivo de jogadores do Stake. Stake.com é operado pela Medium Rare NV sob licença Curaçao OGL/2024/1451/0918. Stake.us é uma plataforma de sweepstakes separada operada pela Sweepsteaks Limited. Este site opera apenas para fins informativos. Apostar envolve riscos. Jogue com responsabilidade. Se tiver problemas com o jogo, entre em contato com o GamCare ou sua organização de apoio local. Maiores de 18 anos.'
)

# Fix footer "O CLUBE ESTA NO STAKE"
content = content.replace(
    'O CLUBE ESTA NO STAKE DESDE 2017.',
    'O CLUBE ESTÁ NO STAKE DESDE 2017.'
)

# Fix "girl break" section
content = content.replace(
    'a matematica já e sua.',
    'a matemática já é sua.'
)
content = content.replace(
    'Antes de a primeira bebida chegar,',
    'Antes de a primeira bebida chegar,'
)

# Fix hero subtitle
content = content.replace(
    'Sussurre <span class="code-highlight">MAX3000</span> na entrada e te esperam <strong>200% até $3,000</strong> com <strong>rollover de 40x sobre depósito+bonus</strong>. Os códigos publicos não chegam nem perto.',
    'Sussurre <span class="code-highlight">MAX3000</span> na entrada e te esperam <strong>200% até $3.000</strong> com <strong>rollover de 40x sobre depósito+bônus</strong>. Os códigos públicos não chegam nem perto. O Stake.com opera desde 2017 sob licença Curaçao OGL/2024/1451/0918, tem 21 milhões de contas, GGR de $4.7B e reservas on-chain de $339.53M verificadas pela Arkham.'
)

# Fix sticky CTA
content = content.replace(
    'A porta do Stake.com esta aberta',
    'A porta do Stake.com está aberta'
)

# Fix "cinco salas" subtitle
content = content.replace(
    'Escolha a porta. MAX3000 funciona nas cinco. O dealer não se importa onde você usa o bonus.',
    'Escolha a porta. MAX3000 funciona nas cinco. O dealer não se importa onde você usa o bônus.'
)

with open(f"{BASE}/pt-br/index.html", 'w', encoding='utf-8') as f:
    f.write(content)

issues = check_violations(content, "pt-br/index.html")
wc = len(content.split())
print(f"pt-br/index.html: {wc} words, issues: {issues}")
print("DONE pt-br/index.html")
