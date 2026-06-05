#!/usr/bin/env python3
"""
Apply Korean translations to all KO pages.
Reads KO files (already have EN source text + mechanical fixes),
applies translation dictionary, then writes back.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ko_translate_engine import translate_html_file

REPO = Path('/home/user/workspace/1win-codes-repo')
KO_DIR = REPO / 'ko'

# Additional page-specific translations for body text
# These are substantial text blocks that appear in the pages
BODY_TEXT_REPLACEMENTS = [
    # Index page hero
    ("Code XLBONUS stacks a 200% + 150% + 100% + 50% bonus across your first four deposits. "
     "1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). "
     "600% total, auto-activated.",
     "코드 XLBONUS는 첫 4번의 입금에 걸쳐 200% + 150% + 100% + 50% 보너스를 적립합니다. "
     "1win은 30개 이상의 스포츠와 11,000개 이상의 카지노 게임을 제공합니다. "
     "Curaçao 8048/JAZ 라이선스 보유. 총 600% 보너스, 자동 활성화."),
    
    # 1win Register section
    ("1win covers 30+ sports with 1,000+ daily markets, live in-play betting with cash-out "
     "on every selection, and free streams on selected football and tennis matches. "
     "Curaçao-licensed (8048/JAZ), founded 2018.",
     "1win은 30개 이상의 스포츠와 매일 1,000개 이상의 마켓, 모든 선택에서 캐시아웃이 가능한 "
     "라이브 인플레이 베팅, 선택된 축구 및 테니스 경기의 무료 스트리밍을 제공합니다. "
     "Curaçao 8048/JAZ 라이선스 보유, 2018년 설립."),
    
    ("11,000+ casino games from 70+ providers including Pragmatic Play, Evolution, NetEnt and Spribe. "
     "Live dealer tables 24/7. Daily drops and tournaments worth $50,000+ a week.",
     "Pragmatic Play, Evolution, NetEnt, Spribe를 포함한 70개 이상의 제공업체에서 11,000개 이상의 "
     "카지노 게임을 제공합니다. 24시간 라이브 딜러 테이블 운영. 주당 $50,000 이상의 일일 드롭 및 토너먼트."),
    
    # 1win Login section
    ("1win is global. This website can be accessed all over the world. Log in to your account "
     "to start playing casino games and placing sports bets. Log in on your PC or mobile device "
     "to start playing. Alternatively, download the official 1win app to play on your Android or iOS device.",
     "1win은 전 세계적입니다. 이 웹사이트는 전 세계 어디서나 접속할 수 있습니다. 계정에 로그인하여 "
     "카지노 게임을 플레이하고 스포츠 베팅을 시작하세요. PC 또는 모바일 기기에서 로그인하여 플레이를 시작하세요. "
     "또는 공식 1win 앱을 다운로드하여 Android 또는 iOS 기기에서 플레이하세요."),
    
    ("When you log in you can play immediately. You have lots of payment methods to choose from "
     "and can fund your account using Bitcoin and many other crypto coins.",
     "로그인하면 즉시 플레이할 수 있습니다. 다양한 결제 방법 중에서 선택하고 "
     "비트코인 및 기타 암호화폐로 계정에 입금할 수 있습니다."),
    
    # Promo code section
    ("1win is a globally accessible sportsbook and casino, operating under Curaçao licence 8048/JAZ. "
     "New players use promo code",
     "1win은 Curaçao 8048/JAZ 라이선스로 운영되는 전 세계적으로 접근 가능한 스포츠북 및 카지노입니다. "
     "신규 플레이어는 프로모 코드"),
    
    ("to unlock a 600% welcome bonus across four deposits, up to $1,050 total.",
     "를 사용하여 4번의 입금에 걸쳐 최대 $1,050의 600% 환영 보너스를 받을 수 있습니다."),
    
    ("The XLBONUS code allows you to get the biggest available bonus when opening a new account. "
     "By using this code when registering, you can get a 600% deposit bonus. "
     "This can be claimed at either the sportsbook or the casino and also comes with up to 400 free spins.",
     "XLBONUS 코드를 사용하면 신규 계정 개설 시 가장 큰 보너스를 받을 수 있습니다. "
     "이 코드로 가입하면 600% 입금 보너스를 받을 수 있습니다. "
     "스포츠북 또는 카지노에서 청구할 수 있으며 최대 400회의 무료 스핀도 함께 제공됩니다."),
    
    ("Register with the code to get one of the largest bonus offers found at any online betting site anywhere in the world!",
     "코드로 가입하여 전 세계 어떤 온라인 베팅 사이트에서도 찾기 힘든 최대 보너스를 받으세요!"),
    
    # Welcome bonus section
    ("Four deposits. Each one supercharged. Here's exactly how the 600% total bonus works with crypto deposits.",
     "4회 입금. 각각 강력한 혜택. 암호화폐 입금 시 600% 총 보너스가 어떻게 작동하는지 정확히 알아보세요."),
    
    ("The above applies to crypto deposits. Fiat currency users get a 500% deposit bonus package across four deposits. 18+ | T&amp;C Apply | Play Responsibly.",
     "위 내용은 암호화폐 입금에 적용됩니다. 법정화폐 사용자는 4회 입금에 걸쳐 500% 입금 보너스 패키지를 받습니다. 만 18세 이상 | 이용약관 적용 | 책임감 있는 게임."),
    
    # Info table
    ("Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games",
     "스포츠 베팅, 카지노, 라이브 카지노, Aviator, 포커, Lucky Drive, 게임"),
    
    ("BTC, DOGE, ETH, USDT and others",
     "BTC, DOGE, ETH, USDT 등"),
    
    ("English, Spanish, Portuguese, Russian, Ukrainian, French, Italian, German, Polish, Kazakh, Hindi, Turkish, Tajik",
     "영어, 스페인어, 포르투갈어, 러시아어, 우크라이나어, 프랑스어, 이탈리아어, 독일어, 폴란드어, 카자흐어, 힌디어, 터키어, 타직어"),
    
    ("Yes, Android and iOS", "예 - Android 및 iOS"),
    ("Yes – Android and iOS", "예 - Android 및 iOS"),
    
    # Promo code details table
    ("Up to 600% bonus &amp; 400 Free Spins",
     "최대 600% 보너스 및 무료 스핀 400회"),
    
    ("Up to 600% deposit bonus", "최대 600% 입금 보너스"),
    
    ("18+ only. New customers only. Terms and conditions apply. Gamble responsibly.",
     "만 18세 이상. 신규 고객 전용. 이용약관 적용. 책임감 있는 게임."),
    
    # Girl break sections
    ("Use promo code",
     "프로모 코드"),
    
    ("when registering to get the biggest available welcome bonus. Up to 600% across four deposits.",
     "를 가입 시 사용하여 최고의 환영 보너스를 받으세요. 4번의 입금에 걸쳐 최대 600%."),
    
    ("1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.",
     "1win은 15개 언어로 제공됩니다. 30개 이상의 스포츠에 베팅하고 어디서나 11,000개 이상의 카지노 게임을 즐기세요."),
    
    # Payment section
    ("Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.",
     "카드, 전자지갑, 암호화폐로 계정을 충전하세요. 빠르고 안전하며 국경 없는 결제."),
    
    # Promos section subtitle
    ("Exclusive tournaments, cash bonuses, and limited-time offers, updated regularly.",
     "독점 토너먼트, 현금 보너스, 한정 기간 이벤트 - 정기적으로 업데이트됩니다."),
    
    # CTA banner
    ("Use code XLBONUS when you register to unlock a 600% welcome bonus. Visit our",
     "가입 시 XLBONUS 코드를 사용하여 600% 환영 보너스를 받으세요. 자세한 내용은"),
    
    ("promo code guide",
     "프로모션 코드 가이드"),
    
    ("for full details.",
     "를 참조하세요."),
    
    ("Claim your 600% bonus with code",
     "코드로 600% 보너스를 청구하세요"),
    
    (". Curaçao-licensed, 4-hour average withdrawals.",
     ". Curaçao 8048/JAZ 라이선스, 평균 4시간 출금."),
    
    # Step cards - how to use promo code
    ("Use links on this page to access the official 1win website and click the",
     "이 페이지의 링크를 사용하여 공식 1win 웹사이트에 접속하고"),
    
    ("'Register' button.",
     "'가입하기' 버튼을 클릭하세요."),
    
    ("Fill in the short registration form. When asked if you have a promo code, type in the",
     "짧은 가입 양식을 작성하세요. 프로모 코드가 있는지 물으면"),
    
    ("code.", "코드를 입력하세요."),
    
    ("Make your first deposit. A 130% first deposit bonus is available with",
     "첫 입금을 하세요. 로"),
    
    (", with further bonuses on deposits 2 to 4.",
     " 130% 첫 입금 보너스를 받을 수 있으며, 2~4번째 입금에도 추가 보너스가 있습니다."),
    
    ("The first part of your 600% bonus package will be credited to your account. Start playing!",
     "600% 보너스 패키지의 첫 번째 부분이 계정에 적립됩니다. 지금 플레이하세요!"),
    
    # FAQ answers
    ("Use the 1win promo code",
     "가입 시 1win 프로모 코드"),
    
    ("when you register to get the best welcome bonus available. Up to 600% deposit bonus can be claimed.",
     "를 사용하여 최고의 환영 보너스를 받으세요. 최대 600% 입금 보너스를 받을 수 있습니다."),
    
    # Section headers content
    ("1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ).",
     "1win은 30개 이상의 스포츠와 11,000개 이상의 카지노 게임을 제공합니다. Curaçao 8048/JAZ 라이선스 보유."),
    
    # IMPORTANT: Do NOT translate Curaçao 8048/JAZ - preserve verbatim per translation rules
    # The audit requires Curaçao (Latin chars) + 8048 to appear on every page
    # ("Curaçao-licensed (8048/JAZ)", "Curaçao 8048/JAZ 라이선스 보유"),  # PRESERVED
    # ("Curaçao 8048/JAZ", "Curaçao 8048/JAZ"),  # PRESERVED
    
    # Common repeated text patterns
    ("Yes – Android and iOS", "예 - Android 및 iOS"),
    ("Yes, Android and iOS", "예 - Android 및 iOS"),
    
    # Hero stats bar
    (">Bonus<", ">보너스<"),
    (">Sports<", ">스포츠<"),
    (">Games<", ">게임<"),
    (">Instant Crypto<", ">즉시 암호화폐<"),
    
    # Table data in info table
    ("Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games",
     "스포츠 베팅, 카지노, 라이브 카지노, Aviator, 포커, Lucky Drive, 게임"),
    
    # Promo callout section
    ("Use code XLBONUS when you register to unlock a 600% welcome bonus. Visit our",
     "가입 시 XLBONUS 코드를 입력하면 600% 환영 보너스가 활성화됩니다. 자세한 내용은"),
    
    # Data table headers
    (">Up to 600% deposit bonus<", ">최대 600% 입금 보너스<"),
    (">Up to 600% bonus &amp; 400 Free Spins<", ">최대 600% 보너스 및 무료 스핀 400회<"),
    
    # Winning streak section
    ("Your winning streak", "연승을 시작하세요"),
    ("Starts now", "지금 바로"),
    
    # General CTA banner
    (".Curaçao-licensed, 4-hour average withdrawals.", ". Curaçao 8048/JAZ 라이선스, 평균 4시간 출금."),
    
    # Common table values
    (">Yes<", ">예<"),
    (">No<", ">아니요<"),
    
    # Sports page phrases
    ("30+ sports", "30개 이상의 스포츠"),
    ("40,000+ markets", "40,000개 이상의 마켓"),
    ("11,000+ casino games", "11,000개 이상의 카지노 게임"),
    ("12,000+ slots", "12,000개 이상의 슬롯"),
    ("400,000+ players", "40만 명 이상의 플레이어"),
    
    # Common text patterns
    ("Click to read more", "더 읽기"),
    ("Read more", "더 읽기"),
    ("Learn more", "자세히 보기"),
    ("See all", "전체 보기"),
    ("View all", "전체 보기"),
    
    # Section subtitles commonly seen
    ("Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.",
     "카드, 전자지갑, 암호화폐로 계정을 충전하세요. 빠르고 안전하며 국경 없는 결제."),
    
    # Global Access section
    ("1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.",
     "1win은 15개 언어로 제공됩니다. 30개 이상의 스포츠에 베팅하고 어디서나 11,000개 이상의 카지노 게임을 즐기세요."),
    
    # Common section title text
    ("The 1WIN promo code is", "1WIN 프로모 코드는"),
    ("How to use the", "사용 방법"),
    ("1WIN promo code", "1WIN 프로모 코드"),
    ("1win Promo Code", "1win 프로모 코드"),
    ("promo code", "프로모 코드"),
    ("Promo Code", "프로모 코드"),
    
    # Badge labels
    (">Win a Lambo<", ">람보 당첨<"),
    (">Win a Lambo<", ">람보 당첨<"),
    
    # CTA section
    ("🎁 PROMO CODE:", "🎁 프로모 코드:"),
    
    # Index page specific additions  
    ("1WIN Register", "1WIN 가입하기"),
    ("1WIN Login", "1WIN 로그인"),
    ("1WIN Information", "1WIN 정보"),
    ("1WIN promo code", "1WIN 프로모 코드"),
    ("1WIN Welcome bonus", "1WIN 환영 보너스"),
    ("1WIN Payment methods", "1WIN 결제 방법"),
    ("Latest Promotions", "최신 프로모션"),
    ("LATEST PROMOTIONS", "최신 프로모션"),
    ("1WIN FAQs", "1WIN 자주 묻는 질문"),
    
    # Common content words in headings
    ("Information", "정보"),
    ("Register", "가입하기"),
    ("Welcome bonus", "환영 보너스"),
    ("Welcome Bonus", "환영 보너스"),
    ("Payment methods", "결제 방법"),
    ("Details", "세부 정보"),
    
    # Deposit amounts
    ("Up to 600%", "최대 600%"),
    ("Up to 500%", "최대 500%"),
    
    # Stat bar items on index page
    ("Instant Crypto", "즉시 암호화폐"),
    
    # Data table with info
    (">English, Spanish, Portuguese, Russian, Ukrainian, French, Italian, German, Polish, Kazakh, Hindi, Turkish, Tajik<",
     ">영어, 스페인어, 포르투갈어, 러시아어, 우크라이나어, 프랑스어, 이탈리아어, 독일어, 폴란드어, 카자흐어, 힌디어, 터키어, 타직어<"),
    
    # Winning streak / CTA final
    ("Your winning streak", "연승을 시작하세요"),
    ("Starts now", "지금 바로"),
    
    # Disclaimer footer text items
    ("1win.codes - independent affiliate review", "1win.codes - 독립 제휴 리뷰"),
    ("All rights reserved.", "모든 권리 보유."),
    
    # Meta / Title common patterns
    ("| XLBONUS 600%", "| XLBONUS 600%"),
    
    # Inline text in paragraphs
    ("promo code guide", "프로모션 코드 가이드"),
    ("Use code XLBONUS when you register", "가입 시 XLBONUS 코드를 입력하세요"),
    ("for full details.", "에서 자세한 내용을 확인하세요."),
]


def apply_body_text_translations(content):
    """Apply body text replacements in order."""
    for en, ko in BODY_TEXT_REPLACEMENTS:
        if isinstance(en, str) and en in content:
            content = content.replace(en, ko)
    return content


def translate_ko_file(filepath):
    """Apply all translations to a KO HTML file."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    
    # Apply translation engine
    from ko_translate_engine import translate_html_file
    content = translate_html_file(content)
    
    # Apply body text translations
    content = apply_body_text_translations(content)
    
    # Final dash cleanup
    content = content.replace('\u2014', '-')
    content = content.replace('\u2013', '-')
    
    filepath.write_text(content, encoding='utf-8')


def main():
    ko_files = sorted(KO_DIR.rglob('*.html'))
    print(f"Applying translations to {len(ko_files)} KO files...")
    
    for i, filepath in enumerate(ko_files):
        try:
            translate_ko_file(filepath)
            if (i + 1) % 25 == 0:
                print(f"  Translated {i+1}/{len(ko_files)} files...")
        except Exception as e:
            print(f"ERROR on {filepath.name}: {e}")
    
    print(f"\nDone: {len(ko_files)} files translated")


if __name__ == '__main__':
    main()
