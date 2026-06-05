#!/usr/bin/env python3
"""
Korean Translation Engine for 1win.codes
Translates text content of HTML files from English to Korean
using a comprehensive translation dictionary and pattern matching.

Rules:
- Preserve: XLBONUS, 1win, Curaçao 8048/JAZ, brand names, slot names, payment brands
- Register: -ㅂ니다/-습니다 polite Korean
- No em/en dashes
- CTA swap: all btn-class anchors → playstake.io
- First paragraph must have: 1win + XLBONUS + specific number + Curaçao 8048/JAZ
"""

import re
from pathlib import Path

# =============================================================================
# TRANSLATION DICTIONARY - comprehensive EN→KO for all page content
# =============================================================================

TITLE_TRANSLATIONS = {
    "1win Promo Code XLBONUS, Get 600% on Your First 4 Deposits (2026)":
        "1win 프로모 코드 XLBONUS - 첫 4회 입금 600% 보너스 (2026)",
    "1win Casino, 11,000+ Slots and Live Tables | XLBONUS 600%":
        "1win 카지노 - 11,000개 이상의 슬롯과 라이브 테이블 | XLBONUS 600%",
    "1win Sportsbook, 30+ Sports, Live Cash-Out and Streaming | XLBONUS":
        "1win 스포츠북 - 30개 이상의 스포츠, 라이브 캐시아웃 및 스트리밍 | XLBONUS",
    "1win Promo Code XLBONUS, 600% Welcome Bonus (2026)":
        "1win 프로모 코드 XLBONUS - 600% 환영 보너스 (2026)",
    "1win Review 2026 | Honest Assessment of Odds, Games & Bonuses":
        "1win 리뷰 2026 | 배당률, 게임 및 보너스 정직한 평가",
    "1win App Download for Android & iOS (2026) | XLBONUS":
        "1win 앱 다운로드 Android & iOS (2026) | XLBONUS",
    "1win Register: How to Open an Account + XLBONUS Bonus 2026":
        "1win 회원가입: 계정 개설 방법 + XLBONUS 보너스 2026",
    "1win Login | Access Your 1win Account 2026":
        "1win 로그인 | 1win 계정 접속 2026",
    "1win Aviator Game Guide + XLBONUS Promo Code (2026)":
        "1win Aviator 게임 가이드 + XLBONUS 프로모 코드 (2026)",
    "1win Mirror and Alternative Links (2026) | Access 1win":
        "1win 미러 및 대체 링크 (2026) | 1win 접속",
    "1win Alternative Link | Access 1win in 2026":
        "1win 대체 링크 | 2026년 1win 접속",
    "1win VIP Club | Rewards and Cashback for Loyal Players":
        "1win VIP 클럽 | 충성 플레이어를 위한 보상 및 캐시백",
    "1win Lucky Drive | Win a Lamborghini with Promo Code XLBONUS":
        "1win Lucky Drive | XLBONUS 프로모 코드로 람보르기니 당첨",
    "1win Poker | Texas Hold'em, Tournaments + XLBONUS":
        "1win 포커 | Texas Hold'em, 토너먼트 + XLBONUS",
    "1win Payment Methods 2026: Cards, Crypto, E-wallets | XLBONUS":
        "1win 결제 방법 2026: 카드, 암호화폐, 전자지갑 | XLBONUS",
    "1win Live Streaming | Watch and Bet 2026":
        "1win 라이브 스트리밍 | 시청 및 베팅 2026",
    "1win Website and Official Links 2026 | Access Guide":
        "1win 웹사이트 및 공식 링크 2026 | 접속 가이드",
    "1win Promotions 2026: Tournaments, Free Spins, and Special Offers":
        "1win 프로모션 2026: 토너먼트, 무료 스핀 및 특별 혜택",
    "1win FAQ 2026 | Most Asked Questions Answered":
        "1win 자주 묻는 질문 2026 | 가장 많이 묻는 질문 답변",
    "1win News & Updates 2026":
        "1win 뉴스 및 업데이트 2026",
}

