#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive rebuild of all 30 thin-content pages across 5 locales.
Strategy: Replace body content between header and sticky-cta/footer with full native-language content.
"""

import os, re, sys

BASE = "/home/user/workspace/winnersclub.com"

def word_count(text):
    """Count words in HTML by stripping tags"""
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&[a-z]+;', ' ', clean)
    words = clean.split()
    return len(words)

def check_violations(content, label):
    issues = []
    # Check for em/en dashes in visible text
    vis = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
    vis_text = re.sub(r'<[^>]+>', ' ', vis)
    if re.search(r'[—–]', vis_text):
        issues.append("EM/EN DASH found")
    # Check exclamation marks (not in HTML attributes)
    if '!' in vis_text.replace('&', '').replace('<!--', '').replace('-->', ''):
        # Allow &middot; and HTML entity formats
        clean_vis = re.sub(r'&[a-z#0-9]+;', '', vis_text)
        if '!' in clean_vis:
            issues.append(f"EXCLAMATION MARK in visible text")
    if 'Welcome to WinnersClub' in content:
        issues.append("BANNED PHRASE: Welcome to WinnersClub")
    return issues

def get_head_and_footer(locale_file):
    """Extract head (up to </head>) and footer (from sticky-cta onward)"""
    with open(locale_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    wc = word_count(content)
    issues = check_violations(content, path)
    print(f"  {os.path.relpath(path, BASE)}: {wc} words{' | ISSUES: '+str(issues) if issues else ''}")
    return wc

# ============================================================
# SHARED CONTENT TEMPLATES - Key facts used across all locales
# ============================================================

STAKE_FACTS = {
    'promo_code': 'MAX3000',
    'affiliate_url': 'https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000',
    'stake_us_url': 'https://stake.us/?c=MAX3000',
    'reserves': '$339.53M',
    'reserves_date': '2026年5月28日',
    'ggr': '$4.7B',
    'accounts': '21M',
    'license': 'Curaçao OGL/2024/1451/0918',
    'founded': '2017',
    'founders': 'Ed Craven & Bijan Tehrani',
    'parent': 'Easygo Group Holdings',
    'revenue_fy2025': 'A$970M',
    'profit_fy2025': 'A$257M',
}

# ==============================================================
# PT-BR PAGES
# ==============================================================

def rebuild_ptbr_casino():
    src = get_head_and_footer(f"{BASE}/pt-br/casino/index.html")
    # Extract header region (header tag and everything in it)
    header_match = re.search(r'(<header.*?</header>)', src, re.DOTALL)
    head_section = re.search(r'^(.*?<body>)', src, re.DOTALL).group(1)
    
    header_html = header_match.group(1) if header_match else ''
    
    # Get footer region
    footer_match = re.search(r'(<!-- STICKY CTA -->.*)', src, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ''
    
    body_content = f"""
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-casino-3.avif') type('image/avif'), url('/images/girl-casino-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Se você encontrou esta página, encontrou o piso do cassino.</p>
        <h1 class="ch-title text-gradient-gold">O Cassino Stake.<span class="h1-sub">Onde o RTP de 99% é o padrão.</span></h1>
        <p class="ch-sub">18 jogos originais com RTP verificável, mais de 4.000 slots de 15 provedores, sala ao vivo Evolution com mais de 50 mesas e clube VIP de 16 níveis. Com o código <span class="code-highlight">MAX3000</span> você desbloqueia 200% até $3.000. Licença Curaçao OGL/2024/1451/0918, operado desde 2017.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Garantir lugar no Stake.com</a>
          <a href="/pt-br/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Código Promo MAX3000</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span></div></div>
  <aside class="promo-strip" aria-label="MAX3000 Código Promocional"><div class="ps-inner"><span class="ps-label">Código Promocional</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% até $3.000 &middot; Rollover 40x</span><a href="/pt-br/promo-code/" class="ps-cta">Ver página do código &rarr;</a></div></aside>

  <!-- LIBRARY NUMBERS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">A <span class="text-gradient-gold">Biblioteca</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Os números por trás do piso.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Mais de 4.000 slots</h3><p>De 3 rolos clássicos a Megaways e cluster pays, com mais de 15 provedores premium e novidades constantes. Pragmatic Play, Hacksaw Gaming, Nolimit City, Push Gaming, Relax Gaming e mais de dez outros estúdios estão na biblioteca. O Stake também oferece versões exclusivas de títulos Pragmatic com RTP aprimorado de 98%, algo que você não vai encontrar em cassinos comuns.</p></div>
        <div class="club-card"><h3>Mais de 50 mesas ao vivo</h3><p>Blackjack, roleta, bacará, Crazy Time e a gama completa de game shows, todos operados pela Evolution em streaming 24 horas por dia, 7 dias por semana. Os limites de aposta variam de $1 a $50.000 por mão, com mesas Stake Live para membros VIP ultrapassando esse teto.</p></div>
        <div class="club-card"><h3>18 Stake Originals</h3><p>Jogos desenvolvidos internamente pela Easygo com verificabilidade criptográfica de resultado. A maioria opera com 99% de RTP, o edge de casa mais baixo do piso. O Blackjack original tem 99,43% de RTP. Você pode verificar qualquer resultado clicando no botão de equidade no jogo.</p></div>
        <div class="club-card"><h3>Stake Engine ao vivo</h3><p>Lançado em abril de 2025. Plataforma RGS aberta para estúdios externos. Gerou $3,31B em volume no primeiro ano. Massive Studio e Twist Gaming já estão ao vivo com jogos exclusivos do Stake.</p></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Lobby de slots Stake</a> &middot; <a href="https://www.freetips.com/casino/cryptocasinos/stake-offers-daily-races-bonus-drops-and-more-20250603-0010/" target="_blank" rel="noopener">freetips.com guia de promoções Stake</a></p>
    </div>
  </section>

  <!-- STAKE ORIGINALS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Originals</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">18 jogos desenvolvidos pela Easygo. Todos com verificação criptográfica. A maioria com 1% de edge de casa.</p>
      </div>
      <div class="club-body">
        <p>Os Stake Originals usam uma semente de servidor criptografada e comprometida antes de cada rodada. Qualquer jogador pode verificar qualquer resultado clicando no botão de verificação dentro do jogo. Como a semente é bloqueada antes de você jogar, nem o Stake nem ninguém pode alterar o resultado após o início. A seguir, o catálogo completo com RTP verificado.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:24px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Jogo</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">RTP</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Edge de casa</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Multiplicador máx.</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Blackjack</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99,43%</td><td style="text-align:right;padding:9px 12px;">0,57%</td><td style="text-align:right;padding:9px 12px;">2,5x (blackjack 3:2)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dice</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">9.900.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Mines</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">5.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Limbo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Crash</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Keno</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">500.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">HiLo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">Sequência ilimitada</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Wheel</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">500x (segmento bônus)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Plinko</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1.000x (alto risco, 16 linhas)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Video Poker</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">~99%</td><td style="text-align:right;padding:9px 12px;">~0,5%</td><td style="text-align:right;padding:9px 12px;">800x (royal flush)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Slide</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">98-99%</td><td style="text-align:right;padding:9px 12px;">1-2%</td><td style="text-align:right;padding:9px 12px;">4.294.967.000x (4,29 bilhões)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Baccarat</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">~98,94%</td><td style="text-align:right;padding:9px 12px;">~1,06% (banca)</td><td style="text-align:right;padding:9px 12px;">N/A</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dragon Tower</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">98%</td><td style="text-align:right;padding:9px 12px;">2%</td><td style="text-align:right;padding:9px 12px;">256.901x (modo Master)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Roulette</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">97,3%</td><td style="text-align:right;padding:9px 12px;">2,7%</td><td style="text-align:right;padding:9px 12px;">35x (número único)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Scarab Spin (slot)</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">97,84%</td><td style="text-align:right;padding:9px 12px;">2,16%</td><td style="text-align:right;padding:9px 12px;">10.000x</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Blue Samurai (slot)</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">97,26%</td><td style="text-align:right;padding:9px 12px;">2,74%</td><td style="text-align:right;padding:9px 12px;">10.000x</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stake.com/casino/group/stake-originals" target="_blank" rel="noopener">Catálogo Stake Originals</a> &middot; <a href="https://stake.com/provably-fair" target="_blank" rel="noopener">Documentação provably fair</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia Stake</a></p>

      <div class="section-header" style="margin-top:40px;">
        <h3 class="section-title anim anim-rise" style="font-size:20px;">Vale conhecer melhor</h3>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin-top:16px;">
        <div class="club-card">
          <h3>Crash, 99% RTP</h3>
          <p>Foguete coletivo que sobe até colidir aleatoriamente. Defina seu multiplicador de "cashout" antes de cada rodada. O placar em tempo real mostra a posição de todos os jogadores. Multiplicador máximo: 1.000.000x. Apostas automáticas com stop-win e stop-loss integrados.</p>
        </div>
        <div class="club-card">
          <h3>Mines, 99% RTP</h3>
          <p>Campo minado digital em grade 5x5. Escolha de 1 a 24 minas, clique nos tiles para encontrar gemas e dê cashout quando quiser. Mais minas significam multiplicadores mais altos por gema. Limite teórico: 5.000.000x. O posicionamento das minas é bloqueado criptograficamente no início da rodada.</p>
        </div>
        <div class="club-card">
          <h3>Slide, limite de 4,29 bilhões</h3>
          <p>Cards de multiplicadores rolam pela tela. Defina seu alvo antes da rodada. Se o card final atingir ou superar o alvo, você ganha. O máximo teórico de 4.294.967.000x é o maior de qualquer Stake Original, mas o limite de $10.000 por vitória limita o pagamento real em multiplicadores extremos.</p>
        </div>
        <div class="club-card">
          <h3>Dragon Tower, 98% RTP</h3>
          <p>Escolha um tile por linha da torre para encontrar ovos e subir. Cinco níveis de dificuldade: Easy (máx. 13x), Medium (37x), Hard (501x), Expert (19.289x), Master (256.901x). Cashout disponível a qualquer momento após linhas bem-sucedidas.</p>
        </div>
        <div class="club-card">
          <h3>Plinko, 99% RTP</h3>
          <p>Tabuleiro clássico de pachinko com 8 a 16 linhas e 3 níveis de risco. Baixo risco: máx. 16x (16 linhas). Médio: 110x. Alto: 1.000x. O valor mínimo de retorno de 0,2x garante que a bola nunca pague zero. Você sempre recebe algo de volta.</p>
        </div>
        <div class="club-card">
          <h3>Blackjack, 99,43% RTP</h3>
          <p>O melhor retorno matemático entre os Originals. Regras padrão com hit, stand, split, double e seguro. Blackjack natural paga 3:2. O edge de casa de 0,57% é mais afiado do que qualquer mesa em Las Vegas.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">200% de bônus <span class="text-gradient-gold">aguardando</span></h2>
      <p class="girl-break-sub">Sussurre <span class="code-highlight">MAX3000</span> na entrada e o bônus do cassino é seu: 200% até $3.000. <a href="/pt-br/promo-code/" style="color:var(--gold);">Ative o MAX3000</a> antes de girar o primeiro rolo.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Dar o código ao dealer</a>
    </div>
  </section>

  <!-- SLOT LIBRARY AND PROVIDERS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Biblioteca de <span class="text-gradient-gold">Slots</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Mais de 4.000 títulos dos nomes que importam.</p>
      </div>
      <div class="club-body">
        <p>Além dos Originals, o Stake tem uma das bibliotecas de slots de terceiros mais profundas do cassino de criptomoedas. Cerca de 4.000 títulos dependendo da fonte e região. Os provedores incluem Pragmatic Play para fãs de Gates of Olympus e Sweet Bonanza, Hacksaw Gaming para caçadores de alta volatilidade com 10.000x, Nolimit City para o extremo de 30.000x do Skate or Die, e Relax Gaming com o Book of 99 (99% de RTP) que rivaliza com os melhores Originals. Versões exclusivas do Stake de títulos populares da Pragmatic Play também rodam com 98% de RTP.</p>
      </div>
      <div class="casino-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:24px;">
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Pragmatic Play</h3><p style="font-size:13px;color:var(--text-dim);">Gates of Olympus, Sweet Bonanza, série Big Bass. Versões exclusivas com 98% de RTP.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Hacksaw Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Wanted Dead or a Wild, Le King, Dork Unit. Alta volatilidade com até 10.000x.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Nolimit City</h3><p style="font-size:13px;color:var(--text-dim);">Skate or Die (máx. 30.000x), slots mecânicos de volatilidade extrema.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Push Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Razor Shark, Fat Santa. Mecânicos de cascata muito populares.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Relax Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Book of 99 (99% RTP), o slot de terceiros com maior RTP do piso.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">ELK Studios</h3><p style="font-size:13px;color:var(--text-dim);">Mecânicos de alto RTP com sistemas de gameplay únicos.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Big Time Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Extra Chilli, inventor do mecanismo Megaways.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Play'n GO</h3><p style="font-size:13px;color:var(--text-dim);">Reactoonz, Book of Dead. Clássicos de cluster pays.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">BGaming</h3><p style="font-size:13px;color:var(--text-dim);">Stake Million (slot co-branded exclusivo, 97,10% RTP).</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Twist Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Brains for Breakfast (97,25% RTP, 10.000x). Via Stake Engine.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Massive Studio</h3><p style="font-size:13px;color:var(--text-dim);">Jawsome, Swamp Things (96,57%, exclusivo Stake). Via Stake Engine.</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Quickspin</h3><p style="font-size:13px;color:var(--text-dim);">Big Bad Wolf (97,34% RTP). Favorito cult da comunidade.</p></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Lobby de slots Stake</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia Stake</a></p>
    </div>
  </section>

  <!-- STAKE ENGINE -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Engine</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">A plataforma que transforma o Stake em publicador de jogos. Lançada em abril de 2025.</p>
      </div>
      <div class="club-body">
        <p>O Stake Engine é um servidor de jogos remoto (RGS) que permite a estúdios externos construir e publicar jogos diretamente na infraestrutura do Stake. Não é apenas um estúdio próprio, é uma plataforma aberta para desenvolvedores. O modelo comercial é direto: o estúdio fica com o resto, e o Stake recebe 10% do GGR mensal, sem taxas ocultas e sem lock-up.</p>
        <p style="margin-top:12px;">A infraestrutura por trás da plataforma já processou 300 bilhões de apostas, 20 milhões de jogadores e pico de 1 milhão de apostas por segundo. Os jogos feitos com Stake Engine já tinham acumulado <strong>$3,31B em volume</strong> nos 12 meses anteriores ao anúncio de lançamento em abril de 2025. Dois estúdios já estão ao vivo: <strong>Massive Studio</strong>, com Jawsome (posição 17 no ranking das 50 apostas mais altas do Stake) e Swamp Things (96,57% de RTP, exclusivo Stake), e <strong>Twist Gaming</strong>, com Samurai Dogs Unleashed (posição 25) e Brains for Breakfast (97,25% de RTP, máx. 10.000x).</p>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stakeengine.com" target="_blank" rel="noopener">Site oficial Stake Engine</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia Stake</a></p>
    </div>
  </section>

  <!-- LIVE CASINO -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Cassino ao Vivo <span class="text-gradient-gold">Evolution</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Operado pela Evolution. Mais de 50 mesas. Funcionamento 24 horas.</p>
      </div>
      <div class="club-body">
        <p>O cassino ao vivo do Stake é operado principalmente pela <strong>Evolution Gaming</strong>, com Pragmatic Play Live também presente. A Evolution é responsável pelos game shows principais e pelas mesas de grande volume, transmitidos em HD com suporte a múltiplos idiomas. Os limites de aposta variam de $1 a $50.000 por mão, com mesas Stake Live Brand subindo mais para membros VIP.</p>
      </div>
      <div class="icon-card-grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:24px;">
        <div class="club-card">
          <h3>Crazy Time</h3>
          <p>Roda da sorte com 4 jogos bônus: Coin Flip, Cash Hunt, Pachinko e roda Crazy Time. Multiplicadores de até 20.000x. O maior game show do cassino ao vivo.</p>
        </div>
        <div class="club-card">
          <h3>Lightning Roulette</h3>
          <p>Roleta europeia padrão onde a cada rodada de 1 a 5 "números relâmpago" aleatórios pagam de 50x a 500x em apostas diretas. Edge de casa europeu com potencial amplificado.</p>
        </div>
        <div class="club-card">
          <h3>Monopoly Big Baller</h3>
          <p>Sorteio em formato bingo com o Sr. Monopoly percorrendo um tabuleiro 3D. Os multiplicadores se acumulam conforme o movimento no tabuleiro. Mecânica única que você não encontra em roleta ou bacará comuns.</p>
        </div>
        <div class="club-card">
          <h3>XXXtreme Lightning Roulette</h3>
          <p>Multiplicadores relâmpago encadeados. Até 2.000x em um único número quando a corrente se conecta. Um nível acima do Lightning padrão.</p>
        </div>
        <div class="club-card">
          <h3>Funky Time</h3>
          <p>Roda da sorte DigiWheel com estética dos anos 70. Quatro jogos bônus com tema disco. Título recente da Evolution que traz variedade ao lobby de game shows.</p>
        </div>
        <div class="club-card">
          <h3>Mega Ball</h3>
          <p>Máquina de bingo que encontra cartelas de bingo. Até 400 cartelas por rodada. Multiplicadores que pousam na última bola podem gerar pagamentos acumulados expressivos.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://www.evolution.com/games/game-shows/" target="_blank" rel="noopener">Catálogo Evolution Game Shows</a></p>
    </div>
  </section>

  <!-- PROMOTIONS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Promoções <span class="text-gradient-gold">Ativas</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">8 premiações recorrentes. Sem inscrição separada. A maioria é automática.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Promoção</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Prize Pool</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Funcionamento</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Corrida Diária</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$100.000</td><td style="padding:9px 12px;">Todas as apostas somam ao placar. Top 5.000 ganham. Reset a cada 24h.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Rifa Semanal</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$75.000</td><td style="padding:9px 12px;">$1.000 apostados = 1 ticket. 15 ganhadores sorteados ao vivo às 14h GMT aos sábados.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Conquista do Cassino</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$50.000</td><td style="padding:9px 12px;">Dois pools: GRANDES VITÓRIAS (maior vitória em dinheiro) e VITÓRIAS SORTUDAS (maior multiplicador) nos jogos indicados.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Stake vs Eddie</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$30.000</td><td style="padding:9px 12px;">Supere a performance do co-fundador Eddie Craven nos jogos selecionados.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Reel Rumble</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20.000</td><td style="padding:9px 12px;">Dois slots selecionados, placares separados, competição pelo maior multiplicador.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Level Up</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20.000</td><td style="padding:9px 12px;">Desafio de multiplicadores em 5 etapas em jogos selecionados.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Original Ascent</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20.000</td><td style="padding:9px 12px;">Exclusivo Stake Originals. Atinja multiplicadores-alvo no Dice, Plinko e Mines para subir no placar.</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Pragmatic Drops e Wins</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">+$2,28M/mês</td><td style="padding:9px 12px;">Promoção de rede Pragmatic. Torneios diários + drops aleatórios em slots elegíveis. Milhares de prêmios por dia.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://www.freetips.com/casino/cryptocasinos/stake-offers-daily-races-bonus-drops-and-more-20250603-0010/" target="_blank" rel="noopener">FreeTips guia de promoções</a> &middot; <a href="https://stake.com/promotions" target="_blank" rel="noopener">Stake Promoções</a></p>
    </div>
  </section>

  <!-- VIP CLUB -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Clube <span class="text-gradient-gold">VIP</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">16 níveis. Progressão vitalícia. Rakeback a partir do Bronze.</p>
      </div>
      <div class="club-body">
        <p>O clube VIP rastreia apostas acumuladas vitalícias e nunca as zera. Apostas no cassino contam 1:1, apostas em esportes contam com peso 3x (esportes $1.000 = VIP $3.000 de progresso). O rakeback se ativa no <strong>Bronze ($10.000 apostados)</strong> com 5% e aumenta com cada nível. A partir do Platinum IV, um host VIP dedicado é atribuído para negociação de bônus personalizados. O marco Obsidian de $1 bilhão em apostas vem com bônus de nível de $1M e é alcançado por pouquíssimos jogadores no mundo.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:20px;">
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">Nível</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">Apostas vitalícias</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">Bônus de nível</th>
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">Benefício principal</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Bronze</td><td style="text-align:right;padding:8px 12px;">$10.000</td><td style="text-align:right;padding:8px 12px;">$15</td><td style="padding:8px 12px;">Rakeback de 5% desbloqueado</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Silver</td><td style="text-align:right;padding:8px 12px;">$50.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Bônus semanal e mensal aumentados</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Gold</td><td style="text-align:right;padding:8px 12px;">$100.000</td><td style="text-align:right;padding:8px 12px;">$110</td><td style="padding:8px 12px;">Bônus mensal desbloqueado</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum I</td><td style="text-align:right;padding:8px 12px;">$250.000</td><td style="text-align:right;padding:8px 12px;">$200</td><td style="padding:8px 12px;">Reload diário</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum II</td><td style="text-align:right;padding:8px 12px;">$500.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Valor de reload aumentado</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum III</td><td style="text-align:right;padding:8px 12px;">$1.000.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Reload diário, horário e a cada 10 min</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum IV</td><td style="text-align:right;padding:8px 12px;">$2.500.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Host VIP dedicado</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum V</td><td style="text-align:right;padding:8px 12px;">$5.000.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Estrutura de bônus personalizada</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum VI</td><td style="text-align:right;padding:8px 12px;">$10.000.000</td><td style="text-align:right;padding:8px 12px;">$8.000</td><td style="padding:8px 12px;">Limites de reload muito ampliados</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond I</td><td style="text-align:right;padding:8px 12px;">$25.000.000</td><td style="text-align:right;padding:8px 12px;">$20.000</td><td style="padding:8px 12px;">Reload renovável; convites a eventos</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond II</td><td style="text-align:right;padding:8px 12px;">$50.000.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Canal Telegram exclusivo para high rollers</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond III</td><td style="text-align:right;padding:8px 12px;">$100.000.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Pacote de host totalmente personalizado</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond IV</td><td style="text-align:right;padding:8px 12px;">$250.000.000</td><td style="text-align:right;padding:8px 12px;">N/A</td><td style="padding:8px 12px;">Convites a eventos exclusivos personalizados</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond V</td><td style="text-align:right;padding:8px 12px;">$500.000.000</td><td style="text-align:right;padding:8px 12px;">$400.000</td><td style="padding:8px 12px;">Stake Sphere e eventos ao vivo exclusivos</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;font-weight:700;color:var(--gold);">Obsidian</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1.000.000.000</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1.000.000</td><td style="padding:8px 12px;font-weight:600;">Prestígio máximo. Tudo totalmente personalizado.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://stake.com/vip" target="_blank" rel="noopener">Página VIP Stake</a> &middot; <a href="https://help.stake.com/en/articles/4793501-what-is-the-stake-vip-program" target="_blank" rel="noopener">Stake Help Center, programa VIP</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia Stake</a></p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Perguntas <span class="text-gradient-gold">na entrada</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Quantos jogos tem o cassino do Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Mais de 4.000 slots de mais de 15 provedores terceirizados, mais de 18 Stake Originals com RTP verificável, e o cassino ao vivo adiciona mais de 50 mesas baseadas em Evolution incluindo game shows.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Qual bônus de cassino eu recebo com MAX3000?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>200% de match no depósito até $3.000. O rollover é 40x sobre o valor combinado de depósito+bônus em 30 dias. Slots e jogos de cassino com edge acima de 4% contribuem 100%, apostas esportivas contribuem 75%.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Qual é o RTP dos Stake Originals?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>A maioria dos Originals opera com 99% de RTP (1% de edge de casa): Crash, Dice, Limbo, Plinko, Mines, HiLo, Keno e Wheel. O Blackjack lidera com 99,43%. O Bacará fica em ~98,94% (aposta banca). A Roleta em 97,3% (zero único). Dragon Tower 98%. Slide em 98-99% com teto de 4,29 bilhões de x.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O que é o Stake Engine?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Lançado em abril de 2025, o Stake Engine é uma plataforma de servidor de jogos remoto que permite a estúdios externos construir e publicar jogos na infraestrutura do Stake. Gerou $3,31B em volume no primeiro ano. Os parceiros incluem Massive Studio e Twist Gaming.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Há cassino ao vivo?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. O piso ao vivo é operado pela Evolution com mais de 50 mesas em streaming 24/7. Os game shows incluem Crazy Time (multiplicador máximo de 20.000x), Lightning Roulette, Monopoly Big Baller e Funky Time.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Como funciona o clube VIP do Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>16 níveis baseados em apostas vitalícias acumuladas. O Bronze começa com $10.000 apostados, desbloqueando 5% de rakeback. O Obsidian exige $1B em apostas e vem com bônus de $1M. O progresso nunca é zerado. Apostas esportivas contam com peso 3x no VIP.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Diga ao dealer que o WinnersClub mandou você.</p>
    </div>
  </section>
