#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild all 6 zh (Simplified Chinese) pages - expand to 1200+ words native content"""
import os, re, sys

BASE = "/home/user/workspace/winnersclub.com"

def word_count(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&[a-z]+;', ' ', clean)
    return len(clean.split())

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

def get_parts(locale_file):
    with open(locale_file, 'r', encoding='utf-8') as f:
        content = f.read()
    head = re.search(r'^(.*?<body>)', content, re.DOTALL).group(1)
    header = re.search(r'(<header.*?</header>)', content, re.DOTALL)
    header_html = header.group(1) if header else ''
    footer = re.search(r'(<!-- STICKY CTA -->.*)', content, re.DOTALL)
    footer_html = footer.group(1) if footer else ''
    return head, header_html, footer_html

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    wc = word_count(content)
    issues = check_violations(content)
    print(f"  {os.path.relpath(path, BASE)}: {wc} words{' | ISSUES: '+str(issues) if issues else ''}")
    return wc


# ============================================================
# ZH INDEX - needs expansion of body sections
# ============================================================

def rebuild_zh_index():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/index.html")
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">能找到这个页面，说明保安已经看顺眼你了。</p>
        <h1 class="ch-title text-gradient-gold">Stake 注册优惠码 MAX3000<span class="h1-sub">进入俱乐部。</span></h1>
        <p class="ch-sub">Stake 专属玩家后台。在入口处低声说出 <span class="code-highlight">MAX3000</span>，等待你的是<strong>最高 $3,000 的 200% 匹配奖励</strong>以及<strong>存款加奖励合并 40 倍流水要求</strong>。与那些廉价的公开码完全不同。Stake.com 自 2017 年运营，Curaçao OGL/2024/1451/0918 牌照，GGR $47 亿，链上储备金 $3.39 亿，可公开追踪。</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">在 Stake.com 领取最高 $3,000 200%</a>
          <a href="/zh/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">MAX3000 能开启什么</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 数据来源：Arkham Intel via cryptotips.com &middot; 2026 年 5 月 28 日快照</span><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 数据来源：Arkham Intel via cryptotips.com &middot; 2026 年 5 月 28 日快照</span></div></div>
  <aside class="promo-strip" aria-label="MAX3000 优惠码"><div class="ps-inner"><span class="ps-label">优惠码</span><span class="ps-code">MAX3000</span><span class="ps-bonus">最高 $3,000 200% &middot; 40 倍流水</span><a href="/zh/promo-code/" class="ps-cta">查看优惠码页面 &rarr;</a></div></aside>

  <!-- WHY THIS CLUB -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">为什么是<span class="text-gradient-gold">这个俱乐部</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">三个让你来对地方的理由。</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>有分量的奖励</h3><p>最高 $3,000 的 200% 匹配，存款加奖励合并 40 倍流水。Stake 上公开流传的其他码上限是 100%、$1,000。注册后 24 小时内不向发牌员出示 <span class="code-highlight">MAX3000</span>，你就只能用基础菜单了。以 $500 存款为例：MAX3000 奖励 $1,000，总资金 $1,500，流水要求 $60,000；普通码奖励 $500，总资金 $1,000，流水要求 $40,000。差距清晰可见。</p></div>
        <div class="club-card"><h3>钱就挂在墙上</h3><p>Arkham 标记储备金：2026 年 5 月 28 日 $339.53M。没有"请相信我们"的 PDF，也没有储备金秀。钱包是公开可读的，任何有 WiFi 的人都可以审计。以太坊占 74%，Solana 占 14%，九位数稳定币余额。Stake 每年处理超过 $1,800 亿的充值，GGR $47 亿，2,100 万账户。这些数字相互印证。<a href="/zh/reserves/" style="color:var(--gold);">查看凭证。</a></p></div>
        <div class="club-card"><h3>庄家有真实面孔</h3><p>Ed Craven（墨尔本，1995 年生）和 Bijan Tehrani。相识于 RuneScape，2017 年共同创立 Stake，2022 年推出 Kick。Forbes 估计两人合计净资产 US$56 亿。不是空壳公司。是两个没有输过的人。母公司 Easygo Group Holdings FY2025 收入 A$9.70 亿，净利润 A$2.57 亿，缴税 A$1.52 亿，636 名员工。</p></div>
      </div>
    </div>
  </section>

  <!-- FIVE ROOMS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">五个房间，<span class="text-gradient-gold">一个码</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">选择入口。MAX3000 在五处均有效。发牌员不管你在哪里用奖励。</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/zh/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">赌场</div></a><a href="/zh/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">体育</div></a><a href="/zh/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">扑克</div></a><a href="/zh/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">飞行员</div></a><a href="/zh/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">现场</div></a></div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">三千美元。<span class="text-gradient-gold">40 倍流水。</span>一个码。</h2>
      <p class="girl-break-sub">注册时向发牌员低声说出 <span class="code-highlight">MAX3000</span>。第一杯酒还没送到，数学已经站在你这边了。</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">向发牌员出示码</a>
    </div>
  </section>

  <!-- INTEL GRID -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">俱乐部<span class="text-gradient-gold">掌握的情报</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">创始人</div><div class="ic-value">Craven &amp; Tehrani</div><div class="ic-detail">Ed Craven（1995 年生，墨尔本）和 Bijan Tehrani。相识于 RuneScape。2017 年共同创立 Stake。2022 年推出 Kick。Forbes Australia 2024 年估计合计净资产 US$56 亿，AFR 2025 富豪榜列 Craven 个人净资产 A$48.2 亿。</div></div>
        <div class="intel-card"><div class="ic-label">运营主体</div><div class="ic-value">Medium Rare NV</div><div class="ic-detail">运营 Stake.com 的库拉索实体，地址：Korporaalweg 10, Willemstad, Curaçao。母公司：Easygo Group Holdings，FY2025 收入 A$9.70 亿。Stake.us 是独立的美国抽奖式博彩实体。</div></div>
        <div class="intel-card"><div class="ic-label">牌照</div><div class="ic-value">Curaçao OGL/2024/1451/0918</div><div class="ic-detail">覆盖大多数国家。2025 年 3 月退出英国。美国屏蔽（Stake.us 美国抽奖式博彩平台在 37 个州可用）。已确认镜像站点 22 个以上，均由 Medium Rare NV 运营。</div></div>
        <div class="intel-card"><div class="ic-label">储备金</div><div class="ic-value">$339.53M</div><div class="ic-detail">2026 年 5 月 28 日 Arkham 标记数据。以太坊 74%，Solana 14%，九位数稳定币余额。可通过 cryptotips.com 追踪。</div></div>
      </div>
    </div>
  </section>

  <!-- STAKE.COM vs STAKE.US -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">两扇门，<span class="text-gradient-gold">一个码</span></h2>
        <p class="section-subtitle">MAX3000 在 Stake.com 和 Stake.us 均被识别。每扇门背后的欢迎内容不同。发牌员会根据你的居住地引导你到合适的门。</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>Stake.com - 真实货币，全球</h3>
          <p>由 Medium Rare NV 在 Curaçao OGL/2024/1451/0918 许可下运营的真实货币平台。接受加密货币和法币。体育、赌场、原创游戏、扑克。使用码 <span class="code-highlight">MAX3000</span>：<strong>最高 $3,000 200% 匹配</strong>，存款加奖励合并 40 倍流水，有效期 30 天，最低存款 $10。存款后通过在线客服领取。需要 KYC 3 级认证。除美国和英国外大多数国家可用。Stake 提供 4,000 款以上老虎机、18 款 RTP 可验证的原创游戏、Evolution 真人赌场以及覆盖 40 多个项目的体育赛事投注。</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">打开全球入口</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - 美国抽奖式博彩</h3>
          <p>由 Sweepsteaks Limited 运营的美国抽奖式博彩平台。Gold Coins 用于游戏，Stake Cash 在 3 倍游戏量后可兑换。没有真实存款和提款，没有体育投注，仅限赌场。码 <span class="code-highlight">MAX3000</span> 也被识别，提供 <strong>560,000 GC + 56 SC + 3.5% 返水</strong>。在 37 个州可用。</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">打开美国入口</a>
        </div>
      </div>
    </div>
  </section>

  <!-- PLATFORM OVERVIEW -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">平台<span class="text-gradient-gold">深度解析</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">持码 MAX3000 进门后你会遇到什么。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>赌场：4,000 款老虎机加 18 款原创</h3>
          <p>赌场汇聚来自 15 个供应商的 4,000 款以上老虎机，包括 Pragmatic Play、Hacksaw Gaming 和 Nolimit City。18 款 Stake Originals 具有链上可验证的 RTP：Crash、Dice、Mines、Plinko、Limbo 和 HiLo 的 RTP 均为 99%，Blackjack 高达 99.43%。没有任何传统赌场能提供如此低的庄家优势。真人赌场由 Evolution 运营，24 小时开放 50 张以上牌桌，包括 Crazy Time（最高 20,000 倍乘数）、Lightning Roulette 和 Monopoly Big Baller。</p>
        </div>
        <div class="club-card">
          <h3>体育投注：40 个运动项目</h3>
          <p>Stake 体育覆盖 40 多个项目，包括足球、篮球、网球、板球和电竞，提供即时投注和赛前市场。体育投注流水可 75% 计入 MAX3000 奖励的流水要求，意味着你可以在赌场和体育之间分配奖励使用。对于同时喜爱体育投注和赌场游戏的玩家来说，这种灵活性极具价值。</p>
        </div>
        <div class="club-card">
          <h3>VIP：16 个等级，终身累积</h3>
          <p>Stake VIP 追踪累计终身投注额，永不清零。Bronze 等级从投注 $10,000 开始，解锁 5% 返水。Platinum IV 在 $250 万处获得专属 VIP 主任。Obsidian 需要 $10 亿投注，附带 $100 万升级奖励。体育投注计 VIP 进度时权重为 3 倍：体育 $1,000 等于 VIP 进度 $3,000。MAX3000 让你从第一笔存款起就进入系统。</p>
        </div>
        <div class="club-card">
          <h3>每周促销：奖金池 $315,000</h3>
          <p>除欢迎奖励外，Stake 维持 8 项循环促销。每日赛跑每天向前 5,000 名投注者分配 $100,000。每周抽奖向 15 名中奖者抽取 $75,000，每 $1,000 投注得一张票。赌场征服赛每周分配 $50,000，分大额获胜和高倍率获胜两组。Pragmatic Drops and Wins 每月为符合条件的 Pragmatic Play 老虎机额外添加 $228 万以上。这些促销无需单独报名，投注即参与。</p>
        </div>
        <div class="club-card">
          <h3>Stake Engine：游戏发布平台</h3>
          <p>2025 年 4 月推出，Stake Engine 是一个远程游戏服务器 (RGS)，允许外部工作室在 Stake 的基础设施上直接构建和发布游戏。首年流水 $33.1 亿。现有合作伙伴包括 Massive Studio（Jawsome、Swamp Things）和 Twist Gaming（Brains for Breakfast，97.25% RTP，最高 10,000 倍乘数）。商业模式：每月 GGR 的 10%，无隐藏费用。</p>
        </div>
        <div class="club-card">
          <h3>支付：22 种加密货币加法币</h3>
          <p>接受 22 种以上加密货币，包括比特币、以太坊、莱特币、狗狗币、瑞波币、波场和 Solana。法币存款可通过 MoonPay 进行。普通加密货币提款 30 到 60 分钟完成。TRX、XRP、SOL 秒到账。最低存款 $10 即可激活 MAX3000 奖励。提款无 Stake 收费，只收区块链网络费。</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Stake 老虎机大厅</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com MAX3000 指南</a> &middot; <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">Stake 帮助中心，欢迎奖励</a></p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">入口处的<span class="text-gradient-gold">常见问题</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">MAX3000 是 Stake 最大的奖励码吗?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>是的。最高 $3,000 200% 匹配，存款加奖励合并 40 倍流水。大多数公开码上限为 100% / $1,000。MAX3000 是俱乐部在门口发放的专属码。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake.com 靠谱吗?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake 由 Medium Rare NV 在 Curaçao OGL/2024/1451/0918 牌照下运营，自 2017 年起运营。2026 年 5 月 28 日链上储备金 $339.53M，可在 Arkham 公开追踪。创始人 Ed Craven（1995 年生，墨尔本）和 Bijan Tehrani 同时运营 Kick。母公司 Easygo Group Holdings 报告 FY2025 收入 A$9.70 亿，净利润 A$2.57 亿。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">可以查看 Stake 的储备金吗?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>可以，请查阅<a href='/zh/reserves/'>储备金报告</a>。2026 年 5 月 28 日快照显示 Arkham 标记钱包中有 $339.53M。以太坊 74%，Solana 14%，九位数稳定币余额。所有数据可通过 <a href='https://cryptotips.com/on-chain/stake/' target='_blank' rel='noopener'>cryptotips.com</a> 上的 Arkham Intel 每周追踪。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">在哪里可以游玩?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Curaçao 牌照覆盖全球大部分地区，但 Stake 自行限制美国、英国、澳大利亚部分地区及少数其他地区。请使用<a href='/zh/mirror/'>镜像页面</a>查找适合你地区的域名。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">提款速度如何?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>普通金额的加密货币提款 30 到 60 分钟内完成。TRX、XRP、SOL 在几秒内到账。大额提款可能触发 2 到 4 个工作日的合规审查。通过 MoonPay 的法币提款需要 1 到 5 个工作日。详细信息请查看<a href='/zh/payments/'>支付页面</a>。</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">告诉发牌员是 WinnersClub 送你来的。</p>
    </div>
  </section>
"""
    
    result = head + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_zh_casino():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/casino/index.html")
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-casino-3.avif') type('image/avif'), url('/images/girl-casino-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">找到这个页面，说明你找到了赌场大厅。</p>
        <h1 class="ch-title text-gradient-gold">赌场大厅。</h1>
        <p class="ch-sub">18 款 Stake Originals，3,000 到 4,000 款以上老虎机，Evolution 真人荷官室，16 级 VIP 俱乐部。使用 <span class="code-highlight">MAX3000</span> 解锁最高 $3,000 200%。Curaçao OGL/2024/1451/0918 牌照。</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">在 Stake.com 占位</a>
          <a href="/zh/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">查看优惠码 MAX3000</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 数据来源：Arkham Intel via cryptotips.com &middot; 2026 年 5 月 28 日快照</span><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 数据来源：Arkham Intel via cryptotips.com &middot; 2026 年 5 月 28 日快照</span></div></div>
  <aside class="promo-strip" aria-label="MAX3000 优惠码"><div class="ps-inner"><span class="ps-label">优惠码</span><span class="ps-code">MAX3000</span><span class="ps-bonus">最高 $3,000 200% &middot; 40 倍流水</span><a href="/zh/promo-code/" class="ps-cta">查看优惠码页面 &rarr;</a></div></aside>

  <!-- LIBRARY -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">游戏<span class="text-gradient-gold">资料库</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">大厅背后的数字。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>3,000-4,000 款以上老虎机</h3><p>从经典三轴到 Megaways 和集群付款，来自 15 款以上顶级供应商，定期更新。Pragmatic Play、Hacksaw Gaming、Nolimit City、Push Gaming、Relax Gaming 均已入驻。Stake 还提供 Pragmatic Play 热门游戏的独家增强 RTP 版本，RTP 达 98%，这是在普通赌场找不到的配置。</p></div>
        <div class="club-card"><h3>50 张以上真人牌桌</h3><p>21 点、轮盘、百家乐、Crazy Time 及完整游戏秀，均由 Evolution 驱动，24/7 全天候直播。每手投注限额从 $1 到 $50,000 不等，Stake Live 品牌牌桌面向 VIP 会员则更高。</p></div>
        <div class="club-card"><h3>18 款 Stake Originals</h3><p>基于 Easygo 技术的自研可证公平游戏。大多数 RTP 为 99%，是大厅中最低的庄家优势。Blackjack 原创游戏 RTP 高达 99.43%。每局游戏结束后可在游戏内点击公平性按钮验证结果。</p></div>
        <div class="club-card"><h3>Stake Engine 已上线</h3><p>2025 年 4 月推出，面向外部工作室的开放 RGS 平台。首年流水 $33.1 亿。Massive Studio 和 Twist Gaming 已入驻，发布了多款 Stake 独家游戏。商业模式：GGR 的 10%，无隐藏费用。</p></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Stake 老虎机大厅</a> &middot; <a href="https://www.freetips.com/casino/cryptocasinos/stake-offers-daily-races-bonus-drops-and-more-20250603-0010/" target="_blank" rel="noopener">freetips.com Stake 促销指南</a></p>
    </div>
  </section>

  <!-- STAKE ORIGINALS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Originals</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Easygo 自研的 18 款游戏。全部可证公平。大多数庄家优势仅 1%。</p>
      </div>
      <div class="club-body">
        <p>Stake Originals 使用在每局游戏开始前哈希并提交的加密服务器种子。玩家可通过游戏内的公平性按钮验证任意结果。由于种子预先锁定，Stake 和任何人都无法在游戏开始后更改结果。以下是包含已验证 RTP 的完整目录。</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:24px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">游戏</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">RTP</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">庄家优势</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">最大倍率</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Blackjack</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99.43%</td><td style="text-align:right;padding:9px 12px;">0.57%</td><td style="text-align:right;padding:9px 12px;">2.5x（3:2 Blackjack）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dice</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">9,900,000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Mines</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">5,000,000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Limbo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1,000,000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Crash</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1,000,000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Keno</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">500,000x</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">HiLo</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">无限连胜</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Wheel</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">500x（奖励区间）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Plinko</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">99%</td><td style="text-align:right;padding:9px 12px;">1%</td><td style="text-align:right;padding:9px 12px;">1,000x（高风险，16 行）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Video Poker</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">~99%</td><td style="text-align:right;padding:9px 12px;">~0.5%</td><td style="text-align:right;padding:9px 12px;">800x（皇家同花顺）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Slide</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">98-99%</td><td style="text-align:right;padding:9px 12px;">1-2%</td><td style="text-align:right;padding:9px 12px;">4,294,967,000x（42.9 亿）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Baccarat</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">~98.94%</td><td style="text-align:right;padding:9px 12px;">~1.06%（庄家）</td><td style="text-align:right;padding:9px 12px;">不适用</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Dragon Tower</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">98%</td><td style="text-align:right;padding:9px 12px;">2%</td><td style="text-align:right;padding:9px 12px;">256,901x（大师模式）</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Roulette</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">97.3%</td><td style="text-align:right;padding:9px 12px;">2.7%</td><td style="text-align:right;padding:9px 12px;">35x（单号）</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Blue Samurai（老虎机）</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">97.26%</td><td style="text-align:right;padding:9px 12px;">2.74%</td><td style="text-align:right;padding:9px 12px;">10,000x</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://stake.com/casino/group/stake-originals" target="_blank" rel="noopener">Stake Originals 目录</a> &middot; <a href="https://stake.com/provably-fair" target="_blank" rel="noopener">Stake 可证公平文档</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake 指南</a></p>

      <div class="section-header" style="margin-top:40px;">
        <h3 class="section-title anim anim-rise" style="font-size:20px;">几款值得深入了解的游戏</h3>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin-top:16px;">
        <div class="club-card">
          <h3>Crash，99% RTP</h3>
          <p>共享桌面火箭，随机时刻坠落前不断上升。每局前设置"兑现"倍率。实时排行榜显示所有玩家的位置。最大倍率：1,000,000x。内置止盈止损条件的自动下注功能。</p>
        </div>
        <div class="club-card">
          <h3>Mines，99% RTP</h3>
          <p>5x5 格子的数字扫雷。选择 1 到 24 个地雷，点击格子发现宝石，随时兑现。地雷越多，每个宝石的倍率越高。理论上限：5,000,000x。地雷位置在局开始时以加密方式锁定，点击后无法更改。</p>
        </div>
        <div class="club-card">
          <h3>Slide，42.9 亿倍上限</h3>
          <p>倍率卡片横向滚动过屏幕。局前设置目标。最终卡片达到或超过目标则获胜。4,294,967,000x 的理论最大值是 Stake Original 中最高的，但大多数下注在极端倍率下受 $10,000 的单次获胜上限约束。</p>
        </div>
        <div class="club-card">
          <h3>Dragon Tower，98% RTP</h3>
          <p>每层选择一个格子发现蛋并向上爬。五个难度级别：Easy（最高 13x）、Medium（37x）、Hard（501x）、Expert（19,289x）、Master（256,901x）。成功通过某行后随时可以兑现。</p>
        </div>
        <div class="club-card">
          <h3>Plinko，99% RTP</h3>
          <p>8 到 16 行、3 种风险级别的经典弹珠台。低风险最高 16x（16 行），中风险 110x，高风险 1,000x。最低回报值 0.2x 意味着球永远不会给零回报，你总会拿到一些东西。</p>
        </div>
        <div class="club-card">
          <h3>Blackjack，99.43% RTP</h3>
          <p>Stake Original 中数学回报率最高。标准规则包含补牌、停牌、分牌、加倍、保险。天然 Blackjack 按 3:2 赔付。0.57% 的庄家优势比拉斯维加斯庄家还要精准。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">200% 匹配<span class="text-gradient-gold">等待中</span></h2>
      <p class="girl-break-sub">在门口低声说出 <span class="code-highlight">MAX3000</span>，赌场欢迎奖励就是你的：最高 $3,000 200%。转动第一个转轴前先<a href="/zh/promo-code/" style="color:var(--gold);">申请 MAX3000</a>。</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">向发牌员出示码</a>
    </div>
  </section>

  <!-- SLOT LIBRARY -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">老虎机<span class="text-gradient-gold">资料库</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">来自重要名称的 3,000 到 4,000 款以上游戏。</p>
      </div>
      <div class="club-body">
        <p>除了 Originals，Stake 还拥有加密货币博彩领域最深的第三方老虎机资料库之一。根据来源和地区，约有 3,000 到 4,000 款以上游戏。供应商包括面向 Gates of Olympus 和 Sweet Bonanza 粉丝的 Pragmatic Play，面向高波动率 10,000x 猎手的 Hacksaw Gaming，面向 Skate or Die 的 30,000x 极限的 Nolimit City，以及拥有 99% RTP Book of 99 的 Relax Gaming，可与最好的 Stake Originals 媲美。Stake 独家增强 RTP 版本的 Pragmatic Play 热门游戏也以 98% RTP 运行。</p>
      </div>
      <div class="casino-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:24px;">
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Pragmatic Play</h3><p style="font-size:13px;color:var(--text-dim);">Gates of Olympus、Sweet Bonanza、Big Bass 系列。Stake 独家 98% RTP 版本。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Hacksaw Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Wanted Dead or a Wild、Le King、Dork Unit。高波动率 10,000x 游戏。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Nolimit City</h3><p style="font-size:13px;color:var(--text-dim);">Skate or Die（最高 30,000x），极端波动率机械老虎机。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Push Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Razor Shark、Fat Santa。广受欢迎的级联机制。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Relax Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Book of 99（99% RTP），大厅中 RTP 最高的第三方老虎机。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Big Time Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Extra Chilli，Megaways 机制的发明者。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Play'n GO</h3><p style="font-size:13px;color:var(--text-dim);">Reactoonz、Book of Dead。集群付款经典作品。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">BGaming</h3><p style="font-size:13px;color:var(--text-dim);">Stake Million（独家联合品牌老虎机，97.10% RTP）。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Twist Gaming</h3><p style="font-size:13px;color:var(--text-dim);">Brains for Breakfast（97.25% RTP，10,000x）。在 Stake Engine 上运行。</p></div>
        <div class="club-card" style="padding:16px;"><h3 style="font-size:14px;margin-bottom:6px;">Massive Studio</h3><p style="font-size:13px;color:var(--text-dim);">Jawsome、Swamp Things（96.57%，Stake 独家）。在 Stake Engine 上运行。</p></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://stake.com/casino/group/slots" target="_blank" rel="noopener">Stake 老虎机大厅</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake 指南</a></p>
    </div>
  </section>

  <!-- PROMOTIONS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">活跃<span class="text-gradient-gold">促销</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">8 个循环奖金池。无需单独报名，大多数自动参与。</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">促销</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">奖金池</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">参与方式</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">每日竞赛</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$100,000</td><td style="padding:9px 12px;">所有投注计入排行榜，前 5,000 名获奖，每 24 小时重置。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">每周抽奖</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$75,000</td><td style="padding:9px 12px;">每 $1,000 投注 = 1 张票，15 名获奖者于格林威治时间周六 14:00 直播抽取。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">赌场征服</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$50,000</td><td style="padding:9px 12px;">两个奖金池：大额获胜（最高现金获胜）和幸运获胜（最高乘率），基于推荐游戏。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Stake vs Eddie</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$30,000</td><td style="padding:9px 12px;">在选定游戏中超越联合创始人 Eddie Craven 的表现。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">转轴对决</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20,000</td><td style="padding:9px 12px;">两款选定老虎机，独立排行榜，最高乘率竞争。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">升级</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20,000</td><td style="padding:9px 12px;">选定游戏中的 5 级乘率挑战。</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">原创攀升</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">$20,000</td><td style="padding:9px 12px;">仅限 Stake Originals。在 Dice、Plinko、Mines 中达到目标乘率以爬升排行榜。</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">Pragmatic Drops &amp; Wins</td><td style="text-align:right;padding:9px 12px;color:var(--gold);">每月 $228 万以上</td><td style="padding:9px 12px;">全网 Pragmatic 促销。符合条件的老虎机上每日锦标赛加随机奖励掉落。每天数千个奖项。</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://www.freetips.com/casino/cryptocasinos/stake-offers-daily-races-bonus-drops-and-more-20250603-0010/" target="_blank" rel="noopener">FreeTips 促销指南</a> &middot; <a href="https://stake.com/promotions" target="_blank" rel="noopener">Stake 促销页面</a></p>
    </div>
  </section>

  <!-- VIP CLUB -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">VIP <span class="text-gradient-gold">俱乐部</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">16 个等级。终身进度。从 Bronze 开始返水。</p>
      </div>
      <div class="club-body">
        <p>VIP 俱乐部追踪累计终身投注额，永不清零。赌场投注按 1:1 计算，体育投注按 3 倍计算（体育 $1,000 = VIP 进度 $3,000）。返水在 <strong>Bronze（投注 $10,000）</strong>时以 5% 激活，随每个等级增加。从 Platinum IV 起，将分配专属 VIP 主任，可协商定制奖励。价值 $10 亿投注的 Obsidian 里程碑附带 $100 万升级奖励，全球只有极少数玩家达到。</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:20px;">
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">等级</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">终身投注额</th>
              <th style="text-align:right;padding:9px 12px;color:var(--gold);">升级奖励</th>
              <th style="text-align:left;padding:9px 12px;color:var(--gold);">主要权益</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Bronze</td><td style="text-align:right;padding:8px 12px;">$10,000</td><td style="text-align:right;padding:8px 12px;">$15</td><td style="padding:8px 12px;">解锁 5% 返水</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Silver</td><td style="text-align:right;padding:8px 12px;">$50,000</td><td style="text-align:right;padding:8px 12px;">不适用</td><td style="padding:8px 12px;">每周和每月奖励增加</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Gold</td><td style="text-align:right;padding:8px 12px;">$100,000</td><td style="text-align:right;padding:8px 12px;">$110</td><td style="padding:8px 12px;">解锁每月奖励</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum I</td><td style="text-align:right;padding:8px 12px;">$250,000</td><td style="text-align:right;padding:8px 12px;">$200</td><td style="padding:8px 12px;">每日充值奖励</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum IV</td><td style="text-align:right;padding:8px 12px;">$2,500,000</td><td style="text-align:right;padding:8px 12px;">不适用</td><td style="padding:8px 12px;">专属 VIP 主任</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Platinum VI</td><td style="text-align:right;padding:8px 12px;">$10,000,000</td><td style="text-align:right;padding:8px 12px;">$8,000</td><td style="padding:8px 12px;">大幅提升充值上限</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond I</td><td style="text-align:right;padding:8px 12px;">$25,000,000</td><td style="text-align:right;padding:8px 12px;">$20,000</td><td style="padding:8px 12px;">可续期充值；活动邀请</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;">Diamond V</td><td style="text-align:right;padding:8px 12px;">$500,000,000</td><td style="text-align:right;padding:8px 12px;">$400,000</td><td style="padding:8px 12px;">Stake Sphere 和独家现场活动</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 12px;font-weight:700;color:var(--gold);">Obsidian</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1,000,000,000</td><td style="text-align:right;padding:8px 12px;font-weight:700;color:var(--gold);">$1,000,000</td><td style="padding:8px 12px;font-weight:600;">最高荣誉。一切完全定制。</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://stake.com/vip" target="_blank" rel="noopener">Stake VIP 页面</a> &middot; <a href="https://help.stake.com/en/articles/4793501-what-is-the-stake-vip-program" target="_blank" rel="noopener">Stake 帮助中心，VIP 计划</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com Stake 指南</a></p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">入口处的<span class="text-gradient-gold">常见问题</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake 赌场有多少款游戏?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>来自 15 个以上第三方供应商的 3,000 到 4,000 款以上老虎机，加上自研 Stake Originals 25 款以上。真人赌场额外增加 50 张以上基于 Evolution 的牌桌，包含游戏秀。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">使用 MAX3000 的赌场奖励是什么?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>最高 $3,000 200% 存款匹配。流水要求为 30 天内存款加奖励合并的 40 倍。庄家优势 4% 以上的赌场游戏 100% 计入，体育投注 75% 计入。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake Originals 的 RTP 是多少?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>大多数 Originals 以 99% RTP（1% 庄家优势）运行：Crash、Dice、Limbo、Plinko、Mines、HiLo、Keno、Wheel。Blackjack 以 99.43% 最高。Baccarat 约 98.94%（庄家押注）。Roulette 97.3%（单零）。Dragon Tower 98%。Slide 在 42.9 亿倍上限下 98-99%。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">有真人荷官部分吗?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>有。真人大厅由 Evolution 运营，50 张以上牌桌 24/7 全天候直播。游戏秀包括 Crazy Time（最高 20,000 倍乘数）、Lightning Roulette、Monopoly Big Baller、Funky Time。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake VIP 俱乐部如何运作?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>基于累计终身投注额的 16 个等级，进度永不清零。Bronze 从投注 $10,000 开始，解锁 5% 返水。Obsidian 需要投注 $10 亿，附带 $100 万升级奖励。体育投注计 VIP 进度时权重为 3 倍。</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">告诉发牌员是 WinnersClub 送你来的。</p>
    </div>
  </section>
"""
    
    result = head + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_zh_promo():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/promo-code/index.html")
    # Read existing and expand - zh promo is already 2331 words, just fix depth
    with open(f"{BASE}/zh/promo-code/index.html", 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # The zh promo-code already has decent content, just needs verification
    # Add expanded terms section
    old_sig = '<!-- SIGNATURE -->'
    new_bonus_section = '''  <!-- BONUS TERMS EXPANDED -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">奖励条款<span class="text-gradient-gold">无隐藏细则</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">没有埋在 PDF 里的小字体。实际条款，直白说明。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>流水：存款加奖励合并 40 倍</h3>
          <p>流水要求作用于存款加奖励的合并金额，而非仅奖励本身。$500 存款加 $1,000 奖励 = $1,500 x 40 = $60,000 流水。在追求最高奖励前，请先计算好数字。</p>
        </div>
        <div class="club-card">
          <h3>必须 KYC 3 级</h3>
          <p>Stake 采用分级认证。1 级可投注，2 级可提高存款上限，<strong>3 级</strong>是解锁欢迎奖励和大额提款的证件认证级别。在账户设置 - 认证中上传身份证件、地址证明及 3 级所需额外材料。</p>
        </div>
        <div class="club-card">
          <h3>游戏类型贡献率</h3>
          <p>庄家优势 4% 以上的赌场老虎机和游戏 100% 计入流水要求。体育投注 75% 计入。真人荷官游戏和低 RTP 老虎机（庄家优势 4% 以下）以较低比例或 0% 计入。重点玩 Stake Originals 或庄家优势 4% 以上的老虎机。</p>
        </div>
        <div class="club-card">
          <h3>领取方式</h3>
          <p>首次存款后，联系在线客服告知 MAX3000。客服确认 KYC 3 级后，<strong>24 到 48 小时</strong>内 200% 奖励入账。没有自动输入推荐码的输入框，欢迎奖励由运营商手动发放。</p>
        </div>
        <div class="club-card">
          <h3>仅限新用户，首次存款</h3>
          <p>MAX3000 仅适用于新 Stake.com 账户的首次合格存款。现有账户无法追溯申请，后续存款不在此欢迎优惠范围内。</p>
        </div>
        <div class="club-card">
          <h3>最低存款与限制地区</h3>
          <p>触发优惠的最低存款为 $10，最高合格存款为 $1,500。美国、英国（2025 年 3 月起）、澳大利亚及大部分欧洲地区对 stake.com 有限制。美国玩家请访问专属<a href="/zh/stake-us-bonus/" style="color:var(--gold);">Stake.us 欢迎</a>，其他地区请在<a href="/zh/mirror/" style="color:var(--gold);">镜像页面</a>查看当地域名。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
'''
    
    result = existing.replace(old_sig, new_bonus_section)
    return result


def rebuild_zh_about():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/about-stake/index.html")
    
    body_content = """
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">找到这个页面，说明你想了解全部。</p>
        <h1 class="ch-title text-gradient-gold">运营 Stake 的人。</h1>
        <p class="ch-sub">两个在 RuneScape 上相识的墨尔本人，不依靠外部融资建立了世界最大的加密货币赌场。GGR 共计 $47 亿，链上 $3.39 亿，俱乐部自 2017 年就在 Stake，低声说出 <span class="code-highlight">MAX3000</span> 即享 200%。</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">进入 Stake.com</a>
          <a href="/zh/reserves/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">查看链上储备金</a>
        </div>
      </div>
    </div>
  </section>
  <div class="reserves-ticker"><div class="rt-inner"><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 2026 年 5 月 28 日快照</span><span>Stake 链上实时数据：标记储备金 $339.53M &middot; 以太坊 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curaçao OGL/2024/1451/0918 &middot; 2026 年 5 月 28 日快照</span></div></div>

  <!-- SCALE NUMBERS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">数字</span>说明规模</h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">不是初创企业。这就是你进入的这家庄的规模。</p>
      </div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">GGR</div><div class="ic-value">$4.7B</div><div class="ic-detail">已报告的总博彩收入，超过多家拉斯维加斯实体赌场的总和。每年处理超 $1,800 亿存款。</div></div>
        <div class="intel-card"><div class="ic-label">账户数</div><div class="ic-value">2,100 万</div><div class="ic-detail">Stake.com 注册账户。活跃用户集中在亚太地区、东欧和大洋洲。</div></div>
        <div class="intel-card"><div class="ic-label">链上储备金</div><div class="ic-value">$339.53M</div><div class="ic-detail">可通过 Arkham Intel 公开追踪。以太坊 74%，Solana 14%，九位数稳定币余额。快照日期：2026 年 5 月 28 日。</div></div>
        <div class="intel-card"><div class="ic-label">FY2025 收入</div><div class="ic-value">A$9.70 亿</div><div class="ic-detail">母公司 Easygo Group Holdings。净利润 A$2.57 亿，缴税 A$1.52 亿，636 名员工。不到两年内从不足 $1 亿增长到超过 $20 亿。</div></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight，Easygo FY2025</a> &middot; <a href="https://www.bloomberg.com/features/2026-stake-drake-crypto-casino-adin-ross-gambling/" target="_blank" rel="noopener">Bloomberg，Stake 存款规模</a></p>
    </div>
  </section>

  <!-- FOUNDERS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">创始人</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">两位澳大利亚人。相识于 RuneScape。未借助外部资金打造出 $56 亿帝国。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));">
        <div class="club-card" style="text-align:center;">
          <h3>Ed Craven</h3>
          <p style="font-size:12px;color:var(--text-muted);margin:-8px 0 14px;text-transform:uppercase;letter-spacing:.08em;">联合创始人 &middot; Easygo CEO</p>
          <p>1995 年生，澳大利亚墨尔本。公开形象代表。Craven 自称 12 岁时在家庭游轮上赢得了 $6,000，从此迷上了博彩统计学。就读于科夫斯港 Bishop Druitt College，很早就对编程和加密货币产生兴趣。十几岁时以"Apple"为网名领导着最大的 RuneScape 骰子部落，在那里认识了 Tehrani，"Stake"这个名字最终也源于此。直到 2021 年底，他始终公开使用别名 <strong>"Edd Miroslav"</strong>，刻意在网上隐藏真实身份。2024 年 10 月，Forbes Australia 将其与 Tehrani 的合计净资产估计为 <strong>US$56 亿</strong>，AFR 2025 年富豪榜列 Craven 个人净资产为 <strong>A$48.2 亿</strong>。2022 年，他以 A$8,000 万在墨尔本 Toorak 购置了一套占地 7,187 平方英尺的废弃豪宅，创下当地史上最贵住宅交易纪录。</p>
        </div>
        <div class="club-card" style="text-align:center;">
          <h3>Bijan Tehrani</h3>
          <p style="font-size:12px;color:var(--text-muted);margin:-8px 0 14px;text-transform:uppercase;letter-spacing:.08em;">联合创始人 &middot; Kick 联合所有人</p>
          <p>伊朗裔父母，出生于美国，后移居墨尔本，现仍居住于此。低调合伙人。负责运营、企业架构和幕后机器。Tehrani 联合拥有 Kick 流媒体平台，持股结构为：Ashwood Holdings 50%，Bijan Tehrani 个人 50%。2025 年 5 月 Forbes 估计净资产：<strong>$28 亿</strong>。2023 年底，他在曼哈顿"亿万富翁大道"以 <strong>$4,700 万</strong>购置了一栋联排别墅，是当年纽约最高成交额住宅交易之一。</p>
        </div>
      </div>
      <p style="margin-top:20px;font-size:15px;color:var(--text-dim);max-width:700px;">"Stake"这个名字是对他们 RuneScape 起源的直接致敬。游戏中有一个玩家在决斗中押注物品的质押机制，Craven 和 Tehrani 通过骰子社区在青少年时期相识，一起开始构建比特币博彩工具，自那以后几乎从未停下脚步。</p>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://en.wikipedia.org/wiki/Ed_Craven" target="_blank" rel="noopener">Wikipedia，Ed Craven</a> &middot; <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">Wikipedia，Bijan Tehrani</a> &middot; <a href="https://www.forbes.com.au/news/billionaires/how-ed-craven-and-bijan-tehrani-built-their-5-6-billion-fortune/" target="_blank" rel="noopener">Forbes Australia，创始人人物介绍</a></p>
    </div>
  </section>

  <!-- ORIGIN STORY -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">起源</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Stake 之前有 Primedice。Primedice 之前有 RuneScape。完整脉络。</p>
      </div>
      <div class="club-body">
        <p><strong>2013 年 5 月</strong>，Craven 和 Tehrani 推出了 <strong>Primedice</strong>，一个比特币骰子网站，普及了如今整个加密货币博彩行业的标准—可证公平加密验证系统。它不是第一个比特币骰子网站，但它是第一个完全在链下运行的网站，具备即时、零手续费的投注和任何人都可验证的开源公平性证明。透明可验证的随机性理念成为了 Stake 的哲学基础。</p>
        <p style="margin-top:12px;">Primedice 运营了 <strong>12 年</strong>，直到 2025 年宣布停运，引导玩家迁移至 Stake.com。Primedice 骰子游戏作为"Prime Dice"在 Stake Originals 中延续。</p>
        <p style="margin-top:12px;"><strong>2016 年春天</strong>，Craven 和 Tehrani 在墨尔本开设办公室，以 18 名员工创立了 <strong>Easygo Solutions</strong> 开发自有赌场技术。<strong>Stake.com 于 2017 年上线</strong>，在库拉索的 Medium Rare N.V. 下运营，瞄准 Primedice 已证明存在的原生加密货币博彩受众。增长起初缓慢，依靠主播推动，但疫情时期的 Twitch 直播合同将一个知名品牌变成了现象级存在。Stake 在不到两年内从 $1 亿增长到 $20 亿营收。</p>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://en.wikipedia.org/wiki/Primedice" target="_blank" rel="noopener">Wikipedia，Primedice 历史</a> &middot; <a href="https://en.wikipedia.org/wiki/Bijan_Tehrani_(entrepreneur)" target="_blank" rel="noopener">Wikipedia，Bijan Tehrani</a></p>
    </div>
  </section>

  <!-- CORPORATE STRUCTURE -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline"><span class="text-gradient-gold">企业架构</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">多个实体，一条控制链。解析架构。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Easygo Group Holdings</h3>
          <p>澳大利亚控股公司。Ed Craven 为唯一董事。FY2025 业绩：<strong>收入 A$9.70 亿</strong>，<strong>净利润 A$2.57 亿</strong>，<strong>净资产 A$50 亿</strong>，<strong>所得税 A$1.52 亿</strong>，<strong>636 名员工</strong>。通过子公司持有 Stake.com 和 Kick.com。</p>
        </div>
        <div class="club-card">
          <h3>Medium Rare N.V.</h3>
          <p>运营 Stake.com 的库拉索注册法人。地址：Korporaalweg 10, Willemstad, Curaçao。持有 <strong>Curaçao OGL/2024/1451/0918 牌照</strong>。所有镜像域名也由 Medium Rare N.V. 运营，非第三方盗版行为。支付通过塞浦路斯尼科西亚子公司处理。</p>
        </div>
        <div class="club-card">
          <h3>Kick Streaming Pty Ltd</h3>
          <p>2022 年 11 月 14 日成立的流媒体平台。母公司：Easygo Entertainment Pty Ltd。股权结构：Ashwood Holdings 50%，Bijan Tehrani 个人 50%。核心招募策略是 95/5 主播收入分成（对比 Twitch 的 50/50）。2025 年第三季度，Kick 是全球观看量第四的直播平台。</p>
        </div>
        <div class="club-card">
          <h3>Stake.us（Sweepsteaks Limited）</h3>
          <p>由 <strong>Sweepsteaks Limited</strong> 运营的美国抽奖式博彩平台，在法律上与 Stake.com 独立。游戏用 Gold Coins，Stake Cash 在 3 倍游戏量后可兑换为奖品，无直接真实货币投注，无加密货币。<strong>在美国 37 个州</strong>可用。<strong>MAX3000 在 Stake.us 上同样被识别</strong>，解锁 560,000 GC + 56 SC + 3.5% 返水。</p>
        </div>
      </div>
      <p style="margin-top:16px;font-size:14px;color:var(--text-dim);"><strong>办公室位置：</strong>澳大利亚墨尔本（主要技术中心，Easygo 总部）；塞尔维亚贝尔格莱德（运营）；塞浦路斯尼科西亚（支付处理）；因拉丁美洲扩张，巴西、哥伦比亚、秘鲁也已设立办公室。</p>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://thestraight.com.au/easygos-250-million-profit/" target="_blank" rel="noopener">The Straight，Easygo FY2025</a> &middot; <a href="https://en.wikipedia.org/wiki/Kick_(service)" target="_blank" rel="noopener">Wikipedia，Kick</a></p>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">钱在<span class="text-gradient-gold">链上</span></h2>
      <p class="girl-break-sub">2026 年 5 月 28 日 Arkham 标记储备金 $339.53M。可公开追踪。<a href="/zh/reserves/" style="color:var(--gold);">查看完整明细 &rarr;</a></p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">持 MAX3000 入场</a>
    </div>
  </section>

  <!-- SPONSORSHIPS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">赞助<span class="text-gradient-gold">与合作</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">没有哪家博彩公司买下了如此多的文化资产。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>Drake</h3>
          <p>2022 年签约。报道价格为 <strong>每年 $1 亿</strong>，部分说法称后重新谈判至 $1.8 亿。Drake 多次在 Stake 上直播博彩。截至 2026 年 6 月，合作关系仍活跃，Stake 官方 X 简介写有"@Drake 认证"。</p>
        </div>
        <div class="club-card">
          <h3>Trainwreckstv</h3>
          <p>Stake 资历最老的主播之一。本人在直播中公开表示 16 个月内获得 <strong>$3.60 亿报酬</strong>。2025 年 7 月，在 Massive Studios 为 Stake 独家开发的 Hex Appeal 上赢得 <strong>$3,750 万</strong>，创下史上最高在线老虎机单次获奖纪录。每注 $6,000，最高倍率 50,000 倍。</p>
        </div>
        <div class="club-card">
          <h3>Everton FC</h3>
          <p>2022 年 6 月公布，2022 年 7 月 1 日生效。估值为 <strong>每年 £1,000 万</strong>，是 Everton 144 年历史上最大的球衣正面赞助合同。多年合同。</p>
        </div>
        <div class="club-card">
          <h3>Stake F1 车队 Kick Sauber</h3>
          <p>Stake 于 2023 年成为 Sauber 的联合冠名赞助商。2024 年成为唯一冠名合作伙伴，球队于 2024 年和 2025 年以 <strong>"Stake F1 Team KICK Sauber"</strong> 名称出赛。2026 年起，随奥迪收购而更名为 Audi。</p>
        </div>
        <div class="club-card">
          <h3>UFC</h3>
          <p>2021 年 1 月：Israel Adesanya 成为首位全球品牌大使。2022 年 2 月：扩展为拉丁美洲和亚洲官方投注合作伙伴。2024 年 2 月：升级为高级全球官方合作伙伴。其他 UFC 选手：Francis Ngannou、Alex Pereira、Merab Dvalishvili、Alexandre Pantoja、Caio Borralho。</p>
        </div>
        <div class="club-card">
          <h3>Sergio Agüero</h3>
          <p>2022 年 2 月 1 日签约。Stake 拍摄了 2022 年 FIFA 世界杯广告，出演者包括 Agüero、Eden Hazard、Iker Casillas 和 Patrice Evra。Agüero 于 2021 年与阿根廷一起夺得美洲杯，这一关联促成了 Stake 于 2026 年在布宜诺斯艾利斯省推出。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">入口处的<span class="text-gradient-gold">常见问题</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake 是谁创立的?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Ed Craven（1995 年生，墨尔本）和 Bijan Tehrani。通过 RuneScape 骰子社区在青少年时期相识。2013 年共同创立 Primedice，2017 年创立 Stake.com。从未寻求外部融资。Forbes Australia 2024 年估计合计净资产为 US$56 亿。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake.com 可信赖吗?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake 由 Medium Rare NV 在 Curaçao OGL/2024/1451/0918 牌照下运营，自 2017 年起运营。2026 年 5 月 28 日链上储备金 $339.53M，可在 Arkham 公开追踪。母公司 Easygo 报告 FY2025 收入 A$9.70 亿，净利润 A$2.57 亿，缴税 A$1.52 亿。</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Stake 与 Kick 是什么关系?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Kick Streaming 由 Easygo Entertainment（Easygo Group Holdings 子公司）和 Bijan Tehrani 个人于 2022 年 11 月创立。持股结构：Ashwood Holdings（与 Easygo 关联）50%，Tehrani 50%。Kick 向主播提供 95/5 收入分成，与 Twitch 相比极具竞争力。</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">告诉发牌员是 WinnersClub 送你来的。</p>
    </div>
  </section>
"""
    
    result = head + "\n<body>\n" + header_html + body_content + footer_html
    return result


def rebuild_zh_mirror():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/mirror/index.html")
    with open(f"{BASE}/zh/mirror/index.html", 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # Add expansion section before signature
    old_sig = '<!-- SIGNATURE -->'
    expansion = '''  <!-- ADDITIONAL MIRROR CONTENT -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">钱包同步：<span class="text-gradient-gold">实际运作方式</span></h2>
      </div>
      <div class="club-body">
        <p>Stake 的所有官方镜像共享同一个后台数据库。当你用同一组账号密码登录任何镜像时，你看到的余额、投注记录、VIP 进度和活跃奖励完全相同。不需要在域名之间转移资金。无论你通过哪个域名访问，钱包都是同一个。</p>
        <p style="margin-top:12px;">这是因为所有镜像域名均指向由 Medium Rare N.V. 管理的同一套服务器基础设施。域名只是 DNS 入口点，处理你下注、持有余额和追踪 VIP 进度的后台是统一且共享的。</p>
        <p style="margin-top:12px;">这一架构意味着，在某一地区的镜像上赢得的资金，可以通过另一地区的镜像提取。进度永远不会丢失。</p>
      </div>
    </div>
  </section>

  <!-- PHISHING TRAPS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">辨别<span class="text-gradient-gold">真假镜像</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">钓鱼网站真实存在。以下是确认自己在正确镜像上的方法。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>1. 检查 SSL 证书</h3>
          <p>点击浏览器中的锁形图标。证书应签发给 stake.* 域名。证书过期或签发给不同域名是立即的危险信号。</p>
        </div>
        <div class="club-card">
          <h3>2. WHOIS 注册信息</h3>
          <p>Stake 官方镜像的 WHOIS 记录显示 Medium Rare 组织信息，或由合法注册商启用了注册人隐私保护。新注册（不足 30 天）的域名值得怀疑。</p>
        </div>
        <div class="club-card">
          <h3>3. 正确的布局和游戏供应商</h3>
          <p>真正的镜像显示相同的 Stake Originals、Evolution 和 Pragmatic 等供应商及相同设计。如果布局不同或游戏缺失，请勿输入账号密码。</p>
        </div>
        <div class="club-card">
          <h3>4. 链接来源</h3>
          <p>通过可信赖的联盟链接或 Stake 自身的域名列表访问镜像。Telegram、WhatsApp 或电子邮件中的非请求链接是常见的钓鱼入口。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- COUNTRIES WHERE BLOCKED -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">受限地区：<span class="text-gradient-gold">完整名单</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Stake.com 在 100 多个国家受到禁止或限制。镜像无法绕过这些限制，它们是访问工具，不是法律规避手段。</p>
      </div>
      <div class="club-body">
        <p>Stake.com 在以下地区自行设置了访问限制：美国（Stake.us 提供抽奖式博彩替代方案）、英国（2025 年 3 月退出）、澳大利亚部分地区（北领地、昆士兰州等）、法国、荷兰、西班牙、德国、意大利及其他建立了本地监管框架的欧盟成员国。中国大陆、香港和澳门同样在限制范围内。如果你所在地区受到限制，镜像只是不同的 DNS 入口，并不改变 Stake 自身的访问政策。</p>
        <p style="margin-top:12px;">对于受限地区的玩家，VPN 可能看起来是一个简单的解决方案，但它会带来风险：如果 Stake 检测到你的 IP 与已验证的身份证件之间存在差异，账户可能被标记进行合规审查。在你所在地区使用官方授权的镜像才是更安全的选择。</p>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
'''
    
    result = existing.replace(old_sig, expansion)
    return result


def rebuild_zh_payments():
    head, header_html, footer_html = get_parts(f"{BASE}/zh/payments/index.html")
    with open(f"{BASE}/zh/payments/index.html", 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # zh payments needs expansion - add before SIGNATURE
    old_sig = '<!-- SIGNATURE -->'
    expansion = '''  <!-- EXPANDED PAYMENT CONTENT -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">加密货币<span class="text-gradient-gold">支付方式</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">主要通道。所有主流链均支持。最低提款额以原生代币单位显示。</p>
      </div>
      <div class="data-table" style="overflow-x:auto;margin-top:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,215,0,0.2);">
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">货币</th>
              <th style="text-align:left;padding:10px 12px;color:var(--gold);">网络</th>
              <th style="text-align:right;padding:10px 12px;color:var(--gold);">提款速度</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">比特币 (BTC)</td><td style="padding:9px 12px;">Bitcoin 主网</td><td style="text-align:right;padding:9px 12px;">30 到 60 分钟</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">以太坊 (ETH)</td><td style="padding:9px 12px;">ERC-20</td><td style="text-align:right;padding:9px 12px;">30 到 60 分钟</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">泰达币 (USDT)</td><td style="padding:9px 12px;">TRC-20 / ERC-20</td><td style="text-align:right;padding:9px 12px;">TRC 秒级到账</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">波场 (TRX)</td><td style="padding:9px 12px;">Tron</td><td style="text-align:right;padding:9px 12px;">秒级</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">瑞波币 (XRP)</td><td style="padding:9px 12px;">XRP Ledger</td><td style="text-align:right;padding:9px 12px;">秒级</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">Solana (SOL)</td><td style="padding:9px 12px;">Solana</td><td style="text-align:right;padding:9px 12px;">秒级</td></tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><td style="padding:9px 12px;font-weight:600;">莱特币 (LTC)</td><td style="padding:9px 12px;">Litecoin</td><td style="text-align:right;padding:9px 12px;">20 到 40 分钟</td></tr>
            <tr><td style="padding:9px 12px;font-weight:600;">BNB / BSC</td><td style="padding:9px 12px;">BEP-20</td><td style="text-align:right;padding:9px 12px;">几分钟</td></tr>
          </tbody>
        </table>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://help.stake.com/en/articles/4793500-supported-currencies" target="_blank" rel="noopener">Stake 帮助中心，支持的货币</a></p>
    </div>
  </section>

  <!-- KYC LEVELS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">KYC <span class="text-gradient-gold">认证级别</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">4 个级别。并非所有玩家都必须完成。根据行为触发。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>1 级：基础</h3>
          <p>电子邮件和用户名。允许投注。存款和提款限额较低。最初无需上传文件。</p>
        </div>
        <div class="club-card">
          <h3>2 级：提高限额</h3>
          <p>邮箱验证加额外个人信息。提高存款限额并解锁更多支付选项。</p>
        </div>
        <div class="club-card">
          <h3>3 级：欢迎奖励</h3>
          <p>证件验证：带照片的身份证、地址证明及 3 级所需额外材料。领取 MAX3000 欢迎奖励及大额提款的必要条件。</p>
        </div>
        <div class="club-card">
          <h3>4 级：资金来源</h3>
          <p>极高交易量或合规申请时触发。可能需要提供资金来源文件、所得税申报表或银行对账单。</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">来源：<a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">Stake 帮助中心，账户验证</a></p>
    </div>
  </section>

  <!-- RESPONSIBLE GAMBLING -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">负责任博彩<span class="text-gradient-gold">工具</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">账户内可用工具。无 GAMSTOP，但有实际限额。</p>
      </div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">
        <div class="club-card">
          <h3>亏损限额</h3>
          <p>设置每日、每周或每月的最大亏损额。达到后，系统在下一周期前阻止新的下注。在账户的限额设置中进行配置。</p>
        </div>
        <div class="club-card">
          <h3>下注限额</h3>
          <p>每注最高限额。可以绝对值设置。有助于控制 Crash 或 Dice 中的自动下注环节。</p>
        </div>
        <div class="club-card">
          <h3>赌场自我排除</h3>
          <p>在指定时间段内取消赌场游戏访问权限。自我排除赌场期间体育投注仍可使用。</p>
        </div>
        <div class="club-card">
          <h3>完全自我排除</h3>
          <p>终止对整个平台的访问。可选择 1 周至永久。需要联系在线客服方可申请。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
'''
    
    result = existing.replace(old_sig, expansion)
    return result


# ---- MAIN EXECUTION ----

print("\n=== ZH REBUILD ===")
BASE_ZH = f"{BASE}/zh"

# Index
idx_content = rebuild_zh_index()
write_file(f"{BASE_ZH}/index.html", idx_content)

# Casino
casino_content = rebuild_zh_casino()
write_file(f"{BASE_ZH}/casino/index.html", casino_content)

# Promo-code
promo_content = rebuild_zh_promo()
write_file(f"{BASE_ZH}/promo-code/index.html", promo_content)

# About-stake
about_content = rebuild_zh_about()
write_file(f"{BASE_ZH}/about-stake/index.html", about_content)

# Mirror
mirror_content = rebuild_zh_mirror()
write_file(f"{BASE_ZH}/mirror/index.html", mirror_content)

# Payments
payments_content = rebuild_zh_payments()
write_file(f"{BASE_ZH}/payments/index.html", payments_content)

print("\nZH rebuild complete.")