META_TRANSLATIONS = {
    "Get a 600% welcome bonus on your first four deposits at 1win with promo code XLBONUS. 30+ sports, 11,000+ casino games, Aviator, crypto payouts in 4 hours average. Curaçao licensed.":
        "1win에서 프로모 코드 XLBONUS로 처음 4번의 입금에 걸쳐 600% 환영 보너스를 받으세요. 30개 이상의 스포츠, 11,000개 이상의 카지노 게임, Aviator, 평균 4시간 암호화폐 출금. Curaçao 8048/JAZ 라이선스 보유.",
    "Enter 1win promo code XLBONUS at registration to unlock a 200% + 150% + 100% + 50% bonus across your first four deposits. Up to $1,050 total. Crypto and card welcome. T&Cs apply, 18+.":
        "1win 프로모 코드 XLBONUS를 가입 시 입력하면 첫 4번의 입금에 걸쳐 200% + 150% + 100% + 50% 보너스를 받을 수 있습니다. 총 최대 $1,050. 암호화폐 및 카드 허용. 이용약관 적용, 만 18세 이상.",
}

# Common phrase translations (EN phrase → KO phrase)
PHRASE_MAP = {
    # Page titles / section headers
    "Register at 1win": "1win 가입하기",
    "Access 1win Registration": "1win 회원가입 접속",
    "Access Your 1win Account": "1win 계정 접속",
    "Login to 1win": "1win 로그인",
    "Join 1win": "1win 가입하기",
    "Claim Bonus": "보너스 받기",
    "Claim Promo Code →": "프로모 코드 받기 →",
    "Register with XLBONUS →": "XLBONUS로 가입하기 →",
    "Open Account": "계정 열기",
    "Play Now": "지금 플레이",
    "Start Playing": "플레이 시작",
    "Get Bonus": "보너스 받기",
    "Claim Now": "지금 받기",
    "Start Now": "지금 시작",
    "Get Started": "시작하기",
    "Sign Up": "가입하기",
    "Register": "가입하기",
    "Sign Up Now": "지금 가입하기",
    "Open 1win": "1win 열기",
    "Visit 1win": "1win 방문하기",
    "Access 1win": "1win 접속",
    "Play Aviator": "Aviator 플레이",
    "Play at 1win": "1win에서 플레이",
    "Bet at 1win": "1win에서 베팅",
    "Download the App": "앱 다운로드",
    "Get the App": "앱 받기",
    
    # Common UI phrases
    "Promo Code": "프로모 코드",
    "Sports Betting": "스포츠 베팅",
    "Casino": "카지노",
    "Live Casino": "라이브 카지노",
    "Poker": "포커",
    "Bonuses": "보너스",
    "VIP Club": "VIP 클럽",
    "Promotions": "프로모션",
    "Free Spins": "무료 스핀",
    "Payment Methods": "결제 방법",
    "Live Streaming": "라이브 스트리밍",
    "Mobile App": "모바일 앱",
    "Review": "리뷰",
    "FAQ": "자주 묻는 질문",
    "News": "뉴스",
    "Crash Games": "크래시 게임",
    "Slot Reviews": "슬롯 리뷰",
    "Game Providers": "게임 제공업체",
    "All Sports": "모든 스포츠",
    "Football": "축구",
    "Cricket": "크리켓",
    "Tennis": "테니스",
    "Basketball": "농구",
    "Esports": "e스포츠",
    "MMA": "MMA",
    "Boxing": "복싱",
    "Ice Hockey": "아이스하키",
    "Volleyball": "배구",
    "Table Tennis": "탁구",
    
    # Common content phrases
    "Welcome Bonus": "환영 보너스",
    "Deposit Bonus": "입금 보너스",
    "No Deposit Bonus": "무입금 보너스",
    "Wagering Requirements": "베팅 조건",
    "Withdrawal": "출금",
    "Deposit": "입금",
    "First Deposit": "첫 번째 입금",
    "Second Deposit": "두 번째 입금",
    "Third Deposit": "세 번째 입금",
    "Fourth Deposit": "네 번째 입금",
    "Cashback": "캐시백",
    "Free Bets": "무료 베팅",
    "Live Betting": "라이브 베팅",
    "In-Play Betting": "인플레이 베팅",
    "Cash Out": "캐시아웃",
    "Odds": "배당률",
    "Markets": "마켓",
    "Jackpot": "잭팟",
    "Tournament": "토너먼트",
    "Leaderboard": "리더보드",
    
    # Footer / disclaimer
    "This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk. Please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.":
        "이 사이트는 비공식 팬 사이트이며 1win과 제휴하거나 1win의 승인을 받은 사이트가 아닙니다. 이 사이트는 정보 제공 목적으로만 운영됩니다. 도박에는 위험이 따르므로 책임감 있게 플레이하십시오. 도박 문제가 있는 경우 GamCare 또는 지역 지원 기관에 연락하십시오.",
    "1win.codes - independent affiliate review": "1win.codes - 독립 제휴 리뷰",
    "All rights reserved.": "모든 권리 보유.",
    "18+ | T&amp;C Apply | Play Responsibly.": "만 18세 이상 | 이용약관 적용 | 책임감 있는 게임.",
    "18+ | T&C Apply | Play Responsibly.": "만 18세 이상 | 이용약관 적용 | 책임감 있는 게임.",
    "18+ only. New customers only. Terms and conditions apply. Gamble responsibly.":
        "만 18세 이상. 신규 고객 전용. 이용약관 적용. 책임감 있는 게임.",
    "Gamble responsibly.": "책임감 있는 게임.",
    "Play Responsibly": "책임감 있게 플레이",
    "18+": "18+",
    "Terms and conditions apply": "이용약관 적용",
    "New customers only": "신규 고객 전용",
    
    # Sports related
    "All sports betting": "전체 스포츠 베팅",
    "Live streaming": "라이브 스트리밍",
    "Slot reviews": "슬롯 리뷰",
    "Game providers": "게임 제공업체",
    "Crash games": "크래시 게임",
    "All bonuses": "전체 보너스",
    "All promotions": "전체 프로모션",
    "All calculators": "전체 계산기",
    "Odds converter": "배당률 변환기",
    "Parlay calculator": "파라레이 계산기",
    "Kelly criterion": "켈리 기준",
    "Arbitrage": "차익거래",
    "Hedge": "헤지",
    "Each-way": "이치웨이",
    "Implied probability": "내재 확률",
    "Bankroll": "뱅크롤",
    "Surebet": "슈어벳",
    "Matched bet": "매치드 벳",
    "Payment methods": "결제 방법",
    "Mobile app": "모바일 앱",
    "India guides": "인도 가이드",
    "About 1win": "1win 소개",
    
    # Wagering
    "Wagering rules": "베팅 규정",
    "Free spins today": "오늘의 무료 스핀",
    
    # Countries
    "Bangladesh": "방글라데시",
    "India": "인도",
    "Pakistan": "파키스탄",
    "Korea": "한국",
    "Malaysia": "말레이시아",
    "Singapore": "싱가포르",
    "South Africa": "남아프리카",
    "Tanzania": "탄자니아",
    "Malawi": "말라위",
    "Kenya": "케냐",
    "Brazil": "브라질",
    "Ghana": "가나",
    "Russia": "러시아",
    "Turkey": "터키",
    "Vietnam": "베트남",
    "Indonesia": "인도네시아",
    "Kazakhstan": "카자흐스탄",
    "Tajikistan": "타지키스탄",
    "Costa Rica": "코스타리카",
    "Gambia": "감비아",
    "Uzbekistan": "우즈베키스탄",
    
    # Navigation
    "Products": "제품",
    "Promos": "프로모션",
    "Support": "지원",
    "Countries": "국가",
    "Casino home": "카지노 홈",
    "Mirror": "미러",
    "Free Money": "무료 머니",
    "Download App": "앱 다운로드",
    "Home": "홈",
    "Login": "로그인",
    "Website": "웹사이트",
    
    # Misc
    "Information": "정보",
    "Details": "세부 정보",
    "How to": "사용 방법",
    "Step": "단계",
    "Guide": "가이드",
    "Overview": "개요",
    "Summary": "요약",
    "Table of Contents": "목차",
    "Yes": "예",
    "No": "아니요",
    "Available": "사용 가능",
    "Not Available": "사용 불가",
    "Recommended": "추천",
    "More info": "더 보기",
    "Read more": "더 읽기",
    "Learn more": "자세히 보기",
    "See all": "전체 보기",
    "View all": "전체 보기",
    "Back to top": "맨 위로",
    "Show more": "더 보기",
    "Show less": "접기",
    
    # Crash game names (keep in English but note)
    "Aviator": "Aviator",
    "JetX": "JetX",
    "Spaceman": "Spaceman",
    "Mines": "Mines",
    "Plinko": "Plinko",
    "HiLo": "HiLo",
    "Aviatrix": "Aviatrix",
    
    # News/Promo badge labels
    "Win a Lambo": "람보 당첨",
    "Hot": "인기",
    "New": "신규",
    "Live": "라이브",
    "Exclusive": "독점",
    "Special": "특별",
    "Bonus": "보너스",
    "Slots": "슬롯",
    "Sports": "스포츠",
    "Casino": "카지노",
    "Poker": "포커",
}

