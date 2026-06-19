#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expand all 6 tr (Turkish) pages to 1200+ words with native Turkish content"""
import os, re

BASE = "/home/user/workspace/winnersclub.com"

def get_parts(locale_file):
    with open(locale_file, 'r', encoding='utf-8') as f:
        content = f.read()
    head = re.search(r'^(.*?<body>)', content, re.DOTALL).group(1)
    header = re.search(r'(<header.*?</header>)', content, re.DOTALL)
    header_html = header.group(1) if header else ''
    footer = re.search(r'(<!-- STICKY CTA -->.*)', content, re.DOTALL)
    footer_html = footer.group(1) if footer else ''
    return head, header_html, footer_html

def check_violations(content):
    issues = []
    vis = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
    vis_text = re.sub(r'<[^>]+>', ' ', vis)
    if re.search(r'[—–]', vis_text):
        issues.append("EM/EN DASH")
    clean_vis = re.sub(r'&[a-z#0-9]+;', ' ', vis_text)
    if '!' in clean_vis:
        issues.append("EXCLAMATION")
    if 'Welcome to WinnersClub' in content:
        issues.append("BANNED PHRASE")
    return issues

def word_count(text):
    vis = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
    vis = re.sub(r'<[^>]+>', ' ', vis)
    return len(vis.split())

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    wc = word_count(content)
    issues = check_violations(content)
    print(f"  {os.path.relpath(path, BASE)}: {wc} words{' | ISSUES: '+str(issues) if issues else ''}")
    return wc