"""

    result = head_section + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_ptbr_promo():
    src = get_head_and_footer(f"{BASE}/pt-br/promo-code/index.html")
    head_section = re.search(r'^(.*?<body>)', src, re.DOTALL).group(1)
    header_match = re.search(r'(<header.*?</header>)', src, re.DOTALL)
    header_html = header_match.group(1) if header_match else ''
    footer_match = re.search(r'(<!-- STICKY CTA -->.*)', src, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ''
    
    # Check if footer exists in src
    if not footer_match:
        footer_match = re.search(r'(<div class="sticky-cta".*)', src, re.DOTALL)
        footer_html = footer_match.group(1) if footer_match else ''
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-promo-3.avif') type('image/avif'), url('/images/girl-promo-3.webp') type('image/webp'));background-image:url('/images/girl-homepage-3.webp');background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Se você encontrou esta página, encontrou o código.</p>
        <h1 class="ch-title text-gradient-gold">Código Promo Stake MAX3000<span class="h1-sub">200% até $3.000 no Stake.com.</span></h1>
        <p class="ch-sub">O código é MAX3000. No primeiro depósito, você recebe 200% de match, com bônus máximo de $3.000. Rollover de 40x sobre o valor combinado de depósito+bônus. KYC nível 3 obrigatório para receber. Jogadores nos EUA usam o <a href="/pt-br/stake-us-bonus/" style="color:var(--gold);text-decoration:underline;">Stake.us sweepstakes</a> com o mesmo código em plataforma separada.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Ativar MAX3000 no Stake.com</a>
          <a href="/pt-br/casino/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Ver o cassino</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span></div></div>
  <aside class="promo-strip" aria-label="MAX3000 Código Promocional"><div class="ps-inner"><span class="ps-label">Código Promocional</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% até $3.000 &middot; Rollover 40x</span><a href="#como-ativar" class="ps-cta">Como ativar &rarr;</a></div></aside>

  <!-- CALCULATOR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Calculadora de <span class="text-gradient-gold">Bônus Stake.com</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Depósito entre $10 e $1.500. O match de 200% chega até $3.000. O rollover de 40x incide sobre depósito+bônus combinados.</p>
      </div>
      <div class="calc-widget" style="background:var(--surface);border:1px solid rgba(255,215,0,.15);border-radius:14px;padding:28px 24px;max-width:600px;">
        <label style="display:block;margin-bottom:8px;font-weight:700;color:var(--gold);">Primeiro depósito no Stake.com</label>
        <input type="range" id="depositSlider" min="10" max="1500" value="500" step="10" style="width:100%;accent-color:var(--gold);">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;">
          <div style="background:var(--card);padding:16px;border-radius:10px;text-align:center;">
            <p style="font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px;">Bônus concedido</p>
            <p id="bonusOut" style="font-size:24px;font-weight:900;color:var(--gold);">$1.000</p>
            <p style="font-size:11px;color:var(--text-dim);">200% do depósito, máx. $3.000</p>
          </div>
          <div style="background:var(--card);padding:16px;border-radius:10px;text-align:center;">
            <p style="font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px;">Rollover necessário</p>
            <p id="wagerOut" style="font-size:24px;font-weight:900;color:var(--gold);">$60.000</p>
            <p style="font-size:11px;color:var(--text-dim);">(depósito + bônus) x 40</p>
          </div>
          <div style="background:var(--card);padding:16px;border-radius:10px;text-align:center;">
            <p style="font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px;">Saldo total</p>
            <p id="totalOut" style="font-size:24px;font-weight:900;color:var(--gold);">$1.500</p>
            <p style="font-size:11px;color:var(--text-dim);">Depósito + bônus após ativação</p>
          </div>
          <div style="background:var(--card);padding:16px;border-radius:10px;text-align:center;">
            <p style="font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px;">Eficiência do match</p>
            <p id="effOut" style="font-size:24px;font-weight:900;color:var(--gold);">200%</p>
            <p style="font-size:11px;color:var(--text-dim);">Cai abaixo de 200% acima de $1.500</p>
          </div>
        </div>
        <p style="margin-top:16px;font-size:13px;color:var(--text-dim);"><strong style="color:var(--gold);">Bônus máximo: $3.000.</strong> Depósitos de $1.500 recebem o bônus completo de $3.000. Depósitos acima de $1.500 são processados, mas o bônus não aumenta além de $3.000.</p>
      </div>
      <script>
        (function(){
          var s=document.getElementById('depositSlider');
          if(!s)return;
          function update(){
            var d=parseInt(s.value);
            var b=Math.min(d*2,3000);
            var w=(d+b)*40;
            var t=d+b;
            var e=Math.round(b/d*100);
            document.getElementById('bonusOut').textContent='$'+b.toLocaleString('pt-BR');
            document.getElementById('wagerOut').textContent='$'+w.toLocaleString('pt-BR');
            document.getElementById('totalOut').textContent='$'+t.toLocaleString('pt-BR');
            document.getElementById('effOut').textContent=e+'%';
          }
          s.addEventListener('input',update);
          update();
        })();
      </script>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake Help Center, bônus de boas-vindas</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com, condições MAX3000</a></p>
    </div>
  </section>

  <!-- CODE COMPARISON -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Comparação de <span class="text-gradient-gold">Códigos Ativos</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Sete códigos, um vencedor. Por que o clube recomenda apenas o MAX3000.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Código</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Match</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Bônus máx.</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Rollover</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.08);background:rgba(255,215,0,0.04);"><td style="padding:9px 12px;font-weight:700;color:var(--gold);">MAX3000</td><td style="text-align:right;padding:9px 12px;font-weight:700;color:var(--gold);">200%</td><td style="text-align:right;padding:9px 12px;font-weight:700;color:var(--gold);">$3.000</td><td style="padding:9px 12px;font-weight:600;">40x (dep.+bônus)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;">HELLA200</td><td style="text-align:right;padding:9px 12px;">200%</td><td style="text-align:right;padding:9px 12px;">$1.000</td><td style="padding:9px 12px;">40x (dep.+bônus)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;">STAKEMAX</td><td style="text-align:right;padding:9px 12px;">100%</td><td style="text-align:right;padding:9px 12px;">$1.000</td><td style="padding:9px 12px;">40x (dep.+bônus)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;">CSGO500</td><td style="text-align:right;padding:9px 12px;">100%</td><td style="text-align:right;padding:9px 12px;">$500</td><td style="padding:9px 12px;">40x (dep.+bônus)</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:16px;font-size:14px;color:var(--text-dim);">O MAX3000 é o único código com bônus máximo de $3.000 disponível publicamente. Com um depósito de $1.500, você recebe $3.000 de bônus, totalizando $4.500 em sala. Nenhum outro código chega perto desse teto.</p>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com guia de códigos Stake</a> &middot; <a href="https://stake.com/promotions/welcome-offer" target="_blank" rel="noopener">Stake termos da oferta de boas-vindas</a></p>
    </div>
  </section>

  <!-- HOW TO CLAIM -->
  <section class="section" id="como-ativar">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Como <span class="text-gradient-gold">Ativar</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Cadastro, verificação, depósito, chat ao vivo com MAX3000. O bônus é concedido manualmente pela operadora.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="step-card"><h3>1. Abra a porta</h3><p>Acesse o Stake.com pelo <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener">link de afiliado</a> e clique em cadastrar. Email, nome de usuário, senha, data de nascimento.</p></div>
        <div class="step-card"><h3>2. Verifique até o nível 3</h3><p>O Stake exige <strong>KYC nível 3</strong> antes de liberar o bônus de boas-vindas. Faça upload do documento de identidade, comprovante de endereço e documentação adicional do nível 3. A oferta de boas-vindas exige essa etapa.</p></div>
        <div class="step-card"><h3>3. Primeiro depósito (mínimo $10)</h3><p>Deposite entre $10 e $1.500. O match de 200% cresce proporcionalmente até o bônus máximo de $3.000. Depósitos acima de $1.500 são aceitos, mas o bônus não aumenta além de $3.000.</p></div>
        <div class="step-card"><h3>4. Solicite MAX3000 no chat ao vivo</h3><p>Após o depósito, abra o chat ao vivo do Stake e informe que se cadastrou com <span class="code-highlight">MAX3000</span> e deseja receber o bônus de boas-vindas. Após confirmação do KYC nível 3, o match de 200% é creditado em <strong>24 a 48 horas</strong>.</p></div>
      </div>
      <div style="background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.2);border-radius:12px;padding:20px 24px;margin-top:24px;">
        <p style="margin:0;font-size:14px;color:var(--text-dim);"><strong style="color:var(--gold);">Importante:</strong> O bônus de boas-vindas do Stake.com não é um campo de inserção de código automático, é um crédito concedido manualmente pela equipe de suporte. Cadastre-se pelo link de afiliado, conclua o KYC nível 3, faça o depósito e abra o chat ao vivo para informar o MAX3000. O progresso do rollover (depósito+bônus) x 40 fica visível na <strong>aba VIP</strong> após a ativação.</p>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">O maior código <span class="text-gradient-gold">do piso</span></h2>
      <p class="girl-break-sub">Sussurre <span class="code-highlight">MAX3000</span> ao dealer. 200% até $3.000 no Stake.com, e o suporte ao vivo cuida do resto.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Dar o código ao dealer</a>
    </div>
  </section>

  <!-- STAKE.US SECTION -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Jogando <span class="text-gradient-gold">nos EUA?</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">O Stake.com tem restrições nos EUA. O código MAX3000 também abre o bônus do Stake.us sweepstakes, mas a estrutura é completamente diferente.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:1fr 1fr;">
        <div class="club-card">
          <h3>Stake.us sweepstakes</h3>
          <p>Plataforma separada, moeda diferente, condições diferentes. Ao se cadastrar no Stake.us com <span class="code-highlight">MAX3000</span>, você recebe <strong>560.000 Gold Coins + 56 Stake Cash + 3,5% de rakeback vitalício</strong>. Gold Coins são para jogar; o Stake Cash pode ser convertido em prêmios após 3x de jogo. Não há depósitos ou saques em dinheiro real, não há apostas esportivas, apenas cassino.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Abrir Stake.us com MAX3000</a>
        </div>
        <div class="club-card">
          <h3>Por que plataformas separadas?</h3>
          <p>O Stake.com opera com moeda real sob licença Curaçao e tem restrições em território americano. O Stake.us opera sob o modelo de sweepstakes dos EUA, que é legal em 37 estados. São entidades jurídicas diferentes: Stake.com é a Medium Rare NV; Stake.us é a Sweepsteaks Limited. Uma conta em uma não acessa a outra. O código MAX3000 funciona nas duas, mas gera benefícios distintos em cada plataforma.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FINE PRINT -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Termos <span class="text-gradient-gold">sem letra miúda</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Sem PDFs enterrados. Os termos reais em linguagem direta.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Rollover: 40x sobre depósito+bônus</h3>
          <p>O rollover incide sobre o valor combinado de depósito e bônus, não apenas sobre o bônus. $500 de depósito + $1.000 de bônus = $1.500 x 40 = $60.000 de rollover. Faça as contas antes de buscar o bônus máximo.</p>
        </div>
        <div class="club-card">
          <h3>KYC nível 3 obrigatório</h3>
          <p>O Stake opera em etapas de verificação. O nível 1 permite apostar, o nível 2 eleva os limites de depósito, o <strong>nível 3</strong> é a verificação documental que libera o bônus de boas-vindas e saques grandes. Acesse configurações, verificação, e envie documento de identidade, comprovante de endereço e documentação do nível 3.</p>
        </div>
        <div class="club-card">
          <h3>Contribuição por tipo de jogo</h3>
          <p>Slots e jogos de cassino com edge acima de 4% contribuem 100% para o rollover. Apostas esportivas contribuem 75%. Jogos ao vivo e slots com edge abaixo de 4% contribuem com taxa reduzida ou zero. Foque nos Stake Originals ou em slots com edge acima de 4%.</p>
        </div>
        <div class="club-card">
          <h3>Concessão manual</h3>
          <p>Após o primeiro depósito, entre em contato com o suporte ao vivo informando o MAX3000. A equipe verifica o KYC nível 3 e credita o match de 200% em <strong>24 a 48 horas</strong>. Não existe campo de inserção de código automático. O bônus de boas-vindas é concedido manualmente pela operadora.</p>
        </div>
        <div class="club-card">
          <h3>Apenas para novos clientes</h3>
          <p>O MAX3000 se aplica apenas ao primeiro depósito de uma nova conta no Stake.com. Contas existentes não podem usar retroativamente. Depósitos subsequentes não se qualificam para esta oferta de boas-vindas.</p>
        </div>
        <div class="club-card">
          <h3>Depósito mínimo e restrições</h3>
          <p>O depósito mínimo para ativar a oferta é $10, com depósito máximo qualificável de $1.500. EUA, Reino Unido, Austrália e a maior parte da Europa têm restrições no stake.com. Jogadores nos EUA devem usar o <a href="/pt-br/stake-us-bonus/" style="color:var(--gold);">Stake.us</a>; outros devem verificar a <a href="/pt-br/mirror/" style="color:var(--gold);">página de espelhos</a> para o domínio da sua região.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com código Stake</a> &middot; <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake Help Center, bônus de boas-vindas</a></p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Perguntas <span class="text-gradient-gold">na entrada</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">MAX3000 é o maior código de bônus do Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. 200% até $3.000 com rollover 40x sobre depósito+bônus. A maioria dos códigos públicos fica em 100% e $1.000. MAX3000 é o código que o clube entrega na porta.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Como o rollover funciona na prática?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>O rollover é calculado sobre depósito+bônus combinados, multiplicado por 40. Com $500 de depósito e $1.000 de bônus, o total é $1.500, e o rollover é $60.000. Slots com edge acima de 4% contribuem 100%, apostas esportivas 75%. O progresso fica visível na aba VIP após a ativação.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O bônus é automático ou manual?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Manual. Após o cadastro pelo link de afiliado, a conclusão do KYC nível 3 e o primeiro depósito, você precisa abrir o chat ao vivo do Stake e informar que se cadastrou com MAX3000. A equipe verifica e credita o bônus em 24 a 48 horas.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Posso usar o bônus em apostas esportivas?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. Apostas esportivas contribuem 75% para o rollover. Slots e jogos de cassino com edge acima de 4% contribuem 100%. Você pode dividir o rollover entre os dois, mas slots são mais eficientes para limpar o requisito.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O que recebo no Stake.us com MAX3000?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>No Stake.us (plataforma separada para os EUA), o MAX3000 entrega 560.000 Gold Coins + 56 Stake Cash + 3,5% de rakeback vitalício. Diferente do Stake.com, não há depósito em dinheiro real envolvido.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Diga ao dealer que o WinnersClub mandou você.</p>
    </div>
  </section>
"""

    result = head_section + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_ptbr_about():
    src = get_head_and_footer(f"{BASE}/pt-br/about-stake/index.html")
    head_section = re.search(r'^(.*?<body>)', src, re.DOTALL).group(1)
    header_match = re.search(r'(<header.*?</header>)', src, re.DOTALL)
    header_html = header_match.group(1) if header_match else ''
    footer_match = re.search(r'(<!-- STICKY CTA -->.*)', src, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ''
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Se você encontrou esta página, quer saber de tudo.</p>
        <h1 class="ch-title text-gradient-gold">As pessoas por trás do Stake.<span class="h1-sub">Dois australianos, um RuneScape, um império de $5,6B.</span></h1>
        <p class="ch-sub">Dois caras de Melbourne que se conheceram no RuneScape construíram o maior cassino de criptomoedas do mundo sem nunca vender a empresa. GGR total de $4.7B. $339M on-chain. O clube está no Stake desde 2017, e o código <span class="code-highlight">MAX3000</span> abre 200% de bônus.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Entrar no Stake.com</a>
          <a href="/pt-br/reserves/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Ver reservas on-chain</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span></div></div>

  <!-- SCALE NUMBERS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">A escala <span class="text-gradient-gold">em números</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Não é uma startup. É o tamanho da casa que você está entrando.</p>
      </div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">GGR</div><div class="ic-value">$4.7B</div><div class="ic-detail">Receita bruta de jogo reportada. Maior que muitos cassinos físicos de Las Vegas combinados. Processou mais de $180B em depósitos anuais.</div></div>
        <div class="intel-card"><div class="ic-label">Contas</div><div class="ic-value">21M</div><div class="ic-detail">21 milhões de contas registradas no Stake.com. Usuários ativos concentrados no Brasil, Ásia, Europa do Leste e Oceania.</div></div>
        <div class="intel-card"><div class="ic-label">Reservas on-chain</div><div class="ic-value">$339.53M</div><div class="ic-detail">Rastreadas publicamente via Arkham Intel. Ethereum 74%, Solana 14%, stablecoin de 9 dígitos. Snapshot: 28 mai 2026.</div></div>
        <div class="intel-card"><div class="ic-label">Receita FY2025</div><div class="ic-value">A$970M</div><div class="ic-detail">Easygo Group Holdings (matriz). Lucro líquido A$257M. Impostos pagos A$152M. 636 funcionários. Crescimento de menos de $100M para mais de $2B em dois anos.</div></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight, Easygo FY2025</a> &middot; <a href="https://www.bloomberg.com/features/2026-stake-drake-crypto-casino-adin-ross-gambling/" target="_blank" rel="noopener">Bloomberg, volume de depósitos Stake</a></p>
    </div>
  </section>

  <!-- FOUNDERS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Os <span class="text-gradient-gold">Fundadores</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Dois australianos. Se conheceram no RuneScape. Construíram um império de $5,6B sem capital externo.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));">
        <div class="club-card" style="text-align:center;">
          <h3>Ed Craven</h3>
          <p style="font-size:12px;color:var(--text-muted);margin:-8px 0 14px;text-transform:uppercase;letter-spacing:.08em;">Cofundador &middot; CEO Easygo</p>
          <p>Nascido em 1995, Melbourne, Austrália. O rosto público. Craven afirma ter ganho $6.000 num cruzeiro com sua família aos doze anos, o que o levou a uma obsessão por estatísticas de jogo. Estudou no Bishop Druitt College em Coffs Harbour, demonstrando interesse precoce em código e criptomoedas. Na adolescência, liderou o maior clã de dados do RuneScape com o apelido "Apple", onde conheceu Tehrani. O próprio nome "Stake" é uma homenagem direta a essa origem no RuneScape. Até o final de 2021, usou publicamente apenas o pseudônimo <strong>"Edd Miroslav"</strong>, ocultando deliberadamente sua identidade real na internet. Em outubro de 2024, a Forbes Australia avaliou o patrimônio combinado com Tehrani em <strong>US$5,6B</strong>. A lista de ricos da AFR 2025 registra o patrimônio individual de Craven em <strong>A$4,82B</strong>. Em 2022, comprou uma mansão em Toorak, Melbourne, por A$80M, o maior negócio imobiliário residencial da história do bairro.</p>
        </div>
        <div class="club-card" style="text-align:center;">
          <h3>Bijan Tehrani</h3>
          <p style="font-size:12px;color:var(--text-muted);margin:-8px 0 14px;text-transform:uppercase;letter-spacing:.08em;">Cofundador &middot; Coproprietário do Kick</p>
          <p>De pais iranianos, nascido nos EUA, posteriormente mudou para Melbourne, onde vive até hoje. O parceiro mais discreto. Cuida das operações, da estrutura corporativa e do maquinário nos bastidores da casa. Tehrani é coproprietário do Kick, a plataforma de streaming. Estrutura de propriedade: Ashwood Holdings 50%, Bijan Tehrani pessoalmente 50%. Patrimônio estimado pela Forbes em maio de 2025: <strong>$2,8B</strong>. Em 2023, comprou uma casa de cidade na "Millionaires' Row" de Manhattan por <strong>$47M</strong>, uma das transações residenciais mais altas de Nova York naquele ano.</p>
        </div>
      </div>
      <p style="margin-top:20px;font-size:15px;color:var(--text-dim);max-width:700px;">"Stake" é uma referência direta às suas origens no RuneScape, onde o jogo tinha um mecanismo de apostas em que jogadores apostavam itens em duelos. Craven e Tehrani se conheceram através da comunidade de dados na adolescência e juntos começaram a construir ferramentas de jogo Bitcoin, sem parar praticamente desde então.</p>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://en.wikipedia.org/wiki/Ed_Craven" target="_blank" rel="noopener">Wikipedia, Ed Craven</a> &middot; <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">Wikipedia, Bijan Tehrani</a> &middot; <a href="https://www.forbes.com.au/news/billionaires/how-ed-craven-and-bijan-tehrani-built-their-5-6-billion-fortune/" target="_blank" rel="noopener">Forbes Australia, perfil dos fundadores</a></p>
    </div>
  </section>

  <!-- ORIGIN STORY -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">A <span class="text-gradient-gold">Origem</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Antes do Stake havia o Primedice. Antes do Primedice havia o RuneScape. O fio completo.</p>
      </div>
      <div class="club-body">
        <p>Em <strong>maio de 2013</strong>, Craven e Tehrani lançaram o <strong>Primedice</strong>, um site de dados Bitcoin que popularizou o sistema de verificação criptográfica de resultados (provably fair) que hoje é padrão em toda a indústria de jogo com criptomoedas. Não foi o primeiro site de dados Bitcoin, mas foi o primeiro a operar completamente off-chain com apostas instantâneas, sem taxas e com prova de honestidade de código aberto verificável por qualquer pessoa. Esse conceito de aleatoriedade transparente e verificável se tornou o fundamento filosófico do Stake.</p>
        <p style="margin-top:12px;">O Primedice funcionou por <strong>12 anos</strong> antes de anunciar o encerramento em 2025, direcionando os jogadores para o Stake.com. O jogo de dados do Primedice sobreviveu como "Prime Dice" dentro dos Stake Originals.</p>
        <p style="margin-top:12px;">Na <strong>primavera de 2016</strong>, Craven e Tehrani abriram um escritório em Melbourne e fundaram a <strong>Easygo Solutions</strong> com 18 funcionários para desenvolver tecnologia própria de cassino. O <strong>Stake.com foi lançado em 2017</strong>, operando sob a Medium Rare N.V. em Curaçao e mirando o público nativo de criptomoedas que o Primedice havia demonstrado existir. O crescimento foi inicialmente lento e impulsionado por streamers, mas os contratos de streaming na Twitch durante a pandemia transformaram uma marca conhecida num fenômeno. O Stake foi de $100M a $2B em faturamento em menos de dois anos.</p>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://en.wikipedia.org/wiki/Primedice" target="_blank" rel="noopener">Wikipedia, história do Primedice</a> &middot; <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">Wikipedia, Bijan Tehrani</a></p>
    </div>
  </section>

  <!-- CORPORATE STRUCTURE -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Estrutura <span class="text-gradient-gold">Corporativa</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Múltiplas entidades. Uma cadeia de controle. Entenda a estrutura.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Easygo Group Holdings</h3>
          <p>Holding australiana. Ed Craven como único diretor. Resultados FY2025: <strong>receita A$970M</strong>, <strong>lucro líquido A$257M</strong>, <strong>patrimônio líquido A$5B</strong>, <strong>imposto de renda A$152M</strong>, <strong>636 funcionários</strong>. Detém o Stake.com e o Kick.com por meio de subsidiárias.</p>
        </div>
        <div class="club-card">
          <h3>Medium Rare N.V.</h3>
          <p>Entidade registrada em Curaçao que opera o Stake.com. Endereço: Korporaalweg 10, Willemstad, Curaçao. Detém a <strong>licença Curaçao OGL/2024/1451/0918</strong>. Todos os domínios espelho também são operados pela Medium Rare N.V., não são piratas de terceiros. Processamento de pagamentos via subsidiária em Nicósia, Chipre.</p>
        </div>
        <div class="club-card">
          <h3>Kick Streaming Pty Ltd</h3>
          <p>Plataforma de streaming fundada em 14 de novembro de 2022. Holding: Easygo Entertainment Pty Ltd. Estrutura: Ashwood Holdings 50%, Bijan Tehrani 50% pessoalmente. A proposta central foi a divisão de receita 95/5 para streamers (vs. 50/50 da Twitch). No terceiro trimestre de 2025, o Kick era a quarta plataforma de livestreaming mais assistida do mundo.</p>
        </div>
        <div class="club-card">
          <h3>Stake.us (Sweepsteaks Limited)</h3>
          <p>Plataforma de sweepstakes americano juridicamente separada operada pela <strong>Sweepsteaks Limited</strong>. Gold Coins para jogar; o Stake Cash é convertível em prêmios após 3x de jogo, sem apostas em dinheiro real direto, sem criptomoedas. Disponível em <strong>37 estados americanos</strong>. O <strong>MAX3000 também é reconhecido no Stake.us</strong> e desbloqueia 560.000 GC + 56 SC + 3,5% de rakeback.</p>
        </div>
      </div>
      <p style="margin-top:16px;font-size:14px;color:var(--text-dim);"><strong>Escritórios:</strong> Melbourne, Austrália (hub de tecnologia principal, sede da Easygo); Belgrado, Sérvia (operações); Nicósia, Chipre (processamento de pagamentos); Brasil, Colômbia e Peru também possuem escritórios abertos para expansão na América Latina.</p>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight, Easygo FY2025</a> &middot; <a href="https://en.wikipedia.org/wiki/Kick_(service)" target="_blank" rel="noopener">Wikipedia, Kick</a></p>
    </div>
  </section>

  <!-- GIRL BREAK - RESERVES -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">O dinheiro está <span class="text-gradient-gold">on-chain</span></h2>
      <p class="girl-break-sub">Reservas Arkham de $339.53M em 28 de maio de 2026. Rastreáveis publicamente. <a href="/pt-br/reserves/" style="color:var(--gold);">Ver detalhes completos &rarr;</a></p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Entrar com MAX3000</a>
    </div>
  </section>

  <!-- SPONSORSHIPS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Patrocínios <span class="text-gradient-gold">e Parcerias</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Nenhuma empresa de jogo comprou mais imóveis culturais no mundo.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Drake</h3>
          <p>Contrato de 2022. Valor reportado de <strong>US$100M/ano</strong>, renegociado para até US$180M segundo alguns relatos. Drake transmitiu sessões de jogo ao vivo no Stake várias vezes. Em junho de 2026, a relação permanece ativa, com a bio oficial do Stake no X dizendo "@Drake approved".</p>
        </div>
        <div class="club-card">
          <h3>Trainwreckstv</h3>
          <p>Um dos streamers mais antigos do Stake. Declarou abertamente em suas transmissões ter recebido <strong>$360M em 16 meses</strong>. Em julho de 2025, ganhou <strong>$37,5M</strong> no Hex Appeal, desenvolvido pela Massive Studios exclusivamente para o Stake, estabelecendo um recorde mundial de vitória em slots online. Aposta de $6.000, multiplicador máximo de 50.000x.</p>
        </div>
        <div class="club-card">
          <h3>Everton FC</h3>
          <p>Anunciado em junho de 2022, efetivo a partir de 1 de julho de 2022. Avaliado em <strong>£10M/ano</strong>, o maior contrato de patrocínio frontal de uniforme em 144 anos de história do Everton. Contrato de vários anos.</p>
        </div>
        <div class="club-card">
          <h3>Stake F1 Team Kick Sauber</h3>
          <p>O Stake entrou como coproprietário de título da Sauber em 2023. Em 2024, tornou-se único parceiro de título, e o time correu como <strong>"Stake F1 Team KICK Sauber"</strong> em 2024 e 2025. A partir de 2026, o time passou por rebranding para Audi após a aquisição.</p>
        </div>
        <div class="club-card">
          <h3>UFC</h3>
          <p>Janeiro de 2021: Israel Adesanya como primeiro embaixador global de marca. Fevereiro de 2022: parceiro oficial de apostas para América Latina e Ásia. Fevereiro de 2024: parceiro oficial de nível premium global. Lutadores adicionais: Francis Ngannou, Alex Pereira, Merab Dvalishvili, Alexandre Pantoja e Caio Borralho.</p>
        </div>
        <div class="club-card">
          <h3>Sergio Agüero</h3>
          <p>Contratado em 1 de fevereiro de 2022. O Stake filmou comerciais para a Copa do Mundo FIFA 2022 com Agüero, Eden Hazard, Iker Casillas e Patrice Evra. Agüero ganhou a Copa América com a Argentina em 2021, conexão que levou ao lançamento do Stake na Província de Buenos Aires em 2026.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Perguntas <span class="text-gradient-gold">na entrada</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Quem fundou o Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Ed Craven (nascido em 1995, Melbourne) e Bijan Tehrani. Se conheceram através da comunidade de dados do RuneScape na adolescência. Fundaram o Primedice em 2013 e o Stake.com em 2017. Nunca buscaram financiamento externo. O patrimônio combinado estimado pela Forbes Australia em 2024 foi de US$5,6B.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O Stake.com é confiável?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>O Stake opera desde 2017 sob licença Curaçao OGL/2024/1451/0918 pela Medium Rare NV. As reservas on-chain em 28 de maio de 2026 são $339.53M, rastreáveis publicamente na Arkham. A matriz Easygo reportou A$970M de receita e A$257M de lucro líquido no FY2025, com A$152M de impostos pagos.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O que é o Stake Engine?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Uma plataforma de servidor de jogos remoto (RGS) lançada em abril de 2025 que permite a estúdios externos publicar jogos na infraestrutura do Stake. Gerou $3,31B em volume no primeiro ano. Parceiros: Massive Studio e Twist Gaming.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Qual é a relação do Stake com o Kick?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>O Kick Streaming foi fundado em novembro de 2022 pela Easygo Entertainment (subsidiária da Easygo Group Holdings) e por Bijan Tehrani pessoalmente. A estrutura é: Ashwood Holdings (relacionada à Easygo) 50%, Tehrani 50%. O Kick oferece divisão de receita 95/5 para streamers, em contraste com a Twitch.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Diga ao dealer que o WinnersClub mandou você.</p>
    </div>
  </section>