# =============================================================================
# HTML TEXT TRANSLATION FUNCTIONS
# =============================================================================

def translate_title_tag(content):
    """Translate <title> tag content."""
    def replace_title(m):
        text = m.group(1)
        # Try exact match first
        for en, ko in TITLE_TRANSLATIONS.items():
            if en == text:
                return f'<title>{ko}</title>'
        # Generic translation patterns
        text = translate_generic_en_to_ko(text)
        return f'<title>{text}</title>'
    
    return re.sub(r'<title>(.*?)</title>', replace_title, content, flags=re.DOTALL)


def translate_meta_description(content):
    """Translate meta description content."""
    def replace_meta(m):
        attr_content = m.group(1)
        for en, ko in META_TRANSLATIONS.items():
            if en == attr_content:
                return f'content="{ko}"'
        return m.group(0)
    
    # Match meta name="description" content="..."
    content = re.sub(
        r'<meta\s+name="description"\s+content="([^"]*)"',
        lambda m: f'<meta name="description" content="{translate_generic_en_to_ko(m.group(1))}"',
        content
    )
    return content


def translate_og_tags(content):
    """Translate og:title and og:description meta tags."""
    content = re.sub(
        r'(<meta\s+property="og:title"\s+content=")([^"]*)"',
        lambda m: m.group(1) + translate_generic_en_to_ko(m.group(2)) + '"',
        content
    )
    content = re.sub(
        r'(<meta\s+property="og:description"\s+content=")([^"]*)"',
        lambda m: m.group(1) + translate_generic_en_to_ko(m.group(2)) + '"',
        content
    )
    return content