def expand_tr_page(filepath, expansion_html, insert_before='<!-- SIGNATURE -->'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if insert_before in content:
        result = content.replace(insert_before, expansion_html + insert_before)
    else:
        # Append before footer
        footer_match = re.search(r'(<!-- STICKY CTA -->)', content)
        if footer_match:
            pos = footer_match.start()
            result = content[:pos] + expansion_html + content[pos:]
        else:
            result = content + expansion_html
    return result


# ---- TR INDEX EXPANSION ----
TR_INDEX_EXPANSION = """
  <!-- PLATFORM DEEP DIVE TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Platform <span class="text-gradient-gold">Derinlemesine</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">MAX3000 ile içeri girdikten sonra ne sizi bekliyor.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Casino: 4.000 Slot ve 18 Orijinal</h3>
          <p>Stake casino, 15 sağlayıcıdan 4.000'den fazla slot barındırıyor: Pragmatic Play, Hacksaw Gaming ve Nolimit City dahil. 18 Stake Orijinal oyununun zincir üzerinde doğrulanabilir RTP'si var. Crash, Dice, Mines, Plinko, Limbo ve HiLo %99 RTP ile çalışırken Blackjack %99,43 ile en yüksek değerde. Hiçbir geleneksel casino bu kadar düşük ev kenarı sunamaz. Canlı casino Evolution tarafından yönetiliyor, Crazy Time (maksimum 20.000x çarpan), Lightning Roulette ve Monopoly Big Baller gibi oyun şovlarıyla 24 saat 50'den fazla masa açık.</p>
        </div>
        <div class="club-card">
          <h3>Spor Bahisleri: 40 Spor Dalı</h3>
          <p>Stake spor birimi futbol, basketbol, tenis, kriket ve esporlar dahil 40'tan fazla sporu kapsıyor. Canlı bahis ve maç öncesi pazarlar mevcut. Spor bahisleri MAX3000 bonusunun çevrim şartına %75 katkıda bulunuyor, yani bonusu hem casinoda hem de sporda kullanabilirsiniz. Türk futbol severler için Süper Lig maçları da kapsama dahil.</p>
        </div>
        <div class="club-card">
          <h3>VIP: 16 Seviye, Ömür Boyu İlerleme</h3>
          <p>Stake VIP kulübü birikimli ömür boyu bahis tutarını takip eder ve asla sıfırlanmaz. Bronze ($10.000 bahis) ile %5 rake-back başlar. Platinum IV'te ($2,5 milyon) özel VIP ev sahibi atanır ve kişisel bonus müzakeresi mümkün hale gelir. Obsidian $1 milyar bahis gerektirir ve $1 milyon seviye atlama bonusu içerir. Spor bahisleri VIP ilerlemeye 3x ağırlıkla sayılır: $1.000 spor bahsi = $3.000 VIP ilerlemesi.</p>
        </div>
        <div class="club-card">
          <h3>Haftalık Promosyonlar: $315.000 Ödül Havuzu</h3>
          <p>Hoş geldin bonusunun yanı sıra Stake 8 döngüsel promosyon sürdürüyor. Günlük Yarış her gün 5.000 kişiye $100.000 dağıtıyor. Haftalık Çekiliş her $1.000 bahis için 1 bilet ile 15 kazanana $75.000 dağıtıyor. Casino Fethi haftada $50.000 paylaşıyor. Pragmatic Drops and Wins uygun Pragmatic Play slotlarına aylık $2,28 milyonun üzerinde ekliyor. Bu promosyonlara katılmak için ayrıca kayıt yaptırmanız gerekmiyor.</p>
        </div>
        <div class="club-card">
          <h3>Stake Engine: Oyun Yayın Platformu</h3>
          <p>Nisan 2025'te başlatılan Stake Engine, dış stüdyoların Stake'in altyapısında doğrudan oyun geliştirip yayınlamasına imkan tanıyan bir uzak oyun sunucusu (RGS). İlk yılında $3,31 milyar devir hacmi elde etti. Mevcut ortaklar Massive Studio (Jawsome, Swamp Things) ve Twist Gaming (Brains for Breakfast, %97,25 RTP, maksimum 10.000x). Ticari model: aylık GGR'nin %10'u, gizli ücret yok.</p>
        </div>
        <div class="club-card">
          <h3>Ödemeler: 22'den Fazla Kripto ve Fiat</h3>
          <p>Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Tron ve Solana dahil 22'den fazla kripto para birimi kabul ediliyor. Fiat para yatırma işlemleri MoonPay aracılığıyla mümkün. Normal kripto para çekimleri 30 ila 60 dakika içinde tamamlanıyor. TRX, XRP, SOL saniyeler içinde sonuçlanıyor. MAX3000 bonusunu etkinleştirmek için minimum yatırım $10. Stake'in çekim ücreti yok, sadece blok zinciri ağ ücreti uygulanıyor.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Stake slot lobisi</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com MAX3000 rehberi</a> &middot; <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake Yardım Merkezi, hoş geldin bonusu</a></p>
    </div>
  </section>

  <!-- TWO DOORS TR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">İki Kapı, <span class="text-gradient-gold">Bir Kod</span></h2>
        <p class="section-subtitle">MAX3000 hem Stake.com hem de Stake.us tarafından tanınıyor. Her kapının arkasındaki karşılama farklı. Yerinize göre doğru kapıya yönlendirileceksiniz.</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>Stake.com - Gerçek Para, Küresel</h3>
          <p>Curaçao OGL/2024/1451/0918 lisansı altında Medium Rare NV tarafından işletilen gerçek para platformu. Kripto ve fiat para kabul ediyor. Spor, casino, orijinal oyunlar, poker. <span class="code-highlight">MAX3000</span> koduyla <strong>200% $3.000'e kadar</strong>, 30 gün içinde yatırım ve bonus toplamının 40 katı çevrim şartı, minimum yatırım $10. Yatırım sonrası canlı destek aracılığıyla talep edin. KYC Seviye 3 gerekli. ABD ve İngiltere dışında çoğu ülkede kullanılabilir.</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Küresel kapıyı aç</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - Sweepstakes, ABD</h3>
          <p>Sweepsteaks Limited tarafından işletilen ABD sweepstakes platformu. Oyun için Gold Coin'ler, 3x oynandıktan sonra ödüle çevrilebilir Stake Cash. Gerçek para yatırma veya çekme yok, spor yok, yalnızca casino. <span class="code-highlight">MAX3000</span> kodu burada da tanınıyor ve <strong>560.000 GC + 56 SC + %3,5 rake-back</strong> açıyor. 37 eyalette kullanılabilir.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">ABD kapısını aç</a>
        </div>
      </div>
    </div>
  </section>

"""

# ---- TR CASINO EXPANSION ----
TR_CASINO_EXPANSION = """
  <!-- VIP TABLE TR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">VIP <span class="text-gradient-gold">Kulübü</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">16 seviye. Ömür boyu ilerleme. Bronze'dan itibaren rake-back.</p>
      </div>
      <div class="club-body">
        <p>VIP kulübü birikimli ömür boyu bahis tutarını takip eder ve asla sıfırlanmaz. Casino bahisleri 1:1 sayılır, spor bahisleri 3 kat sayılır (spor $1.000 = VIP ilerlemesi $3.000). Rake-back <strong>Bronze ($10.000 bahis)</strong> ile %5 olarak başlar ve her seviyede artar. Platinum IV'ten itibaren kişisel müzakere için özel VIP ev sahibi atanır. 1 milyar dolarlık Obsidian kilometre taşı $1 milyon seviye atlama bonusu içerir ve dünya genelinde yalnızca çok az sayıda oyuncu bu seviyeye ulaşmıştır.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:20px;">
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">Seviye</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">Ömür Boyu Bahis</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">Seviye Bonusu</th>
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">Ana Avantaj</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Bronze</td><td style="text-align:right;padding:8px 12px;">$10.000</td><td style="text-align:right;padding:8px 12px;">$15</td><td style="padding:8px 12px;">%5 rake-back aktif</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Silver</td><td style="text-align:right;padding:8px 12px;">$50.000</td><td style="text-align:right;padding:8px 12px;">Yok</td><td style="padding:8px 12px;">Haftalık ve aylık bonus artışı</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Gold</td><td style="text-align:right;padding:8px 12px;">$100.000</td><td style="text-align:right;padding:8px 12px;">$110</td><td style="padding:8px 12px;">Aylık bonus aktif</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum I</td><td style="text-align:right;padding:8px 12px;">$250.000</td><td style="text-align:right;padding:8px 12px;">$200</td><td style="padding:8px 12px;">Günlük yenileme bonusu</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum IV</td><td style="text-align:right;padding:8px 12px;">$2.500.000</td><td style="text-align:right;padding:8px 12px;">Yok</td><td style="padding:8px 12px;">Özel VIP ev sahibi</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond I</td><td style="text-align:right;padding:8px 12px;">$25.000.000</td><td style="text-align:right;padding:8px 12px;">$20.000</td><td style="padding:8px 12px;">Yenilenebilir reload, etkinlik davetleri</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond V</td><td style="text-align:right;padding:8px 12px;">$500.000.000</td><td style="text-align:right;padding:8px 12px;">$400.000</td><td style="padding:8px 12px;">Stake Sphere ve özel canlı etkinlikler</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;font-weight:700;color:var(--gold);">Obsidian</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1.000.000.000</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1.000.000</td><td style="padding:8px 12px;font-weight:600;">En yüksek prestij. Her şey tamamen özel.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://stake.com/vip" target="_blank" rel="noopener">Stake VIP sayfası</a> &middot; <a href="https://help.stake.com/en/articles/4793501-what-is-the-stake-vip-program" target="_blank" rel="noopener">Stake Yardım Merkezi, VIP programı</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake rehberi</a></p>
    </div>
  </section>

  <!-- ORIGINALS TABLE TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Originals</span> RTP Tablosu</h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Easygo tarafından geliştirilen 18 oyun. Tümü kanıtlanabilir adil. Çoğunun ev kenarı sadece %1.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Oyun</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">RTP</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Ev Kenarı</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Maksimum Çarpan</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Blackjack</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99,43</td><td style="text-align:right;padding:9px 12px;">%0,57</td><td style="text-align:right;padding:9px 12px;">2,5x (3:2 Blackjack)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dice</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99</td><td style="text-align:right;padding:9px 12px;">%1</td><td style="text-align:right;padding:9px 12px;">9.900.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Mines</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99</td><td style="text-align:right;padding:9px 12px;">%1</td><td style="text-align:right;padding:9px 12px;">5.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Crash</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99</td><td style="text-align:right;padding:9px 12px;">%1</td><td style="text-align:right;padding:9px 12px;">1.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Plinko</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99</td><td style="text-align:right;padding:9px 12px;">%1</td><td style="text-align:right;padding:9px 12px;">1.000x (yüksek risk, 16 satır)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Limbo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%99</td><td style="text-align:right;padding:9px 12px;">%1</td><td style="text-align:right;padding:9px 12px;">1.000.000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Slide</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%98-99</td><td style="text-align:right;padding:9px 12px;">%1-2</td><td style="text-align:right;padding:9px 12px;">4.294.967.000x (4,29 milyar)</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dragon Tower</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%98</td><td style="text-align:right;padding:9px 12px;">%2</td><td style="text-align:right;padding:9px 12px;">256.901x (Master modu)</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Roulette</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">%97,3</td><td style="text-align:right;padding:9px 12px;">%2,7</td><td style="text-align:right;padding:9px 12px;">35x (tek sayı)</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://stake.com/casino/group/stake-originals" target="_blank" rel="noopener">Stake Originals kataloğu</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake rehberi</a></p>
    </div>
  </section>

"""

# ---- TR MIRROR EXPANSION ----
TR_MIRROR_EXPANSION = """
  <!-- MIRROR DEEP DIVE TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake'in <span class="text-gradient-gold">Ayna Alanlarını</span> Neden Kullandığı</h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Şeffaflık eksikliği değil. DNS sansürü ve düzenleyicilere karşı altyapı.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Türkiye: ISP DNS Filtreleri</h3>
          <p>Türk internet servis sağlayıcıları belirli bahis sitelerini DNS düzeyinde engelliyor. Farklı TLD'lere sahip ayna siteler bu engel listelerinden kurtulabiliyor. Hangi ayna yolu kullanırsanız kullanın, cüzdan aynı kalıyor.</p>
        </div>
        <div class="club-card">
          <h3>Brezilya: 5.200 Alan Adı Engellendi</h3>
          <p>2024'te Brezilya, stake.com dahil 5.200'den fazla bahis alanını engelledi. Stake, bölgesel aynalar ile yanıt verdi. Ödeme için Pix MoonPay aracılığıyla çalışmaya devam ediyor.</p>
        </div>
        <div class="club-card">
          <h3>Hindistan, Filipinler, Japonya</h3>
          <p>Her yetki alanının çevrimiçi bahis için farklı yaklaşımları var. Tüm pazarlardan çekilmek yerine Stake, yerel engel listelerinde yer almayan alternatif alanlar kullanıyor. Tümü aynı yasal kuruluş tarafından işletiliyor.</p>
        </div>
        <div class="club-card">
          <h3>Uygulama Mağazasından Kaldırma</h3>
          <p>Apple ve Google, belirli bölgelerden bahis uygulamalarını periyodik olarak kaldırıyor. Ayrı mobil web uygulamalarına sahip ayna alanlar, oyuncular için işlevsellik kaybetmeden mağaza kaldırmalarını aşıyor.</p>
        </div>
        <div class="club-card">
          <h3>Sunucu Yük Dağılımı</h3>
          <p>Sadece düzenleyici bir mesele değil. Bazı aynalar, ana sunucuya gecikme yüksek olan bölgeler için CDN düğümleri işlevi görüyor. Bu, düşük gecikme gerektiren canlı oyunlarda performansı artırıyor.</p>
        </div>
        <div class="club-card">
          <h3>VPN: Daha Yüksek Riskli Yol</h3>
          <p>VPN basit görünebilir, ancak KYC riskini artırıyor. Stake IP'niz ile doğrulanmış kimlik belgeniz arasında tutarsızlık tespit ederse hesabınız uyum incelemesi için işaretlenebilir. Bölgenizdeki yetkili bir ayna kullanmak daha güvenli.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN MIRRORS TABLE TR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Ana <span class="text-gradient-gold">Ayna Listesi</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Tümü aynı Curaçao lisansı altında Medium Rare N.V. tarafından işletiliyor. Aynı arka uç, gerçek zamanlı cüzdan senkronizasyonu.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Alan Adı</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Ana Bölge</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Notlar</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.com</td><td style="padding:9px 12px;">Küresel</td><td style="padding:9px 12px;">Ana alan. Bazı ülkelerde engellenmiş olabilir.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.games</td><td style="padding:9px 12px;">Küresel</td><td style="padding:9px 12px;">Birincil alternatif ayna. Tam işlevsellik.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake.bet</td><td style="padding:9px 12px;">Küresel</td><td style="padding:9px 12px;">Tüm özelliklerle aktif ayna.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">getstake.it</td><td style="padding:9px 12px;">Ortaklık Bağlantısı</td><td style="padding:9px 12px;">İzleme parametreleriyle stake.com'a yönlendiriyor. MAX3000 tarafından kullanılıyor.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">stake1.com - stake8.com</td><td style="padding:9px 12px;">Ülkeye özgü</td><td style="padding:9px 12px;">Alternatif TLD'lerin engelleri aştığı yetki alanları için numaralı seri.</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">stake.us</td><td style="padding:9px 12px;">ABD (37 eyalet)</td><td style="padding:9px 12px;">Ayrı platform. Sweepstakes. Medium Rare NV değil, Sweepsteaks Limited tarafından işletiliyor.</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:16px;font-size:14px;color:var(--text-dim);">Tüm resmi Stake aynaları aynı veritabanı arka ucunu paylaşıyor. Herhangi bir aynada aynı kullanıcı adı ve parolayla giriş yaptığınızda aynı bakiyeyi, bahis geçmişini ve VIP ilerlemesini görürsünüz. Alanlar arasında fon transferi gerekmez.</p>
    </div>
  </section>

  <!-- PHISHING TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Gerçek Ayna <span class="text-gradient-gold">Nasıl Doğrulanır</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Phishing gerçek. Doğru aynada olup olmadığınızı nasıl anlarsınız.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>1. SSL Sertifikasını Kontrol Et</h3>
          <p>Tarayıcınızdaki kilit simgesine tıklayın. Sertifika stake.* alanı için düzenlenmiş olmalı. Süresi dolmuş veya farklı alanlar için düzenlenmiş sertifikalar anında kırmızı bayrak.</p>
        </div>
        <div class="club-card">
          <h3>2. WHOIS Kayıt Bilgisi</h3>
          <p>Resmi Stake aynaları, Medium Rare kuruluş bilgilerini gösteren veya meşru bir kayıt şirketi tarafından gizlilik korumalı WHOIS kayıtlarına sahip. 30 günden yeni kayıtlar şüpheli.</p>
        </div>
        <div class="club-card">
          <h3>3. Doğru Düzen ve Oyun Sağlayıcıları</h3>
          <p>Gerçek aynalar aynı Stake Originals, Evolution ve Pragmatic gibi sağlayıcıları ve aynı tasarımı gösterir. Düzen farklıysa veya oyunlar eksikse kimlik bilgilerinizi girmeyin.</p>
        </div>
        <div class="club-card">
          <h3>4. Bağlantı Kaynağı</h3>
          <p>Güvenilir ortaklık bağlantıları veya Stake'in kendi alan adı listesi aracılığıyla aynalara erişin. Telegram, WhatsApp veya e-postadaki istenmeyen bağlantılar yaygın phishing vektörleri.</p>
        </div>
      </div>
    </div>
  </section>

"""

# ---- TR PAYMENTS EXPANSION ----
TR_PAYMENTS_EXPANSION = """
  <!-- PAYMENTS DEEP DIVE TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Kripto Para <span class="text-gradient-gold">Yöntemleri</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Ana kanal. Tüm büyük zincirler destekleniyor. Minimum çekim tutarları ana kripto birimi cinsinden gösteriliyor.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Para Birimi</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">Ağ</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">Çekim Hızı</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Bitcoin (BTC)</td><td style="padding:9px 12px;">Bitcoin mainnet</td><td style="text-align:right;padding:9px 12px;">30 ila 60 dk</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Ethereum (ETH)</td><td style="padding:9px 12px;">ERC-20</td><td style="text-align:right;padding:9px 12px;">30 ila 60 dk</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">USDT</td><td style="padding:9px 12px;">TRC-20 / ERC-20</td><td style="text-align:right;padding:9px 12px;">TRC saniyeler</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Tron (TRX)</td><td style="padding:9px 12px;">Tron</td><td style="text-align:right;padding:9px 12px;">Saniyeler</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Ripple (XRP)</td><td style="padding:9px 12px;">XRP Ledger</td><td style="text-align:right;padding:9px 12px;">Saniyeler</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Solana (SOL)</td><td style="padding:9px 12px;">Solana</td><td style="text-align:right;padding:9px 12px;">Saniyeler</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Litecoin (LTC)</td><td style="padding:9px 12px;">Litecoin</td><td style="text-align:right;padding:9px 12px;">20 ila 40 dk</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">BNB / BSC</td><td style="padding:9px 12px;">BEP-20</td><td style="text-align:right;padding:9px 12px;">Dakikalar</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynak: <a href="https://help.stake.com/en/articles/4793500-supported-currencies" target="_blank" rel="noopener">Stake Yardım Merkezi, desteklenen para birimleri</a></p>
    </div>
  </section>

  <!-- FIAT ROUTES TR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Fiat Para <span class="text-gradient-gold">Yatırma Yolları</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Kripto cüzdanı yönetmek istemeyenler için.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>MoonPay</h3>
          <p>Fiat'ı kripto'ya çevirir ve doğrudan Stake'e yatırır. Visa, Mastercard ve birçok ülkede banka havalesi kabul edilir. Ücret: yönteme göre %4,5 ile %5,9 arası. MoonPay aracılığıyla fiat çekimler 1 ila 5 iş günü sürer.</p>
        </div>
        <div class="club-card">
          <h3>AstroPay</h3>
          <p>Türkiye dahil Latin Amerika ve Avrupa'nın çeşitli ülkelerinde kullanılabilen dijital cüzdan. Birden fazla yerel para birimini kabul ediyor. Online casinolarda kredi kartlarının kısıtlandığı pazarlar için iyi bir seçenek.</p>
        </div>
        <div class="club-card">
          <h3>Interac (Kanada)</h3>
          <p>Kanadalı oyuncular için anında banka havalesi. Ağ ücreti yok, dakikalar içinde sonuçlanır. İşlem başına limit bankaya göre değişir.</p>
        </div>
        <div class="club-card">
          <h3>Opay ve MomoPay</h3>
          <p>Özellikle Nijerya ve Batı Afrika ülkeleri için mobil cüzdanlar. Kredi kartı gerektirmeden yerel para biriminde para yatırmayı mümkün kılıyor.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- KYC LEVELS TR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">KYC <span class="text-gradient-gold">Seviyeleri</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">4 adım. Herkese zorunlu değil. Davranışa göre tetikleniyor.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>Seviye 1: Temel</h3>
          <p>E-posta ve kullanıcı adı. Bahis yapmayı sağlar. Düşük para yatırma ve çekme limitleri. Başlangıçta belge yükleme gerekmez.</p>
        </div>
        <div class="club-card">
          <h3>Seviye 2: Limitler Artırılır</h3>
          <p>E-posta doğrulama ve ek kişisel bilgiler. Para yatırma limitlerini artırır ve daha fazla ödeme seçeneğinin kilidini açar.</p>
        </div>
        <div class="club-card">
          <h3>Seviye 3: Hoş Geldin Bonusu</h3>
          <p>Belge doğrulaması: fotoğraflı kimlik, adres kanıtı ve Seviye 3'e özgü ek belgeler. MAX3000 hoş geldin bonusu ve büyük çekimler için zorunlu.</p>
        </div>
        <div class="club-card">
          <h3>Seviye 4: Fon Kaynağı</h3>
          <p>Çok yüksek hacimler veya uyum talebi ile tetiklenir. Fon kaynağı belgeleri, vergi beyannameleri veya banka ekstreleri gerektirebilir.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynak: <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">Stake Yardım Merkezi, hesap doğrulama</a></p>
    </div>
  </section>

"""

# ---- EXECUTE EXPANSIONS ----

print("\n=== TR REBUILD ===")
BASE_TR = f"{BASE}/tr"

# Index
content = expand_tr_page(f"{BASE_TR}/index.html", TR_INDEX_EXPANSION)
write_file(f"{BASE_TR}/index.html", content)

# Casino 
content = expand_tr_page(f"{BASE_TR}/casino/index.html", TR_CASINO_EXPANSION)
write_file(f"{BASE_TR}/casino/index.html", content)

# Promo-code - already 1206 words, just verify
with open(f"{BASE_TR}/promo-code/index.html", 'r', encoding='utf-8') as f:
    promo = f.read()
wc = word_count(promo)
issues = check_violations(promo)
print(f"  tr/promo-code/index.html: {wc} words (no changes needed){' | ISSUES: '+str(issues) if issues else ''}")

# About-stake - already 1511 words, just verify
with open(f"{BASE_TR}/about-stake/index.html", 'r', encoding='utf-8') as f:
    about = f.read()
wc = word_count(about)
issues = check_violations(about)
print(f"  tr/about-stake/index.html: {wc} words (no changes needed){' | ISSUES: '+str(issues) if issues else ''}")

# Mirror
content = expand_tr_page(f"{BASE_TR}/mirror/index.html", TR_MIRROR_EXPANSION)
write_file(f"{BASE_TR}/mirror/index.html", content)

# Payments
content = expand_tr_page(f"{BASE_TR}/payments/index.html", TR_PAYMENTS_EXPANSION)
write_file(f"{BASE_TR}/payments/index.html", content)

print("\nTR rebuild complete.")
