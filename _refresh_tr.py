#!/usr/bin/env python3
"""Refresh underweight /tr/ pages to KO depth.
Strategy: preserve TR header/footer/nav/promo-strip; replace main body content.
"""
import os, re

ROOT = '/home/user/workspace/winnersclub.com'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_header_and_footer(tr_content):
    """Return (head_block, header_block, after_hero_ticker_promo, footer_block, scripts_block)"""
    # Split at <!-- HERO --> start (after header ends)
    # We'll keep everything up to after promo strip (if present) then inject body then footer
    return tr_content

def inject_body_between_promo_and_footer(tr_content, new_body_html):
    """
    Keep the TR file intact from start to just after promo strip / reserves ticker / hero,
    then replace everything between that and STICKY CTA with new_body_html,
    then keep from sticky CTA to end.
    """
    # Find where to inject: after promo strip or after hero or after reserves ticker
    # Strategy: find <!-- STICKY CTA --> and replace everything before it (after hero section)
    # Actually: replace between first </section>\n and <!-- STICKY CTA -->
    
    # Simpler: find end of hero/ticker/promo section (after the promo-strip aside if exists,
    # or after reserves ticker, or just after the hero section)
    
    # Find the STICKY CTA comment
    sticky_marker = '<!-- STICKY CTA -->'
    if sticky_marker not in tr_content:
        sticky_marker = '  <!-- STICKY CTA -->'
    if sticky_marker not in tr_content:
        sticky_marker = '<div class="sticky-cta"'
    
    if sticky_marker not in tr_content:
        print(f"  WARNING: no sticky CTA marker found")
        return tr_content
    
    sticky_pos = tr_content.index(sticky_marker)
    
    # Find the end of the ticker/promo block
    # Look for the last occurrence of </aside> or </div> after promo-strip
    # Simpler: find all </section> before sticky, find the last one
    # Or find the promo-strip aside closing tag
    
    # Strategy: find start of first <section class="section"> after hero
    hero_end = tr_content.find('</section>', tr_content.find('class="club-hero"'))
    if hero_end == -1:
        hero_end = tr_content.find('</section>') + 10
    else:
        hero_end += len('</section>')
    
    # Now find ticker and promo strip after hero
    # Seek past reserves-ticker and promo-strip
    search_pos = hero_end
    # Skip ticker
    ticker_start = tr_content.find('class="reserves-ticker"', search_pos)
    if ticker_start != -1 and ticker_start < sticky_pos:
        ticker_end = tr_content.find('</div></div>', ticker_start)
        if ticker_end != -1:
            search_pos = ticker_end + len('</div></div>')
    # Skip promo-strip
    promo_start = tr_content.find('class="promo-strip"', search_pos)
    if promo_start != -1 and promo_start < sticky_pos:
        promo_end = tr_content.find('</aside>', promo_start)
        if promo_end != -1:
            search_pos = promo_end + len('</aside>')
    
    # Also eat the verified-stamp time if present
    # Now insert new body between search_pos and sticky_pos
    before = tr_content[:search_pos]
    after = tr_content[sticky_pos:]
    
    return before + '\n' + new_body_html + '\n  ' + after

# ── Helper HTML generators (Turkish) ──────────────────────────────────────

def tr_intel_cards(cards):
    html = '<div class="intel-grid anim-stagger">'
    for label, value, detail in cards:
        html += f'<div class="intel-card"><div class="ic-label">{label}</div><div class="ic-value">{value}</div><div class="ic-detail">{detail}</div></div>'
    html += '</div>'
    return html

def tr_club_cards(cards):
    html = '<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">'
    for h3, p in cards:
        html += f'<div class="club-card"><h3>{h3}</h3><p>{p}</p></div>'
    html += '</div>'
    return html

def tr_step_cards(steps):
    html = '<div class="step-cards anim-stagger">'
    for title, content in steps:
        html += f'<div class="step-card"><h3>{title}</h3><p>{content}</p></div>'
    html += '</div>'
    return html

def tr_faq_section(items, title='Sık Sorulan Sorular'):
    html = f'''  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{title}</h2></div>
      <div class="faq-list">'''
    for q, a in items:
        html += f'''
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>'''
    html += '''
      </div>
    </div>
  </section>'''
    return html

def tr_girl_break(title, sub, cta='Giriş Yap', img='girl-homepage'):
    return f'''  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/{img}-2.avif') type('image/avif'), url('/images/{img}-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">{title}</h2>
      <p class="girl-break-sub">{sub}</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{cta}</a>
    </div>
  </section>'''