def translate_aria_labels(content):
    """Translate aria-label attributes that are English."""
    def replace_aria(m):
        label = m.group(1)
        translated = {
            "Sign Up": "가입하기",
            "Toggle menu": "메뉴 열기/닫기",
            "1win home": "1win 홈",
            "Language": "언어",
            "Open menu": "메뉴 열기",
            "Close menu": "메뉴 닫기",
            "Back to top": "맨 위로",
            "Search": "검색",
            "Close": "닫기",
            "Previous": "이전",
            "Next": "다음",
        }.get(label, label)
        return f'aria-label="{translated}"'
    
    return re.sub(r'aria-label="([^"]*)"', replace_aria, content)


def translate_generic_en_to_ko(text):
    """
    Generic EN to KO translation for meta/title content.
    Applies known phrase substitutions and patterns.
    """
    if not text:
        return text
    
    # Preserve these terms
    preserved = ['XLBONUS', '1win', 'Curaçao', 'Curacao', '8048/JAZ', 'GamCare', 'SSL']
    
    result = text
    
    # Apply known phrase translations (longest first to avoid partial replacements)
    for en, ko in sorted(PHRASE_MAP.items(), key=lambda x: -len(x[0])):
        if en in result and en not in preserved:
            result = result.replace(en, ko)
    
    return result


