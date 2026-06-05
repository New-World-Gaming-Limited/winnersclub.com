#!/usr/bin/env python3
"""
Comprehensive body text translation for KO pages.
Applies paragraph-by-paragraph and sentence-by-sentence translations
using a large dictionary of common EN phrases → KO translations.
"""

import re
from pathlib import Path

ko_dir = Path('/home/user/workspace/1win-codes-repo/ko')

# Large body text translation dictionary
# These are complete sentences and paragraphs that appear across pages
BODY_TRANSLATIONS = [
    # ===== PROMO CODE PAGE =====
    ("1win promo code XLBONUS is the only code that unlocks the full 600% welcome bonus across four deposits, up to $1,050 USDT. 1win holds Curaçao licence 8048/JAZ.",
     "1win 프로모 코드 XLBONUS는 4번의 입금에 걸쳐 최대 $1,050 USDT의 600% 환영 보너스 전체를 잠금 해제하는 유일한 코드입니다. 1win은 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    ("Most operators sell a \"200% welcome bonus\" and stop there. XLBONUS keeps paying across four deposits.",
     "대부분의 업체는 \"200% 환영 보너스\"를 제공하고 끝냅니다. XLBONUS는 4번의 입금에 걸쳐 계속 지급됩니다."),
    
    ("Crypto rate +200%, fiat rate +175%. Example: deposit $100, play with $300.",
     "암호화폐 요율 +200%, 법정화폐 요율 +175%. 예시: $100 입금 시 $300으로 플레이."),
    
    ("Crypto rate +150%, fiat rate +125%. Example: deposit $100, play with $250.",
     "암호화폐 요율 +150%, 법정화폐 요율 +125%. 예시: $100 입금 시 $250으로 플레이."),
    
    ("Crypto rate +160%, fiat rate +135%. Example: deposit $100, play with $260.",
     "암호화폐 요율 +160%, 법정화폐 요율 +135%. 예시: $100 입금 시 $260으로 플레이."),
    
    ("Crypto rate +170%, fiat rate +140%. Example: deposit $100, play with $270.",
     "암호화폐 요율 +170%, 법정화폐 요율 +140%. 예시: $100 입금 시 $270으로 플레이."),
    
    # ===== CASINO PAGE =====
    ("1win casino offers 11,000+ games across slots, live tables, crash games and jackpot titles from 70+ providers. Use code XLBONUS to unlock a 600% welcome bonus across four deposits. 1win holds Curaçao licence 8048/JAZ, operating since 2018.",
     "1win 카지노는 70개 이상의 제공업체의 슬롯, 라이브 테이블, 크래시 게임, 잭팟 타이틀 등 11,000개 이상의 게임을 제공합니다. 코드 XLBONUS로 4번의 입금에 걸쳐 600% 환영 보너스를 받으세요. 1win은 2018년부터 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    # ===== SPORTS BETTING PAGE =====
    ("1win sportsbook covers 30+ sports with 1,000+ daily markets. Every market has live in-play betting with cash-out available. Use code XLBONUS for 600% on your first four deposits. Curaçao licence 8048/JAZ, founded 2018.",
     "1win 스포츠북은 30개 이상의 스포츠와 매일 1,000개 이상의 마켓을 제공합니다. 모든 마켓에서 캐시아웃이 가능한 라이브 인플레이 베팅을 즐길 수 있습니다. 코드 XLBONUS로 첫 4번의 입금에 걸쳐 600%. Curaçao 8048/JAZ 라이선스, 2018년 설립."),
    
    # ===== COMMON SECTION TEXT =====
    ("First deposit 200%", "첫 번째 입금 200%"),
    ("Second deposit 150%", "두 번째 입금 150%"),
    ("Third deposit 150%", "세 번째 입금 150%"),
    ("Fourth deposit 100%", "네 번째 입금 100%"),
    
    # ===== REGISTER PAGE =====
    ("1win registration takes under 60 seconds. Three methods: one-click, phone number, or email. Enter code XLBONUS in the promo field to activate a 600% welcome bonus across four deposits. 1win holds Curaçao licence 8048/JAZ, operating since 2018.",
     "1win 가입은 60초 이내에 완료됩니다. 세 가지 방법: 원클릭, 전화번호, 이메일. 프로모 코드 입력란에 XLBONUS를 입력하면 4번의 입금에 걸쳐 600% 환영 보너스가 활성화됩니다. 1win은 2018년부터 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    # ===== APP PAGE =====
    ("The 1win app brings the full sportsbook and casino to your Android or iOS device. Download the APK directly for Android or install via TestFlight for iOS. Use code XLBONUS at registration for 600% on four deposits. Curaçao 8048/JAZ licensed.",
     "1win 앱은 Android 또는 iOS 기기에서 전체 스포츠북과 카지노를 즐길 수 있게 해줍니다. Android의 경우 APK를 직접 다운로드하거나 iOS의 경우 TestFlight를 통해 설치하세요. 가입 시 코드 XLBONUS로 4번의 입금에 걸쳐 600%. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== AVIATOR PAGE =====
    ("1win Aviator is the original Spribe crash game with a 97% RTP. A plane ascends and a multiplier rises with it. Cash out before the plane flies away to lock in your winnings. Use code XLBONUS for 600% on your first four deposits. 1win is Curaçao 8048/JAZ licensed.",
     "1win Aviator는 RTP 97%의 오리지널 Spribe 크래시 게임입니다. 비행기가 상승하면서 배수도 함께 올라갑니다. 비행기가 날아가기 전에 캐시아웃하여 당신의 상금을 확보하세요. 코드 XLBONUS로 첫 4번의 입금에 걸쳐 600%. 1win은 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    # ===== VIP PAGE =====
    ("1win VIP Club runs across eight tiers from Starter to Legendary. Points accumulate with every bet and climb through tiers. Higher tiers unlock cashback, dedicated account managers, exclusive bonuses and priority withdrawals. Enter XLBONUS at signup for a 600% welcome bonus. Curaçao 8048/JAZ.",
     "1win VIP 클럽은 스타터부터 레전더리까지 8개 등급으로 운영됩니다. 모든 베팅으로 포인트가 쌓이고 등급이 올라갑니다. 높은 등급에서는 캐시백, 전담 계정 매니저, 독점 보너스, 우선 출금이 제공됩니다. 가입 시 XLBONUS를 입력하면 600% 환영 보너스. Curaçao 8048/JAZ."),
    
    # ===== LUCKY DRIVE PAGE =====
    ("1win Lucky Drive is a ticket-based promotion where every deposit earns a free lottery ticket. Tickets enter a monthly draw for a Lamborghini Urus SE or other luxury prizes. Use code XLBONUS at registration for 600% bonus on four deposits. Curaçao 8048/JAZ licensed.",
     "1win Lucky Drive는 모든 입금으로 무료 복권 티켓을 받는 티켓 기반 프로모션입니다. 티켓으로 람보르기니 우루스 SE 또는 기타 럭셔리 상품의 월간 추첨에 참여할 수 있습니다. 가입 시 코드 XLBONUS로 4번의 입금에 걸쳐 600% 보너스. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== POKER PAGE =====
    ("1win poker runs on a dedicated software client and mobile app. Games include Texas Hold'em cash tables from $0.01/$0.02, sit-and-go, freerolls and scheduled tournaments. Use code XLBONUS at registration for a 600% welcome bonus. 1win holds Curaçao licence 8048/JAZ.",
     "1win 포커는 전용 소프트웨어 클라이언트와 모바일 앱에서 실행됩니다. $0.01/$0.02부터 시작하는 Texas Hold'em 현금 테이블, 싯앤고, 프리롤, 예정된 토너먼트가 포함됩니다. 가입 시 코드 XLBONUS로 600% 환영 보너스. 1win은 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    # ===== FAQ ANSWERS =====
    ("1win is global and can be accessed in lots of countries. You can access the sportsbook and casino via this page.",
     "1win은 글로벌 서비스로 많은 국가에서 접속할 수 있습니다. 이 페이지를 통해 스포츠북과 카지노에 접속할 수 있습니다."),
    
    ("Use the 1win promo code XLBONUS when you register to get the best welcome bonus available. Up to 600% deposit bonus can be claimed.",
     "가입 시 1win 프로모 코드 XLBONUS를 사용하여 최고의 환영 보너스를 받으세요. 최대 600% 입금 보너스를 받을 수 있습니다."),
    
    ("Use the 1win promo code",
     "1win 프로모 코드"),
    
    ("when you register to get the best welcome bonus available. Up to 600% deposit bonus can be claimed.",
     "를 가입 시 사용하여 최고의 환영 보너스를 받으세요. 최대 600% 입금 보너스를 받을 수 있습니다."),
    
    ("1win is a legitimate online betting site offering sports betting, casino games and much more. The official website at 1win.pro holds a Curacao gambling licence.",
     "1win은 스포츠 베팅, 카지노 게임 등 다양한 서비스를 제공하는 합법적인 온라인 베팅 사이트입니다. 공식 웹사이트 1win.pro는 Curaçao 8048/JAZ 게임 라이선스를 보유하고 있습니다."),
    
    ("Yes. The 1win app is available on Android and iOS. Register to get the download.",
     "네. 1win 앱은 Android와 iOS에서 사용할 수 있습니다. 가입 후 다운로드하세요."),
    
    ("1win Lucky Drive is a ticket-based promotion allowing players to win luxury vehicles, gadgets and free bets.",
     "1win Lucky Drive는 플레이어들이 럭셔리 차량, 가젯, 무료 베팅을 받을 수 있는 티켓 기반 프로모션입니다."),
    
    # ===== PAYMENT METHODS COMMON =====
    ("Instant deposit. No fees on the 1win side. Crypto deposits may take 10-30 minutes to confirm on-chain.",
     "즉시 입금. 1win 측 수수료 없음. 암호화폐 입금은 온체인 확인에 10-30분이 소요될 수 있습니다."),
    
    ("No fees on the 1win side.", "1win 측 수수료 없음."),
    ("Instant deposit.", "즉시 입금."),
    
    # ===== COUNTRY PAGES COMMON =====
    ("1win operates under Curaçao licence 8048/JAZ and has been active since 2018.",
     "1win은 Curaçao 8048/JAZ 라이선스로 운영되며 2018년부터 활동하고 있습니다."),
    
    ("1win is licensed under Curaçao 8048/JAZ.",
     "1win은 Curaçao 8048/JAZ 라이선스를 보유하고 있습니다."),
    
    ("Curaçao licence 8048/JAZ", "Curaçao 8048/JAZ 라이선스"),
    ("Curaçao-licensed (8048/JAZ)", "Curaçao 8048/JAZ 라이선스 보유"),
    ("Curaçao 8048/JAZ licensed platform", "Curaçao 8048/JAZ 라이선스 플랫폼"),
    ("Curaçao 8048/JAZ.", "Curaçao 8048/JAZ."),
    ("Curaçao licence", "Curaçao 라이선스"),
    ("Curacao 8048/JAZ", "Curaçao 8048/JAZ"),
    ("Curacao gambling licence", "Curaçao 게임 라이선스"),
    
    # ===== PROMOTIONS PAGE =====
    ("Current 1win promotions include tournaments, free spins, cashback, enhanced odds and the Lucky Drive luxury car prize draw. All promotions are available with code XLBONUS. Curaçao 8048/JAZ licensed.",
     "현재 1win 프로모션에는 토너먼트, 무료 스핀, 캐시백, 향상된 배당률, Lucky Drive 럭셔리 카 추첨이 포함됩니다. 모든 프로모션은 코드 XLBONUS와 함께 이용 가능합니다. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== BONUS PAGES =====
    ("1win welcome bonus runs across four deposits. Use promo code XLBONUS at signup to unlock the full package. First deposit: 200% crypto / 175% fiat. Total: up to 600% crypto or 500% fiat. Curaçao 8048/JAZ.",
     "1win 환영 보너스는 4번의 입금에 걸쳐 제공됩니다. 가입 시 프로모 코드 XLBONUS를 사용하면 전체 패키지가 잠금 해제됩니다. 첫 번째 입금: 암호화폐 200% / 법정화폐 175%. 총합: 최대 암호화폐 600% 또는 법정화폐 500%. Curaçao 8048/JAZ."),
    
    # ===== COMMON SENTENCES =====
    ("Use promo code XLBONUS at registration to unlock this bonus.", 
     "가입 시 프로모 코드 XLBONUS를 사용하면 이 보너스가 잠금 해제됩니다."),
    
    ("Enter code XLBONUS when registering to get 600% across four deposits.",
     "가입 시 코드 XLBONUS를 입력하면 4번의 입금에 걸쳐 600%를 받을 수 있습니다."),
    
    ("Use code XLBONUS at registration for a 600% welcome bonus.",
     "가입 시 코드 XLBONUS를 사용하면 600% 환영 보너스를 받을 수 있습니다."),
    
    ("Use code XLBONUS at signup for a 600% welcome bonus.",
     "가입 시 코드 XLBONUS를 사용하면 600% 환영 보너스를 받을 수 있습니다."),
    
    ("Use code XLBONUS for a 600% welcome bonus on your first four deposits.",
     "코드 XLBONUS로 첫 4번의 입금에 걸쳐 600% 환영 보너스를 받으세요."),
    
    ("Use code XLBONUS for 600% on your first four deposits.",
     "코드 XLBONUS로 첫 4번의 입금에 걸쳐 600%를 받으세요."),
    
    ("Use XLBONUS for 600% welcome bonus.",
     "XLBONUS로 600% 환영 보너스를 받으세요."),
    
    ("Enter XLBONUS at signup for a 600% welcome bonus.",
     "가입 시 XLBONUS를 입력하면 600% 환영 보너스를 받을 수 있습니다."),
    
    ("Enter XLBONUS for a 600% bonus on four deposits.",
     "4번의 입금에 걸쳐 600% 보너스를 위해 XLBONUS를 입력하세요."),
    
    (" with code XLBONUS at registration.", " 가입 시 코드 XLBONUS를 사용하세요."),
    
    ("with promo code XLBONUS", "프로모 코드 XLBONUS를 사용하여"),
    ("with code XLBONUS", "코드 XLBONUS를 사용하여"),
    ("via code XLBONUS", "코드 XLBONUS를 통해"),
    
    # ===== REVIEW PAGE =====
    ("1win is a licensed online sportsbook and casino launched in 2018 under Curaçao licence 8048/JAZ. It covers 30+ sports, 11,000+ casino games from 70+ providers, and offers a 600% welcome bonus to new players who register with promo code XLBONUS.",
     "1win은 2018년 Curaçao 8048/JAZ 라이선스로 출시된 합법적인 온라인 스포츠북 및 카지노입니다. 30개 이상의 스포츠, 70개 이상의 제공업체에서 11,000개 이상의 카지노 게임을 제공하며, 프로모 코드 XLBONUS로 가입하는 신규 플레이어에게 600% 환영 보너스를 제공합니다."),
    
    # ===== MIRROR/ALTERNATIVE LINK PAGES =====
    ("1win mirror links are alternative domains that point to the same 1win platform. When your ISP blocks the main domain, mirrors provide instant access. All 1win mirrors listed here are manually verified. Use code XLBONUS at signup for a 600% welcome bonus. Curaçao 8048/JAZ.",
     "1win 미러 링크는 동일한 1win 플랫폼으로 연결되는 대체 도메인입니다. ISP가 메인 도메인을 차단할 때 미러가 즉시 접속을 제공합니다. 여기에 나열된 모든 1win 미러는 수동으로 검증되었습니다. 가입 시 코드 XLBONUS로 600% 환영 보너스. Curaçao 8048/JAZ."),
    
    # ===== SLOTS =====
    ("This slot is available at 1win casino. Use promo code XLBONUS at registration to unlock a 600% welcome bonus across four deposits. Curaçao 8048/JAZ licensed.",
     "이 슬롯은 1win 카지노에서 이용 가능합니다. 가입 시 프로모 코드 XLBONUS를 사용하면 4번의 입금에 걸쳐 600% 환영 보너스가 잠금 해제됩니다. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== TOOLS PAGES =====
    ("This free calculator helps you make smarter bets at 1win. Use promo code XLBONUS at registration for a 600% welcome bonus across four deposits. Curaçao 8048/JAZ licensed.",
     "이 무료 계산기는 1win에서 더 스마트한 베팅을 도와줍니다. 가입 시 프로모 코드 XLBONUS를 사용하면 4번의 입금에 걸쳐 600% 환영 보너스가 잠금 해제됩니다. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== CRASH GAMES =====
    ("This crash game is available at 1win casino. Use code XLBONUS at registration for 600% on four deposits. Curaçao 8048/JAZ licensed.",
     "이 크래시 게임은 1win 카지노에서 이용 가능합니다. 가입 시 코드 XLBONUS로 4번의 입금에 걸쳐 600%. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== SPORTS PAGES =====
    ("1win covers this sport with live in-play betting, cash-out and pre-match markets. Use code XLBONUS for 600% welcome bonus on four deposits. Curaçao 8048/JAZ licensed.",
     "1win은 이 스포츠를 라이브 인플레이 베팅, 캐시아웃, 경기 전 마켓으로 커버합니다. 코드 XLBONUS로 4번의 입금에 걸쳐 600% 환영 보너스. Curaçao 8048/JAZ 라이선스 보유."),
    
    # ===== TIPS PAGES =====
    ("These tips are for informational purposes only. Use code XLBONUS at 1win for a 600% welcome bonus. Curaçao 8048/JAZ licensed. 18+. Gamble responsibly.",
     "이 팁들은 정보 제공 목적으로만 제공됩니다. 1win에서 코드 XLBONUS로 600% 환영 보너스. Curaçao 8048/JAZ 라이선스 보유. 만 18세 이상. 책임감 있는 게임."),
    
    # ===== NEWS PAGES =====
    ("1win is Curaçao-licensed (8048/JAZ) and has been operating since 2018.",
     "1win은 Curaçao 8048/JAZ 라이선스를 보유하며 2018년부터 운영되고 있습니다."),
    
    # ===== COMMON PHRASES ACROSS PAGES =====
    ("promo code guide", "프로모션 코드 가이드"),
    ("for full details.", "에서 자세한 내용을 확인하세요."),
    ("Use code XLBONUS when you register", "가입 시 코드 XLBONUS를 입력하세요"),
    ("visit our", "방문하세요"),
    
    # Common patterns
    ("18+ | T&amp;C Apply | Play Responsibly.", "만 18세 이상 | 이용약관 적용 | 책임감 있는 게임."),
    ("18+ | T&C Apply | Play Responsibly.", "만 18세 이상 | 이용약관 적용 | 책임감 있는 게임."),
    ("18+ only. New customers only. Terms and conditions apply. Gamble responsibly.", "만 18세 이상. 신규 고객 전용. 이용약관 적용. 책임감 있는 게임."),
    ("Gamble responsibly.", "책임감 있는 게임."),
    ("Play Responsibly.", "책임감 있게 플레이하세요."),
    
    # Common table content
    ("English, Spanish, Portuguese, Russian, Ukrainian, French, Italian, German, Polish, Kazakh, Hindi, Turkish, Tajik",
     "영어, 스페인어, 포르투갈어, 러시아어, 우크라이나어, 프랑스어, 이탈리아어, 독일어, 폴란드어, 카자흐어, 힌디어, 터키어, 타직어"),
    
    ("Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games",
     "스포츠 베팅, 카지노, 라이브 카지노, Aviator, 포커, Lucky Drive, 게임"),
    
    ("BTC, DOGE, ETH, USDT and others", "BTC, DOGE, ETH, USDT 등"),
    ("Yes, Android and iOS", "예 - Android 및 iOS"),
    ("Yes – Android and iOS", "예 - Android 및 iOS"),
    ("Up to 600%", "최대 600%"),
    ("Up to 600% deposit bonus", "최대 600% 입금 보너스"),
    ("Up to 600% bonus &amp; 400 Free Spins", "최대 600% 보너스 및 무료 스핀 400회"),
    
    # CTA section text
    ("Your winning streak", "연승을 시작하세요"),
    ("Starts now", "지금 바로"),
    ("Claim your 600% bonus with code", "코드로 600% 보너스를 받으세요"),
    (". Curaçao-licensed, 4-hour average withdrawals.", ". Curaçao 8048/JAZ 라이선스, 평균 4시간 출금."),
    
    # Hero section
    ("Code XLBONUS stacks a 200% + 150% + 100% + 50% bonus across your first four deposits. 1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). 600% total, auto-activated.",
     "코드 XLBONUS는 첫 4번의 입금에 걸쳐 200% + 150% + 100% + 50% 보너스를 적립합니다. 1win은 30개 이상의 스포츠와 11,000개 이상의 카지노 게임을 제공합니다. Curaçao 8048/JAZ 라이선스 보유. 총 600% 보너스, 자동 활성화."),
    
    # Promo callout
    ("Use code XLBONUS when you register to unlock a 600% welcome bonus. Visit our",
     "가입 시 코드 XLBONUS를 입력하면 600% 환영 보너스가 잠금 해제됩니다. 자세한 내용은"),
    
    # Footer
    ("1win.codes - independent affiliate review", "1win.codes - 독립 제휴 리뷰"),
    ("All rights reserved.", "모든 권리 보유."),
    ("This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk. Please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.",
     "이 사이트는 비공식 팬 사이트이며 1win과 제휴하거나 1win의 승인을 받은 사이트가 아닙니다. 이 사이트는 정보 제공 목적으로만 운영됩니다. 도박에는 위험이 따르므로 책임감 있게 플레이하십시오. 도박 문제가 있는 경우 GamCare 또는 지역 지원 기관에 연락하십시오."),
]


def apply_body_translations(content):
    """Apply all body text translations."""
    for en, ko in BODY_TRANSLATIONS:
        if en in content:
            content = content.replace(en, ko)
    return content


def translate_section_headings(content):
    """Translate h1/h2/h3 headings that are still in English."""
    
    # Common h2 patterns in section headers
    heading_map = {
        # These appear inside <h2 class="section-title"> etc
        ">1WIN Register<": ">1WIN 가입하기<",
        ">1WIN Login<": ">1WIN 로그인<",
        ">1WIN Information<": ">1WIN 정보<",
        ">1WIN Welcome bonus<": ">1WIN 환영 보너스<",
        ">1WIN Welcome Bonus<": ">1WIN 환영 보너스<",
        ">1WIN Payment methods<": ">1WIN 결제 방법<",
        ">1WIN FAQs<": ">1WIN 자주 묻는 질문<",
        ">1WIN promo code Details<": ">1WIN 프로모 코드 세부 정보<",
        ">1WIN promo code<": ">1WIN 프로모 코드<",
        ">Latest Promotions<": ">최신 프로모션<",
        ">LATEST PROMOTIONS<": ">최신 프로모션<",
        ">Your winning streak<": ">연승을 시작하세요<",
        ">Starts now<": ">지금 바로<",
        ">Global<": ">글로벌<",
        ">Access<": ">접속<",
        ">Register<": ">가입하기<",
        ">Information<": ">정보<",
        ">Details<": ">세부 정보<",
        ">Welcome bonus<": ">환영 보너스<",
        ">Welcome Bonus<": ">환영 보너스<",
        ">Payment methods<": ">결제 방법<",
        ">Get your<": ">받으세요<",
        ">600% bonus<": ">600% 보너스<",
        ">FAQs<": ">자주 묻는 질문<",
        
        # Step cards
        ">Visit 1win<": ">1win 방문<",
        ">Deposit<": ">입금<",
        ">Get Your Bonus<": ">보너스 받기<",
        ">First Deposit<": ">첫 번째 입금<",
        ">Second Deposit<": ">두 번째 입금<",
        ">Third Deposit<": ">세 번째 입금<",
        ">Fourth Deposit<": ">네 번째 입금<",
        
        # Table headers
        ">Product<": ">제품<",
        ">Promo Code<": ">프로모 코드<",
        ">Bonus Offer<": ">보너스 혜택<",
        ">Website<": ">웹사이트<",
        ">Products<": ">제품<",
        ">Established<": ">설립<",
        ">Accepted Crypto<": ">지원 암호화폐<",
        ">Website Languages<": ">지원 언어<",
        ">App<": ">앱<",
        ">Live Streaming<": ">라이브 스트리밍<",
        ">Live Support<": ">라이브 지원<",
        ">Promo code<": ">프로모 코드<",
        ">Deposit bonus<": ">입금 보너스<",
        ">Up to 600% deposit bonus<": ">최대 600% 입금 보너스<",
        ">Up to 600% bonus &amp; 400 Free Spins<": ">최대 600% 보너스 및 무료 스핀 400회<",
        
        # News/promo badges
        ">Win a Lambo<": ">람보 당첨<",
        ">Casino<": ">카지노<",
        ">Poker<": ">포커<",
        ">Aviator<": ">Aviator<",
        ">Slots<": ">슬롯<",
        ">Sports<": ">스포츠<",
        ">Bonus<": ">보너스<",
        ">Special<": ">특별<",
        
        # Promotions news cards
        ">Lucky Drive: Win a Lamborghini Urus SE<": ">Lucky Drive: 람보르기니 우루스 SE 당첨<",
        ">Deposit and claim your free ticket daily. Monthly luxury car draws await.<": ">매일 입금하고 무료 티켓을 받으세요. 매월 럭셔리 카 추첨이 기다립니다.<",
        ">Sins and Spins Tournament: $50,000 Prize Pool<": ">신스 앤 스핀 토너먼트 - $50,000 상금<",
        ">Spin the reels and climb the leaderboard for massive rewards.<": ">릴을 돌리고 리더보드를 오르며 엄청난 보상을 받으세요.<",
        ">Legends Tournament: $100,000 in Prizes<": ">레전드 토너먼트: $100,000 상금<",
        ">Compete against the best. Weekly tournaments with scheduled payouts.<": ">최고의 플레이어들과 경쟁하세요. 지급이 보장된 주간 토너먼트.<",
        ">Aviamasters: Crash Game Championship<": ">에비아마스터스: 크래시 게임 챔피언십<",
        ">Prove you're the ultimate Aviator pilot. Top cashouts win big.<": ">최고의 Aviator 파일럿임을 증명하세요. 최고 현금화로 크게 이기세요.<",
        ">Gamzix Slots Fest: Free Spins Galore<": ">Gamzix 슬롯 페스트 - 무료 스핀 대잔치<",
        ">Play featured Gamzix slots and earn free spins plus cash bonuses.<": ">선택된 Gamzix 슬롯을 플레이하고 무료 스핀과 현금 보너스를 받으세요.<",
        ">Olympics Special: Enhanced Odds on Every Sport<": ">올림픽 스페셜: 모든 스포츠 배당률 향상<",
        ">Boosted odds across all Olympic events. Back your country to win gold.<": ">모든 올림픽 이벤트에서 향상된 배당률. 자국의 금메달을 응원하세요.<",
        ">Republic Day Bonus: 200 Free Spins<": ">공화국 기념일 보너스: 무료 스핀 200회<",
        ">Celebrate with 200 free spins on selected slots. Limited time only.<": ">선택된 슬롯에서 무료 스핀 200회로 축하하세요. 기간 한정.<",
        ">Love Fest: Share the Jackpot<": ">러브 페스트: 잭팟 나눠갖기<",
        ">Refer a friend and both receive bonus cash. Spread the love, stack the wins.<": ">친구를 추천하면 두 분 모두 보너스 현금을 받습니다. 사랑을 나누고 승리를 쌓으세요.<",
        
        # FAQ items
        ">Can I access 1win?<": ">1win에 접속할 수 있나요?<",
        ">What is the 1win Promo Code?<": ">1win 프로모 코드는 무엇인가요?<",
        ">Is 1win legit?<": ">1win은 합법적인가요?<",
        ">Can I download a 1win app?<": ">1win 앱을 다운로드할 수 있나요?<",
        ">What is 1win Lucky Drive?<": ">1win Lucky Drive란 무엇인가요?<",
        
        # FAQ answers
        ">1win is global and can be accessed in lots of countries. You can access the sportsbook and casino via this page.<": ">1win은 글로벌 서비스로 많은 국가에서 접속할 수 있습니다. 이 페이지를 통해 스포츠북과 카지노에 접속할 수 있습니다.<",
        ">Yes. The 1win app is available on Android and iOS. Register to get the download.<": ">네. 1win 앱은 Android와 iOS에서 사용할 수 있습니다. 가입 후 다운로드하세요.<",
        ">1win Lucky Drive is a ticket-based promotion allowing players to win luxury vehicles, gadgets and free bets.<": ">1win Lucky Drive는 플레이어들이 럭셔리 차량, 가젯, 무료 베팅을 받을 수 있는 티켓 기반 프로모션입니다.<",
        
        # CTA button texts
        ">Register at 1win<": ">1win 가입하기<",
        ">Access 1win Registration<": ">1win 회원가입 접속<",
        ">Access Your 1win Account<": ">1win 계정 접속<",
        ">Login to 1win<": ">1win 로그인<",
        ">Join 1win<": ">1win 가입하기<",
        ">Claim Bonus<": ">보너스 받기<",
        ">Register with XLBONUS →<": ">XLBONUS로 가입하기 →<",
        ">Claim Promo Code →<": ">프로모 코드 받기 →<",
        ">Get Bonus<": ">보너스 받기<",
        ">Get Started<": ">시작하기<",
        ">Start Playing<": ">플레이 시작<",
        ">Play Now<": ">지금 플레이<",
        ">Claim Now<": ">지금 받기<",
        ">Sign Up Now<": ">지금 가입하기<",
        ">Sign Up<": ">가입하기<",
        ">Open Account<": ">계정 열기<",
        ">Download the App<": ">앱 다운로드<",
        ">Get the App<": ">앱 받기<",
        ">Start Now<": ">지금 시작<",
        ">Claim Your Bonus<": ">보너스 받기<",
        ">Register Now<": ">지금 가입하기<",
        ">Join Now<": ">지금 가입하기<",
        
        # Step card titles
        ">Visit 1win<": ">1win 방문<",
        
        # Promo code step cards
        ">Use links on this page to access the official 1win website and click the<": ">이 페이지의 링크를 클릭하여 공식 1win 웹사이트에 접속하고<",
        ">'Register' button.<": ">'가입하기' 버튼을 클릭하세요.<",
        
        # Welcome bonus deposit descriptions
        ">Crypto deposit bonus on your opening deposit.<": ">첫 입금 시 암호화폐 입금 보너스.<",
        ">Even bigger on your second top-up.<": ">두 번째 충전 시 더욱 큰 보너스.<",
        ">Serious boost on deposit number three.<": ">세 번째 입금 시 큰 보너스 혜택.<",
        ">The biggest single bonus on your fourth deposit.<": ">네 번째 입금 시 가장 큰 단일 보너스.<",
        
        # Section subtitles
        ">Four deposits. Each one supercharged. Here's exactly how the 600% total bonus works with crypto deposits.<": ">4회 입금. 각각 강력한 혜택. 암호화폐 입금 시 600% 총 보너스가 어떻게 작동하는지 정확히 알아보세요.<",
        ">Exclusive tournaments, cash bonuses, and limited-time offers, updated regularly.<": ">독점 토너먼트, 현금 보너스, 한정 기간 이벤트 - 정기적으로 업데이트됩니다.<",
        ">Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.<": ">카드, 전자지갑, 암호화폐로 계정을 충전하세요. 빠르고 안전하며 국경 없는 결제.<",
        
        # Payment section
        ">Cards &amp; E-Wallets<": ">카드 및 전자지갑<",
        ">Cryptocurrency<": ">암호화폐<",
        
        # Footer text
        ">1win.codes - independent affiliate review<": ">1win.codes - 독립 제휴 리뷰<",
        ">All rights reserved.<": ">모든 권리 보유.<",
        
        # CTA banner
        ">🎁 PROMO CODE: <": ">🎁 프로모 코드: <",
        
        # Disclaimer
        ">The above applies to crypto deposits. Fiat currency users get a 500% deposit bonus package across four deposits. 18+ | T&amp;C Apply | Play Responsibly.<": ">위 내용은 암호화폐 입금에 적용됩니다. 법정화폐 사용자는 4회 입금에 걸쳐 500% 입금 보너스 패키지를 받습니다. 만 18세 이상 | 이용약관 적용 | 책임감 있는 게임.<",
        ">18+ only. New customers only. Terms and conditions apply. Gamble responsibly.<": ">만 18세 이상. 신규 고객 전용. 이용약관 적용. 책임감 있는 게임.<",
    }
    
    for en, ko in heading_map.items():
        content = content.replace(en, ko)
    
    return content


def main():
    html_files = sorted(ko_dir.rglob('*.html'))
    print(f"Applying body translations to {len(html_files)} files...")
    
    updated = 0
    for filepath in html_files:
        content = filepath.read_text(encoding='utf-8', errors='replace')
        original = content
        
        content = apply_body_translations(content)
        content = translate_section_headings(content)
        
        # Final dash cleanup
        content = content.replace('\u2014', '-')
        content = content.replace('\u2013', '-')
        
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            updated += 1
        
        if (html_files.index(filepath) + 1) % 25 == 0:
            print(f"  Processed {html_files.index(filepath) + 1}/{len(html_files)}...")
    
    print(f"Updated {updated} files")


if __name__ == '__main__':
    main()