"""
    
    result = head_section + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_ptbr_mirror():
    src = get_head_and_footer(f"{BASE}/pt-br/mirror/index.html")
    head_section = re.search(r'^(.*?<body>)', src, re.DOTALL).group(1)
    header_match = re.search(r'(<header.*?</header>)', src, re.DOTALL)
    header_html = header_match.group(1) if header_match else ''
    footer_match = re.search(r'(<!-- STICKY CTA -->.*)', src, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ''
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Se você encontrou esta página, a porta já está meio aberta.</p>
        <h1 class="ch-title text-gradient-gold">Mais de 20 portas, uma casa.<span class="h1-sub">Diretório completo de espelhos do Stake.</span></h1>
        <p class="ch-sub">O diretório completo de espelhos do Stake: por que cada domínio existe, qual usar na sua região, como distinguir espelhos reais de falsificações. O código <span class="code-highlight">MAX3000</span> funciona em todos os espelhos.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Entrar com MAX3000</a>
          <a href="/pt-br/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Código Promo MAX3000</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span></div></div>

  <!-- WHY MIRRORS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Por que o Stake usa <span class="text-gradient-gold">domínios espelho</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Não é falta de transparência. É infraestrutura contra censura de DNS e reguladores agressivos.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Brasil: 5.200 domínios bloqueados</h3>
          <p>Em 2024, o Brasil bloqueou mais de 5.200 domínios de jogo online, incluindo o stake.com original. O Stake respondeu com espelhos regionais. O Pix ainda funciona via MoonPay para depósitos em fiat. Brasileiros representam uma fatia significativa da base de jogadores global do Stake.</p>
        </div>
        <div class="club-card">
          <h3>Índia: filtros DNS dos ISPs</h3>
          <p>Operadoras de telecomunicações indianas implementaram filtros de DNS de camada 3 que bloqueiam o stake.com em algumas redes. Os espelhos com diferentes TLDs escapam da lista de bloqueio. A carteira não muda entre domínios, apenas o ponto de entrada.</p>
        </div>
        <div class="club-card">
          <h3>Filipinas, Turquia, Japão</h3>
          <p>Cada jurisdição tem abordagens diferentes para o jogo online. Em vez de sair de mercados inteiros, o Stake mantém domínios alternativos que ficam fora das listas de bloqueio locais. Todos são operados pela mesma entidade legal, a Medium Rare N.V.</p>
        </div>
        <div class="club-card">
          <h3>Exclusões de loja de apps</h3>
          <p>A Apple e o Google removem periodicamente apps de jogo de regiões específicas. Domínios espelho com webapps mobile separados contornam as remoções da App Store sem perder funcionalidade para o jogador.</p>
        </div>
        <div class="club-card">
          <h3>Distribuição de carga de servidor</h3>
          <p>Não é apenas questão regulatória. Alguns espelhos servem como nós de CDN para regiões com latência alta para o servidor principal. Isso melhora o desempenho para jogadores em jogos ao vivo que necessitam de baixa latência.</p>
        </div>
        <div class="club-card">
          <h3>VPN: caminho com mais risco</h3>
          <p>Uma VPN pode parecer mais simples, mas aumenta o risco de KYC. Se o Stake detectar uma discrepância entre seu IP e seu documento de identidade verificado, a conta pode ser marcada para revisão de compliance. Usar um espelho autorizado na sua região é mais seguro.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN MIRRORS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Lista de <span class="text-gradient-gold">Espelhos Principais</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Todos operados pela Medium Rare N.V. sob a mesma licença Curaçao. Mesmo backend, sincronização de carteira em tempo real.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Domínio</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Região principal</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Notas</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.com</td><td style="padding:9px 12px;">Global</td><td style="padding:9px 12px;">Domínio principal. Bloqueado em alguns países.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.games</td><td style="padding:9px 12px;">Global</td><td style="padding:9px 12px;">Principal espelho alternativo. Funcionalidade completa.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.bet</td><td style="padding:9px 12px;">Global</td><td style="padding:9px 12px;">Espelho ativo com todas as funcionalidades.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">getstake.it</td><td style="padding:9px 12px;">Link de afiliado</td><td style="padding:9px 12px;">Redireciona para stake.com com parâmetros de rastreamento. Usado pelo MAX3000.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake1.com a stake8.com</td><td style="padding:9px 12px;">Específico por país</td><td style="padding:9px 12px;">Série de numeração para jurisdições onde TLDs alternativos contornam bloqueios.</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">stake.us</td><td style="padding:9px 12px;">EUA (37 estados)</td><td style="padding:9px 12px;">Plataforma separada. Sweepstakes. Operada pela Sweepsteaks Limited, não pela Medium Rare NV.</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">Acesso em qualquer lugar <span class="text-gradient-gold">com MAX3000</span></h2>
      <p class="girl-break-sub">O código <span class="code-highlight">MAX3000</span> funciona em todos os espelhos oficiais. 200% até $3.000, não importa qual porta você usa.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Dar o código ao dealer</a>
    </div>
  </section>

  <!-- HOW TO VERIFY -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Como verificar <span class="text-gradient-gold">espelhos reais</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Phishing existe. Veja como identificar se você está no espelho correto.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>1. Verifique o certificado SSL</h3>
          <p>Clique no cadeado no navegador. O certificado deve ser emitido para um domínio stake.*. Certificados expirados ou emitidos para domínios diferentes são sinal vermelho imediato.</p>
        </div>
        <div class="club-card">
          <h3>2. Registro WHOIS</h3>
          <p>Espelhos oficiais do Stake têm registros WHOIS com informações de organização Medium Rare ou privacidade de registrante habilitada por um registrador legítimo. Registros novos (menos de 30 dias) são suspeitos.</p>
        </div>
        <div class="club-card">
          <h3>3. Layout e provedores corretos</h3>
          <p>Espelhos reais mostram os mesmos Stake Originals, provedores como Evolution e Pragmatic, e o mesmo design. Se o layout estiver diferente ou os jogos estiverem faltando, não insira suas credenciais.</p>
        </div>
        <div class="club-card">
          <h3>4. Fonte do link</h3>
          <p>Acesse espelhos por links de afiliados confiáveis ou pela própria lista de domínios do Stake. Links em mensagens não solicitadas no Telegram, WhatsApp ou e-mail são vetores de phishing comuns.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- WALLET SYNC -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Sincronização <span class="text-gradient-gold">de carteira</span></h2>
      </div>
      <div class="club-body">
        <p>Todos os espelhos oficiais do Stake compartilham o mesmo backend de banco de dados. Quando você acessa qualquer espelho com o mesmo nome de usuário e senha, você vê o mesmo saldo, histórico de apostas, progresso VIP e bônus ativos. Não é necessário transferir fundos entre domínios. A carteira é a mesma, independentemente do domínio que você usar para acessar.</p>
        <p style="margin-top:12px;">Isso funciona porque todos os domínios espelho apontam para a mesma infraestrutura de servidores gerenciada pela Medium Rare N.V. O domínio é apenas o ponto de entrada DNS. O backend que processa suas apostas, mantém seu saldo e acompanha seu progresso VIP é único e compartilhado.</p>
      </div>
    </div>
  </section>

  <!-- STAKE.COM vs STAKE.US -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake.us vs Stake.com: <span class="text-gradient-gold">dois produtos, um código</span></h2>
      </div>
      <div class="club-grid" style="grid-template-columns:1fr 1fr;">
        <div class="club-card">
          <h3>Stake.com, entrada global</h3>
          <p>Moeda real, criptomoedas e fiat. Esportes, cassino, originais, pôquer. Disponível na maioria dos países exceto EUA, Reino Unido, Austrália e alguns outros. Licença Curaçao OGL/2024/1451/0918. Com <span class="code-highlight">MAX3000</span>: 200% até $3.000 de bônus.</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Abrir porta global</a>
        </div>
        <div class="club-card">
          <h3>Stake.us, entrada americana</h3>
          <p>Sweepstakes. Gold Coins para jogar, Stake Cash resgatável. Sem apostas em dinheiro real, apenas cassino. Disponível em 37 estados americanos. Operado pela Sweepsteaks Limited. Com <span class="code-highlight">MAX3000</span>: 560.000 GC + 56 SC + 3,5% de rakeback.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Abrir porta americana</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Perguntas <span class="text-gradient-gold">na entrada</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Os espelhos do Stake são seguros?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Os espelhos oficiais do Stake são todos operados pela Medium Rare N.V. sob a mesma licença Curaçao OGL/2024/1451/0918. Eles não são sites de terceiros: são domínios alternativos do mesmo operador, compartilhando o mesmo backend. Verifique sempre o certificado SSL e a fonte do link.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Minha carteira funciona em todos os espelhos?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. Todos os espelhos oficiais compartilham o mesmo backend. Faça login com suas credenciais em qualquer espelho e você verá o mesmo saldo, histórico e progresso VIP. Não é necessária transferência de fundos.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">O MAX3000 funciona em todos os espelhos?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. O MAX3000 funciona em qualquer domínio espelho oficial do Stake.com. No Stake.us, o mesmo código também é reconhecido, mas com benefícios distintos (sweepstakes).</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Devo usar VPN para acessar o Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Não é recomendado. VPNs podem criar discrepâncias entre o IP detectado e o documento de identidade verificado durante o KYC, o que pode marcar a conta para revisão de compliance. Usar um espelho oficial na sua região é mais seguro.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Diga ao dealer que o WinnersClub mandou você.</p>
    </div>
  </section>
"""
    
    result = head_section + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_ptbr_payments():
    src = get_head_and_footer(f"{BASE}/pt-br/payments/index.html")
    head_section = re.search(r'^(.*?<body>)', src, re.DOTALL).group(1)
    header_match = re.search(r'(<header.*?</header>)', src, re.DOTALL)
    header_html = header_match.group(1) if header_match else ''
    footer_match = re.search(r'(<!-- STICKY CTA -->.*)', src, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ''
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Se você encontrou esta página, veio falar de dinheiro.</p>
        <h1 class="ch-title text-gradient-gold">Entra e sai.<span class="h1-sub">22 criptomoedas, rotas fiat locais, KYC em 4 etapas, saques desde $2,50.</span></h1>
        <p class="ch-sub">Mais de 22 criptomoedas, rotas de depósito fiat regionais, 4 níveis de KYC e saques sem limite máximo definido a partir de $2,50. Com o código <span class="code-highlight">MAX3000</span>, o Stake.com oferece 200% até $3.000 no primeiro depósito, com rollover 40x, KYC nível 3 obrigatório.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Entrar com MAX3000</a>
          <a href="/pt-br/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Código MAX3000</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span><span>Stake on-chain agora: reservas rotuladas $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Licença Curaçao OGL/2024/1451/0918 &middot; Fonte: Arkham Intel via cryptotips.com &middot; Snapshot 28 mai 2026</span></div></div>

  <!-- KEY NUMBERS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Números <span class="text-gradient-gold">chave</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">O Stake processa mais de $180B em depósitos anuais. Veja como o caixa funciona.</p>
      </div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">Criptomoedas aceitas</div><div class="ic-value">22+</div><div class="ic-detail">Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Tron, Solana e mais. Depósito mínimo varia por moeda.</div></div>
        <div class="intel-card"><div class="ic-label">Saque mínimo</div><div class="ic-value">$2,50</div><div class="ic-detail">Sem limite máximo definido pelo Stake. Saques grandes podem acionar revisão de compliance de 2 a 4 dias úteis.</div></div>
        <div class="intel-card"><div class="ic-label">Volume anual</div><div class="ic-value">$180B</div><div class="ic-detail">Depósitos totais processados anualmente. Demonstra escala operacional e liquidez da plataforma.</div></div>
        <div class="intel-card"><div class="ic-label">Velocidade cripto</div><div class="ic-value">30 a 60 min</div><div class="ic-detail">Para saques normais em criptomoeda. TRX, XRP, SOL liquidam em segundos. Grandes volumes podem levar 2 a 4 dias úteis.</div></div>
      </div>
    </div>
  </section>

  <!-- CRYPTO METHODS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Criptomoedas <span class="text-gradient-gold">aceitas</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">A via principal. Todas as principais chains suportadas. Mínimos de saque expressos em moeda nativa.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Moeda</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Network</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Velocidade de saque</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Notas</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Bitcoin (BTC)</td><td style="padding:9px 12px;">Bitcoin mainnet</td><td style="text-align:right;padding:9px 12px;">30 a 60 min</td><td style="text-align:right;padding:9px 12px;">Taxa de rede variável</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Ethereum (ETH)</td><td style="padding:9px 12px;">ERC-20</td><td style="text-align:right;padding:9px 12px;">30 a 60 min</td><td style="text-align:right;padding:9px 12px;">Gas fees aplicáveis</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Litecoin (LTC)</td><td style="padding:9px 12px;">Litecoin</td><td style="text-align:right;padding:9px 12px;">20 a 40 min</td><td style="text-align:right;padding:9px 12px;">Taxa baixa</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">USDT</td><td style="padding:9px 12px;">TRC-20 / ERC-20</td><td style="text-align:right;padding:9px 12px;">Segundos (TRC)</td><td style="text-align:right;padding:9px 12px;">TRC-20 mais barato</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Tron (TRX)</td><td style="padding:9px 12px;">Tron</td><td style="text-align:right;padding:9px 12px;">Segundos</td><td style="text-align:right;padding:9px 12px;">Mais rápido para stablecoins</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Ripple (XRP)</td><td style="padding:9px 12px;">XRP Ledger</td><td style="text-align:right;padding:9px 12px;">Segundos</td><td style="text-align:right;padding:9px 12px;">Liquidação quase instantânea</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Solana (SOL)</td><td style="padding:9px 12px;">Solana</td><td style="text-align:right;padding:9px 12px;">Segundos</td><td style="text-align:right;padding:9px 12px;">Alta velocidade, taxa baixa</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dogecoin (DOGE)</td><td style="padding:9px 12px;">Dogecoin</td><td style="text-align:right;padding:9px 12px;">20 a 40 min</td><td style="text-align:right;padding:9px 12px;">Popular na comunidade Stake</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">BNB / BSC</td><td style="padding:9px 12px;">BEP-20</td><td style="text-align:right;padding:9px 12px;">Minutos</td><td style="text-align:right;padding:9px 12px;">Taxa baixa na BSC</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://help.stake.com/en/articles/4793500-supported-currencies" target="_blank" rel="noopener">Stake Help Center, moedas aceitas</a></p>
    </div>
  </section>

  <!-- FIAT ROUTES -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Rotas de <span class="text-gradient-gold">depósito fiat</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Para quem não quer gerenciar uma carteira cripto.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>MoonPay</h3>
          <p>Converte fiat para cripto e deposita diretamente no Stake. Aceita Visa, Mastercard e transferência bancária em muitos países. Taxa: 4,5% a 5,9% dependendo do método. Saques fiat via MoonPay levam 1 a 5 dias úteis.</p>
        </div>
        <div class="club-card">
          <h3>Pix (Brasil)</h3>
          <p>Jogadores brasileiros podem usar Pix via MoonPay para conversão rápida. A liquidação Pix no Brasil é instantânea, mas a conversão para cripto adiciona 30 a 60 minutos ao processo total. Disponível 24 horas por dia, 7 dias por semana.</p>
        </div>
        <div class="club-card">
          <h3>AstroPay</h3>
          <p>Carteira digital disponível em vários países da América Latina e Europa. Aceita múltiplas moedas locais. Boa opção para mercados onde cartões de crédito têm restrições em cassinos online.</p>
        </div>
        <div class="club-card">
          <h3>Interac (Canadá)</h3>
          <p>Transferência bancária instantânea disponível para jogadores canadenses. Sem taxa de rede, liquidação em minutos. Limite por transação varia por banco.</p>
        </div>
        <div class="club-card">
          <h3>UPI (Índia)</h3>
          <p>Rota de pagamento disponível para alguns jogadores indianos via MoonPay. Sujeito a disponibilidade regional e políticas bancárias locais.</p>
        </div>
        <div class="club-card">
          <h3>Opay e MomoPay</h3>
          <p>Carteiras móveis para mercados africanos, especialmente Nigéria e países da África do Oeste. Permitem depósitos em moeda local sem necessidade de cartão de crédito.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">Depósito mínimo <span class="text-gradient-gold">de $10</span></h2>
      <p class="girl-break-sub">Com <span class="code-highlight">MAX3000</span>, o primeiro depósito de $10 já ativa o bônus de boas-vindas. Máximo de $1.500 para o bônus completo de $3.000.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Entrar com MAX3000</a>
    </div>
  </section>

  <!-- WITHDRAWAL SPEED -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Velocidade <span class="text-gradient-gold">de saque</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Cripto é a saída mais rápida. Sem atrasos de processamento além da revisão de compliance.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Método</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Tempo de processamento</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Notas</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">TRX, XRP, SOL</td><td style="padding:9px 12px;color:var(--gold);">Segundos</td><td style="padding:9px 12px;">Liquidação mais rápida disponível</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">BTC, ETH, LTC, DOGE</td><td style="padding:9px 12px;color:var(--gold);">30 a 60 min</td><td style="padding:9px 12px;">Condições normais, sem revisão de compliance</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Saques grandes</td><td style="padding:9px 12px;color:var(--gold);">2 a 4 dias úteis</td><td style="padding:9px 12px;">Revisão de compliance acionada por volume</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Fiat via MoonPay</td><td style="padding:9px 12px;color:var(--gold);">1 a 5 dias úteis</td><td style="padding:9px 12px;">Processamento bancário adicional</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- KYC LEVELS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Níveis <span class="text-gradient-gold">de KYC</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">4 etapas. Não obrigatórias para todos. Ativadas conforme o comportamento.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>Nível 1: Básico</h3>
          <p>E-mail e nome de usuário. Permite apostas. Limites de depósito e saque reduzidos. Sem upload de documentos necessário inicialmente.</p>
        </div>
        <div class="club-card">
          <h3>Nível 2: Limites ampliados</h3>
          <p>Verificação de e-mail + dados pessoais adicionais. Eleva os limites de depósito e desbloqueia mais opções de pagamento.</p>
        </div>
        <div class="club-card">
          <h3>Nível 3: Bônus de boas-vindas</h3>
          <p>Verificação documental: documento de identidade com foto, comprovante de endereço e documentação adicional específica do nível 3. Obrigatório para receber o bônus de boas-vindas MAX3000 e para saques grandes.</p>
        </div>
        <div class="club-card">
          <h3>Nível 4: Origem de fundos</h3>
          <p>Acionado para volumes muito altos ou por solicitação de compliance. Pode exigir documentação de origem de fundos, declarações de imposto de renda ou extratos bancários.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Fontes: <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">Stake Help Center, verificação de conta</a></p>
    </div>
  </section>

  <!-- RESPONSIBLE GAMBLING -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Ferramentas de <span class="text-gradient-gold">jogo responsável</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Disponíveis dentro da conta. Sem GAMSTOP, mas com limites práticos reais.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>Limite de perda</h3>
          <p>Defina uma perda máxima diária, semanal ou mensal. Quando atingida, o sistema bloqueia novas apostas até o próximo período. Configurável em conta, seção de limites.</p>
        </div>
        <div class="club-card">
          <h3>Limite de aposta</h3>
          <p>Limite máximo por aposta. Pode ser definido em valores absolutos. Útil para controlar sessões de apostas automáticas no Crash ou Dice.</p>
        </div>
        <div class="club-card">
          <h3>Autoexclusão do cassino</h3>
          <p>Remove acesso a jogos de cassino por um período definido. Apostas esportivas ainda ficam disponíveis durante a autoexclusão do cassino.</p>
        </div>
        <div class="club-card">
          <h3>Autoexclusão completa</h3>
          <p>Encerra o acesso a toda a plataforma. Pode ser de 1 semana a permanente. Contato com suporte ao vivo necessário para aplicar.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Perguntas <span class="text-gradient-gold">na entrada</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Quais criptomoedas o Stake aceita?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Mais de 22 criptomoedas, incluindo Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Tron, Solana, BNB e USDT (TRC-20 e ERC-20). Depósitos em fiat são possíveis via MoonPay, com suporte ao Pix para jogadores brasileiros.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Qual é a velocidade dos saques?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>TRX, XRP e SOL liquidam em segundos. Bitcoin, Ethereum e Litecoin levam de 30 a 60 minutos em condições normais. Saques grandes podem acionar revisão de compliance de 2 a 4 dias úteis. Saques fiat via MoonPay levam de 1 a 5 dias úteis.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Preciso do KYC nível 3 para o bônus MAX3000?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim. O Stake exige KYC nível 3 para liberar o bônus de boas-vindas. Isso inclui documento de identidade com foto, comprovante de endereço e documentação adicional do nível 3. Conclua a verificação antes de solicitar o bônus via chat ao vivo.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Posso depositar com Pix no Brasil?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Sim, via MoonPay. O Pix liquida instantaneamente no lado brasileiro, mas a conversão para cripto e o depósito no Stake adicionam de 30 a 60 minutos ao processo total. Disponível 24 horas por dia, 7 dias por semana.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Diga ao dealer que o WinnersClub mandou você.</p>
    </div>
  </section>
"""
    
    result = head_section + "\n<body>\n" + header_html + body_content + footer_html
    return result


# ---- MAIN EXECUTION ----

print("\n=== PT-BR REBUILD ===")
BASE_PTBR = f"{BASE}/pt-br"

# Casino
casino_content = rebuild_ptbr_casino()
wc = write_file(f"{BASE_PTBR}/casino/index.html", casino_content)

# Promo-code
promo_content = rebuild_ptbr_promo()
wc = write_file(f"{BASE_PTBR}/promo-code/index.html", promo_content)

# About-stake
about_content = rebuild_ptbr_about()
wc = write_file(f"{BASE_PTBR}/about-stake/index.html", about_content)

# Mirror
mirror_content = rebuild_ptbr_mirror()
wc = write_file(f"{BASE_PTBR}/mirror/index.html", mirror_content)

# Payments
payments_content = rebuild_ptbr_payments()
wc = write_file(f"{BASE_PTBR}/payments/index.html", payments_content)

print("\nPT-BR rebuild complete.")