def translate_nav_and_footer_text(content):
    """Translate navigation and footer text nodes."""
    # Fix nav links that are in English
    nav_translations = {
        '>Promo Code<': '>프로모 코드<',
        '>Sports<': '>스포츠<',
        '>Casino<': '>카지노<',
        '>Bonuses<': '>보너스<',
        '>Tools<': '>도구<',
        '>News<': '>뉴스<',
        '>More<': '>더 보기<',
        '>Register<': '>가입하기<',
        '>Login<': '>로그인<',
        '>All sports betting<': '>전체 스포츠 베팅<',
        '>Football<': '>축구<',
        '>Cricket<': '>크리켓<',
        '>Tennis<': '>테니스<',
        '>Basketball<': '>농구<',
        '>Esports<': '>e스포츠<',
        '>Live streaming<': '>라이브 스트리밍<',
        '>Casino home<': '>카지노 홈<',
        '>Slot reviews<': '>슬롯 리뷰<',
        '>Game providers<': '>게임 제공업체<',
        '>Crash games<': '>크래시 게임<',
        '>All bonuses<': '>전체 보너스<',
        '>First deposit 200%<': '>첫 번째 입금 200%<',
        '>Second deposit 150%<': '>두 번째 입금 150%<',
        '>Third deposit 150%<': '>세 번째 입금 150%<',
        '>Fourth deposit 100%<': '>네 번째 입금 100%<',
        '>Wagering rules<': '>베팅 조건<',
        '>Free spins today<': '>오늘의 무료 스핀<',
        '>All promotions<': '>전체 프로모션<',
        '>All calculators<': '>전체 계산기<',
        '>Odds converter<': '>배당률 변환기<',
        '>Parlay calculator<': '>파라레이 계산기<',
        '>Kelly criterion<': '>켈리 기준<',
        '>Arbitrage<': '>차익거래<',
        '>Each-way<': '>이치웨이<',
        '>Implied probability<': '>내재 확률<',
        '>Matched bet<': '>매치드 벳<',
        '>Payment methods<': '>결제 방법<',
        '>Mobile app<': '>모바일 앱<',
        '>India guides<': '>인도 가이드<',
        '>Mirrors<': '>미러<',
        '>Mirror<': '>미러<',
        '>Review<': '>리뷰<',
        '>About 1win<': '>1win 소개<',
        '>Products<': '>제품<',
        '>Promos<': '>프로모션<',
        '>Support<': '>지원<',
        '>Countries<': '>국가<',
        '>Sports Betting<': '>스포츠 베팅<',
        '>VIP Club<': '>VIP 클럽<',
        '>Promotions<': '>프로모션<',
        '>Free Money<': '>무료 머니<',
        '>Download App<': '>앱 다운로드<',
        '>Bangladesh<': '>방글라데시<',
        '>India<': '>인도<',
        '>Pakistan<': '>파키스탄<',
        '>Korea<': '>한국<',
        '>Malaysia<': '>말레이시아<',
        '>Singapore<': '>싱가포르<',
        '>South Africa<': '>남아프리카<',
        '>Tanzania<': '>탄자니아<',
        '>Malawi<': '>말라위<',
        '>Kenya<': '>케냐<',
        '>Website<': '>웹사이트<',
        '>FAQ<': '>자주 묻는 질문<',
        '>1win home<': '>1win 홈<',
        '>Home<': '>홈<',
        '>Cashback<': '>캐시백<',
        '>Live Casino<': '>라이브 카지노<',
        '>VIP<': '>VIP<',
    }
    
    for en, ko in nav_translations.items():
        content = content.replace(en, ko)
    
    return content


def translate_footer_disclaimer(content):
    """Translate the footer disclaimer text."""
    old = ('This is an unofficial fan site and is not affiliated with or endorsed by 1win. '
           'This site is for informational purposes only. Gambling involves risk. Please play responsibly. '
           'If you or someone you know has a gambling problem, please contact GamCare or a local support organization.')
    new = ('이 사이트는 비공식 팬 사이트이며 1win과 제휴하거나 1win의 승인을 받은 사이트가 아닙니다. '
           '이 사이트는 정보 제공 목적으로만 운영됩니다. 도박에는 위험이 따르므로 책임감 있게 플레이하십시오. '
           '도박 문제가 있는 경우 GamCare 또는 지역 지원 기관에 연락하십시오.')
    content = content.replace(old, new)
    
    old2 = '1win.codes - independent affiliate review'
    new2 = '1win.codes - 독립 제휴 리뷰'
    content = content.replace(old2, new2)
    
    old3 = 'All rights reserved.'
    new3 = '모든 권리 보유.'
    content = content.replace(old3, new3)
    
    return content


