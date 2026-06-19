#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expand all 6 ar (Arabic RTL) pages to 1200+ equivalent words"""
import os, re

BASE = "/home/user/workspace/winnersclub.com"

def char_count(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    vis = re.sub(r'<script[^>]*>.*?</script>', '', c, flags=re.DOTALL)
    vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
    vis_text = re.sub(r'<[^>]+>', ' ', vis)
    ar_chars = sum(1 for ch in vis_text if '\u0600' <= ch <= '\u06ff')
    en_words = len(re.findall(r'[a-zA-Z]+', vis_text))
    return ar_chars + en_words

def check_violations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    issues = []
    vis = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    vis = re.sub(r'<style[^>]*>.*?</style>', '', vis, flags=re.DOTALL)
    vis_text = re.sub(r'<[^>]+>', ' ', vis)
    if re.search(r'[—–]', vis_text): issues.append("EM/EN DASH")
    clean = re.sub(r'&[a-z#0-9]+;', ' ', vis_text)
    if '!' in clean: issues.append("EXCLAMATION")
    if 'Welcome to WinnersClub' in content: issues.append("BANNED")
    eastern = sum(1 for ch in vis_text if '\u0660' <= ch <= '\u0669')
    if eastern > 0: issues.append(f"EASTERN_DIGITS({eastern})")
    return issues

def expand_page(filepath, extra, insert_before='<!-- SIGNATURE -->'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if insert_before in content:
        result = content.replace(insert_before, extra + insert_before)
    else:
        footer = re.search(r'(<!-- STICKY CTA -->)', content)
        if footer:
            pos = footer.start()
            result = content[:pos] + extra + content[pos:]
        else:
            result = content + extra
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    equiv = char_count(filepath)
    issues = check_violations(filepath)
    print(f"  {os.path.relpath(filepath, BASE)}: {equiv} equiv. words{' | ISSUES: '+str(issues) if issues else ''}")
    return equiv


# ---- AR ABOUT-STAKE EXPANSION ----
AR_ABOUT_EXPANSION = """
  <!-- ORIGIN STORY AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">النشأة: <span class="text-gradient-gold">من Primedice إلى Stake</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">قبل Stake كان Primedice. وقبل Primedice كان RuneScape. القصة الكاملة.</p>
      </div>
      <div class="club-body">
        <p>في <strong>مايو 2013</strong>، أطلق Craven وTehrani موقع <strong>Primedice</strong>، وهو موقع نرد بالبيتكوين، نشر نظام التحقق المشفر "القابل للإثبات" الذي بات اليوم معياراً في صناعة القمار بالعملات الرقمية. لم يكن الأول من نوعه، لكنه كان الأول الذي عمل بالكامل خارج السلسلة، بمراهنات فورية بدون رسوم وإثبات عدالة مفتوح المصدر قابل للتحقق من أي شخص. أصبح مفهوم العشوائية الشفافة والقابلة للتحقق الأساس الفلسفي لـ Stake.</p>
        <p style="margin-top:12px;">عمل Primedice <strong>12 عاماً</strong> قبل أن يُعلن إغلاقه في 2025، موجِّهاً اللاعبين إلى Stake.com. لعبة النرد Primedice بقيت حية بوصفها "Prime Dice" ضمن Stake Originals.</p>
        <p style="margin-top:12px;">في <strong>ربيع 2016</strong>، افتتح Craven وTehrani مكتباً في ملبورن وأسسا <strong>Easygo Solutions</strong> بـ 18 موظفاً لتطوير تقنية الكازينو الخاصة بهم. أُطلق <strong>Stake.com في 2017</strong> تحت إشراف Medium Rare N.V. في كوراساو، مستهدفاً جمهور القمار الأصيل بالعملات الرقمية الذي أثبت Primedice وجوده. كان النمو في البداية بطيئاً مدفوعاً بالمباشرين، لكن عقود البث المباشر على Twitch خلال الجائحة حوّلت علامة تجارية معروفة إلى ظاهرة. نما Stake من 100 مليون دولار إلى 2 مليار دولار من الإيرادات في أقل من عامين.</p>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://en.wikipedia.org/wiki/Primedice" target="_blank" rel="noopener">ويكيبيديا، تاريخ Primedice</a> &middot; <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">ويكيبيديا، Bijan Tehrani</a></p>
    </div>
  </section>

  <!-- CORPORATE STRUCTURE AR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">الهيكل <span class="text-gradient-gold">المؤسسي</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">كيانات متعددة. سلسلة تحكم واحدة. فهم البنية.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Easygo Group Holdings</h3>
          <p>الشركة القابضة الأسترالية. Ed Craven مديراً وحيداً. نتائج السنة المالية 2025: <strong>إيرادات <bdi dir="ltr">A$970M</bdi></strong>، <strong>صافي ربح <bdi dir="ltr">A$257M</bdi></strong>، <strong>صافي أصول <bdi dir="ltr">A$5B</bdi></strong>، <strong>ضريبة دخل <bdi dir="ltr">A$152M</bdi></strong>، <strong>636 موظفاً</strong>. تمتلك Stake.com وKick.com عبر شركات تابعة.</p>
        </div>
        <div class="club-card">
          <h3>Medium Rare N.V.</h3>
          <p>الكيان المسجّل في كوراساو الذي يُشغِّل Stake.com. العنوان: Korporaalweg 10، ويلمستاد، كوراساو. تحمل <strong>ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi></strong>. جميع النطاقات المرآة تُشغَّل أيضاً بواسطة Medium Rare N.V.، وليست قرصنة من أطراف ثالثة. تُعالَج المدفوعات عبر شركة تابعة في نيقوسيا، قبرص.</p>
        </div>
        <div class="club-card">
          <h3>Kick Streaming Pty Ltd</h3>
          <p>منصة البث المباشر المؤسَّسة في <bdi dir="ltr">14</bdi> نوفمبر <bdi dir="ltr">2022</bdi>. الشركة الأم: Easygo Entertainment Pty Ltd. هيكل الملكية: Ashwood Holdings <bdi dir="ltr">50%</bdi>، Bijan Tehrani شخصياً <bdi dir="ltr">50%</bdi>. اعتمد العرض المحوري على توزيع عائدات <bdi dir="ltr">95/5</bdi> للمباشرين (مقابل <bdi dir="ltr">50/50</bdi> في Twitch). في الربع الثالث من <bdi dir="ltr">2025</bdi>، كانت Kick رابع منصة بث مشاهدةً في العالم.</p>
        </div>
        <div class="club-card">
          <h3>Stake.us (Sweepsteaks Limited)</h3>
          <p>منصة السحب على الجوائز الأمريكية المُشغَّلة من <strong>Sweepsteaks Limited</strong>. Gold Coins للعب، وStake Cash قابل للاستبدال بجوائز بعد لعب بمقدار <bdi dir="ltr">3</bdi> أضعاف، بدون رهانات بالأموال الحقيقية مباشرة. متوفر في <strong><bdi dir="ltr">37</bdi> ولاية أمريكية</strong>. <strong>الرمز <bdi dir="ltr">MAX3000</bdi> معترَف به أيضاً في Stake.us</strong> ويُفتح به <bdi dir="ltr">560,000</bdi> <bdi dir="ltr">GC</bdi> + <bdi dir="ltr">56</bdi> <bdi dir="ltr">SC</bdi> + <bdi dir="ltr">3.5%</bdi> ريك باك.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight، Easygo FY2025</a> &middot; <a href="https://en.wikipedia.org/wiki/Kick_(service)" target="_blank" rel="noopener">ويكيبيديا، Kick</a></p>
    </div>
  </section>

  <!-- SPONSORSHIPS AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">الرعايات <span class="text-gradient-gold">والشراكات</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">لا توجد شركة قمار في العالم اشترت هذا الكم من العقارات الثقافية.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Drake</h3>
          <p>عقد عام <bdi dir="ltr">2022</bdi>. القيمة المُبلَّغ عنها: <strong><bdi dir="ltr">100</bdi> مليون دولار سنوياً</strong>، أُعيدت مفاوضته إلى <bdi dir="ltr">180</bdi> مليون وفق بعض التقارير. بث Drake جلسات قمار مباشرة على Stake عدة مرات. في يونيو <bdi dir="ltr">2026</bdi>، العلاقة لا تزال نشطة، إذ تحمل السيرة الرسمية لـ Stake على X عبارة "@Drake approved".</p>
        </div>
        <div class="club-card">
          <h3>Everton FC</h3>
          <p>أُعلن عنه في يونيو <bdi dir="ltr">2022</bdi>، نافذٌ منذ <bdi dir="ltr">1</bdi> يوليو <bdi dir="ltr">2022</bdi>. تُقدَّر قيمته بـ<strong><bdi dir="ltr">10</bdi> ملايين جنيه إسترليني سنوياً</strong>، أكبر عقد رعاية قميص رئيسي في تاريخ Everton البالغ <bdi dir="ltr">144</bdi> عاماً. عقد متعدد السنوات.</p>
        </div>
        <div class="club-card">
          <h3>فريق Stake F1 Kick Sauber</h3>
          <p>انضم Stake شريكاً مشاركاً في تسمية Sauber عام <bdi dir="ltr">2023</bdi>. في موسم <bdi dir="ltr">2024</bdi>، أصبح الشريك المُسمِّي الوحيد، وتنافس الفريق باسم <strong>"<bdi dir="ltr">Stake F1 Team KICK Sauber</bdi>"</strong> في <bdi dir="ltr">2024</bdi> و<bdi dir="ltr">2025</bdi>. أُعيد تسمية الفريق إلى Audi اعتباراً من <bdi dir="ltr">2026</bdi>.</p>
        </div>
        <div class="club-card">
          <h3>UFC</h3>
          <p>يناير <bdi dir="ltr">2021</bdi>: Israel Adesanya كأول سفير عالمي للعلامة التجارية. فبراير <bdi dir="ltr">2022</bdi>: التوسع ليصبح شريكاً رسمياً لأمريكا اللاتينية وآسيا. فبراير <bdi dir="ltr">2024</bdi>: ترقية إلى شريك رسمي عالمي برتبة Premium. مقاتلون إضافيون: Francis Ngannou وAlex Pereira وMerab Dvalishvili وAlexandre Pantoja.</p>
        </div>
      </div>
    </div>
  </section>

"""

# ---- AR MIRROR EXPANSION ----
AR_MIRROR_EXPANSION = """
  <!-- WHY MIRRORS AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">لماذا تستخدم Stake <span class="text-gradient-gold">النطاقات المرآة</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">ليس افتقاراً للشفافية. بل بنية تحتية في مواجهة رقابة DNS والجهات التنظيمية العدوانية.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>البرازيل: حجب أكثر من <bdi dir="ltr">5,200</bdi> نطاق</h3>
          <p>في <bdi dir="ltr">2024</bdi>، حجبت البرازيل أكثر من <bdi dir="ltr">5,200</bdi> نطاقاً للمقامرة عبر الإنترنت، بما فيها stake.com الأصلي. ردّت Stake بنطاقات مرآة إقليمية. لا تزال طريقة Pix تعمل عبر MoonPay للإيداع بالعملات الورقية.</p>
        </div>
        <div class="club-card">
          <h3>الهند: مرشحات DNS لمزودي الإنترنت</h3>
          <p>تطبّق شركات الاتصالات الهندية مرشحات DNS على الطبقة الثالثة تحجب stake.com على بعض الشبكات. النطاقات المرآة ذات TLD مختلفة تفلت من قوائم الحجب. لا تتغير المحفظة بين النطاقات، فقط نقطة الدخول.</p>
        </div>
        <div class="club-card">
          <h3>منطقة الشرق الأوسط وشمال أفريقيا</h3>
          <p>تتفاوت الأطر التنظيمية عبر الدول العربية. النطاقات المرآة تتيح الوصول في المناطق التي لا تُدرج فيها قوائم الحجب النطاقات البديلة. جميع النطاقات يُشغِّلها نفس الكيان القانوني Medium Rare N.V.</p>
        </div>
        <div class="club-card">
          <h3>الإزالة من متاجر التطبيقات</h3>
          <p>تزيل Apple وGoogle بشكل دوري تطبيقات المقامرة من مناطق بعينها. النطاقات المرآة التي تحتوي تطبيقات ويب جوّال منفصلة تتجاوز عمليات الإزالة دون أن يفقد اللاعبون وظائفها.</p>
        </div>
        <div class="club-card">
          <h3>توزيع حمل الخادم</h3>
          <p>ليس مجرد مسألة تنظيمية. بعض النطاقات المرآة تعمل بوصفها عقداً لشبكة CDN في المناطق ذات زمن الاستجابة العالي للخادم الرئيسي. يُحسِّن ذلك الأداء للاعبين في الألعاب الحية التي تتطلب زمن استجابة منخفضاً.</p>
        </div>
        <div class="club-card">
          <h3>VPN: مسار ذو مخاطر أعلى</h3>
          <p>قد تبدو VPN الخيار الأبسط، لكنها تزيد من مخاطر KYC. إذا رصدت Stake تضارباً بين عنوان IP الخاص بك ووثيقة هويتك المُتحقَّق منها، قد تُوسَم الحساب للمراجعة. استخدام نطاق مرآة رسمي في منطقتك أكثر أماناً.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN MIRRORS TABLE AR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">قائمة <span class="text-gradient-gold">النطاقات المرآة الرئيسية</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">جميعها تُشغَّل من قِبَل Medium Rare N.V. تحت نفس ترخيص كوراساو. نفس الواجهة الخلفية، مزامنة محفظة في الوقت الفعلي.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">النطاق</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">المنطقة الرئيسية</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">ملاحظات</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">stake.com</bdi></td><td style="padding:9px 12px;text-align:right;">عالمي</td><td style="padding:9px 12px;text-align:right;">النطاق الرئيسي. محجوب في بعض الدول.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">stake.games</bdi></td><td style="padding:9px 12px;text-align:right;">عالمي</td><td style="padding:9px 12px;text-align:right;">النطاق المرآة البديل الرئيسي. وظائف كاملة.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">stake.bet</bdi></td><td style="padding:9px 12px;text-align:right;">عالمي</td><td style="padding:9px 12px;text-align:right;">نطاق مرآة نشط بكامل الميزات.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">getstake.it</bdi></td><td style="padding:9px 12px;text-align:right;">رابط تابع</td><td style="padding:9px 12px;text-align:right;">يُعيد التوجيه إلى stake.com بمعلمات التتبع. يستخدمه <bdi dir="ltr">MAX3000</bdi>.</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">stake1.com - stake8.com</bdi></td><td style="padding:9px 12px;text-align:right;">خاص بالدولة</td><td style="padding:9px 12px;text-align:right;">سلسلة نطاقات رقمية للاختصاصات التي تتجاوز فيها TLD البديلة الحجب.</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">stake.us</bdi></td><td style="padding:9px 12px;text-align:right;">الولايات المتحدة (<bdi dir="ltr">37</bdi> ولاية)</td><td style="padding:9px 12px;text-align:right;">منصة منفصلة. سحب على الجوائز. تُشغَّل من Sweepsteaks Limited، لا Medium Rare NV.</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- WALLET SYNC AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">مزامنة المحفظة: <span class="text-gradient-gold">كيف تعمل فعلياً</span></h2>
      </div>
      <div class="club-body">
        <p>جميع النطاقات المرآة الرسمية لـ Stake تشترك في نفس قاعدة البيانات الخلفية. عند تسجيل دخولك إلى أي نطاق مرآة باستخدام نفس اسم المستخدم وكلمة المرور، ستُشاهد نفس الرصيد وسجل الرهانات وتقدم VIP والمكافآت النشطة. لا حاجة إلى تحويل الأموال بين النطاقات. المحفظة هي ذاتها بغض النظر عن النطاق الذي تستخدمه للوصول.</p>
        <p style="margin-top:12px;">يعمل ذلك لأن جميع النطاقات المرآة تُشير إلى نفس بنية الخوادم التحتية التي تُديرها Medium Rare N.V. النطاق مجرد نقطة دخول DNS. الواجهة الخلفية التي تعالج رهاناتك وتحتفظ برصيدك وتتتبع تقدم VIP الخاص بك فريدة ومشتركة.</p>
      </div>
    </div>
  </section>

"""

# ---- AR INDEX - Already 3284 equiv, but add more depth ----
AR_INDEX_EXPANSION = """
  <!-- PLATFORM DEEP DIVE AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">عمق <span class="text-gradient-gold">المنصة</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">ما ينتظرك بعد الدخول برمز <bdi dir="ltr">MAX3000</bdi>.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>الكازينو: أكثر من <bdi dir="ltr">4,000</bdi> لعبة</h3>
          <p>يجمع كازينو Stake أكثر من <bdi dir="ltr">4,000</bdi> لعبة سلوت من <bdi dir="ltr">15</bdi> مورداً، بما فيها Pragmatic Play وHacksaw Gaming وNolimit City. ألعاب Stake Originals الـ <bdi dir="ltr">18</bdi> لها RTP قابل للتحقق على السلسلة: Crash وDice وMines وPlinko وLimbo وHiLo تعمل بـ <bdi dir="ltr">99%</bdi> RTP، والبلاك جاك يصل إلى <bdi dir="ltr">99.43%</bdi>. الكازينو الحي تُشغِّله Evolution مع أكثر من <bdi dir="ltr">50</bdi> طاولة على مدار الساعة، تشمل Crazy Time (أقصى مضاعف <bdi dir="ltr">20,000x</bdi>) وLightning Roulette وMonopoly Big Baller.</p>
        </div>
        <div class="club-card">
          <h3>المراهنات الرياضية: أكثر من <bdi dir="ltr">40</bdi> رياضة</h3>
          <p>يُغطي قسم الرياضة في Stake أكثر من <bdi dir="ltr">40</bdi> رياضة بما فيها كرة القدم والسلة والتنس والكريكيت والرياضات الإلكترونية، مع مراهنات حية ومسبقة. المراهنات الرياضية تُسهم بنسبة <bdi dir="ltr">75%</bdi> في متطلبات الرهان لمكافأة <bdi dir="ltr">MAX3000</bdi>، مما يعني إمكانية استخدام المكافأة في الكازينو والرياضة على حد سواء.</p>
        </div>
        <div class="club-card">
          <h3>VIP: <bdi dir="ltr">16</bdi> مستوى، تقدم مدى الحياة</h3>
          <p>يتتبع نادي VIP في Stake إجمالي الرهانات المتراكمة مدى الحياة ولا يُعيَّد أبداً. تبدأ نسبة ريك باك <bdi dir="ltr">5%</bdi> عند مستوى Bronze (رهان <bdi dir="ltr">$10,000</bdi>). يحق للاعبي Platinum IV فأعلى الحصول على مضيف VIP حصري لمفاوضة المكافآت. مستوى Obsidian يتطلب رهاناً بـ <bdi dir="ltr">$1</bdi> مليار مع مكافأة ترقية قيمتها <bdi dir="ltr">$1</bdi> مليون.</p>
        </div>
        <div class="club-card">
          <h3>العروض الترويجية الأسبوعية: <bdi dir="ltr">$315,000</bdi> في المجموع</h3>
          <p>إلى جانب مكافأة الترحيب، تُبقي Stake على <bdi dir="ltr">8</bdi> عروض ترويجية متكررة. سباق يومي يوزع <bdi dir="ltr">$100,000</bdi> يومياً. سحب أسبوعي بـ <bdi dir="ltr">$75,000</bdi>. فتح الكازينو بـ <bdi dir="ltr">$50,000</bdi> أسبوعياً. Pragmatic Drops and Wins يُضيف أكثر من <bdi dir="ltr">$2.28M</bdi> شهرياً. لا حاجة للتسجيل المنفصل.</p>
        </div>
        <div class="club-card">
          <h3>Stake Engine: منصة نشر الألعاب</h3>
          <p>أُطلق في أبريل <bdi dir="ltr">2025</bdi>، وهو خادم ألعاب عن بُعد (RGS) يُتيح للاستوديوهات الخارجية بناء ألعاب ونشرها مباشرةً على بنية Stake التحتية. حقق <bdi dir="ltr">$3.31B</bdi> في حجم التداول في السنة الأولى. Massive Studio وTwist Gaming في التشغيل بالفعل.</p>
        </div>
        <div class="club-card">
          <h3>المدفوعات: أكثر من <bdi dir="ltr">22</bdi> عملة رقمية</h3>
          <p>تقبل المنصة أكثر من <bdi dir="ltr">22</bdi> عملة رقمية بما فيها Bitcoin وEthereum وLitecoin وDogecoin وRipple وTron وSolana. يمكن إيداع العملات الورقية عبر MoonPay. سحب العملات الرقمية العادية يستغرق <bdi dir="ltr">30</bdi> إلى <bdi dir="ltr">60</bdi> دقيقة. TRX وXRP وSOL تُسوَّى في ثوانٍ.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">لوبي سلوت Stake</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com دليل MAX3000</a></p>
    </div>
  </section>

"""

# ---- AR CASINO EXPANSION ----
AR_CASINO_EXPANSION = """
  <!-- ORIGINALS TABLE AR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">جدول Stake <span class="text-gradient-gold">Originals</span> و RTP</h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1"><bdi dir="ltr">18</bdi> لعبة طوّرتها Easygo. جميعها قابلة للإثبات بشكل عادل. معظمها بهامش منزل <bdi dir="ltr">1%</bdi> فقط.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:24px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">اللعبة</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">RTP</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">هامش المنزل</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">أقصى مضاعف</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Blackjack</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99.43%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">0.57%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">2.5x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Dice</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">9,900,000x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Mines</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">5,000,000x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Crash</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1,000,000x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Plinko</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1,000x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Limbo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1,000,000x</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;">Slide</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">98-99%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">1-2%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">4,294,967,000x</bdi></td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;text-align:right;">Roulette</td><td style="text-align:right;padding:9px 12px;color:var(--gold);"><bdi dir="ltr">97.3%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">2.7%</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">35x</bdi></td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://stake.com/casino/group/stake-originals" target="_blank" rel="noopener">كتالوج Stake Originals</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com دليل Stake</a></p>
    </div>
  </section>

  <!-- VIP TABLE AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">نادي <span class="text-gradient-gold">VIP</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1"><bdi dir="ltr">16</bdi> مستوى. تقدم مدى الحياة. ريك باك من Bronze.</p>
      </div>
      <div class="club-body">
        <p>يتتبع نادي VIP إجمالي الرهانات المتراكمة مدى الحياة ولا يُعيَّد أبداً. تُحتسب رهانات الكازينو بنسبة <bdi dir="ltr">1:1</bdi>، وتُحتسب الرهانات الرياضية بـ <bdi dir="ltr">3</bdi> أضعاف (رياضة <bdi dir="ltr">$1,000</bdi> = تقدم VIP <bdi dir="ltr">$3,000</bdi>). تبدأ نسبة ريك باك عند <strong>Bronze (رهان <bdi dir="ltr">$10,000</bdi>)</strong> بـ <bdi dir="ltr">5%</bdi> وتزداد مع كل مستوى. من Platinum IV فصاعداً، يُعيَّن مضيف VIP حصري للتفاوض على المكافآت المخصصة. مسيرة الـ <bdi dir="ltr">$1</bdi> مليار لـ Obsidian تأتي معها مكافأة ترقية بـ <bdi dir="ltr">$1</bdi> مليون ولا يصل إليها سوى أقل القليل من اللاعبين حول العالم.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:20px;">
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">المستوى</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">الرهان المدى الحياة</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">مكافأة الترقية</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">الميزة الرئيسية</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;text-align:right;">Bronze</td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$10,000</bdi></td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$15</bdi></td><td style="padding:8px 12px;text-align:right;">تفعيل <bdi dir="ltr">5%</bdi> ريك باك</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;text-align:right;">Gold</td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$100,000</bdi></td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$110</bdi></td><td style="padding:8px 12px;text-align:right;">مكافأة شهرية مُفعَّلة</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;text-align:right;">Platinum IV</td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$2,500,000</bdi></td><td style="text-align:right;padding:8px 12px;">لا يوجد</td><td style="padding:8px 12px;text-align:right;">مضيف VIP حصري</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;text-align:right;">Diamond V</td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$500,000,000</bdi></td><td style="text-align:right;padding:8px 12px;"><bdi dir="ltr">$400,000</bdi></td><td style="padding:8px 12px;text-align:right;">Stake Sphere وفعاليات حصرية</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;font-weight:700;color:var(--gold);text-align:right;">Obsidian</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);"><bdi dir="ltr">$1,000,000,000</bdi></td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);"><bdi dir="ltr">$1,000,000</bdi></td><td style="padding:8px 12px;font-weight:600;text-align:right;">أعلى مستوى. كل شيء مُخصَّص تماماً.</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

"""

# ---- AR PAYMENTS EXPANSION ----
AR_PAYMENTS_EXPANSION = """
  <!-- CRYPTO METHODS AR -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">العملات الرقمية <span class="text-gradient-gold">المدعومة</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">القناة الرئيسية. جميع السلاسل الكبرى مدعومة. الحد الأدنى للسحب يظهر بوحدة العملة الأصلية.</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">العملة</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">الشبكة</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">سرعة السحب</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Bitcoin (BTC)</bdi></td><td style="padding:9px 12px;text-align:right;">الشبكة الرئيسية</td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">30-60</bdi> دقيقة</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Ethereum (ETH)</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">ERC-20</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">30-60</bdi> دقيقة</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">USDT</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">TRC-20 / ERC-20</bdi></td><td style="text-align:right;padding:9px 12px;">ثوانٍ عبر <bdi dir="ltr">TRC</bdi></td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Tron (TRX)</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">Tron</bdi></td><td style="text-align:right;padding:9px 12px;">ثوانٍ</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Ripple (XRP)</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">XRP Ledger</bdi></td><td style="text-align:right;padding:9px 12px;">ثوانٍ</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Solana (SOL)</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">Solana</bdi></td><td style="text-align:right;padding:9px 12px;">ثوانٍ</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;text-align:right;"><bdi dir="ltr">Litecoin (LTC)</bdi></td><td style="padding:9px 12px;text-align:right;"><bdi dir="ltr">Litecoin</bdi></td><td style="text-align:right;padding:9px 12px;"><bdi dir="ltr">20-40</bdi> دقيقة</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصدر: <a href="https://help.stake.com/en/articles/4793500-supported-currencies" target="_blank" rel="noopener">مركز مساعدة Stake، العملات المدعومة</a></p>
    </div>
  </section>

  <!-- KYC AR -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">مستويات <span class="text-gradient-gold">KYC</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1"><bdi dir="ltr">4</bdi> مراحل. ليست إلزامية للجميع. تُفعَّل بحسب السلوك.</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>المستوى <bdi dir="ltr">1</bdi>: أساسي</h3>
          <p>بريد إلكتروني واسم مستخدم. يُتيح المراهنة. حدود إيداع وسحب منخفضة. لا يُطلب تحميل مستندات في البداية.</p>
        </div>
        <div class="club-card">
          <h3>المستوى <bdi dir="ltr">2</bdi>: رفع الحدود</h3>
          <p>التحقق من البريد الإلكتروني وبيانات شخصية إضافية. يرفع حدود الإيداع ويفتح المزيد من خيارات الدفع.</p>
        </div>
        <div class="club-card">
          <h3>المستوى <bdi dir="ltr">3</bdi>: مكافأة الترحيب</h3>
          <p>التحقق من المستندات: وثيقة هوية بصورة وإثبات عنوان ومستندات إضافية خاصة بالمستوى <bdi dir="ltr">3</bdi>. إلزامي للحصول على مكافأة <bdi dir="ltr">MAX3000</bdi> وللسحوبات الكبيرة.</p>
        </div>
        <div class="club-card">
          <h3>المستوى <bdi dir="ltr">4</bdi>: مصدر الأموال</h3>
          <p>يُفعَّل بحجوم معاملات عالية جداً أو بطلب الامتثال. قد يتطلب وثائق مصدر الأموال أو الإقرارات الضريبية أو كشوف الحساب البنكية.</p>
        </div>
      </div>
    </div>
  </section>

"""

# Execute expansions
print("\n=== AR REBUILD ===")

# Index - already 3284 equiv, but add more
expand_page(f"{BASE}/ar/index.html", AR_INDEX_EXPANSION)

# Casino
expand_page(f"{BASE}/ar/casino/index.html", AR_CASINO_EXPANSION)

# Promo-code - already 4507 equiv, verify
print(f"  ar/promo-code/index.html: {char_count(BASE+'/ar/promo-code/index.html')} equiv (no changes)")

# About-stake
expand_page(f"{BASE}/ar/about-stake/index.html", AR_ABOUT_EXPANSION)

# Mirror
expand_page(f"{BASE}/ar/mirror/index.html", AR_MIRROR_EXPANSION)

# Payments
expand_page(f"{BASE}/ar/payments/index.html", AR_PAYMENTS_EXPANSION)

print("\nAR rebuild complete.")