# ═══════════════════════════════════════════════════════
# about-stake: TR 2486w -> KO 7416w target
# ═══════════════════════════════════════════════════════
def body_about_stake():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Rakamlarla <span class="text-gradient-gold">Stake</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">Bir startup degil. Girdiginiz evin büyüklügü budur.</p></div>
      {tr_intel_cards([
        ('GGR 2024', '$4.7B', '2024 yili toplam oyun geliri. 2022\'ye kıyasla %80 büyüme. Dünyanin en büyük kripto kumarhanesi.'),
        ('Yillik Para Yatirma', '$18B', 'Craven\'in kendi analitik verilerine göre Aralik 2024 itibariyle yilliklandirilmis para yatirma hacmi.'),
        ('Aylik Ziyaret', '127 Milyon', 'Tüm Stake domainleri toplaminda Similarweb takibi. Stake.com ve 22+ ayna dahil.'),
        ('Hesap Sayisi', '21 Milyonun Üzeri', '2025 itibariyle küresel kayit. Subat 2026\'da tek bir ayda 6,78 milyardan fazla bahis islendi.'),
        ('On-chain Rezervler', '$339.53M', '28 Mayis 2026 Arkham etiketli snapshot. Kamuya açik takip. Detaylar icin rezerv sayfasina bakin.'),
        ('Easygo Geliri', 'A$970M', 'Easygo Group Holdings FY2025 geliri. Net kâr A$257M. Net varlik A$5 Milyar. Kurumlar vergisi A$152M.'),
      ])}
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://www.tradingview.com/news/cointelegraph:8bc196325094b:0-crypto-casino-revenue-hit-81b-in-2024-despite-global-restrictions/" target="_blank" rel="noopener">CoinTelegraph - 2024 GGR</a> · <a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight - Easygo FY2025</a></p>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">Kurucular</span></h2><p class="section-subtitle">Iki Avustralyali. RuneScape\'de tanisti. Dis finansman olmadan 5,6 milyar dolarlik imparatorluk kurdu.</p></div>
      {tr_club_cards([
        ('Ed Craven', '1995 Melbourne dogumlu. Kamuya açik yüz. Craven, 12 yasinda bir aile kruvaziyer seyahatinde kumar oynayarak 6.000 dolar kazandigini iddia etti. Gencliginde "Apple" takma adiyla en büyük RuneScape zar klanini yönetti; orada Tehrani ile tanisti. 2021 sonuna kadar "Edd Miroslav" takma adiyla çalisarak kimligini kasitli olarak gizledi. Forbes Avustralya Ekim 2024: Tehrani ile birlikte net varlik <strong>US$5,6 milyar</strong>. AFR 2025 zenginler listesi Craven\'in bireysel varligi: <strong>A$4,82 milyar</strong>. 2022\'de Melbourne Toorak\'ta A$8,000\'e 7.187 metrekarelik tarihi kösk satin aldi.'),
        ('Bijan Tehrani', 'Iran kökenli ebeveynlerden Amerika\'da dogdu, Melbourne\'a tasindi. Sessiz ortak. Operasyon, kurumsal yapi ve arka planda çalisan mekanizmalar. Kick\'i ortak sahipleniyor. Forbes Mayis 2025 net varlik: <strong>$2,8 milyar</strong>. 2023 sonunda Manhattan\'da <strong>47 milyon dolarlik</strong> apartman satin aldi.'),
      ])}
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://en.wikipedia.org/wiki/Ed_Craven" target="_blank" rel="noopener">Wikipedia - Ed Craven</a> · <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">Wikipedia - Bijan Tehrani</a> · <a href="https://www.forbes.com/profile/edward-craven/" target="_blank" rel="noopener">Forbes - Ed Craven profili</a></p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">Kurumsal Yapi</span></h2></div>
      {tr_club_cards([
        ('Easygo Group Holdings', 'Avustralya ana sirketi. Ed Craven tek yöneticisi. FY2025: <strong>A$970M gelir</strong>, <strong>A$257M net kâr</strong>, <strong>A$5 milyar net varlik</strong>, <strong>A$152M kurumlar vergisi</strong>, <strong>636 çalisann</strong>. Stake.com ve Kick.com\'un tamamini dogan istirakler araciligiyla sahipleniyor.'),
        ('Medium Rare N.V.', 'Stake.com\'u isleten Curaçao tescilli sirket. <strong>Curaçao OGL/2024/1451/0918 lisansi</strong>. Tüm ayna domainler de Medium Rare N.V. tarafindan isletiliyor. Ödemeler Kibris Lefkosa\'daki bagli ortaklik araciligiyla isleniyor.'),
        ('Kick Streaming Pty Ltd', '14 Kasim 2022\'de kuruldu. Ana sirket: Easygo Entertainment Pty Ltd. Sahiplik: Ashwood Holdings %50, Bijan Tehrani %50. Twitch\'in %50/50 yerine %95/5 yayinci gelir paylasimi. 2025 3. ceyrek itibariyle küresel olarak en çok izlenen 4. canli yayin platformu.'),
        ('Stake.us', '<strong>Sweepsteaks Limited</strong> tarafindan isletilen ABD pazarinda ayrı bir yarisma platformu. Oynamak icin Gold Coins, 3x oynama sonrasi ödüle çevrilebilen Stake Cash. Gerçek para bahsi yok, kripto yok. <strong>37 ABD eyaletinde</strong> mevcut. <strong>MAX3000 Stake.us\'ta da çalisiyor</strong>: 560.000 GC + 56 SC + %3,5 rakeback.'),
      ])}
    </div>
  </section>

  {tr_girl_break('Para <span class="text-gradient-gold">on-chain\'de</span>', '28 Mayis 2026 itibariyle Arkham etiketli rezervler: $339.53M. Kamuya açik takip. <a href="/tr/reserves/" style="color:var(--gold);">Tüm detaylar &rarr;</a>', 'Hesap Aç - MAX3000 Kodunu Kullan', 'girl-homepage')}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Sponsorluklar <span class="text-gradient-gold">&amp; Ortakliklar</span></h2><p class="section-subtitle">Dünyanin hiçbir kumar sirketi bu kadar fazla kültürel alana bu kadar para yatirmadi.</p></div>
      {tr_club_cards([
        ('Drake', '2022 anlasması, raporlanan bedel <strong>yilda 100 milyon dolar</strong>. Drake birçok kez Stake\'te canli kumar yayini yapti. Haziran 2026 itibariyle iliski aktif. Stake\'in resmi X biyografisinde "Drake onayli" yaziyor.'),
        ('Trainwreckstv', 'Stake\'in en eski yayinci ismi. Kendi yayininda 16 ay boyunca <strong>360 milyon dolar ödeme</strong> aldigini açikladi. Temmuz 2025\'te Massive Studios\'un Stake icin gelistirdigi Hex Appeal\'de <strong>37,5 milyon dolar</strong> kazanarak en büyük online slot kazanç rekoru kirdi. Spin basina 6.000 dolar, maksimum çarpan 50.000x.'),
        ('Everton FC', '2022 Haziran\'da duyuruldu. Yilda <strong>10 milyon sterlin</strong>. Everton\'in 144 yillik tarihindeki en büyük forma ön sponsorlugu anlasması. Çok yillik kontrat.'),
        ('Watford FC', '22 Temmuz 2021 duyuruldu. Premier Lig sezonu 2021/22\'de ana forma sponsoru. Kulüp rekoru sozlesme.'),
        ('Stake F1 Team Kick Sauber', '2023\'te Sauber\'in ortak baslik ortagi oldu. 2024\'te tek baslik sponsoru. Takim 2024-2025\'te "Stake F1 Team KICK Sauber" adıyla yaristi. 2026\'dan itibaren Audi.'),
        ('UFC', '2021 Ocak: Israel Adesanya ilk global marka elçisi. 2024 Subat: premium global ortak statüsüne yükseltildi. Ek UFC sporcusu: Francis Ngannou, Alex Pereira, Merab Dvalishvili.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">Tarihsel Zaman Çizelgesi</span></h2><p class="section-subtitle">Melbourne ofisinden dünyanin en büyük kripto kumarhanesine 9 yil.</p></div>
      <div class="club-body anim anim-fade-up">
        <p><strong>2013</strong> - Primedice yayina girdi. Craven ve Tehrani kanıtlanabilir derecede adil Bitcoin kumarinin bir kitlesi oldugunu ispatladi.</p>
        <p><strong>2016</strong> - Melbourne\'da Easygo Solutions kuruldu. 18 çalisanla kendi teknoloji altyapisi gelistiriliyor.</p>
        <p><strong>2017</strong> - Stake.com yayina girdi. Curaçao OGL/2024/1451/0918 kapsaminda Medium Rare N.V. tarafindan isletiliyor.</p>
        <p><strong>2021</strong> - Ocak: Israel Adesanya Stake\'in ilk global elçisi. Temmuz: Watford FC forma sponsorlugu. Aralik: stake.uk.com (TGP Europe araciligiyla) acildi.</p>
        <p><strong>2022</strong> - Drake anlasması imzalandi. Haziran: Everton sponsorlugu. Aralik: Kick yayina girdi ve Twitch kumar reklamlari yasagiladi.</p>
        <p><strong>2023</strong> - Stake F1 Team Kick Sauber ortakligi basladi. <strong>4 Eylül:</strong> Lazarus Group saldirisi, sicak cüzdanlardan 41 milyon dolar çalindi. FBI 3 gün içinde kuzey Kore\'ye bagladi. Stake saatler içinde para çekme islemlerini yeniden baslatti. Kullanici fonlari etkilenmedi.</p>
        <p><strong>2024</strong> - Stake F1 Team Kick Sauber yeniden markalasmasi. Brezilya lisansi. Yillik GGR 4,7 milyar dolara ulasti.</p>
        <p><strong>2025 Mart</strong> - <strong>Ingiltere\'den çekilme.</strong> TGP Europe 11 Mart 2025\'te stake.uk.com\'u kapatti. Stake bunu dogrudan lisans stratejisine geçis olarak nitelendirdi.</p>
        <p><strong>2025 Temmuz</strong> - Trainwreckstv Hex Appeal\'de <strong>37,5 milyon dolar</strong> kazandi. Tüm zamanlarin en büyük online slot kazanci.</p>
        <p><strong>2025</strong> - Primedice kapandi. Easygo Group Holdings FY2025 geliri A$970M, kâr A$257M açikladi.</p>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://www.gamblingcommission.gov.uk/news/article/consumer-information-notice-stake-leaving-gb-market" target="_blank" rel="noopener">UKGC - Stake GB piyasasi bildirimi</a> · <a href="https://www.trmlabs.com/resources/blog/fbi-confirms-that-north-korea-was-behind-41-million-stake-com-exploit" target="_blank" rel="noopener">TRM Labs - FBI Lazarus bildirim onayı</a></p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">41 Milyon Dolarlik Hack</span></h2></div>
      <div class="club-body anim anim-fade-up">
        <p><strong>4 Eylül 2023</strong>, Stake\'in sicak cüzdanindan yaklasik <strong>41 milyon dolar kripto</strong> çalindi. Ethereum hesaplarindan ~16 milyon, Binance Smart Chain ve Polygon\'dan ~25,6 milyon dolar.</p>
        <p>Saldiri, özel anahtarlari dogrudan ele geçirmeyi içermiyordu. Stake\'in Ethereum, Polygon ve BNB Chain islemleri için kullandigi <strong>üçüncü taraf islem onay servisi</strong> hedef alindi. Ed Craven, ihlalın <strong>20 dakika içinde tespit edildigini ve 4 saat içinde tamamen çözüldügünü</strong> açikladi. Para çekme islemi o gün yeniden basladi.</p>
        <p><strong>7 Eylül 2023</strong>, <strong>FBI saldiriyi kuzey Kore Lazarus Group\'una resmi olarak bagladi.</strong> Çalinti fonlar karakteristik kara para aklama yollarindan geçirildi. Kullanici fonlari etkilenmedi. Hack sonrasi Arkham takipli rezervler 300 milyon dolarin üzerinde kalmaya devam etti.</p>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">VIP <span class="text-gradient-gold">Kulübü</span></h2><p class="section-subtitle">16 seviye. Ömür boyu bahis kilidi açma. Obsidian seviyesi için 1 milyar dolar gerekiyor.</p></div>
      <div class="club-body anim anim-fade-up">
        <p>Stake\'in VIP sistemi para yatirma miktarina degil <strong>kümülatif ömür boyu bahise</strong> göre çalisiyor. Casino\'ya yapilan her dolar bahis seviyenize sayiliyor. Spor bahisleri <strong>3x hizda</strong> sayiliyor. Bronze 10.000 dolar bahiste açiliyor. Obsidian için 1 milyar dolar gerekiyor. Avantajlar: haftalik boostlar, rakeback, Platinum ve üzerinden reload bonusu, üst seviyelerde özel VIP yöneticisi.</p>
      </div>
      <table class="data-table" style="max-width:700px;margin-top:24px;">
        <thead><tr><th>Seviye</th><th>Gereken Kümülatif Bahis</th></tr></thead>
        <tbody>
          <tr><td><strong>Bronze</strong></td><td>$10,000</td></tr>
          <tr><td><strong>Silver</strong></td><td>$50,000</td></tr>
          <tr><td><strong>Gold</strong></td><td>$100,000</td></tr>
          <tr><td><strong>Platinum I</strong></td><td>$250,000</td></tr>
          <tr><td><strong>Platinum II</strong></td><td>$500,000</td></tr>
          <tr><td><strong>Platinum III</strong></td><td>$1,000,000</td></tr>
          <tr><td><strong>Platinum IV</strong></td><td>$2,500,000</td></tr>
          <tr><td><strong>Platinum V</strong></td><td>$5,000,000</td></tr>
          <tr><td><strong>Platinum VI</strong></td><td>$10,000,000</td></tr>
          <tr><td><strong>Diamond I-V</strong></td><td>$25M - $500M</td></tr>
          <tr><td><strong>Obsidian</strong></td><td>$1,000,000,000</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  {tr_faq_section([
    ("Stake'i kim isletiyor?", "Ed Craven (1995, Melbourne) ve Bijan Tehrani. RuneScape zar topluluğunda gençken tanıştılar. 2017'de Curaçao'daki Medium Rare N.V. altında Stake'i birlikte kurdu, 2022'de Kick'i başlattı. Ortak Forbes net değeri: Ekim 2024 itibarıyla US$5,6 milyar."),
    ("Stake.com'u hangi şirket işletiyor?", "Curaçao'da kurulu Medium Rare N.V., OGL/2024/1451/0918 lisansını elinde bulunduruyor. Avustralya ana şirketi, Ed Craven'ın tek yönetici olduğu Easygo Group Holdings. Easygo FY2025'te A$970M gelir ve A$257M net kâr bildirdi."),
    ("Stake ne kadar büyük?", "GGR $4.7B (2024), yıllık para yatırma hacmi $18B, aylık ziyaretçi 127 milyon, kayıtlı hesap 21 milyonun üzerinde."),
    ("Stake hacklenmesi ne oldu?", "4 Eylül 2023'te Stake'in sıcak cüzdanından yaklaşık 41 milyon dolar çalındı. FBI 7 Eylül'de bunu Kuzey Kore Lazarus Grubu'na bağladı. Stake saatler içinde para çekmeyi yeniden başlattı. Kullanıcı fonları etkilenmedi."),
    ("Stake neden Birleşik Krallık'tan çekildi?", "Stake, 2021 Aralık'ta TGP Europe Ltd aracılığıyla Birleşik Krallık'a girdi. Aralık 2024'teki viral sosyal medya videoları UKGC soruşturmasını başlattı. TGP Europe 11 Mart 2025'te stake.uk.com'u kapattı. Stake bunu doğrudan lisans stratejisine geçiş olarak nitelendirdi."),
    ("Stake.us, Stake.com ile aynı mı?", "Hayır. Stake.us, Sweepsteaks Limited tarafından işletilen ayrı bir sweepstakes platformudur. Gerçek para bahsi yok, kripto yok. Stake.com ise Curaçao OGL/2024/1451/0918 kapsamında gerçek para uluslararası platformdur. MAX3000 her ikisinde de çalışır."),
  ], 'Sık Sorulan Sorular')}'''


# ═══════════════════════════════════════════════════════
# casino: TR 2294w -> KO 7979w target
# ═══════════════════════════════════════════════════════
def body_casino():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Casino <span class="text-gradient-gold">Salonu</span></h2></div>
      {tr_intel_cards([
        ('Toplam Oyun', '3.000+', 'Slot, masa oyunlari, canli casino, Stake Originals. Her hafta yeni oyunlar.'),
        ('RTP Araligi', '%94-%97', 'Yüksek RTP slotlar. Stake Originals (Dice, Limbo) ev kenari %1.'),
        ('Canli Casino', '24/7', 'Gerçek krupiyeli blackjack, rulet, bakara, poker. Gece gündüz açik.'),
        ('Stake Originals', 'Münhasir', 'Crash, Dice, Limbo, Mines, Keno, Plinko. Kanıtlanabilir adil RNG.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Oyun <span class="text-gradient-gold">Kategorileri</span></h2></div>
      {tr_club_cards([
        ('Slotlar', 'Pragmatic Play, Hacksaw Gaming, NoLimit City, NetEnt, Play\'n GO\'dan 3.000+ slot. Sweet Bonanza, Gates of Olympus, Wanted Dead or a Wild, Book of Dead. Her hafta yeni basliklar ekleniyor.'),
        ('Canli Casino', 'Evolution, Pragmatic Play Live, Ezugi krupiye yazilimcilari. Blackjack, rulet, bakara, poker, Crazy Time, Monopoly Live. Her zaman 100+ aktif masa.'),
        ('Stake Originals', 'Crash, Dice, Limbo, Mines, Keno, Plinko, Hilo, Wheel. Stake tarafindan gelistirilen münhasir oyunlar. Her tur dogrulanabilir. MAX3000 bahis sartiyla %100 katkida bulunuyor.'),
        ('Masa Oyunlari', 'Blackjack, rulet, bakara, video poker, Casino Hold\'em gibi çesitler. RNG ve canli versiyonlar mevcut. Düsük ve yüksek bahisli tablolar.'),
        ('MAX3000 Casino Bonusu', 'Kod <span class="code-highlight">MAX3000</span> ile 200% $3.000\'e kadar. Ev kenari %4+ olan casino oyunlari bahis sartina %100 katkida bulunuyor. Originals ve yüksek ev kenari slotlari en verimli seçenekler.'),
        ('Oyun Arama ve Filtreleme', 'Tedarikçi, RTP, popülarite ve yenilige göre filtrele. Favori oyunlarini kolayca bul. Oyun içi istatistikler mevcut.'),
      ])}
    </div>
  </section>

  {tr_girl_break('3.000+ Oyun. <span class="text-gradient-gold">Bir Kod.</span>', '<span class="code-highlight">MAX3000</span> 200% $3.000\'e kadar açar. Oyununuzu seçin ve baslayin.', 'Casino\'ya Giriş Yap', 'girl-casino')}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Sürekli Casino <span class="text-gradient-gold">Promosyonlari</span></h2></div>
      {tr_club_cards([
        ('$100.000 Günlük Yaris', 'Tüm kayıtlı oyuncular için otomatik katilim. Casino oyunlari oyna, lider tablosu puani kazan. Her 24 saatte bir en iyi 5.000 oyuncu $100.000 priz havuzunu paylasiyor. Yarislar sürekli sifirlaniyor.'),
        ('$75.000 Haftalik Çekilis', 'Uygunluk döneminde her $1.000 bahis için bir çekilis bileti. Haftalik $75.000 her Cumartesi GMT 14:00\'te canli yayin ile çekilmektedir.'),
        ('$50.000 Casino\'yu Fethettir', 'Yeni ve öne çikan oyunlarda haftalik görev promosyonu. $0,10\'dan baslayan bahisler uygun. $50.000 haftalik ödül en büyük bahisçiler ve rastgele ödül düsüsleri arasinda paylasilir.'),
        ('Pragmatic Drops & Wins', 'Stake, Pragmatic Play\'in öncü ag promosyonunu isletiyor: Sweet Bonanza, Gates of Olympus 1000, Sugar Rush. Gercek para spinleri sirasinda ödüller rastgele düsüyor. Haftada 50.000+ ödül.'),
        ('Spor Kitabi Sigorta Promosyonlari', 'Etkinlige özgü sigorta teklifleri: NHL erken ödeme, NBA devre arasi, UFC bolünmüs karar sigortası, Premier Lig erken ödeme, Stake Shield parlay korumasi.'),
        ('VIP Reload Bonusu', 'Platinum ve üzeri VIP\'ler reload bonuslari aliyor: Platinum I 14 günde bir, Platinum IV istediginiz zaman. Miktarlar son kayiplara göre agirliklandiriliyor.'),
      ])}
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://stake.com/promotions" target="_blank" rel="noopener">Stake promosyon sayfasi</a> · <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake rehberi</a></p>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Casino Bahis <span class="text-gradient-gold">Uyumluluğu</span></h2></div>
      {tr_club_cards([
        ('Stake Originals - %100', 'Crash, Dice, Limbo, Mines, Plinko, Keno. Hepsi bahis sartina %100 katkida bulunuyor. Düsük ev kenari ile verimli çevrim.'),
        ('Yüksek Ev Kenari Slotlar - %100', 'Ev kenari %4+ olan slotlar bahis sartina %100 katkida. Pragmatic Play, Hacksaw, NoLimit City titlelari genellikle bu kategoriye girer.'),
        ('Spor Bahisleri - %75', 'Spor bahisleri %75 katkida bulunuyor. Casino oyunlarina göre daha az verimli ama yine de sayiliyor.'),
        ('Canli Krupiye - Azaltilmis', 'Canli krupiye oyunlari ve düsük RTP slotlari azaltilmis oranda veya %0 katkida bulunuyor. Bahis sarти için tavsiye edilmiyor.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake casino'da kaç oyun var?", "3.000+ casino oyunu: slotlar, masa oyunları, canlı casino, Stake Originals. Pragmatic Play, Evolution, Hacksaw Gaming, NetEnt, Play'n GO ve daha fazlası."),
    ("Canlı casino mevcut mu?", "Evet. Stake gerçek krupiyeli blackjack, rulet, bakara ve poker masaları işletiyor. Gece gündüz 7/24 açık."),
    ("MAX3000 casino'da kullanılabilir mi?", "Evet. 200% $3.000'e kadar hoşgeldin bonusu tüm Stake casino, spor kitabı ve poker genelinde geçerli. Ev kenarı %4+ olan casino oyunları bahis şartına %100 katkıda bulunuyor."),
    ("Stake Originals nedir?", "Stake'in kendi geliştirdiği münhasır oyunlar: Crash, Dice, Limbo, Mines, Keno, Plinko. Kanıtlanabilir adil RNG, her el doğrulanabilir. MAX3000 bahis şartına %100 katkıda bulunuyor."),
  ], 'Sık Sorulan Sorular')}'''


# ═══════════════════════════════════════════════════════
# promo-code: TR 2502w -> KO 6490w target
# ═══════════════════════════════════════════════════════
def body_promo_code():
    return f'''  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">Kulübün Kodu</div>
        <div class="code-display">MAX3000</div>
        <div class="code-meta">%200 eslesme &middot; $3.000\'e kadar bonus &middot; Minimum para yatirma $10 &middot; Depozit+bonus üzerinden 40x çevrim &middot; KYC Seviye 3 zorunlu &middot; 18+ yeni musteriler</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">Kodu Kopyala</button>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Kodu Krupiyeye Ver &rarr;</a>
        </div>
      </div>
    </div></section>

  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake.com Bonus <span class="text-gradient-gold">Hesaplayici</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Kaydiriciyi hareket ettirin. $10 ile $1.500 arasi depozit, %200 eslesme $3.000 bonusa kadar, 40x çevrim toplam üzerinden.</p>
      </div>
      <div class="bonus-calc">
        <h3>Stake.com İlk Para Yatirma Miktari</h3>
        <div class="bonus-calc-input">
          <label for="depAmount">Para Yatirma Miktari (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat"><p class="stat-label">Verilen Bonus</p><p class="stat-value" id="bonusOut">$1,000</p><p class="stat-sub">%200 eslesme, $3.000 bonus limitine kadar</p></div>
          <div class="stat"><p class="stat-label">Bahis Gereksimi</p><p class="stat-value" id="wagerOut">$60,000</p><p class="stat-sub">(Depozit + Bonus) × 40</p></div>
          <div class="stat"><p class="stat-label">Toplam Oynanabilir Fon</p><p class="stat-value" id="totalOut">$1,500</p><p class="stat-sub">Talep sonrasi hesap bakiyesi</p></div>
          <div class="stat"><p class="stat-label">Eslesme Verimliligi</p><p class="stat-value" id="effOut">200%</p><p class="stat-sub">$1.500 limitini asarsa %200 altina düser</p></div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">Maksimum bonus $3.000\'dir.</strong> $1.500 yatirin, tam $3.000\'i alin. $1.500 üzeri yatirimlar islenir ancak bonus artmaz.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="bonus-calc-cta">Stake.com\'da MAX3000 ile Talep Et &rarr;</a>
      </div>
      <div class="eligibility-grid">
        <div class="item"><strong>Yas</strong><span>18+ (bazi bölgelerde 21+)</span></div>
        <div class="item"><strong>Müsteri Türü</strong><span>Yeni müsteri, yalnizca ilk para yatirma</span></div>
        <div class="item"><strong>Minimum Para Yatirma</strong><span>USD $10 veya es degeri kripto</span></div>
        <div class="item"><strong>Maksimum Bonus</strong><span>$3.000 ($1.500 yatirildiginda maksimum)</span></div>
        <div class="item"><strong>KYC</strong><span>Bonus kreditlenmesinden önce Seviye 3 zorunlu</span></div>
        <div class="item"><strong>Talep Yöntemi</strong><span>Ilk para yatirma sonrasinda canli destekle iletisim</span></div>
        <div class="item"><strong>Ödeme Süresi</strong><span>Ekip uygunlugu dogruladiktan sonra 24-48 saat</span></div>
        <div class="item"><strong>Ilerleme Takibi</strong><span>VIP sekmesinde bahis ilerlemesi görüntülenebilir</span></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake Yardim, hosgeldin bonusu</a> &middot; <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">Stake Yardim, KYC seviyeleri</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com, MAX3000 sartlari</a></p>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Tüm Aktif Stake Kodlarinin <span class="text-gradient-gold">Karsilastirmasi</span></h2><p class="section-subtitle">Yedi kod, bir kazanan. Kulübün neden yalnizca MAX3000\'i önerdigi.</p></div>
      <table class="data-table" style="max-width:100%;overflow-x:auto;display:block;">
        <thead><tr><th>Kod</th><th>Eslesme %</th><th>Maks. Bonus</th><th>Min. Para Yatirma</th><th>Not</th></tr></thead>
        <tbody>
          <tr class="win"><td><strong>MAX3000</strong></td><td>%200</td><td>$3.000</td><td>$10</td><td>Kulüp kodu. Canli destek %200 eslesmeyi manuel olarak ekler, depozit+bonus 40x.</td></tr>
          <tr><td>NEWBONUS</td><td>%200</td><td>$3.000</td><td>$10</td><td>Genel kullanim kodu, tüm aynalanarda çalisiyor.</td></tr>
          <tr><td>HELLA200</td><td>%200</td><td>$3.000</td><td>$50</td><td>Daha yüksek minimum para yatirma. Spin yok.</td></tr>
          <tr><td>STRAFECASVIP</td><td>%200</td><td>$2.000</td><td>$10</td><td>Strafe ortakligi. MAX3000\'den $1.000 daha düsük limit.</td></tr>
          <tr><td>HELLAGOOD</td><td>Hayir</td><td>Hayir</td><td>Hayir</td><td>Yalnizca %5 rakeback. Para yatirma eslesmesi yok.</td></tr>
          <tr><td>HELLAFREE</td><td>Hayir</td><td>$1 para yatirmasiz</td><td>Yok</td><td>KYC sonrasi $1 ücretsiz. Düsük deger.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Talep <span class="text-gradient-gold">Adimlari</span></h2></div>
      {tr_step_cards([
        ('1. Kapiyi Açin', '<a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener">Ortaklik linki ile Stake.com\'a</a> gidin ve kaydol\'a basin. E-posta, kullanici adi, sifre, dogum tarihi.'),
        ('2. Seviye 3\'e Kadar Dogrulayin', 'Stake hosgeldin bonusunu ödemeden önce <strong>KYC Seviye 3</strong> gerektiriyor. Kimlik fotografi, adres belgesi, ek seviye 3 belgelerini yükleyin.'),
        ('3. Ilk Para Yatirmayi Yapin ($10+)', '$10 ile $1.500 arasinda para yatirin. %200 eslesme $3.000 bonus limitine kadar orantili artiyor. $1.500 üzeri islenir ama bonus artmaz.'),
        ('4. MAX3000\'i Canli Destek Üzerinden Talep Edin', 'Para yatirma onaylandiktan sonra Stake canli destek ekibine <span class="code-highlight">MAX3000</span> ile kaydoldugunuzu ve hosgeldin bonusunu istediginizi bildirin. <strong>24-48 saat</strong> içinde %200 eslesme hesabiniza geliyor.'),
      ])}
      <div class="club-body" style="margin-top:32px;padding:20px;background:var(--elevated);border-radius:10px;border-left:3px solid var(--gold);">
        <p style="margin:0;font-size:14px;color:var(--text-dim);"><strong style="color:var(--gold);">Önemli:</strong> Stake.com hosgeldin bonusu otomatik uygulanan bir referans kodu degil, operatör tarafindan manuel olarak verilen bir kredidir. Ortaklik linki ile kaydolun, KYC Seviye 3\'ü tamamlayin, para yatirin ve canli deskete MAX3000\'i bildirin. (Depozit + Bonus) × 40 ilerleme aktivasyondan sonra <strong>VIP sekmesinde</strong> görüntülenebilir.</p>
      </div>
    </div>
  </section>

  {tr_girl_break('Floordaki En Büyük <span class="text-gradient-gold">Kod</span>', 'Krupiyeye <span class="code-highlight">MAX3000</span>\'i fislillayin. Stake.com\'da %200 $3.000\'e kadar, canli destek gerisisini halleder.', 'Kodu Krupiyeye Ver', 'girl-promo')}

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Bonus Drop Kodlari: <span class="text-gradient-gold">Az Bilinen Avantaj</span></h2><p class="section-subtitle">Hosgeldin teklifinin ötesinde Stake zaman sinirli ücretsiz kodlar isletiyor. Çogu oyuncunun kaçirdigi kisim budur.</p></div>
      <div class="club-body">
        <p>Bonus drop kodlari, Stake\'in resmi Telegram kanali ve sosyal medyasinda paylasilir. Hosgeldin bonusunun aksine bahis gereksimi yoktur, ödeme ücretsiz nakittir. Ancak son 7 günde belirli bir miktarin üzerinde bahis yapilmis olmasi gerekir ve limit dolunca hizla süreleri doluyor.</p>
        <p>Tipik deger <strong>kod basina $1-$5</strong>, kanallar genelinde her gün birkaç kod yayinlaniyor. VIP Gold ve üzeri için e-posta ve özel Telegram alt kanallarinda daha yüksek nominal degerli kodlar ayruca saglanmakta.</p>
      </div>
      {tr_club_cards([
        ('@StakecomDailyDrops', 'Genel drop kodlari için ana Telegram kanali. Günde birkaç kod yayinlaniyor. Bildirimler açik olsun, limit dolunca kodlar aninda sona eriyor.'),
        ('@StakeCasino', 'Stake\'in ana Telegram\'i. Resmi duyurular ve daha büyük promosyon kodlari. Drop kanaliyla birlikte takip edin.'),
        ('@Stakelivechallenges', 'Canli zorluk bildirimleri ve ilgili ödüller. Drop kodlarindan farkli mekanizma ama ayni düsük engelli bonus kategorisi.'),
        ('@Stake (X)', 'Büyük promosyonlar veya spor etkinliklerinde Stake\'in Twitter/X hesabinda da drop kodlari cikiyor.'),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Sürekli Promosyonlar: <span class="text-gradient-gold">Haftada $700.000+</span></h2><p class="section-subtitle">Hosgeldin teklifi yalnizca baslangic. Stake mevcut oyunculara her hafta 700.000 dolardan fazla ödül dagitmaktadir.</p></div>
      {tr_club_cards([
        ('$100.000 Günlük Yaris', 'Tüm kayıtlı oyuncular için otomatik katilim. Casino oyunlari oyna, lider tablosu puani kazan. 24 saatlik uygunluk süresinin ardindan en iyi 5.000 oyuncu $100.000 priz havuzunu paylasir.'),
        ('$75.000 Haftalik Çekilis', 'Uygunluk süresinde her $1.000 bahis için bir çekilis bileti. Her Cumartesi GMT 14:00\'te canli yayin ile çekilmekte.'),
        ('$50.000 Casino\'yu Fethettir', 'Yeni ve öne çikan oyunlarda haftalik görevler. $0,10\'dan baslayan bahisler. $50.000 haftalik ödül.'),
        ('Pragmatic Drops & Wins', 'Sweet Bonanza, Gates of Olympus 1000, Sugar Rush. Gerçek para spinleri sirasinda rastgele ödüller. Haftada 50.000+ ödül.'),
        ('Spor Kitabi Sigortasi', 'NHL erken ödeme, NBA devre arasi, UFC bolünmüs karar, Premier Lig erken ödeme, Stake Shield parlay korumasi.'),
        ('VIP Reload Bonusu', 'Platinum ve üzeri VIP\'ler reload bonuslari aliyor. Miktarlar son kayiplara göre agirliklandiriliyor.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake.com promosyon kodu nedir?", "Kod <span class='code-highlight'>MAX3000</span>'dir. Ortaklık linki ile Stake.com'a kaydolun, KYC Seviye 3'ü tamamlayın, $10 ile $1.500 arasında ilk para yatirmani yapın, ardından canlı sohbeti açın ve MAX3000'i bildirin. Ekip uygunluğu doğruladıktan sonra 24-48 saat içinde %200'e kadar $3.000 esleşme yapılır."),
    ("MAX3000 bonusunun maksimum miktarı nedir?", "%200 eşleşme ile maksimum $3.000 bonus. $1.500 yatırmak tam $3.000'e ulaşır. Minimum uygun para yatırma $10, maksimum $1.500. $1.500 üzeri işlenir ama bonus artmaz."),
    ("Bahis şartı nedir?", "Depozit ve bonus toplamının 40 katı. Örnek: $500 depozit + $1.000 bonus = $1.500 × 40 = $60.000 bahis. Ev kenarı %4+ casino oyunları %100 katkıda, spor bahisleri %75."),
    ("Kimlik doğrulama gerekli mi?", "Evet. Stake.com hosgeldin bonusunu ödemeden önce KYC Seviye 3 doğrulaması gerektiriyor. Ayarlar → Doğrulama'dan fotoğraflı kimlik, adres kanıtı, fon kaynağı belgelerini gönderin."),
    ("Bonus nasıl ödeniyor?", "Otomatik uygulanan bir referans kodu değil, operatör tarafından manuel verilen bir kredi. İlk para yatırma işleminden sonra Stake canlı desteğini açın ve MAX3000 ile kaydolduğunuzu bildirin. 24-48 saat içinde %200 eşleşme geliyor."),
    ("Yalnızca yeni oyuncular için mi geçerli?", "Evet. MAX3000 yeni Stake.com hesaplarındaki ilk uygun para yatırmaya uygulanır. Mevcut hesaplar geriye dönük uygunluk kazanamaz."),
  ], 'Sık Sorulan Sorular')}'''


# ═══════════════════════════════════════════════════════
# mirror: TR 2585w -> KO 7779w
# ═══════════════════════════════════════════════════════
def body_mirror():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Resmi <span class="text-gradient-gold">Ayna Domainler</span></h2></div>
      {tr_intel_cards([
        ('stake.com', 'Ana Domain', 'Orijinal site. ABD ve Birlesik Krallik haricinde çogu ülkede erisim saglanir.'),
        ('stake.ac', 'Resmi Ayna', 'Resmi alternatif domain. Ayni platform, ayni hesap, ayni kodlar.'),
        ('stake.bet', 'Resmi Ayna', 'Ikinci resmi ayna. Tüm cihazlar ve tarayicilarda çalisiyor.'),
        ('stake.games', 'Resmi Ayna', 'Üçüncü resmi ayna. Stake.com\'un engellenebilecegi bölgelerde kullanisli.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">MAX3000 <span class="text-gradient-gold">Tüm Domainlerde Çalisiyor</span></h2></div>
      <div class="club-body" style="max-width:720px;margin:0 auto;">
        <p>Tanitim kodu <span class="code-highlight">MAX3000</span>, stake.com, stake.ac, stake.bet ve stake.games üzerinde ayni kosullarla çalisiyor: %200 eslesme $3.000\'e kadar, depozit ve bonus üzerinden 40x çevrim sarти, KYC Seviye 3 zorunlu.</p>
        <p>Stake.com bölgenizde erisilmiyorsa stake.ac, stake.bet veya stake.games\'i deneyin. Hepsi ayni platforma ve ayni hesaba ulastirir.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:20px;display:inline-block;">MAX3000 ile Simdi Giriş Yap</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Neden Ayna <span class="text-gradient-gold">Domainler Var</span></h2></div>
      {tr_club_cards([
        ('DNS Tabanli Engellemeler', 'Bazi internet servis saglayicilari veya hükümetler belirli domainlere erisimi engelliyor. Ayna domainler, ayni platformun farkli bir adresle erisilen kopyasi.'),
        ('Ayni Sirket, Ayni Lisans', 'stake.ac, stake.bet ve stake.games hepsi Medium Rare N.V. tarafindan isletilmektedir. Curaçao OGL/2024/1451/0918 lisansi tüm resmi aynalara uygulanir.'),
        ('Hesap Portabilite', 'stake.com ile kurulan hesabinizla stake.ac veya stake.bet üzerinden de giris yapabilirsiniz. Ayni bakiye, ayni oyun gecmisi.'),
        ('Güvenli Ayna Dogrulama', 'Yalnizca resmi aynalari kullanin: stake.ac, stake.bet, stake.games. Resmi olmayan "ayna" siteler dolandiricilik riskidir. Stake\'in resmi sitelerini her zaman dogrulayin.'),
        ('Ülke Kisitlamalari', 'ABD ve Birlesik Krallik stake.com\'dan kisitilanmistir. ABD\'li oyuncular stake.us kullaniyor (sweepstakes, farkli platform). Diger bölgeler ayna domainler üzerinden erisim saglayabilir.'),
        ('MAX3000 Her Yerde', 'Hangi resmi Stake domaini kullanirsaniz kullanin, kod MAX3000 ayni kosullarla çalisiyor: %200, $3.000\'e kadar, 40x, KYC Seviye 3.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake Lisansi ve <span class="text-gradient-gold">Düzenleyici Çerçeve</span></h2></div>
      {tr_club_cards([
        ('Curaçao OGL/2024/1451/0918', 'Stake\'in ana lisansi. 2024 itibariyle GCB (Gaming Control Board of Curaçao) tarafindan duzenleniyor. Lisans 100+ ülkeyi kapsiyor.'),
        ('Medium Rare N.V.', 'Curaçao\'da tescilli is̈leten sirket. Tüm resmi Stake domainleri bu lisans altinda faaliyet gösteriyor.'),
        ('Birlesik Krallik Çekilmesi', 'Stake Mart 2025\'te Birlesik Krallik pazarindan çekildi. Ingiliz oyuncular artik erisim saglayamiyor. Direkt lisans stratejisine geçiyor.'),
        ('Italya, Brezilya, Arjantin', 'Stake bu ülkelerde direkt lisanslar aldi. Mevzuata uyumlu, dogrudan lisansli operasyon.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake ayna siteleri nedir?", "Ayna siteler, Stake.com'un resmi alternatif domainleridir. Bilinen domainler: stake.ac, stake.bet, stake.games. Stake.com'un erişilemediği bölgelerde kullanılır."),
    ("MAX3000 ayna sitelerde çalışıyor mu?", "Evet. MAX3000, tüm resmi Stake alternatif domainlerinde aynı koşullarla çalışıyor: %200 $3.000'e kadar, 40x çevrim."),
    ("Ayna siteler güvenli mi?", "Resmi domainler: stake.ac, stake.bet, stake.games güvenlidir ve aynı şirket tarafından işletiliyor. Hesap açmadan önce her zaman domaini doğrulayın."),
  ], 'Sık Sorulan Sorular')}'''

# ═══════════════════════════════════════════════════════
# payments: TR 2278w -> KO 6342w
# ═══════════════════════════════════════════════════════
def body_payments():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Ödemeleri</span></h2></div>
      {tr_intel_cards([
        ('Para Yatirma Hizi', 'Aninda', 'Çogu kripto, ag onayindan sonra 1-5 dakika içinde onaylaniyor.'),
        ('Para Çekme Hizi', '30 dk - 1 saat', 'Normal kriptolar. TRX, SOL, XRP saniyeler içinde. Büyük çekimler 2-4 is̈ günü.'),
        ('Stake Ücretleri', 'Sifir', 'Dahili ücret yok. Ag ücretleri kullaniciya ait.'),
        ('Desteklenen Para Birimleri', '20+ kripto', 'BTC ETH LTC XRP SOL TRX BNB DOGE AVAX BCH EOS USDT USDC ve daha fazlasi.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Desteklenen <span class="text-gradient-gold">Kriptolar</span></h2></div>
      {tr_club_cards([
        ('Bitcoin (BTC)', 'Kral. Para yatirma ve çekme destekleniyor. Onay süresi 10-60 dakika. Degisken ag ücretleri. En yüksek talep.'),
        ('Ethereum (ETH)', 'Ikinci en popüler. Gas ücretleri degisiyor. BTC\'den daha hizli onay. ERC-20 USDT ve USDC destekliyor.'),
        ('Solana (SOL)', 'Süper hizli, çok düsük ücretler. Onay saniyeler içinde. Hizli ve sik çekimler için ideal.'),
        ('Tron (TRX)', 'TRC-20 USDT çok düsük ücretli (genellikle $1\'in altinda). Onay saniyeler-dakikalar içinde.'),
        ('Ripple (XRP)', 'Süper hizli, birkaç sent ücret. Hizli transferler için mükemmel.'),
        ('MoonPay (Fiat)', 'Kredi karti ve banka transferiyle para yatirma. MoonPay ücretleri geçerli. Fiat para çekme 1-5 is̈ günü.'),
      ])}
    </div>
  </section>

  {tr_girl_break('Kripto <span class="text-gradient-gold">Hizli Girer, Hizli Çikar.</span>', '<span class="code-highlight">MAX3000</span> ile %200 $3.000\'e kadar. 20+ kripto destekli.', 'Stake\'e Giriş Yap', 'girl-homepage')}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">KYC <span class="text-gradient-gold">Seviyeleri</span></h2></div>
      {tr_step_cards([
        ('KYC Seviye 1 - Temel', 'E-posta ve sifre. Sinirli para yatirma ve çekme. Büyük bonuslar için yeterli degil.'),
        ('KYC Seviye 2 - Geniş', 'Fotografi kimlik ve adres belgesi. Daha yüksek para yatirma ve çekme limitleri. Çogu normal para çekme için yeterli.'),
        ('KYC Seviye 3 - Tam', 'Fotografi kimlik, adres belgesi ve fon kaynagi. MAX3000 hosgeldin bonusu ve büyük çekimler için zorunlu. En yüksek seviye.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Para Çekme <span class="text-gradient-gold">Hizi Rehberi</span></h2></div>
      {tr_club_cards([
        ('TRX, XRP, SOL', 'En hizli. Genellikle birkaç saniye ile birkaç dakika arasinda. Küçük ve orta büyüklükteki çekimler için önerilir.'),
        ('ETH, BNB', 'Orta hiz. 5-30 dakika. Gas degiskenliginden etkilenebilir.'),
        ('BTC', 'Daha yavas. 10-60 dakika. Ag yogunluguna göre degisir.'),
        ('Büyük Çekimler', '2-4 is̈ günü uyum incelemesi. Bu standarttir ve sirayiyla uygulanmaktadir.'),
        ('MoonPay Fiat', '1-5 is̈ günü. En yavas seçenek. Kredi karti ve banka transferi.'),
        ('VIP Öncelikli', 'Platinum ve üzeri VIP çekimleri öncelikli isleniyor. Bekleyis süresi daha kisa.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake hangi kripto paraları kabul ediyor?", "Stake; BTC, ETH, LTC, XRP, SOL, TRX, BNB, DOGE, AVAX, BCH, EOS, USDT, USDC ve daha fazlasını kabul ediyor. Liste sürekli genişliyor."),
    ("Para çekme hızı nedir?", "Normal kripto çekimleri: 30 dakika-1 saat. TRX, XRP, SOL saniyeler içinde. Büyük çekimler 2-4 iş günü. MoonPay fiat 1-5 iş günü."),
    ("Yatırma veya çekme ücreti var mı?", "Stake dahili ücret almıyor. Ağ ücretleri (gas) kullanıcıya ait. MoonPay kendi ücretlerini uyguluyor."),
    ("KYC para çekme için gerekli mi?", "KYC Seviye 2 normal para çekimler için yeterlidir. Seviye 3, büyük çekimler ve MAX3000 hosgeldin bonusu için zorunludur."),
  ], 'Sık Sorulan Sorular')}'''


# ═══════════════════════════════════════════════════════
# poker: TR 2247w -> KO 5357w
# ═══════════════════════════════════════════════════════
def body_poker():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Poker <span class="text-gradient-gold">Salonu</span></h2></div>
      {tr_club_cards([
        ('Cash Games', 'No-Limit Hold\'em ve Pot-Limit Omaha çesitli stakeslarda. Istediginiz zaman masaya oturun veya kalkın. Rekabetçi rake.'),
        ('Sit & Go', 'Dolu masada baslayan anlık turnuvalar. 2 ile 9 oyuncu arasi. Kısa seanslar için uygun.'),
        ('Multi-Table Tournaments', 'Garanti ödüllü MTT\'ler, büyük turnuvalar için Satellite\'lar. Daha büyük ödüller hedefleyenler için.'),
        ('Kanıtlanabilir Adil', 'Her el dogrulanabilir. Stake seffaflık ilkesine bagli.'),
        ('MAX3000 Bonusu', '%200 $3.000\'e kadar. Poker masalarinda bonusu kullanin. Rake katkisini hesaplamak için simdi kontrol edin.'),
        ('Çok Dilli Destek', 'Türkçe dahil onlarca dilde 7/24 canli destek. Ekip 24-48 saat içinde MAX3000 talebini isliyor.'),
      ])}
    </div>
  </section>

  {tr_girl_break('Poker <span class="text-gradient-gold">Masasi Hazir.</span>', '<span class="code-highlight">MAX3000</span> ile %200 $3.000\'e kadar. Cash Games ve turnuvalar sizi bekliyor.', 'Poker Masasina Otur', 'girl-poker')}

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Poker Strateji <span class="text-gradient-gold">Rehberi</span></h2></div>
      {tr_club_cards([
        ('Pos̈isyon Anlayisi', 'Tüm poker formatlarinda kilit. Dealer düğmesine yakın pozisyonlar daha fazla bilgiyle karar almanızı saglar. En başarılı oyuncular bu avantajı tutarlı şekilde kullanır.'),
        ('Bütçe Yönetimi', 'Cash game için önerilen buy-in: oturum başına toplam bütçenizin %5-10\'u. Kisa vadeli varyansa karşı tampon. Uzun vadeli performansı korur.'),
        ('Pot Odds Hesabi', 'Bet\'in büyüklügünü karşı konulan pot büyüklügüyle karşılastırın. Matematiksel deger teslim etmeye karşı kararlı kararlar alın. Uzun vadede kaybeden oyunculari bu adim ayırt eder.'),
        ('Rakip Okuma', 'Bet boyutu örüntüleri, zamanlaması ve tutarsızlıkları izleyin. Live kazanma oranı açısından en güçlü oyuncular, kazanamayacakları elleri en aza indiren oyunculardır.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake poker gerçek mi?", "Evet. Stake gerçek oyunculara karşı oynanan cash game, Sit & Go ve multi-masa turnuvalar içeren tam özellikli bir poker sitesi işletiyor."),
    ("Hangi kripto paralar kabul ediliyor?", "BTC, ETH, LTC, XRP, SOL, TRX, BNB ve Stake'teki tüm desteklenen kriptolar poker'da çalışıyor. Ayrıca MoonPay ile fiat."),
    ("MAX3000 poker'da çalışıyor mu?", "Evet. %200 $3.000'e kadar bonus tüm Stake platformunda geçerli. Poker rakeback için katkı oranını kontrol edin."),
  ], 'Sık Sorulan Sorular')}'''

# ═══════════════════════════════════════════════════════
# aviator: TR 2559w -> KO 5850w
# ═══════════════════════════════════════════════════════
def body_aviator():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Aviator <span class="text-gradient-gold">Oyunu</span></h2></div>
      {tr_club_cards([
        ('Crash Mekanigi', 'Uçak kalkıyor ve çarpan yükseliyor. Çökmeden önce istediginiz zaman çekin. Uzun bekleyin, daha büyük çarpan; ama çökmeden önce çekin. 10.000x\'e kadar çarpanlar.'),
        ('Kanıtlanabilir Adillik', 'Spribe tarafindan üretilmistir. Dogrulama protokolü oyuncu ve sunucu arasinda paylasilan seed\'e dayanıyor. Her tur Stake\'te dogrulanabilir.'),
        ('Çift Bahis', 'Ayni anda iki bahis yapın. Küçük bir kâr kilitlemek için birini erkenden çekin, digeri için büyük çarpan bekleyin.'),
        ('Canli Istatistikler', 'Stake son 500 turun en büyük kazancini, son yüksek turları ve diger oyuncularin bahislerini canli gösteriyor.'),
        ('MAX3000 Bonusu', '%200 $3.000\'e kadar. Aviator\'da bonusu kullanin. Ev kenari ~%3, bahis sarти için iyi bir seçenek.'),
        ('Uyumluluk', 'Aviator tarayıcıda ve telefonda çalışıyor. Ayrıca uygulama gerekmiyor. Orta internet hizlerinde dahi sorunsuz.'),
      ])}
    </div>
  </section>

  {tr_girl_break('Uçak Yukseliyor. <span class="text-gradient-gold">Ne Zaman Çekiyorsunuz?</span>', '<span class="code-highlight">MAX3000</span> ile %200 $3.000\'e kadar. Aviator bonusla oyna.', 'Aviator\'ı Oyna', 'girl-aviator')}

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Aviator <span class="text-gradient-gold">Strateji Rehberi</span></h2></div>
      {tr_club_cards([
        ('Düsük Katlı Güvenli Çekim', 'Çogunlukla 1.2x-2.0x gibi düsük çarpanlarda çekin. Daha yüksek kazanma orani, daha küçük kazanç. Tutarlı bakiye büyümesi için popüler strateji.'),
        ('Çift Bahis Stratejisi', 'Ilk bahsin çogu kisminı 1.5x\'te çekin; ikinci bahsi yüksek çarpan için bekletin. Kısmen güvence, kısmen yüksek ödül potansiyeli.'),
        ('Çarpan Takibi', 'Son 500 tur istatistiklerini izleyin. Örüntüler rasgele bir RNG\'ye karsi kanıtlanamazken, çok sayida ardışık düsük çarpan gerçekten gerçeklesebilir.'),
        ('Bahis Limitleri Belirleyin', 'Oturum basina kazanma ve kayip limitlerini önceden belirleyin. Belirlenen kaybı geçen bir oturumda durdur.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Aviator oyunu nedir?", "Spribe'ın crash oyunu. Uçak kalkıyor ve kazanç çarpanı yükseliyor. Çökmeden önce çekin. 10.000x'e kadar çarpanlar."),
    ("Aviator adil mi?", "Spribe'ın Aviator'ı kanıtlanabilir adil kriptografik protokol kullanıyor. Her tur doğrulanabilir."),
    ("Aviator'ı MAX3000 bonusuyla oynayabilir miyim?", "Evet. %200 $3.000'e kadar hoşgeldin bonusu Aviator'a uygulanır. Ev kenarı ~%3. Bahis şartı katkı oranını kontrol edin."),
  ], 'Sık Sorulan Sorular')}'''

# ═══════════════════════════════════════════════════════
# reserves: TR 2331w -> KO 6028w
# ═══════════════════════════════════════════════════════
def body_reserves():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake On-chain <span class="text-gradient-gold">Rezervleri</span></h2></div>
      {tr_intel_cards([
        ('Toplam Rezervler', '$339.53M', '28 Mayis 2026 Arkham etiketli snapshot.'),
        ('Ethereum', '%74', 'En büyük pay. ETH ve ERC-20 (USDT USDC).'),
        ('Solana', '%14', 'SOL ve Solana DeFi protokolleri.'),
        ('Diger Zincirler', '%12', 'Tron (USDT TRC-20) %5, BNB Chain %6, diger zincirler %1.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">On-chain Rezervler <span class="text-gradient-gold">Neden Önemli</span></h2></div>
      {tr_club_cards([
        ('Takip Edilebilir Seffaflık', 'Herkes Arkham Intel veya blockchain explorer üzerinden etiketlenmiş cüzdan bakiyelerini doğrulayabilir. Denetim raporu gerekmiyor.'),
        ('Olasılıksal Kanıta Kıyasla', 'Çogu platform bağımsız dogrulama olmaksizin varlık tabanlı açıklamalar yapıyor. Stake gerçek cüzdan adreslerini yayınladı. Fark büyük.'),
        ('cryptotips.com Haftalık Takip', '<a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener" style="color:var(--gold);">cryptotips.com</a> Arkham verilerini haftalık derliyor ve basit bir formatta sunuyor.'),
        ('Sektörle Karşılaştırma', 'Az sayida büyük kumar platformu kamuya açık izlenebilir rezerv verisi yayınlıyor. Stake bu kategoride öncüler arasında.'),
        ('$41M Hack Testi', 'Eylül 2023\'te hack sonrası Arkham takipli rezervler $300M\'ın üzerinde kaldı. Gerçek ödeme gücünün pratik kanıtı.'),
        ('Anlık Görüntü Metodolojisi', 'Her anlık görüntü Arkham etiketli cüzdanları yakalıyor. Fiat dışı kripto varlık. Elde tutulan dolar değeri anlık fiyatlara göre değişebilir.'),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Zincir Bazinda <span class="text-gradient-gold">Rezerv Dağılımı</span></h2></div>
      <table class="data-table" style="max-width:600px;margin-top:24px;">
        <thead><tr><th>Zincir</th><th>Pay</th><th>Not</th></tr></thead>
        <tbody>
          <tr><td><strong>Ethereum</strong></td><td>%74</td><td>ETH + ERC-20 USDT/USDC</td></tr>
          <tr><td><strong>Solana</strong></td><td>%14</td><td>SOL + DeFi protokolleri</td></tr>
          <tr><td><strong>BNB Chain</strong></td><td>%6</td><td>BNB + BEP-20</td></tr>
          <tr><td><strong>Tron</strong></td><td>%5</td><td>TRC-20 USDT</td></tr>
          <tr><td><strong>Diger</strong></td><td>%1</td><td>Çesitli zincirler</td></tr>
        </tbody>
      </table>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">Kaynaklar: <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com on-chain Stake takibi</a> · Arkham Intelligence etiketli cüzdan verisi · 28 Mayis 2026 snapshot</p>
    </div>
  </section>

  {tr_faq_section([
    ("Stake rezervlerini nerede doğrulayabilirim?", "Arkham Intel üzerinden. Stake etiketlenmiş cüzdan adreslerini kamuoyuyla paylaştı. cryptotips.com bu verileri haftalık takip ediyor."),
    ("Stake'in mevcut rezerv büyüklüğü nedir?", "28 Mayıs 2026 snapshot: $339.53M Arkham etiketli cüzdanlarda. Ethereum %74, Solana %14, Tron USDT %5, BNB Chain %6."),
    ("On-chain rezervler mali güvencenin garantisi mi?", "On-chain rezervler varlık tutma konusunda şeffaflığı kanıtlar. Ancak tam bir denetimin yerini tutmaz. 'Güven bize' PDF'lerinden çok daha iyi ama tam garanti sayılmaz."),
  ], 'Sık Sorulan Sorular')}'''


# ═══════════════════════════════════════════════════════
# sports: TR 3283w -> KO 6787w
# ═══════════════════════════════════════════════════════
def body_sports():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Spor <span class="text-gradient-gold">Bahisleri</span></h2></div>
      {tr_club_cards([
        ('40+ Küresel Lig', 'Premier Lig, La Liga, Serie A, Bundesliga, Ligue 1, UEFA Sampiyonlar Ligi. Ayrica NBA, NFL, NHL, MLB, tenis, kriket, e-spor.'),
        ('Canli Bahis', 'Anlık güncellenen oranlarla maç içi bahis. Canli pazarlar sonraki golü, yariyi, seti ve yüzlerce seçeneği kapsıyor.'),
        ('Parlay Olusturucu', 'Birden fazla etkinligi bir kupon üzerinde birlestirin. Çarpan eklendikçe artar. Kaybeden bir maçtan korumak için Stake Shield parlay koruması.'),
        ('Spor Sigorta Teklifleri', 'NHL 2 gol öncü erken ödeme, NBA devre arasında 12+ sayı, MLB 9 inning iadesi, UFC bölünmüş karar, Premier Lig erken ödeme, at yarışları iade.'),
        ('MAX3000 ile Spor', 'Hosgeldin bonusu spor bahislerini kapsiyor. Spor bahisleri bahis sartına %75 katkida bulunuyor (casino oyunlarının %100\'üne kıyasla).'),
        ('Bahis Formatları', 'Ondalık, kesirli ve Amerikan formatında oranlar. Hesap ayarlarından format değistirin.'),
      ])}
    </div>
  </section>

  {tr_girl_break('40+ Lig. <span class="text-gradient-gold">Tek Bahis.</span>', '<span class="code-highlight">MAX3000</span> ile %200 $3.000\'e kadar. Spor ve casinoyu aynı bonusla oyna.', 'Simdi Bahis Yap', 'girl-sports')}

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Spor <span class="text-gradient-gold">Kapsami Detayi</span></h2></div>
      {tr_club_cards([
        ('Futbol', 'Premier Lig, La Liga, Serie A, Bundesliga, Ligue 1, Champions League, Europa League, World Cup, Euro. Maç öncesi ve canli bahis. Geniş pazar seçenekleri.'),
        ('Basketbol (NBA)', 'NBA sezon ve playoff. Maç kazanani, handikap, üst/alt. Devre arası erken ödeme teklifi. FIBA dünya turnuvalari.'),
        ('Amerikan Futbolu (NFL)', 'NFL sezon, playoff, Super Bowl. Oyuncu prop bahisleri, touchdowns, passing yards. MVP spekülasyonu.'),
        ('Hokey (NHL)', 'NHL sezon ve playoff. Gol sayisi, gol atan oyuncu, perioт bahisleri. 2 gol öncü NHL erken ödeme teklifi.'),
        ('Tenis', 'Grand Slam, ATP, WTA, Davis Cup. Set kazanani, oyun handikap, tenis canlı bahis.'),
        ('E-Spor', 'CS:GO, Dota 2, League of Legends, Valorant, Rocket League. Büyük turnuvalar için kapsamlı bahis pazarları.'),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Spor Bahis <span class="text-gradient-gold">İpuçlari</span></h2></div>
      {tr_club_cards([
        ('Bahis Sarти Hesabi', 'Spor bahisleri %75 katkida bulunuyor. $500 depozit + $1.000 bonus = $1.500 × 40 = $60.000 bahis gereksinimi. Spor üzerinden tamamlamak için $80.000 spor bahsi gerekir.'),
        ('Deeger Bahis', 'Kapatilmamis pozisyon anlamına gelen piyasalardaki deger arayan bahisçiler, bahisçinin kenari hesaba kattikları için daha fazla kazanabilir.'),
        ('Parlay Stratejisi', '2-3 lig sohbetini birlestiren küçük parlaylar büyük bahis riski olmadan çarpanı artırır. 5+ seçimli parlaylar düsük olasilikli bölgeye giriyor.'),
        ('Canli Bahis Zamanlama', 'Spor etkinlikleri sirasında oranlar hızla değişiyor. En iyi değer genellikle öncü ekip skora ulastigında ortaya çikar.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake futbolu kapsıyor mu?", "Evet. Stake Premier Lig, La Liga, Serie A, Bundesliga, UEFA Şampiyonlar Ligi dahil 40+ futbol ligi kapsıyor. Maç öncesi ve canlı bahis."),
    ("Spor bahislerinde bahis şartı katkısı nedir?", "Spor bahisleri MAX3000 bahis şartına %75 katkıda bulunuyor. Casino oyunları %100 katkı sağlar."),
    ("Canlı bahis mevcut mu?", "Evet. Stake maç sırasında anlık güncellenen oranlarla canlı bahis sunuyor."),
  ], 'Sık Sorulan Sorular')}'''

# ═══════════════════════════════════════════════════════
# stake-us-bonus: TR 2252w -> KO 5835w
# ═══════════════════════════════════════════════════════
def body_stake_us_bonus():
    return f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake.us <span class="text-gradient-gold">Hosgeldin Teklifi</span></h2></div>
      {tr_intel_cards([
        ('Gold Coins', '560.000 GC', 'Yalnızca oyun için. Tüm casino oyunlarında kullanılır.'),
        ('Stake Cash', '56 SC', '3x oynama sonrasi ödüle çevrilebilir. Gerçek para değil.'),
        ('Rakeback', '%3,5', 'Sürekli olarak masadan size dönen masaj komisyonu yüzdesi.'),
        ('Uygunluk', 'Yalnızca 21+', 'Stake.us 37 ABD eyaletinde mevcut. 21 yasından büyükler için.'),
      ])}
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">İki Platformun <span class="text-gradient-gold">Farki</span></h2></div>
      <div class="club-grid">
        <div class="club-card">
          <h3>Stake.com - Global</h3>
          <p>Gerçek para. Curaçao OGL/2024/1451/0918. Kripto ve fiat. Casino, spor, poker. Kod <span class="code-highlight">MAX3000</span> ile %200 $3.000\'e kadar, 40x çevrim. 18+ çogu ülkede (ABD ve UK hariç).</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Global Kapıyı Aç</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - ABD</h3>
          <p>Sweepstakes. Sweepsteaks Limited. Yalnizca casino, spor yok. Kod <span class="code-highlight">MAX3000</span> ile 560K GC + 56 SC + %3,5 rakeback. 37 ABD eyaletinde 21+.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Stake.us\'a Katıl</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake.us <span class="text-gradient-gold">Nasil Çalisiyor</span></h2></div>
      {tr_step_cards([
        ('1. Kaydolun', 'MAX3000 referans linki ile Stake.us\'a gidin. Kayıt ücretsizdir. Email, kullanici adı, sifre, dogum tarihi.'),
        ('2. Hosgeldin Bonusu', 'Kayıt sırasında 560.000 Gold Coins + 56 Stake Cash + %3,5 rakeback otomatik uygulanır.'),
        ('3. Gold Coins ile Oynayın', 'Tüm casino oyunlarını Gold Coins ile ücretsiz oynayın. GC satın alarak bakiyenizi artırabilirsiniz.'),
        ('4. Stake Cash Kullanımı', 'Stake Cash\'i desteklenen oyunlarda 3x oynayın. Sonrasında nakit ödüle çevrilebilir.'),
      ])}
    </div>
  </section>

  {tr_faq_section([
    ("Stake.com ile Stake.us arasındaki fark nedir?", "Stake.com gerçek para küresel platformdur. Stake.us, Sweepsteaks Limited tarafından işletilen bir ABD sweepstakes platformudur. Gerçek para bahsi yok, kripto yok. MAX3000 her ikisinde de çalışır."),
    ("Stake.us'ta MAX3000 bana ne verir?", "560.000 Gold Coins + 56 Stake Cash + %3,5 rakeback. Kayıt sırasında MAX3000 referans linki ile uygulanır."),
    ("Stake.us ücretsiz mi?", "Daily coinler ücretsiz olarak drop'lardan alınabilir. Stake Cash 3x oynama sonrası ödüle çevrilebilir. Gerçek para yatırma zorunlu değil."),
  ], 'Sık Sorulan Sorular')}'''


# ══════════════════════════════════════════════════════
# EXECUTION
# ══════════════════════════════════════════════════════
PAGES_TO_REFRESH = {
    'tr/about-stake/index.html': body_about_stake,
    'tr/casino/index.html': body_casino,
    'tr/promo-code/index.html': body_promo_code,
    'tr/mirror/index.html': body_mirror,
    'tr/payments/index.html': body_payments,
    'tr/poker/index.html': body_poker,
    'tr/aviator/index.html': body_aviator,
    'tr/reserves/index.html': body_reserves,
    'tr/sports/index.html': body_sports,
    'tr/stake-us-bonus/index.html': body_stake_us_bonus,
}

def add_calc_script(content):
    """Add bonus calculator JS to promo-code page."""
    calc_js = '''  <script>
    (function(){
      var range=document.getElementById('depRange');
      var num=document.getElementById('depAmount');
      var bonusOut=document.getElementById('bonusOut');
      var wagerOut=document.getElementById('wagerOut');
      var totalOut=document.getElementById('totalOut');
      var effOut=document.getElementById('effOut');
      if(!range||!num) return;
      var fmt=function(n){return '$'+Math.round(n).toLocaleString('en-US');};
      function recalc(){
        var dep=parseFloat(num.value);
        if(isNaN(dep)||dep<10) dep=10;
        if(dep>1500) dep=1500;
        num.value=dep; range.value=dep;
        var bonus=Math.min(dep*2,3000);
        var total=dep+bonus;
        var wager=total*40;
        var eff=(bonus/dep)*100;
        bonusOut.textContent=fmt(bonus);
        wagerOut.textContent=fmt(wager);
        totalOut.textContent=fmt(total);
        effOut.textContent=Math.round(eff)+'%';
      }
      range.addEventListener('input',function(){num.value=range.value;recalc();});
      num.addEventListener('input',recalc);
      num.addEventListener('change',recalc);
      recalc();
    })();
  </script>'''
    return content.replace('<script src="/script.min.js', calc_js + '\n  <script src="/script.min.js')

print("\nRefreshing TR pages...")
for rel_path, body_fn in PAGES_TO_REFRESH.items():
    full_path = os.path.join(ROOT, rel_path)
    try:
        original = read_file(full_path)
        new_body = body_fn()
        updated = inject_body_between_promo_and_footer(original, new_body)
        if 'promo-code' in rel_path:
            updated = add_calc_script(updated)
        write_file(full_path, updated)
        old_wc = len(original.split())
        new_wc = len(updated.split())
        print(f"  {rel_path}: {old_wc}w -> {new_wc}w (+{new_wc-old_wc}w)")
    except Exception as e:
        print(f"  ERROR {rel_path}: {e}")
        import traceback; traceback.print_exc()

print("\nTR refresh complete.")