def translate_cta_button_text(content):
    """Translate CTA button text while preserving the Stake URL."""
    cta_map = {
        '>Register at 1win<': '>1win 가입하기<',
        '>Access 1win Registration<': '>1win 회원가입 접속<',
        '>Access Your 1win Account<': '>1win 계정 접속<',
        '>Login to 1win<': '>1win 로그인<',
        '>Join 1win<': '>1win 가입하기<',
        '>Claim Bonus<': '>보너스 받기<',
        '>Register with XLBONUS →<': '>XLBONUS로 가입하기 →<',
        '>Claim Promo Code →<': '>프로모 코드 받기 →<',
        '>Get Bonus<': '>보너스 받기<',
        '>Get Started<': '>시작하기<',
        '>Start Playing<': '>플레이 시작<',
        '>Play Now<': '>지금 플레이<',
        '>Claim Now<': '>지금 받기<',
        '>Sign Up Now<': '>지금 가입하기<',
        '>Sign Up<': '>가입하기<',
        '>Register<': '>가입하기<',
        '>Open Account<': '>계정 열기<',
        '>Open 1win<': '>1win 열기<',
        '>Visit 1win<': '>1win 방문하기<',
        '>Access 1win<': '>1win 접속<',
        '>Play Aviator<': '>Aviator 플레이<',
        '>Play at 1win<': '>1win에서 플레이<',
        '>Bet at 1win<': '>1win에서 베팅<',
        '>Download the App<': '>앱 다운로드<',
        '>Get the App<': '>앱 받기<',
        '>Start Now<': '>지금 시작<',
        '>Claim Your Bonus<': '>보너스 받기<',
        '>Claim XLBONUS<': '>XLBONUS 받기<',
        '>Use XLBONUS<': '>XLBONUS 사용하기<',
        '>Register Now<': '>지금 가입하기<',
        '>Register at 1win →<': '>1win 가입하기 →<',
        '>Join Now<': '>지금 가입하기<',
        '>Join<': '>가입하기<',
        '>Create Account<': '>계정 만들기<',
        '>Open Account Now<': '>지금 계정 열기<',
        '>Try 1win Poker<': '>1win 포커 해보기<',
        '>Try It<': '>해보기<',
        '>Bet Now<': '>지금 베팅<',
        '>Bet on Cricket<': '>크리켓 베팅<',
        '>Bet on Football<': '>축구 베팅<',
        '>Bet on Tennis<': '>테니스 베팅<',
        '>Bet on Basketball<': '>농구 베팅<',
        '>Bet on Esports<': '>e스포츠 베팅<',
        '>Go to 1win<': '>1win으로 이동<',
        '>Start Betting<': '>베팅 시작<',
        '>Start Playing Slots<': '>슬롯 플레이 시작<',
        '>Play Slots<': '>슬롯 플레이<',
        '>Try Slot<': '>슬롯 해보기<',
        '>Play Casino<': '>카지노 플레이<',
        '>Try Poker<': '>포커 해보기<',
        '>Download App<': '>앱 다운로드<',
        '>Get App<': '>앱 받기<',
        '>Latest Mirrors<': '>최신 미러<',
        '>Access Mirror<': '>미러 접속<',
        '>Access Site<': '>사이트 접속<',
        '>Alternative Access<': '>대체 접속<',
        '>View All Promotions<': '>전체 프로모션 보기<',
        '>View Promotions<': '>프로모션 보기<',
        '>All Bonuses<': '>전체 보너스<',
        '>View Bonus Details<': '>보너스 세부 정보 보기<',
        '>Enter Code<': '>코드 입력<',
        '>Use Code<': '>코드 사용<',
        '>Apply Code<': '>코드 적용<',
    }
    
    for en, ko in cta_map.items():
        content = content.replace(en, ko)
    
    return content


def translate_common_section_headers(content):
    """Translate common section/heading text."""
    header_map = {
        # Section titles with span patterns
        '>Register<': '>가입하기<',
        '>Login<': '>로그인<',
        '>Information<': '>정보<',
        '>Details<': '>세부 정보<',
        '>Welcome bonus<': '>환영 보너스<',
        '>Welcome Bonus<': '>환영 보너스<',
        '>Deposit Bonus<': '>입금 보너스<',
        '>First Deposit<': '>첫 번째 입금<',
        '>Second Deposit<': '>두 번째 입금<',
        '>Third Deposit<': '>세 번째 입금<',
        '>Fourth Deposit<': '>네 번째 입금<',
        '>Payment methods<': '>결제 방법<',
        '>Payment Methods<': '>결제 방법<',
        '>FAQs<': '>자주 묻는 질문<',
        '>Latest Promotions<': '>최신 프로모션<',
        '>LATEST PROMOTIONS<': '>최신 프로모션<',
        '>Promotions<': '>프로모션<',
        '>PROMOTIONS<': '>프로모션<',
        '>Your winning streak<': '>연승을 시작하세요<',
        '>Starts now<': '>지금 바로<',
        '>Global<': '>글로벌<',
        '>Access<': '>접속<',
        '>Get your<': '>받으세요<',
        '>600% bonus<': '>600% 보너스<',
        '>Visit 1win<': '>1win 방문<',
        '>Deposit<': '>입금<',
        '>Get Your Bonus<': '>보너스 받기<',
        '>Crypto deposit bonus on your opening deposit.<': '>첫 입금 시 암호화폐 입금 보너스.<',
        '>Even bigger on your second top-up.<': '>두 번째 충전 시 더욱 큰 보너스.<',
        '>Serious boost on deposit number three.<': '>세 번째 입금 시 큰 보너스 혜택.<',
        '>The biggest single bonus on your fourth deposit.<': '>네 번째 입금 시 가장 큰 단일 보너스.<',
        '>The above applies to crypto deposits. Fiat currency users get a 500% deposit bonus package across four deposits. 18+ | T&amp;C Apply | Play Responsibly.<': '>위 내용은 암호화폐 입금에 적용됩니다. 법정화폐 사용자는 4회 입금에 걸쳐 500% 입금 보너스 패키지를 받습니다. 만 18세 이상 | 이용약관 적용 | 책임감 있는 게임.<',
        # Table header items
        '>Product<': '>제품<',
        '>Promo Code<': '>프로모 코드<',
        '>Bonus Offer<': '>보너스 혜택<',
        '>Website<': '>웹사이트<',
        '>Products<': '>제품<',
        '>Established<': '>설립<',
        '>Accepted Crypto<': '>지원 암호화폐<',
        '>Website Languages<': '>지원 언어<',
        '>App<': '>앱<',
        '>Live Streaming<': '>라이브 스트리밍<',
        '>Live Support<': '>라이브 지원<',
        '>Promo code<': '>프로모 코드<',
        '>Deposit bonus<': '>입금 보너스<',
        # Step cards
        '>Visit 1win<': '>1win 방문<',
        '>Fill in the short registration form. When asked if you have a promo code, type in the <': '>짧은 가입 양식을 작성하세요. 프로모 코드가 있는지 물으면 <',
        ' code.<': ' 코드를 입력하세요.<',
        '>Make your first deposit. A 130% first deposit bonus is available with <': '>첫 입금을 하세요. <',
        '>, with further bonuses on deposits 2 to 4.<': '>로 130% 첫 입금 보너스를 받을 수 있으며, 2~4번째 입금에도 추가 보너스가 있습니다.<',
        '>The first part of your 600% bonus package will be credited to your account. Start playing!<': '>600% 보너스 패키지의 첫 번째 부분이 계정에 적립됩니다. 지금 플레이하세요!<',
        '>Use links on this page to access the official 1win website and click the &lsquo;Register&rsquo; button.<': '>이 페이지의 링크를 사용하여 공식 1win 웹사이트에 접속하고 &lsquo;가입하기&rsquo; 버튼을 클릭하세요.<',
        # FAQ
        '>Can I access 1win?<': '>1win에 접속할 수 있나요?<',
        '>What is the 1win Promo Code?<': '>1win 프로모 코드는 무엇인가요?<',
        '>Is 1win legit?<': '>1win은 합법적인가요?<',
        '>Can I download a 1win app?<': '>1win 앱을 다운로드할 수 있나요?<',
        '>What is 1win Lucky Drive?<': '>1win Lucky Drive란 무엇인가요?<',
        # Promotions section
        '>Lucky Drive: Win a Lamborghini Urus SE<': '>Lucky Drive: 람보르기니 우루스 SE 당첨<',
        '>Deposit and claim your free ticket daily. Monthly luxury car draws await.<': '>매일 입금하고 무료 티켓을 받으세요. 매월 럭셔리 카 추첨이 기다립니다.<',
        '>Sins and Spins Tournament: $50,000 Prize Pool<': '>신스 앤 스핀 토너먼트 - $50,000 상금<',
        '>Spin the reels and climb the leaderboard for massive rewards.<': '>릴을 돌리고 리더보드를 오르며 엄청난 보상을 받으세요.<',
        '>Legends Tournament: $100,000 in Prizes<': '>레전드 토너먼트: $100,000 상금<',
        '>Compete against the best. Weekly tournaments with scheduled payouts.<': '>최고의 플레이어들과 경쟁하세요. 지급이 보장된 주간 토너먼트.<',
        '>Aviamasters: Crash Game Championship<': '>에비아마스터스: 크래시 게임 챔피언십<',
        ">Prove you're the ultimate Aviator pilot. Top cashouts win big.<": '>최고의 Aviator 파일럿임을 증명하세요. 최고 현금화로 크게 이기세요.<',
        '>Gamzix Slots Fest: Free Spins Galore<': '>Gamzix 슬롯 페스트 - 무료 스핀 대잔치<',
        '>Play featured Gamzix slots and earn free spins plus cash bonuses.<': '>선택된 Gamzix 슬롯을 플레이하고 무료 스핀과 현금 보너스를 받으세요.<',
        '>Olympics Special: Enhanced Odds on Every Sport<': '>올림픽 스페셜: 모든 스포츠 배당률 향상<',
        ">Boosted odds across all Olympic events. Back your country to win gold.<": '>모든 올림픽 이벤트에서 향상된 배당률. 자국의 금메달을 응원하세요.<',
        '>Republic Day Bonus: 200 Free Spins<': '>공화국 기념일 보너스: 무료 스핀 200회<',
        '>Celebrate with 200 free spins on selected slots. Limited time only.<': '>선택된 슬롯에서 무료 스핀 200회로 축하하세요. 기간 한정.<',
        '>Love Fest: Share the Jackpot<': '>러브 페스트: 잭팟 나눠갖기<',
        '>Refer a friend and both receive bonus cash. Spread the love, stack the wins.<': '>친구를 추천하면 두 분 모두 보너스 현금을 받습니다. 사랑을 나누고 승리를 쌓으세요.<',
        # FAQ answers
        '>1win is global and can be accessed in lots of countries. You can access the sportsbook and casino via this page.<': '>1win은 글로벌 서비스로 많은 국가에서 접속할 수 있습니다. 이 페이지를 통해 스포츠북과 카지노에 접속할 수 있습니다.<',
        '> when you register to get the best welcome bonus available. Up to 600% deposit bonus can be claimed.<': '>를 가입 시 사용하여 최고의 환영 보너스를 받으세요. 최대 600% 입금 보너스를 받을 수 있습니다.<',
        '>1win is a legitimate online betting site offering sports betting, casino games and much more. The official website at 1win.pro holds a Curacao gambling licence.<': '>1win은 스포츠 베팅, 카지노 게임 등 다양한 서비스를 제공하는 합법적인 온라인 베팅 사이트입니다. 공식 웹사이트 1win.pro는 Curacao 8048/JAZ 게임 라이선스를 보유하고 있습니다.<',
        '>Yes. The 1win app is available on Android and iOS. Register to get the download.<': '>네. 1win 앱은 Android와 iOS에서 사용할 수 있습니다. 가입 후 다운로드하세요.<',
        '>1win Lucky Drive is a ticket-based promotion allowing players to win luxury vehicles, gadgets and free bets.<': '>1win Lucky Drive는 플레이어들이 럭셔리 차량, 가젯, 무료 베팅을 받을 수 있는 티켓 기반 프로모션입니다.<',
        # Hero section
        '>1win Promo Code XLBONUS - Get a 600% Welcome Bonus<': '>1win 프로모 코드 XLBONUS - 600% 환영 보너스 받기<',
        '>Bonus<': '>보너스<',
        '>Sports<': '>스포츠<',
        '>Games<': '>게임<',
        '>Instant Crypto<': '>즉시 암호화폐<',
        # CTA banner
        '>PROMO CODE: <': '>프로모 코드: <',
        '>Register with XLBONUS →<': '>XLBONUS로 가입하기 →<',
        # Win streak section
        '>Your winning streak<': '>연승을 시작하세요<',
        # Payment section labels
        '>Cards &amp; E-Wallets<': '>카드 및 전자지갑<',
        '>Cryptocurrency<': '>암호화폐<',
        # Step numbering
        '>1. Visit 1win<': '>1. 1win 방문<',
        '>2. Register<': '>2. 가입하기<',
        '>3. Deposit<': '>3. 입금<',
        '>4. Get Your Bonus<': '>4. 보너스 받기<',
    }
    
    for en, ko in header_map.items():
        content = content.replace(en, ko)
    
    return content


def translate_html_file(content):
    """
    Apply all translation functions to an HTML file content.
    """
    # Translate title
    content = translate_title_tag(content)
    
    # Translate meta description 
    content = translate_meta_description(content)
    
    # Translate og tags
    content = translate_og_tags(content)
    
    # Translate aria labels
    content = translate_aria_labels(content)
    
    # Translate nav and footer
    content = translate_nav_and_footer_text(content)
    
    # Translate footer disclaimer
    content = translate_footer_disclaimer(content)
    
    # Translate CTA button texts
    content = translate_cta_button_text(content)
    
    # Translate common section headers and text
    content = translate_common_section_headers(content)
    
    # Fix em/en dashes one more time after all translations
    content = content.replace('\u2014', '-')
    content = content.replace('\u2013', '-')
    
    return content


if __name__ == '__main__':
    print("Korean translation engine loaded")
    # Test a simple phrase
    test = "Register at 1win"
    result = translate_generic_en_to_ko(test)
    print(f"Test translation: '{test}' → '{result}'")
