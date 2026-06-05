#!/usr/bin/env python3
"""
Full Korean body translation for 1win-codes-repo/ko/
Translates paragraph text, headings, and common UI strings.
Rules:
- NEVER translate "Curaçao 8048/JAZ" or "Curaçao" → keep as Latin chars
- Keep brand names, game names, provider names verbatim
- Keep XLBONUS verbatim
- No em dash (—) or en dash (–) → already handled by process_ko.py
"""

import os, re, glob

KO_DIR = '/home/user/workspace/1win-codes-repo/ko'

# ─────────────────────────────────────────────
# TRANSLATION DICTIONARIES
# Order matters: more specific strings first
# ─────────────────────────────────────────────

# Exact paragraph translations (matched as complete text of <p> tag content)
PARA_EXACT = {
    # Disclaimer / footer
    "This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling may be restricted in your country. Please gamble responsibly.":
        "이 사이트는 비공식 팬 사이트로 1win과 제휴 관계가 없으며 1win의 승인을 받지 않았습니다. 본 사이트는 정보 제공 목적으로만 운영됩니다. 귀하의 국가에서는 도박이 제한될 수 있습니다. 책임감 있는 베팅을 하시기 바랍니다.",
    "This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only.":
        "이 사이트는 비공식 팬 사이트로 1win과 제휴 관계가 없으며 1win의 승인을 받지 않았습니다. 본 사이트는 정보 제공 목적으로만 운영됩니다.",
    "This is a fan-made informational site about 1win. Not affiliated with 1win. Gambling involves risk. Play responsibly.":
        "이 사이트는 1win에 관한 팬이 만든 정보 사이트입니다. 1win과 무관합니다. 도박에는 위험이 따릅니다. 책임감 있게 플레이하세요.",
    "© 2024 1win.codes. For entertainment purposes only.":
        "© 2024 1win.codes. 순수 엔터테인먼트 목적으로만 제공됩니다.",
    "This page has moved.":
        "이 페이지가 이동되었습니다.",
    "Read the latest article →":
        "최신 기사 읽기 →",
    "Sign up with XLBONUS →":
        "XLBONUS로 가입하기 →",
    "1win Launches Massive Spring Tournament Series with $2M Prize Pool":
        "1win, 상금 200만 달러의 대규모 스프링 토너먼트 시리즈 출시",
    "Champions League Quarter-Finals: Enhanced Odds & Free Bets at 1win":
        "챔피언스리그 8강: 1win에서 향상된 배당률과 무료 베팅",
    "New Exclusive Slot Games from Pragmatic Play & Evolution at 1win":
        "1win에 Pragmatic Play & Evolution의 새 독점 슬롯 게임 추가",
    "Create your 1win account in under 2 minutes. Enter XLBONUS to activate your 600% welcome bonus.":
        "2분 이내에 1win 계정을 만드세요. XLBONUS를 입력하여 600% 환영 보너스를 활성화하세요.",
    "Use XLBONUS when registering for a 600% welcome bonus.":
        "가입 시 XLBONUS를 입력하여 600% 환영 보너스를 받으세요.",
    "Click the registration link on this page. If direct access is unavailable, use the current mirror from our mirrors page.":
        "이 페이지의 가입 링크를 클릭하세요. 직접 접속이 불가능한 경우 미러 페이지의 현재 미러를 이용하세요.",
    "1win is available globally. Select your country for a dedicated guide with local payment methods, sports, and registration tips.":
        "1win은 전 세계에서 이용 가능합니다. 현지 결제 수단, 스포츠, 가입 팁이 담긴 전용 가이드를 보려면 국가를 선택하세요.",
    "Our support team is available around the clock.":
        "고객 지원팀은 24시간 연중무휴 운영됩니다.",
    "No matching questions found. Try a different search term or clear the search.":
        "일치하는 질문이 없습니다. 다른 검색어를 시도하거나 검색을 지우세요.",
    "Join millions of players already winning. Sign up in 30 seconds, claim your 600% bonus, and start playing today.":
        "이미 수백만 명의 플레이어가 수익을 올리고 있습니다. 30초 만에 가입하고, 600% 보너스를 받아 오늘 바로 플레이를 시작하세요.",
    "Registration, bonuses, payments, verification, everything you need to know in one place.":
        "가입, 보너스, 결제, 인증 - 알아야 할 모든 것이 한곳에.",
    "24/7 live chat support. Average response time under 30 seconds. Available on the 1win website and app.":
        "24시간 라이브 채팅 지원. 평균 응답 시간 30초 미만. 1win 웹사이트와 앱에서 이용 가능.",
    "Send a detailed message for complex issues. Response within 24 hours. Attach screenshots for faster resolution.":
        "복잡한 문제에 대한 상세 메시지 전송. 24시간 이내 답변. 빠른 해결을 위해 스크린샷을 첨부하세요.",
    "Reach out on Telegram, Instagram, or Twitter. Community managers respond to DMs and public inquiries.":
        "Telegram, Instagram 또는 Twitter로 연락하세요. 커뮤니티 매니저가 DM과 공개 문의에 답변합니다.",

    # Casino
    "Whatever your style, classic slots, live dealers, or jackpot hunting, we've got 11,000+ ways to win.":
        "클래식 슬롯, 라이브 딜러, 잭팟 사냥 등 어떤 스타일이든 11,000가지 이상의 승리 방법이 있습니다.",
    "From classic fruit machines to cinematic video slots with massive progressive jackpots. New titles added weekly.":
        "클래식 과일 머신부터 거대한 프로그레시브 잭팟이 있는 시네마틱 비디오 슬롯까지. 매주 새 타이틀이 추가됩니다.",
    "Real dealers. Real cards. Blackjack, Roulette, Baccarat, and Game Shows, all streamed in 4K HD quality.":
        "실제 딜러. 실제 카드. 블랙잭, 룰렛, 바카라, 게임 쇼 - 모두 4K HD 품질로 스트리밍됩니다.",
    "Blackjack, Poker, Roulette, Baccarat and beyond. Every variant, every stake level. RNG-certified fair play.":
        "블랙잭, 포커, 룰렛, 바카라 그리고 그 이상. 모든 변형, 모든 베팅 수준. RNG 인증 공정 플레이.",
    "Progressive jackpots that climb every second. One spin could change your life. Mega Moolah, Hall of Gods, and more.":
        "매초 증가하는 프로그레시브 잭팟. 한 번의 스핀이 삶을 바꿀 수 있습니다. Mega Moolah, Hall of Gods 등.",
    "Aviator, JetX, Spaceman, ride the multiplier curve, cash out before it crashes. Pure adrenaline.":
        "Aviator, JetX, Spaceman - 배수 곡선을 타고 충돌 전에 현금을 인출하세요. 순수한 아드레날린.",
    "Fresh releases every week from the world's top providers. Be the first to play the latest hits.":
        "세계 최고 제공업체의 신작이 매주 출시됩니다. 최신 인기 게임을 가장 먼저 즐겨보세요.",
    "European, American, Lightning Roulette, spin the wheel with real dealers. Multiple camera angles.":
        "유럽식, 아메리카식, 라이트닝 룰렛 - 실제 딜러와 함께 휠을 돌리세요. 다양한 카메라 앵글.",
    "Classic, VIP, Infinite Blackjack, take on the dealer in real-time. Side bets and perfect pairs available.":
        "클래식, VIP, 인피니트 블랙잭 - 실시간으로 딜러에 도전하세요. 사이드 베팅과 퍼펙트 페어 이용 가능.",
    "Speed Baccarat, Dragon Tiger, Squeeze, the game of choice for high rollers. Elegant and fast-paced.":
        "스피드 바카라, 드래곤 타이거, 스퀴즈 - 하이 롤러를 위한 게임. 우아하고 빠른 진행.",
    "Crazy Time, Monopoly Live, Dream Catcher, interactive game show experiences with massive multipliers.":
        "Crazy Time, Monopoly Live, Dream Catcher - 거대한 배수를 가진 인터랙티브 게임 쇼 경험.",
    "Daily and weekly slot tournaments with prize pools up to $100,000. Compete on the leaderboard and claim your share.":
        "상금이 최대 10만 달러인 일일 및 주간 슬롯 토너먼트. 리더보드에서 경쟁하고 상금을 받으세요.",
    "Get up to 30% cashback on losses every week. Play without fear, your bankroll always has a safety net.":
        "매주 손실의 최대 30%를 캐시백으로 받으세요. 두려움 없이 플레이하세요, 뱅크롤에는 항상 안전망이 있습니다.",
    "Exclusive high-limit tables for serious players. Personal dealer, private rooms, and premium rewards.":
        "진지한 플레이어를 위한 전용 고한도 테이블. 개인 딜러, 프라이빗 룸, 프리미엄 보상.",
    "1win casino features over 11,000 games including 8,000+ slots, 500+ table games, 100+ live dealer tables, 50+ crash games, and exclusive 1win Originals. New games are added every week from top providers.":
        "1win 카지노에는 8,000개 이상의 슬롯, 500개 이상의 테이블 게임, 100개 이상의 라이브 딜러 테이블, 50개 이상의 크래시 게임, 독점 1win 오리지널 게임을 포함하여 11,000개 이상의 게임이 있습니다. 상위 제공업체의 새 게임이 매주 추가됩니다.",
    "Popular titles include Gates of Olympus, Sweet Bonanza, Dog House Megaways, Book of Dead, and Starburst. 1win also features exclusive titles you won't find elsewhere. Check the 'Popular' and 'New' sections for trending games.":
        "인기 타이틀에는 Gates of Olympus, Sweet Bonanza, Dog House Megaways, Book of Dead, Starburst가 포함됩니다. 1win에는 다른 곳에서 찾을 수 없는 독점 타이틀도 있습니다. 트렌딩 게임은 '인기'와 '새 게임' 섹션을 확인하세요.",
    "Yes. All games use certified Random Number Generators (RNG) from licensed providers. Live casino games are streamed from regulated studios. Crash games like Aviator use provably fair technology with verifiable cryptographic hashes.":
        "네. 모든 게임은 라이선스 제공업체의 인증된 난수 발생기(RNG)를 사용합니다. 라이브 카지노 게임은 규제된 스튜디오에서 스트리밍됩니다. Aviator 같은 크래시 게임은 검증 가능한 암호화 해시를 사용하는 공정성 증명 기술을 사용합니다.",
    "Absolutely. All 11,000+ games are optimized for mobile play through the 1win app (iOS & Android) or mobile browser. No downloads required for browser play, just log in and start spinning.":
        "물론입니다. 모든 11,000개 이상의 게임은 1win 앱(iOS 및 Android) 또는 모바일 브라우저를 통해 모바일 플레이에 최적화되어 있습니다. 브라우저 플레이에는 다운로드가 필요 없으며, 그냥 로그인하고 스핀을 시작하세요.",
    "Powered by the biggest names in iGaming. Only the best make the cut.":
        "iGaming의 최대 이름들이 제공합니다. 최고만이 선정됩니다.",
    "Over 11,000 games from the world's top providers. Slots, live dealers, jackpots, every spin could change everything.":
        "세계 최고 제공업체의 11,000개 이상의 게임. 슬롯, 라이브 딜러, 잭팟 - 모든 스핀이 모든 것을 바꿀 수 있습니다.",
    "Step into the action with real dealers, real cards, and real-time gameplay. This is as close to Vegas as it gets.":
        "실제 딜러, 실제 카드, 실시간 게임플레이로 액션에 참여하세요. 베가스에 가장 가까운 경험입니다.",
    "These numbers climb every second. One lucky spin is all it takes.":
        "이 숫자들은 매초 상승합니다. 운 좋은 스핀 한 번이면 충분합니다.",
    "Progressive jackpots growing every second. Someone has to win, why not you?":
        "프로그레시브 잭팟이 매초 증가합니다. 누군가는 이겨야 하는데, 왜 당신이 아닌가요?",
    "1win Casino stands out in a saturated market because of the scale and quality of its game catalogue. With over 11,000 titles from 70+ providers, it delivers genuine depth across every category.":
        "1win 카지노는 포화된 시장에서 게임 카탈로그의 규모와 품질로 두각을 나타냅니다. 70개 이상의 제공업체로부터 11,000개 이상의 타이틀로 모든 카테고리에서 진정한 깊이를 제공합니다.",
    "The live casino section is powered primarily by Evolution, the industry leader in live dealer streaming, and delivers 100+ tables including game shows like Crazy Time and Lightning Roulette.":
        "라이브 카지노 섹션은 주로 라이브 딜러 스트리밍의 업계 리더인 Evolution이 운영하며, Crazy Time과 Lightning Roulette 같은 게임 쇼를 포함한 100개 이상의 테이블을 제공합니다.",
    "In addition to the welcome offer, 1win Casino provides weekly cashback of up to 30% on net losses, which creates a meaningful ongoing value proposition beyond the initial bonus.":
        "환영 보너스 외에도 1win 카지노는 순손실의 최대 30%의 주간 캐시백을 제공하여 초기 보너스를 넘어 지속적인 가치를 제공합니다.",
    "All games at 1win Casino use certified random number generators from their respective licensed providers. Crash games like Aviator use provably fair technology.":
        "1win 카지노의 모든 게임은 각 라이선스 제공업체의 인증된 난수 발생기를 사용합니다. Aviator 같은 크래시 게임은 공정성 증명 기술을 사용합니다.",
    "If you are blocked from accessing 1win.pro in your region, you can claim XLBONUS and access the full casino catalogue through the current working mirror link on our mirrors page.":
        "귀하의 지역에서 1win.pro 접속이 차단된 경우, XLBONUS를 받고 미러 페이지의 현재 작동 중인 미러 링크를 통해 전체 카지노 카탈로그에 접속할 수 있습니다.",

    # Aviator
    "Aviator is a crash-style game where a multiplier increases from 1.00x upward. Place your bet, watch the plane fly, and cash out before it crashes.":
        "Aviator는 배수가 1.00x부터 증가하는 크래시 스타일의 게임입니다. 베팅하고, 비행기가 날아가는 것을 지켜보며, 추락하기 전에 현금을 인출하세요.",
    "Choose your stake before the round starts. You can place two simultaneous bets for different strategies.":
        "라운드 시작 전에 배팅 금액을 선택하세요. 서로 다른 전략으로 두 개의 동시 베팅을 할 수 있습니다.",
    "The multiplier starts at 1.00x and climbs. 2x... 5x... 10x... 50x, the longer it flies, the higher the payout.":
        "배수는 1.00x에서 시작하여 올라갑니다. 2x... 5x... 10x... 50x - 더 오래 날수록 더 높은 지급액.",
    "Hit the cash-out button before the plane crashes. Your bet is multiplied by the current multiplier. Miss it, and you lose.":
        "비행기가 추락하기 전에 현금 인출 버튼을 누르세요. 베팅액에 현재 배수가 곱해집니다. 놓치면 잃습니다.",
    "Three strategies for three types of players. Conservative, balanced, or full send, pick your risk level.":
        "세 가지 유형의 플레이어를 위한 세 가지 전략. 보수적, 균형적, 또는 전면 도전 - 위험 수준을 선택하세요.",
    "Cash out at 1.2x-1.5x. Small, consistent wins. Low risk, sustainable bankroll growth. Win rate: ~85%.":
        "1.2x-1.5x에서 현금 인출. 소액의 꾸준한 승리. 낮은 위험, 지속 가능한 뱅크롤 성장. 승률: 약 85%.",
    "Target 2x-5x. Moderate risk with solid reward potential. The sweet spot for most experienced players. Win rate: ~50%.":
        "2x-5x 목표. 적당한 위험과 확실한 보상 가능성. 대부분의 경험 많은 플레이어에게 최적의 구간. 승률: 약 50%.",
    "Hold for 10x, 50x, or beyond. Maximum risk, maximum reward. When it hits, it hits HARD. Win rate: ~10%.":
        "10x, 50x 이상 유지. 최대 위험, 최대 보상. 적중하면 크게 적중합니다. 승률: 약 10%.",
    "The multiplier climbs. Your heart races. Cash out at the perfect moment, or watch it soar to 100x and beyond.":
        "배수가 올라갑니다. 심장이 두근거립니다. 완벽한 순간에 현금을 인출하거나 100x 이상으로 치솟는 것을 지켜보세요.",
    "Return to Player rate, among the highest in online gaming.":
        "환수율(RTP) - 온라인 게임 중 가장 높은 수준.",
    "The highest recorded multiplier. One bet, life-changing money.":
        "최고 기록 배수. 베팅 하나로 인생이 바뀌는 돈.",
    "Average crash point across millions of rounds played globally.":
        "전 세계 수백만 라운드에 걸친 평균 충돌 지점.",
    "Every round hash-verified. You can audit any result yourself.":
        "모든 라운드가 해시 검증됩니다. 누구든 결과를 직접 확인할 수 있습니다.",
    "Set your strategy and let the system execute it perfectly. No emotions, no hesitation.":
        "전략을 설정하고 시스템이 완벽하게 실행하도록 하세요. 감정도 없고 망설임도 없습니다.",
    "Decide your bankroll before playing. Never chase losses. Discipline is the ultimate strategy in crash games.":
        "플레이 전에 뱅크롤을 결정하세요. 절대 손실을 쫓지 마세요. 규율이 크래시 게임의 궁극적인 전략입니다.",
    "Place one conservative bet (1.5x auto-cashout) and one aggressive bet. Secures consistent small wins while chasing big multipliers.":
        "보수적 베팅(1.5x 자동 현금 인출)과 공격적 베팅을 동시에 하세요. 큰 배수를 추구하면서 꾸준한 소액 승리를 확보합니다.",
    "Remove emotion from the equation. Set a target multiplier and let the system do the work. Consistency beats impulse.":
        "감정을 제거하세요. 목표 배수를 설정하고 시스템이 작동하도록 하세요. 일관성이 충동을 이깁니다.",
    "Begin with minimum bets to learn the rhythm. Increase stakes gradually as you develop your own strategy and timing.":
        "리듬을 익히기 위해 최소 베팅으로 시작하세요. 자신만의 전략과 타이밍을 개발하면서 베팅 금액을 점차 늘려가세요.",

    # App
    "Everything the website offers, optimized for mobile speed and convenience.":
        "웹사이트가 제공하는 모든 것을 모바일 속도와 편의성에 최적화하여 제공합니다.",
    "Real-time alerts for live odds changes, promotions, and winning bets.":
        "라이브 배당률 변경, 프로모션, 당첨 베팅에 대한 실시간 알림.",
    "Place bets in seconds with streamlined one-tap betting interface.":
        "간소화된 원탭 베팅 인터페이스로 몇 초 만에 베팅하세요.",
    "Watch matches live directly in the app. No third-party apps needed.":
        "앱에서 직접 경기를 라이브로 시청하세요. 타사 앱이 필요 없습니다.",
    "Face ID and fingerprint authentication for fast, secure access.":
        "빠르고 안전한 접속을 위한 Face ID 및 지문 인증.",
    "Browse odds and review bets even without internet connection.":
        "인터넷 연결 없이도 배당률을 탐색하고 베팅을 확인하세요.",
    "Available on iOS and Android. Free to download, free to use.":
        "iOS 및 Android에서 이용 가능. 무료 다운로드, 무료 사용.",
    "iPhone and iPad. Requires iOS 13 or later. Available on the App Store.":
        "iPhone 및 iPad. iOS 13 이상 필요. App Store에서 이용 가능.",
    "All Android devices. Requires Android 7.0 or later. APK or Google Play.":
        "모든 Android 기기. Android 7.0 이상 필요. APK 또는 Google Play.",
    "The full 1win experience in your pocket. Lightning-fast, beautifully designed, and packed with features.":
        "주머니 속의 완전한 1win 경험. 번개처럼 빠르고, 아름답게 디자인되었으며, 다양한 기능으로 가득 찬.",

    # Access/Mirror
    "A 1win alternative link bypasses ISP blocks instantly, no VPN, no extra software. Your full account, balance, and bonuses remain intact.":
        "1win 대체 링크는 VPN이나 추가 소프트웨어 없이 즉시 ISP 차단을 우회합니다. 전체 계정, 잔액, 보너스가 그대로 유지됩니다.",
    "A 1win alternative link (also called a mirror link or access link) is a working URL on a different domain that routes directly to the 1win platform.":
        "1win 대체 링크(미러 링크 또는 접속 링크라고도 함)는 1win 플랫폼으로 직접 연결되는 다른 도메인의 작동 URL입니다.",
    "Three steps to get back on the platform in under 60 seconds.":
        "60초 이내에 플랫폼으로 돌아가는 3단계.",
    "Yes, official 1win mirrors are completely safe. They use the same SSL/TLS encryption and security infrastructure as the main domain.":
        "네, 공식 1win 미러는 완전히 안전합니다. 메인 도메인과 동일한 SSL/TLS 암호화 및 보안 인프라를 사용합니다.",
    "A mirror is a complete copy of the official 1win website, allowing players to bypass ISP blocks and access the full platform.":
        "미러는 공식 1win 웹사이트의 완전한 복사본으로, 플레이어가 ISP 차단을 우회하고 전체 플랫폼에 접속할 수 있게 해줍니다.",
    "Mirror sites are identical copies of the main 1win platform. They offer the same games, bonuses, payment options, and customer support.":
        "미러 사이트는 메인 1win 플랫폼의 동일한 복사본입니다. 동일한 게임, 보너스, 결제 옵션, 고객 지원을 제공합니다.",

    # Promotions
    "Every bet earns tickets. Win a Lamborghini Urus SE worth $240,000 or cash prizes up to $50,000.":
        "모든 베팅으로 티켓을 받으세요. 24만 달러 상당의 Lamborghini Urus SE 또는 최대 5만 달러의 현금 상품을 획득하세요.",
    "Weekly slot tournament with a $50,000 prize pool. Play eligible slots to climb the leaderboard.":
        "5만 달러 상금 풀의 주간 슬롯 토너먼트. 적격 슬롯을 플레이하여 리더보드를 오르세요.",
    "The most prestigious casino tournament. $100,000 in prizes across live dealer and table games.":
        "가장 권위 있는 카지노 토너먼트. 라이브 딜러와 테이블 게임에 걸친 10만 달러 상금.",
    "Compete against other Aviator players. Highest multipliers and biggest wins take the top prizes.":
        "다른 Aviator 플레이어들과 경쟁하세요. 최고 배수와 최대 승리가 1위 상품을 차지합니다.",
    "From weekly freerolls to million-dollar tournament series, every moment is a chance to win big.":
        "주간 프리롤부터 백만 달러 토너먼트 시리즈까지, 모든 순간이 크게 이길 수 있는 기회입니다.",

    # Registration
    "Click the registration link on this page to reach the official 1win platform. The registration form loads instantly, no app download required.":
        "이 페이지의 가입 링크를 클릭하여 공식 1win 플랫폼으로 이동하세요. 가입 양식이 즉시 로드되며, 앱 다운로드가 필요 없습니다.",
    "Select from four registration options: one-click (fastest), mobile phone, email address, or social media login via Google or Facebook.":
        "네 가지 가입 옵션 중 선택하세요: 원클릭(가장 빠름), 휴대폰, 이메일 주소, 또는 Google이나 Facebook을 통한 소셜 미디어 로그인.",
    "Choose the method that best suits your needs. All create the same full account.":
        "필요에 가장 적합한 방법을 선택하세요. 모두 동일한 전체 계정을 만듭니다.",

    # Payments
    "Cards, bank transfers, and regional payment systems. Choose what works for you.":
        "카드, 은행 이체, 지역 결제 시스템. 원하는 방법을 선택하세요.",
    "Zero fees. Instant processing. Maximum privacy. Crypto is the ultimate way to fund your account.":
        "수수료 없음. 즉시 처리. 최대 프라이버시. 암호화폐가 계정을 충전하는 최고의 방법입니다.",
    "8 cryptocurrencies. Zero fees. No minimum withdrawals. Your money moves at your speed.":
        "8가지 암호화폐. 수수료 없음. 최소 출금 없음. 돈이 당신의 속도로 움직입니다.",
    "Compare all payment options at a glance.":
        "모든 결제 옵션을 한눈에 비교하세요.",
    "Go to the Cashier section and choose your preferred payment method from the list above.":
        "캐셔 섹션으로 이동하여 위 목록에서 선호하는 결제 수단을 선택하세요.",
    "Type your deposit amount and confirm. Funds appear in your account instantly for most methods.":
        "입금 금액을 입력하고 확인하세요. 대부분의 방법으로 자금이 즉시 계정에 나타납니다.",
    "Your funds and data are protected by enterprise-level security infrastructure.":
        "귀하의 자금과 데이터는 기업 수준의 보안 인프라로 보호됩니다.",
    "256-bit SSL encryption on every transaction. The same standard used by major banks worldwide.":
        "모든 거래에 256비트 SSL 암호화. 전 세계 주요 은행들이 사용하는 것과 동일한 기준.",
    "Optional 2FA via Google Authenticator or SMS. An extra layer of protection for your account.":
        "Google Authenticator 또는 SMS를 통한 선택적 2FA. 계정에 대한 추가 보호 계층.",
    "95% of crypto funds stored in offline cold wallets. Protected from hacking and unauthorized access.":
        "암호화폐 자금의 95%가 오프라인 콜드 월렛에 저장됩니다. 해킹 및 무단 접근으로부터 보호됩니다.",
    "Crypto withdrawals are processed instantly. Card withdrawals take 1-3 business days. Bank transfers take 1-3 business days.":
        "암호화폐 출금은 즉시 처리됩니다. 카드 출금은 영업일 1-3일이 걸립니다. 은행 이체는 영업일 1-3일이 걸립니다.",
    "Crypto withdrawals are processed instantly. Card and bank transfers take 1-3 business days.":
        "암호화폐 출금은 즉시 처리됩니다. 카드 및 은행 이체는 영업일 1-3일이 걸립니다.",

    # Poker
    "Yes. 1win offers up to 50% rakeback depending on your playing volume. Rakeback is calculated on every hand you play and credited weekly.":
        "네. 1win은 플레이 볼륨에 따라 최대 50% 레이크백을 제공합니다. 레이크백은 플레이하는 모든 핸드에 계산되어 매주 지급됩니다.",
    "Yes. 1win runs multiple freeroll tournaments every day with real money prize pools and zero buy-in. They're the perfect way to build your bankroll from scratch.":
        "네. 1win은 실제 상금 풀과 바이인이 없는 프리롤 토너먼트를 매일 여러 번 개최합니다. 처음부터 뱅크롤을 만들기에 완벽한 방법입니다.",

    # VIP/FAQ
    "Yes. 1win supports responsible gambling. You can set deposit limits, loss limits, session time limits, or request a temporary self-exclusion.":
        "네. 1win은 책임감 있는 도박을 지원합니다. 입금 한도, 손실 한도, 세션 시간 한도를 설정하거나 일시적인 자기 배제를 요청할 수 있습니다.",
    "1win offers 24/7 live chat support accessible from any page. You can also reach support via email. VIP members have access to a dedicated account manager.":
        "1win은 모든 페이지에서 접근 가능한 24/7 라이브 채팅 지원을 제공합니다. 이메일로도 지원팀에 연락할 수 있습니다. VIP 회원은 전담 계정 매니저를 이용할 수 있습니다.",
    "No. Each person is allowed only one account on 1win. Creating multiple accounts violates the terms of service and may result in account suspension.":
        "아니요. 각 사람은 1win에 하나의 계정만 허용됩니다. 여러 계정을 생성하는 것은 서비스 약관을 위반하며 계정 정지로 이어질 수 있습니다.",
    "The wagering requirement is 5x the bonus amount. For example, if you receive a $100 bonus, you need to place $500 in total wagers before the bonus converts to cash.":
        "베팅 요건은 보너스 금액의 5배입니다. 예를 들어 100달러의 보너스를 받으면 보너스가 현금으로 전환되기 전에 총 500달러의 베팅을 해야 합니다.",
    "Yes. The XLBONUS welcome bonus applies to your main account balance and can be used across the sportsbook, casino, Aviator, and poker sections.":
        "네. XLBONUS 환영 보너스는 메인 계정 잔액에 적용되며 스포츠북, 카지노, Aviator, 포커 섹션에서 사용할 수 있습니다.",

    # Sports betting
    "1win covers professional basketball across five continents, giving bettors a live fixture at almost any hour of the day.":
        "1win은 다섯 대륙의 프로 농구를 커버하여 베터들에게 거의 매 시간 라이브 경기를 제공합니다.",
    "Cricket at 1win spans all three formats and every major competition on the international and domestic calendar.":
        "1win의 크리켓은 세 가지 형식 모두와 국제 및 국내 일정의 모든 주요 대회를 아우릅니다.",
    "Yes. 1win covers all 82 regular-season NBA games per team plus the full playoff bracket and NBA Finals, with markets including match winner, spread, totals, and player props.":
        "네. 1win은 팀당 82경기의 정규 시즌 NBA 게임 전체와 플레이오프 브래킷, NBA 파이널을 커버하며, 승자, 스프레드, 토탈, 플레이어 프롭을 포함한 마켓을 제공합니다.",
    "Yes. Full and partial cashout is available 24/7 on eligible basketball bets at 1win, covering both pre-match and in-play selections.":
        "네. 1win의 적격 농구 베팅에 대해 24/7로 전체 및 부분 현금 인출이 가능하며, 경기 전 및 인플레이 선택 모두를 포함합니다.",

    # India specific
    "Cricket (IPL), Football & Kabaddi, live in-play betting, competitive odds, and extensive markets.":
        "크리켓(IPL), 축구 & 카바디, 라이브 인플레이 베팅, 경쟁력 있는 배당률, 광범위한 마켓.",
    "The Indian Premier League (IPL) is the biggest cricket competition in the world by viewership and betting volume. 1win covers all 74 IPL matches per season.":
        "인도 프리미어 리그(IPL)는 시청률과 베팅 볼륨 면에서 세계 최대 크리켓 대회입니다. 1win은 시즌당 74개의 모든 IPL 경기를 커버합니다.",
    "Slots, live dealer games, Aviator, and more, all accessible in India.":
        "슬롯, 라이브 딜러 게임, Aviator 등 인도에서 모두 이용 가능합니다.",
    "Access 1win from India, no VPN required.":
        "인도에서 VPN 없이 1win에 접속하세요.",
    "Yes. 1win is accessible in India and accepts Indian players. The platform supports INR and popular Indian payment methods.":
        "네. 1win은 인도에서 접속 가능하며 인도 플레이어를 받아들입니다. 플랫폼은 INR과 인기 있는 인도 결제 수단을 지원합니다.",
    "Yes. Teen Patti is available in the 1win live casino section with dedicated tables and real dealers.":
        "네. 틴 파티는 전용 테이블과 실제 딜러와 함께 1win 라이브 카지노 섹션에서 이용 가능합니다.",
    "Yes. 1win has extensive IPL coverage including pre-match markets, live in-play betting, player props, and outright winner markets.":
        "네. 1win은 경기 전 마켓, 라이브 인플레이 베팅, 플레이어 프롭, 아웃라이트 우승자 마켓을 포함한 광범위한 IPL 커버리지를 갖추고 있습니다.",

    # Kenya specific
    "Football, Rugby & Cricket, live in-play betting, competitive odds, and extensive markets.":
        "축구, 럭비 & 크리켓, 라이브 인플레이 베팅, 경쟁력 있는 배당률, 광범위한 마켓.",
    "Slots, live dealer games, Aviator, and more, all accessible in Kenya.":
        "슬롯, 라이브 딜러 게임, Aviator 등 케냐에서 모두 이용 가능합니다.",
    "Access 1win from Kenya, no VPN required.":
        "케냐에서 VPN 없이 1win에 접속하세요.",

    # Korea specific
    "K-League, Baseball & Esports, live in-play betting, competitive odds, and extensive markets.":
        "K리그, 야구 & e스포츠, 라이브 인플레이 베팅, 경쟁력 있는 배당률, 광범위한 마켓.",
    "Slots, live dealer games, Aviator, and more, all accessible in Korea.":
        "슬롯, 라이브 딜러 게임, Aviator 등 한국에서 모두 이용 가능합니다.",
    "Access 1win from Korea, no VPN required.":
        "한국에서 VPN 없이 1win에 접속하세요.",

    # General FAQ answers
    "Yes. 1win operates under a Curaçao eGaming license (License No. 8048/JAZ), which allows it to offer online gambling services in over 50 countries.":
        "네. 1win은 Curaçao 8048/JAZ 이게이밍 라이선스 하에 운영되며, 이를 통해 50개 이상의 국가에서 온라인 도박 서비스를 제공할 수 있습니다.",
    "Yes. 1win uses 256-bit SSL encryption to protect all data transmissions, two-factor authentication (2FA) for account security, and stores 95% of funds in offline cold wallets.":
        "네. 1win은 모든 데이터 전송을 보호하기 위해 256비트 SSL 암호화를 사용하고, 계정 보안을 위한 이중 인증(2FA)과 자금의 95%를 오프라인 콜드 월렛에 저장합니다.",
    "1win is available in over 50 countries across Asia, Africa, Latin America, Europe, and CIS regions. Some countries may have access restrictions.":
        "1win은 아시아, 아프리카, 라틴 아메리카, 유럽, CIS 지역의 50개 이상의 국가에서 이용 가능합니다. 일부 국가에서는 접속 제한이 있을 수 있습니다.",
    "You must be at least 18 years old to register and play on 1win. Age verification is required during the KYC process, and 1win reserves the right to request ID at any time.":
        "1win에 가입하고 플레이하려면 18세 이상이어야 합니다. KYC 과정에서 나이 확인이 필요하며 1win은 언제든지 신분증을 요청할 권리가 있습니다.",
    "Crypto withdrawals are processed instantly. Card withdrawals take 1-3 business days. Bank transfers take 1-3 business days. VIP members may get priority processing.":
        "암호화폐 출금은 즉시 처리됩니다. 카드 출금은 영업일 1-3일, 은행 이체는 영업일 1-3일이 걸립니다. VIP 회원은 우선 처리를 받을 수 있습니다.",
    "Yes. The minimum withdrawal is $10 for all methods. There are no maximum withdrawal limits for verified VIP members.":
        "네. 모든 방법의 최소 출금액은 10달러입니다. 인증된 VIP 회원에게는 최대 출금 한도가 없습니다.",
    "1win accepts Bitcoin (BTC), Ethereum (ETH), Tether (USDT), Litecoin (LTC), Dogecoin (DOGE), Binance Coin (BNB), TRON (TRX), and Solana (SOL).":
        "1win은 Bitcoin(BTC), Ethereum(ETH), Tether(USDT), Litecoin(LTC), Dogecoin(DOGE), Binance Coin(BNB), TRON(TRX), Solana(SOL)을 받습니다.",
    "Withdrawals may be pending due to: KYC verification not completed, bonus wagering requirements not met, or standard processing time.":
        "출금이 보류될 수 있는 이유: KYC 인증 미완료, 보너스 베팅 요건 미충족, 또는 표준 처리 시간.",
    "The welcome bonus is valid for 30 days from the date of activation. You must complete the wagering requirements within this period.":
        "환영 보너스는 활성화 날짜로부터 30일 동안 유효합니다. 이 기간 내에 베팅 요건을 완료해야 합니다.",
    "Cashback is a percentage of your net losses returned to your account. The percentage depends on your VIP tier (3%-15%). Cashback is credited weekly.":
        "캐시백은 순손실의 일정 비율이 계정으로 반환되는 것입니다. 비율은 VIP 등급에 따라 다릅니다(3%-15%). 캐시백은 매주 지급됩니다.",
    "No. Bonus funds must be wagered 5x before withdrawal. You can withdraw your original deposit at any time, but withdrawing cancels any active bonus.":
        "아니요. 보너스 자금은 출금 전에 5회 베팅해야 합니다. 원래 입금액은 언제든지 출금할 수 있지만, 출금하면 활성 보너스가 취소됩니다.",

    # Live streaming
    "Yes. The 1win live streaming service is completely free for all registered players. There is no streaming subscription and no minimum bet required to watch.":
        "네. 1win 라이브 스트리밍 서비스는 모든 등록 플레이어에게 완전히 무료입니다. 스트리밍 구독이나 시청을 위한 최소 베팅이 필요 없습니다.",
    "Yes. Live streaming is fully supported on the 1win mobile app (Android and iOS) and on the mobile-optimised website accessible through any mobile browser.":
        "네. 라이브 스트리밍은 1win 모바일 앱(Android 및 iOS)과 모든 모바일 브라우저를 통해 접속 가능한 모바일 최적화 웹사이트에서 완전히 지원됩니다.",

    # Lucky Drive
    "Every real-money bet you place on 1win earns you automatic raffle tickets. The more you play, the more tickets you accumulate.":
        "1win에서 하는 모든 실제 돈 베팅으로 자동으로 추첨 티켓을 받습니다. 더 많이 플레이할수록 더 많은 티켓을 모읍니다.",
    "Three simple steps stand between you and a Lamborghini.":
        "람보르기니와 당신 사이에 세 가지 간단한 단계가 있습니다.",
    "Every $10 wagered earns you 1 Lucky Drive ticket.":
        "10달러를 베팅할 때마다 Lucky Drive 티켓 1장을 받습니다.",
    "Yes. Grand prize winners have the option to receive the cash equivalent ($240,000) instead of the vehicle. The choice is theirs.":
        "네. 대상 수상자는 차량 대신 현금 상당액(24만 달러)을 받을 수 있는 옵션이 있습니다. 선택은 수상자에게 달려 있습니다.",

    # Bonus pages
    "XLBONUS splits the 600% across four deposits instead of one. Crypto deposits qualify for the full 600% rate. Fiat deposits qualify for a 75%-equivalent rate.":
        "XLBONUS는 600%를 하나가 아닌 네 번의 입금에 걸쳐 나눕니다. 암호화폐 입금은 전체 600% 요율을 적용받습니다. 법정 화폐 입금은 75% 상당의 요율을 적용받습니다.",
    "Everything you need to know before you deposit.":
        "입금 전에 알아야 할 모든 것.",
    "The welcome bonus is the start. Weekly cashback, accumulator boosts, Lucky Drive tickets, and VIP rewards all stack on top.":
        "환영 보너스는 시작입니다. 주간 캐시백, 어큐뮬레이터 부스트, Lucky Drive 티켓, VIP 보상이 모두 그 위에 쌓입니다.",
    "Code XLBONUS must be entered on the registration form. It cannot be added after signup. Up to $1,050 total bonus credit.":
        "코드 XLBONUS는 가입 양식에 입력해야 합니다. 가입 후에는 추가할 수 없습니다. 최대 1,050달러의 총 보너스 크레딧.",

    # News
    "The latest promotions, tournament announcements, new game releases, and platform updates. Be the first to know.":
        "최신 프로모션, 토너먼트 발표, 새 게임 출시, 플랫폼 업데이트. 가장 먼저 알아보세요.",
    "Join 1win today and get instant access to the latest promotions, tournaments, and exclusive bonuses. Use code XLBONUS for a 600% welcome bonus.":
        "오늘 1win에 가입하고 최신 프로모션, 토너먼트, 독점 보너스에 즉시 접근하세요. 코드 XLBONUS로 600% 환영 보너스를 받으세요.",
    "200+ countries. Debit and credit. Instant.":
        "200개 이상의 국가. 직불카드 및 신용카드. 즉시.",
}

# Heading exact translations
HEADING_EXACT = {
    # Common section headings
    "Country availability and currency": "국가 이용 가능성 및 통화",
    "Alternative payment methods": "대체 결제 수단",
    "CLAIM YOUR 600% BONUS": "600% 보너스 받기",
    "Limits and timing": "한도 및 시간",
    "Bonus features": "보너스 기능",
    "Strategy and session tips": "전략 및 세션 팁",
    "Frequently asked questions": "자주 묻는 질문",
    "Frequently Asked Questions": "자주 묻는 질문",
    "Can I use XLBONUS after I have already registered?": "이미 가입한 후에 XLBONUS를 사용할 수 있나요?",
    "Bitcoin (BTC)": "Bitcoin (BTC)",
    "How this calculator works": "이 계산기 사용 방법",
    "Why use it at 1win": "1win에서 사용하는 이유",
    "Related tools": "관련 도구",
    "USDT (Tether)": "USDT (Tether)",
    "Related Articles": "관련 기사",
    "Related Reading": "관련 읽을거리",
    "→ 1win Mirror, Access from Anywhere": "→ 1win 미러, 어디서나 접속",
    "→ More 1win News": "→ 더 많은 1win 뉴스",
    "RTP transparency": "RTP 투명성",
    "Ethereum (ETH)": "Ethereum (ETH)",
    "Bank Transfer": "은행 이체",
    "Wagering and rules": "베팅 및 규칙",
    "Hero stats": "주요 통계",
    "Tournaments and competitions covered": "커버하는 토너먼트 및 대회",
    "Cashout and bet builder": "현금 인출 및 베팅 빌더",
    "All sports tips today": "오늘의 전체 스포츠 팁",
    "Visa/Mastercard": "Visa/Mastercard",
    "Visa / Mastercard": "Visa / Mastercard",
    "Make Your First Deposit": "첫 번째 입금하기",
    "Claim your 600% bonus": "600% 보너스 받기",
    "Create Your Account": "계정 만들기",
    "Visit the Website": "웹사이트 방문",
    "Access 1win and claim your 600% bonus": "1win에 접속하고 600% 보너스 받기",
    "Access fromAnywhere": "어디서나 접속",
    "SSL Encryption": "SSL 암호화",
    "Download the 1win app": "1win 앱 다운로드",
    "Social Media": "소셜 미디어",
    "1win mirror - working alternative link": "1win 미러 - 작동하는 대체 링크",
    "Android App": "Android 앱",
    "1win App 4.0 Released, Faster, Sleeker, Smarter": "1win 앱 4.0 출시 - 더 빠르고, 더 세련되고, 더 스마트하게",
    "1win Adds Solana & TRON, Now Supporting 8 Cryptocurrencies": "1win, Solana & TRON 추가 - 이제 8가지 암호화폐 지원",
    "Kelly criterion calculator": "켈리 기준 계산기",
    "Matched bet calculator": "매치드 베팅 계산기",
    "Game categories": "게임 카테고리",
    "Table Games": "테이블 게임",
    "Jackpot Games": "잭팟 게임",
    "Crash Games": "크래시 게임",
    "Top providers on the platform": "플랫폼의 주요 제공업체",
    "Claim your 600% casino bonus": "600% 카지노 보너스 받기",
    "Live casino at 1win": "1win의 라이브 카지노",
    "Live Roulette": "라이브 룰렛",
    "Live Blackjack": "라이브 블랙잭",
    "Live Baccarat": "라이브 바카라",
    "Game Shows": "게임 쇼",
    "Current jackpots": "현재 잭팟",
    "Tournaments and drops": "토너먼트 및 드롭",
    "Tournaments": "토너먼트",
    "VIP Tables": "VIP 테이블",
    "Daily and weekly rewards": "일일 및 주간 보상",
    "Why play at 1win casino": "1win 카지노에서 플레이하는 이유",
    "1win Aviator": "1win Aviator",
    "How the game works in 90 seconds": "90초 안에 게임 작동 방법",
    "Place Your Bet": "베팅하기",
    "Watch the Plane Fly": "비행기 날아가는 것 보기",
    "Cash Out in Time": "제때 현금 인출",
    "When to cash out": "현금 인출 시기",
    "Steady Grinder": "꾸준한 수익형",
    "Smart Player": "스마트 플레이어",
    "High Roller": "하이 롤러",
    "Play Aviator with XLBONUS": "XLBONUS로 Aviator 플레이",
    "Provably Fair": "공정성 증명",
    "Aviator features at 1win": "1win의 Aviator 기능",
    "Auto Cash-Out": "자동 현금 인출",
    "Cash-out strategies": "현금 인출 전략",
    "Set a Budget": "예산 설정",
    "Use Two Bets": "두 가지 베팅 사용",
    "Watch the History": "역사 보기",
    "Use Auto Cash-Out": "자동 현금 인출 사용",
    "Start Small": "소액으로 시작",
    "Related crash games on 1win": "1win의 관련 크래시 게임",
    "Aviator on 1win with XLBONUS": "XLBONUS와 함께 1win에서 Aviator",
    "Get 600% more to play Aviator": "Aviator 플레이를 위해 600% 더 받기",
    "1win live streaming": "1win 라이브 스트리밍",
    "1WIN freeLive stream": "1WIN 무료 라이브 스트리밍",
    "1WIN INDIA OVERVIEW": "1WIN 인도 개요",
    "HOW TO REGISTER AT 1WIN IN INDIA": "인도에서 1WIN 가입 방법",
    "Complete Registration": "가입 완료",
    "BET ON INDIA": "인도 베팅",
    "PAYMENT METHODS IN INDIA": "인도 결제 수단",
    "POPULAR SPORTS BETTING IN INDIA": "인도의 인기 스포츠 베팅",
    "1WIN CASINO IN INDIA": "인도의 1WIN 카지노",
    "1WIN MIRROR INDIA": "인도 1WIN 미러",
    "Is 1win available in India?": "인도에서 1win을 이용할 수 있나요?",
    "How do I use UPI to deposit at 1win?": "1win에서 UPI로 입금하는 방법은?",
    "Does 1win cover IPL betting?": "1win은 IPL 베팅을 제공하나요?",
    "1WIN BANGLADESH OVERVIEW": "1WIN 방글라데시 개요",
    "HOW TO REGISTER AT 1WIN IN BANGLADESH": "방글라데시에서 1WIN 가입 방법",
    "Visit 1win Bangladesh": "1win 방글라데시 방문",
    "Choose Registration Method": "가입 방법 선택",
    "Complete Your First Deposit": "첫 번째 입금 완료",
    "1WIN BANGLADESH PROMO CODE": "1WIN 방글라데시 프로모 코드",
    "BET ON BANGLADESH": "방글라데시 베팅",
    "PAYMENT METHODS IN BANGLADESH": "방글라데시 결제 수단",
    "POPULAR SPORTS BETTING IN BANGLADESH": "방글라데시의 인기 스포츠 베팅",
    "1WIN CASINO IN BANGLADESH": "방글라데시의 1WIN 카지노",
    "1WIN MIRROR BANGLADESH": "방글라데시 1WIN 미러",
    "1WIN KENYA OVERVIEW": "1WIN 케냐 개요",
    "HOW TO REGISTER AT 1WIN IN KENYA": "케냐에서 1WIN 가입 방법",
    "Open 1win Kenya": "1win 케냐 열기",
    "Deposit via M-Pesa": "M-Pesa로 입금",
    "1WIN KENYA PROMO CODE": "1WIN 케냐 프로모 코드",
    "BET ON KENYA": "케냐 베팅",
    "PAYMENT METHODS IN KENYA": "케냐 결제 수단",
    "POPULAR SPORTS BETTING IN KENYA": "케냐의 인기 스포츠 베팅",
    "1WIN CASINO IN KENYA": "케냐의 1WIN 카지노",
    "1WIN MIRROR KENYA": "케냐 1WIN 미러",
    "Can Kenyan players join 1win?": "케냐 플레이어가 1win에 가입할 수 있나요?",
    "How do I deposit with M-Pesa at 1win?": "1win에서 M-Pesa로 입금하는 방법은?",
    "Does 1win cover the Kenyan Premier League?": "1win은 케냐 프리미어 리그를 커버하나요?",
    "Is the 1win casino available in Kenya?": "케냐에서 1win 카지노를 이용할 수 있나요?",
    "1WIN KOREA OVERVIEW": "1WIN 한국 개요",
    "HOW TO REGISTER AT 1WIN IN KOREA": "한국에서 1WIN 가입 방법",
    "Visit 1win Korea": "1win 한국 방문",
    "Choose Your Registration Method": "가입 방법 선택",
    "1WIN KOREA PROMO CODE": "1WIN 한국 프로모 코드",
    "BET ON KOREA": "한국 베팅",
    "PAYMENT METHODS IN KOREA": "한국 결제 수단",
    "Litecoin (LTC)": "Litecoin (LTC)",
    "POPULAR SPORTS BETTING IN KOREA": "한국의 인기 스포츠 베팅",
    "1WIN CASINO IN KOREA": "한국의 1WIN 카지노",
    "1WIN MIRROR KOREA": "한국 1WIN 미러",
    "Can Korean players use 1win?": "한국 플레이어가 1win을 사용할 수 있나요?",
    "Does 1win cover K-League betting?": "1win은 K리그 베팅을 제공하나요?",
    "Is KBO baseball available at 1win?": "1win에서 KBO 야구를 이용할 수 있나요?",
    "Can I bet on esports at 1win Korea?": "1win 한국에서 e스포츠에 베팅할 수 있나요?",
    "1WIN RUSSIA OVERVIEW": "1WIN 러시아 개요",
    "HOW TO REGISTER AT 1WIN IN RUSSIA": "러시아에서 1WIN 가입 방법",
    "1WIN RUSSIA PROMO CODE": "1WIN 러시아 프로모 코드",
    "BET ON RUSSIA": "러시아 베팅",
    "PAYMENT METHODS IN RUSSIA": "러시아 결제 수단",
    "POPULAR SPORTS BETTING IN RUSSIA": "러시아의 인기 스포츠 베팅",
    "1WIN CASINO IN RUSSIA": "러시아의 1WIN 카지노",
    "1WIN MIRROR RUSSIA": "러시아 1WIN 미러",
    "1WIN TURKEY OVERVIEW": "1WIN 터키 개요",
    "HOW TO REGISTER AT 1WIN IN TURKEY": "터키에서 1WIN 가입 방법",
    "1WIN TURKEY PROMO CODE": "1WIN 터키 프로모 코드",
    "BET ON TURKEY": "터키 베팅",
    "PAYMENT METHODS IN TURKEY": "터키 결제 수단",
    "POPULAR SPORTS BETTING IN TURKEY": "터키의 인기 스포츠 베팅",
    "1WIN CASINO IN TURKEY": "터키의 1WIN 카지노",
    "1WIN MIRROR TURKEY": "터키 1WIN 미러",
    "1WIN VIETNAM OVERVIEW": "1WIN 베트남 개요",
    "HOW TO REGISTER AT 1WIN IN VIETNAM": "베트남에서 1WIN 가입 방법",
    "1WIN VIETNAM PROMO CODE": "1WIN 베트남 프로모 코드",
    "BET ON VIETNAM": "베트남 베팅",
    "PAYMENT METHODS IN VIETNAM": "베트남 결제 수단",
    "POPULAR SPORTS BETTING IN VIETNAM": "베트남의 인기 스포츠 베팅",
    "1WIN CASINO IN VIETNAM": "베트남의 1WIN 카지노",
    "1WIN MIRROR VIETNAM": "베트남 1WIN 미러",
    "1WIN BRAZIL OVERVIEW": "1WIN 브라질 개요",
    "HOW TO REGISTER AT 1WIN IN BRAZIL": "브라질에서 1WIN 가입 방법",
    "1WIN BRAZIL PROMO CODE": "1WIN 브라질 프로모 코드",
    "BET ON BRAZIL": "브라질 베팅",
    "PAYMENT METHODS IN BRAZIL": "브라질 결제 수단",
    "POPULAR SPORTS BETTING IN BRAZIL": "브라질의 인기 스포츠 베팅",
    "1WIN CASINO IN BRAZIL": "브라질의 1WIN 카지노",
    "1WIN MIRROR BRAZIL": "브라질 1WIN 미러",
    "1WIN GHANA OVERVIEW": "1WIN 가나 개요",
    "HOW TO REGISTER AT 1WIN IN GHANA": "가나에서 1WIN 가입 방법",
    "Visit 1win Ghana": "1win 가나 방문",
    "Deposit with MTN MoMo or Vodafone Cash": "MTN MoMo 또는 Vodafone Cash로 입금",
    "1WIN GHANA PROMO CODE": "1WIN 가나 프로모 코드",
    "BET ON GHANA": "가나 베팅",
    "PAYMENT METHODS IN GHANA": "가나 결제 수단",
    "Vodafone Cash": "Vodafone Cash",
    "POPULAR SPORTS BETTING IN GHANA": "가나의 인기 스포츠 베팅",
    "1WIN CASINO IN GHANA": "가나의 1WIN 카지노",
    "1WIN MIRROR GHANA": "가나 1WIN 미러",
    "1WIN PAKISTAN OVERVIEW": "1WIN 파키스탄 개요",
    "HOW TO REGISTER AT 1WIN IN PAKISTAN": "파키스탄에서 1WIN 가입 방법",
    "1WIN PAKISTAN PROMO CODE": "1WIN 파키스탄 프로모 코드",
    "BET ON PAKISTAN": "파키스탄 베팅",
    "PAYMENT METHODS IN PAKISTAN": "파키스탄 결제 수단",
    "POPULAR SPORTS BETTING IN PAKISTAN": "파키스탄의 인기 스포츠 베팅",
    "1WIN CASINO IN PAKISTAN": "파키스탄의 1WIN 카지노",
    "1WIN MIRROR PAKISTAN": "파키스탄 1WIN 미러",
    "Easypaisa": "Easypaisa",
    "1WIN INDIA PROMO CODE": "1WIN 인도 프로모 코드",
    "Bank Transfer (IMPS/NEFT)": "은행 이체(IMPS/NEFT)",
    "Is Teen Patti available at 1win India?": "1win 인도에서 틴 파티를 이용할 수 있나요?",
    "1win Register": "1win 가입",
    "1win register - open your account in 30 seconds": "1win 가입 - 30초 만에 계정 열기",
    "Jump To Section": "섹션으로 이동",
    "1win registration - quick facts": "1win 가입 - 빠른 사실",
    "The fastest signup - register by phone": "가장 빠른 가입 - 전화로 가입",
    "Visit the 1win Site": "1win 사이트 방문",
    "Choose Your Method": "방법 선택",
    "Enter Code XLBONUS": "코드 XLBONUS 입력",
    "Poker game types at 1win": "1win의 포커 게임 유형",
    "Texas Hold'em": "텍사스 홀덤",
    "Short Deck": "숏 덱",
    "Tournament schedule": "토너먼트 일정",
    "Multi-Table Tournaments": "멀티 테이블 토너먼트",
    "Freerolls": "프리롤",
    "Cash table stakes and options": "캐시 테이블 스테이크 및 옵션",
    "Cash tables at 1win": "1win의 캐시 테이블",
    "Poker features at 1win": "1win의 포커 기능",
    "Multi-Table": "멀티 테이블",
    "Hand History": "핸드 히스토리",
    "Statistics": "통계",
    "Anonymous Tables": "익명 테이블",
    "Rakeback and loyalty program": "레이크백 및 충성도 프로그램",
    "Up to 50% Rakeback": "최대 50% 레이크백",
    "Weekly Rakeback Bonus": "주간 레이크백 보너스",
    "Poker with XLBONUS": "XLBONUS로 포커",
    "1win poker - platform overview": "1win 포커 - 플랫폼 개요",
    "Frequently askedQuestions": "자주 묻는 질문",
    "The 600% breakdown - exactly what you get": "600% 세부 내역 - 정확히 받는 것",
    "First deposit": "첫 번째 입금",
    "Second deposit": "두 번째 입금",
    "Third deposit": "세 번째 입금",
    "Fourth deposit": "네 번째 입금",
    "How to activate XLBONUS in four steps": "네 단계로 XLBONUS 활성화 방법",
    "Step 2: Pick your currency": "2단계: 통화 선택",
    "Step 3: Confirm code and deposit": "3단계: 코드 확인 및 입금",
    "Unlock 600% with XLBONUS": "XLBONUS로 600% 잠금 해제",
    "Bonus terms in plain English": "간단한 영어로 설명한 보너스 조건",
    "Why XLBONUS beats the default 1win sign-up offer": "XLBONUS가 기본 1win 가입 오퍼보다 좋은 이유",
    "Other current 1win promotions": "다른 현재 1win 프로모션",
    "VIP Club - 5 tiers": "VIP 클럽 - 5단계",
    "Lucky Drive raffle": "Lucky Drive 추첨",
    "Weekly cashback and boost": "주간 캐시백 및 부스트",
    "More with XLBONUS": "XLBONUS로 더 많이",
    "Country promo guides": "국가별 프로모 가이드",
    "Claim your 600% bonus now": "지금 600% 보너스 받기",
    "1win promotions 2026": "1win 2026 프로모션",
    "Lucky Drive, Win a Lamborghini": "Lucky Drive - 람보르기니 획득",
    "Sins & Spins Tournament": "Sins & Spins 토너먼트",
    "Legends Tournament": "Legends 토너먼트",
    "AviaMasters, Aviator Tournament": "AviaMasters, Aviator 토너먼트",
    "Gamzix Challenge": "Gamzix 챌린지",
    "Olympics Bonus": "올림픽 보너스",
    "Republic Day Special": "공화국의 날 스페셜",
    "Lovefest Promotion": "Lovefest 프로모션",
    "CelebrationNever stops": "축제는 끝나지 않는다",
    "Every day isPayday": "매일이 급여일",
    "Current1WIN promotions": "현재 1WIN 프로모션",
    "Start with600% more": "600% 더 많이 시작하기",
    "1win deposits and withdrawals": "1win 입금 및 출금",
    "Choose your method by what matters": "중요한 것에 따라 방법 선택",
    "Mastercard": "Mastercard",
    "Crypto in detail": "암호화폐 상세 정보",
    "4-hour average payouts": "평균 4시간 지급",
    "Regional methods": "지역 결제 수단",
    "How to deposit in 4 steps": "4단계로 입금하는 방법",
    "SELECT METHOD": "방법 선택",
    "ENTER AMOUNT": "금액 입력",
    "How to withdraw": "출금 방법",
    "Fees, limits, and the small print": "수수료, 한도 및 세부 사항",
    "Two-Factor Auth (2FA)": "이중 인증(2FA)",
    "Cold Storage": "콜드 스토리지",
    "Fast, safe, fee-free crypto payouts": "빠르고 안전하며 수수료 없는 암호화폐 지급",
    "Crypto deposits at 1win": "1win의 암호화폐 입금",
    "Make your first deposit": "첫 번째 입금하기",
    "1win basketball betting: NBA, EuroLeague and global hoops": "1win 농구 베팅: NBA, 유로리그 및 글로벌 농구",
    "Most popular basketball betting markets": "가장 인기 있는 농구 베팅 마켓",
    "In-play and live basketball betting": "인플레이 및 라이브 농구 베팅",
    "Mobile basketball betting with the 1win app": "1win 앱으로 모바일 농구 베팅",
    "How to start betting on basketball at 1win": "1win에서 농구 베팅을 시작하는 방법",
    "1win cricket betting: IPL, T20 World Cup and every format covered": "1win 크리켓 베팅: IPL, T20 월드컵 및 모든 형식 커버",
    "Most popular cricket betting markets": "가장 인기 있는 크리켓 베팅 마켓",
    "In-play and live cricket betting": "인플레이 및 라이브 크리켓 베팅",
    "Mobile cricket betting with the 1win app": "1win 앱으로 모바일 크리켓 베팅",
    "How to start betting on cricket at 1win": "1win에서 크리켓 베팅을 시작하는 방법",
    "Lucky Drive - Win a Lamborghini Urus SE": "Lucky Drive - Lamborghini Urus SE 획득",
    "Lamborghini Urus SE": "Lamborghini Urus SE",
    "Why Lucky Drive?": "왜 Lucky Drive인가?",
    "How to enter in three steps": "세 단계로 참가하는 방법",
    "REGISTER ON 1WIN": "1WIN에 가입",
    "PLAY ANY GAME": "아무 게임이나 플레이",
    "WIN THE DRAW": "추첨에서 당첨",
    "Earn more tickets every day": "매일 더 많은 티켓 획득",
    "Prize tiers - not just the Lamborghini": "상품 등급 - 람보르기니만이 아니다",
    "Past Lucky Drive winners": "과거 Lucky Drive 당첨자",
    "Mohammed R.": "Mohammed R.",
    "When the draw happens": "추첨이 이루어지는 시기",
    "Ticket earn rate": "티켓 획득 요율",
    "More tickets, more chances": "더 많은 티켓, 더 많은 기회",
    "What is a 1win mirror?": "1win 미러란 무엇인가요?",
    "How to access the current 1win mirror": "현재 1win 미러에 접속하는 방법",
    "Mirror on iOS and Android": "iOS 및 Android의 미러",
    "PC / Desktop": "PC / 데스크탑",
    "Mobile Browser": "모바일 브라우저",
    "Three backup mirror methods": "세 가지 백업 미러 방법",
    "Quick Registration": "빠른 가입",
    "Phone Registration": "전화 가입",
    "Is the mirror safe?": "미러는 안전한가요?",
    "Make First Deposit": "첫 입금하기",
    "Why your main 1win URL might not load": "주요 1win URL이 로드되지 않을 수 있는 이유",
    "Why mirrors exist": "미러가 존재하는 이유",
    "Verifying a mirror is safe": "미러가 안전한지 확인하기",
    "Mirror vs VPN": "미러 vs VPN",
    "How to find the latest working mirror": "최신 작동 미러를 찾는 방법",
    "Bookmark This Page": "이 페이지 북마크",
    "Check Our Telegram Channel": "텔레그램 채널 확인",
    "Use the 1win App": "1win 앱 사용",
    "Access current mirror and claim your bonus": "현재 미러에 접속하고 보너스 받기",
    "Is 1win legal in Bangladesh?": "방글라데시에서 1win은 합법인가요?",
    "What currency does 1win Bangladesh use?": "1win 방글라데시는 어떤 통화를 사용하나요?",
    "How do I deposit with bKash at 1win?": "1win에서 bKash로 입금하는 방법은?",
    "Why can't I access 1win in Bangladesh?": "방글라데시에서 1win에 접속할 수 없는 이유는?",
    "1win Brasil: PIX deposits, Aviator and the XLBONUS welcome": "1win 브라질: PIX 입금, Aviator 및 XLBONUS 환영",
    "Access 1win Brazil": "1win 브라질 접속",
    "Deposit via Pix": "Pix로 입금",
    "Bank Transfer (TED/DOC)": "은행 이체(TED/DOC)",
    "Boleto Bancário": "Boleto Bancário",
    "Can Brazilian players use 1win?": "브라질 플레이어가 1win을 사용할 수 있나요?",
    "How do I deposit with Pix at 1win?": "1win에서 Pix로 입금하는 방법은?",
    "Does 1win cover Brasileirão betting?": "1win은 브라질레이라웅 베팅을 커버하나요?",
    "Is the 1win platform available in Portuguese?": "1win 플랫폼이 포르투갈어로 이용 가능한가요?",
    "Is 1win available in Ghana?": "가나에서 1win을 이용할 수 있나요?",
    "How do I use MTN MoMo at 1win?": "1win에서 MTN MoMo를 사용하는 방법은?",
    "Does 1win cover Ghana Premier League?": "1win은 가나 프리미어 리그를 커버하나요?",
    "Can I bet on AFCON at 1win?": "1win에서 AFCON에 베팅할 수 있나요?",
    "1win India: UPI deposits, IPL markets and the XLBONUS code": "1win 인도: UPI 입금, IPL 마켓 및 XLBONUS 코드",
    "Access 1win India": "1win 인도 접속",
    "Deposit via UPI, Paytm, or PhonePe": "UPI, Paytm 또는 PhonePe로 입금",
    "1win Pakistan: Easypaisa, JazzCash and XLBONUS for cricket": "1win 파키스탄: Easypaisa, JazzCash 및 크리켓을 위한 XLBONUS",
    "Access 1win Pakistan": "1win 파키스탄 접속",
    "Select Registration Type": "가입 유형 선택",
    "Deposit via Easypaisa or JazzCash": "Easypaisa 또는 JazzCash로 입금",
    "How do I access 1win in Pakistan?": "파키스탄에서 1win에 접속하는 방법은?",
    "Can I use Easypaisa to deposit at 1win?": "Easypaisa로 1win에 입금할 수 있나요?",
    "Does 1win cover PSL betting?": "1win은 PSL 베팅을 커버하나요?",
    "Is the 1win app available in Pakistan?": "파키스탄에서 1win 앱을 이용할 수 있나요?",
    "1win Russia: ruble play, hockey markets and the XLBONUS code": "1win 러시아: 루블 플레이, 하키 마켓 및 XLBONUS 코드",
    "Open 1win Russia": "1win 러시아 열기",
    "Deposit via Bank Card, Qiwi, or YooMoney": "은행 카드, Qiwi 또는 YooMoney로 입금",
    "Bank Cards (Visa/Mir)": "은행 카드(Visa/Mir)",
    "Qiwi Wallet": "Qiwi 월렛",
    "YooMoney (formerly Yandex.Money)": "YooMoney(구 Yandex.Money)",
    "How do I access 1win in Russia?": "러시아에서 1win에 접속하는 방법은?",
    "Can I use Qiwi to deposit at 1win?": "Qiwi로 1win에 입금할 수 있나요?",
    "Does 1win cover KHL hockey betting?": "1win은 KHL 하키 베팅을 커버하나요?",
    "Is 1win available in Russian language?": "1win이 러시아어로 이용 가능한가요?",
    "1win Türkiye: lira play, Süper Lig markets and XLBONUS": "1win 터키: 리라 플레이, 슈페르 리그 마켓 및 XLBONUS",
    "Access 1win Turkey": "1win 터키 접속",
    "Bank Transfer (Havale/EFT)": "은행 이체(Havale/EFT)",
    "How do I access 1win in Turkey?": "터키에서 1win에 접속하는 방법은?",
    "Can I use Papara at 1win Turkey?": "1win 터키에서 Papara를 사용할 수 있나요?",
    "Does 1win cover Süper Lig betting?": "1win은 슈페르 리그 베팅을 커버하나요?",
    "Is 1win a safe platform for Turkish players?": "1win이 터키 플레이어에게 안전한 플랫폼인가요?",
    "1win Vietnam: VND play, V.League markets and XLBONUS": "1win 베트남: VND 플레이, V.리그 마켓 및 XLBONUS",
    "Access 1win Vietnam": "1win 베트남 접속",
    "Deposit via MoMo or ZaloPay": "MoMo 또는 ZaloPay로 입금",
    "Can Vietnamese players use 1win?": "베트남 플레이어가 1win을 사용할 수 있나요?",
    "How do I deposit with MoMo at 1win?": "1win에서 MoMo로 입금하는 방법은?",
    "Does 1win cover V.League betting?": "1win은 V.리그 베팅을 커버하나요?",
    "Is 1win accessible in Vietnam?": "베트남에서 1win에 접속할 수 있나요?",
    "StillNeed help?": "아직도 도움이 필요하신가요?",
    "Email Support": "이메일 지원",
    "We've gotAnswers": "답변을 가지고 있습니다",
    "Ready toStart?": "시작할 준비가 되셨나요?",
    "Everything you need to know about1WIN": "1WIN에 대해 알아야 할 모든 것",
    "Ready toGet started?": "시작할 준비가 되셨나요?",
    "LatestStories": "최신 스토리",
    "Champions League Quarter-Finals: Enhanced Odds & Free Bets": "챔피언스리그 8강: 향상된 배당률과 무료 베팅",
    "New Exclusive Slot Games from Pragmatic Play & Evolution": "Pragmatic Play & Evolution의 새 독점 슬롯 게임",
    "Aviator Player Hits Record 847x Multiplier, Wins $42,350": "Aviator 플레이어 기록 847x 배수 달성, 4만 2,350달러 획득",
    "VIP Lucky Drive Q2 Draw: Win a Lamborghini Urus SE": "VIP Lucky Drive Q2 추첨: Lamborghini Urus SE 획득",
    "Weekly Poker Freerolls Now Live, $10,000 Prize Pool Every Sunday": "주간 포커 프리롤 라이브 - 매주 일요일 1만 달러 상금 풀",
    "UFC 315 Betting Preview: Card Analysis & Best Odds": "UFC 315 베팅 프리뷰: 카드 분석 및 최고 배당률",
    "StayInformed": "최신 정보 유지",
    "Join theAction": "액션에 참여하기",
    "Never missA beat": "아무것도 놓치지 마세요",
    "1win website - operator information": "1win 웹사이트 - 운영자 정보",
    "1win operator information": "1win 운영자 정보",
    "Make a Deposit": "입금하기",
    "Products on the 1win platform": "1win 플랫폼의 제품",
    "Sportsbook": "스포츠북",
    "1st Deposit": "1번째 입금",
    "2nd Deposit": "2번째 입금",
    "3rd Deposit": "3번째 입금",
    "4th Deposit": "4번째 입금",
    "Explore the1WIN website": "1WIN 웹사이트 탐색",
    "How to access the 1win website": "1win 웹사이트에 접속하는 방법",
    "Open your 1win account with XLBONUS": "XLBONUS로 1win 계정 열기",
    "All sports tips today": "오늘의 전체 스포츠 팁",
    "Game providers at 1win: compare all 8 studios": "1win의 게임 제공업체: 8개 스튜디오 모두 비교",
    "All 8 providers at a glance": "한눈에 보는 8개 제공업체",
    "RTP overview across all 8 providers": "8개 제공업체의 RTP 개요",
    "About BGaming": "BGaming 소개",
    "BGaming at 1win: provably fair and crypto-native": "1win의 BGaming: 공정성 증명 및 크립토 네이티브",
    "About Evolution Gaming": "Evolution Gaming 소개",
    "Evolution Gaming live casino at 1win": "1win의 Evolution Gaming 라이브 카지노",
    "About Hacksaw Gaming": "Hacksaw Gaming 소개",
    "Hacksaw Gaming slots at 1win": "1win의 Hacksaw Gaming 슬롯",
    "About NetEnt": "NetEnt 소개",
    "NetEnt slots at 1win: 28 years of iGaming": "1win의 NetEnt 슬롯: iGaming 28년",
    "About Play'n GO": "Play'n GO 소개",
    "Play'n GO slots at 1win": "1win의 Play'n GO 슬롯",
    "About Pragmatic Play": "Pragmatic Play 소개",
    "Pragmatic Play slots at 1win": "1win의 Pragmatic Play 슬롯",
    "About Relax Gaming": "Relax Gaming 소개",
    "Relax Gaming slots at 1win: Money Train and beyond": "1win의 Relax Gaming 슬롯: Money Train 그리고 그 이상",
    "About Spribe": "Spribe 소개",
    "Spribe games at 1win: Aviator and instant-win titles": "1win의 Spribe 게임: Aviator 및 즉시 당첨 타이틀",
    "1win Review": "1win 리뷰",
    "Big Bass Bonanza review": "Big Bass Bonanza 리뷰",
    "How Big Bass Bonanza works": "Big Bass Bonanza 작동 방법",
    "How to play Big Bass Bonanza at 1win": "1win에서 Big Bass Bonanza 플레이 방법",
    "Book of Dead review": "Book of Dead 리뷰",  # Approximate
    "Sweet Bonanza review": "Sweet Bonanza 리뷰",
    "How Sweet Bonanza works": "Sweet Bonanza 작동 방법",
    "How to play Sweet Bonanza at 1win": "1win에서 Sweet Bonanza 플레이 방법",
    "Wolf Gold review": "Wolf Gold 리뷰",
    "How Wolf Gold works": "Wolf Gold 작동 방법",
    "How to play Wolf Gold at 1win": "1win에서 Wolf Gold 플레이 방법",
    "Starburst slot review": "Starburst 슬롯 리뷰",
    "How Starburst works": "Starburst 작동 방법",
    "How to play Starburst at 1win": "1win에서 Starburst 플레이 방법",
    "Razor Shark review": "Razor Shark 리뷰",
    "How Razor Shark works": "Razor Shark 작동 방법",
    "How to play Razor Shark at 1win": "1win에서 Razor Shark 플레이 방법",
    "Reactoonz slot review": "Reactoonz 슬롯 리뷰",  # approximate
    "Play Reactoonz at 1win": "1win에서 Reactoonz 플레이",
    "How Reactoonz works": "Reactoonz 작동 방법",
    "How to play Reactoonz at 1win": "1win에서 Reactoonz 플레이 방법",
    "Sugar Rush 1000 review": "Sugar Rush 1000 리뷰",
    "How Sugar Rush 1000 works": "Sugar Rush 1000 작동 방법",
    "How to play Sugar Rush 1000 at 1win": "1win에서 Sugar Rush 1000 플레이 방법",
    "Rise of Olympus 100 at 1win": "1win의 Rise of Olympus 100",
    "How Rise of Olympus 100 works": "Rise of Olympus 100 작동 방법",
    "How to play Rise of Olympus 100 at 1win": "1win에서 Rise of Olympus 100 플레이 방법",
    "Wanted Dead or a Wild review": "Wanted Dead or a Wild 리뷰",
    "How Wanted Dead or a Wild works": "Wanted Dead or a Wild 작동 방법",
    "How to play Wanted Dead or a Wild at 1win": "1win에서 Wanted Dead or a Wild 플레이 방법",
    "Money Train 4 review": "Money Train 4 리뷰",
    "How Money Train 4 works": "Money Train 4 작동 방법",
    "How to play Money Train 4 at 1win": "1win에서 Money Train 4 플레이 방법",
    "1win cashback: weekly losses returned": "1win 캐시백: 주간 손실 환급",
    "Key facts: cashback bonus": "핵심 사항: 캐시백 보너스",
    "How to access cashback at 1win": "1win에서 캐시백에 접근하는 방법",
    "Best games to use cashback credit on": "캐시백 크레딧을 사용하기에 최적의 게임",
    "FAQ: cashback bonus": "FAQ: 캐시백 보너스",
    "1win first deposit bonus: 200% match": "1win 첫 번째 입금 보너스: 200% 매치",
    "Key facts: first deposit bonus": "핵심 사항: 첫 번째 입금 보너스",
    "How to claim the first deposit bonus": "첫 번째 입금 보너스 받는 방법",
    "Best games to use the first deposit bonus on": "첫 번째 입금 보너스를 사용하기에 최적의 게임",
    "FAQ: first deposit bonus": "FAQ: 첫 번째 입금 보너스",
    "Second deposit at 1win: 150% top up": "1win 두 번째 입금: 150% 탑업",
    "Key facts: second deposit bonus": "핵심 사항: 두 번째 입금 보너스",
    "How to claim the second deposit bonus": "두 번째 입금 보너스 받는 방법",
    "Best games to use the second deposit bonus on": "두 번째 입금 보너스를 사용하기에 최적의 게임",
    "FAQ: second deposit bonus": "FAQ: 두 번째 입금 보너스",
    "Third deposit boost at 1win: 150% match": "1win 세 번째 입금 부스트: 150% 매치",
    "Key facts: third deposit bonus": "핵심 사항: 세 번째 입금 보너스",
    "How to claim the third deposit bonus": "세 번째 입금 보너스 받는 방법",
    "Best games to use the third deposit bonus on": "세 번째 입금 보너스를 사용하기에 최적의 게임",
    "FAQ: third deposit bonus": "FAQ: 세 번째 입금 보너스",
    "Fourth deposit bonus at 1win: 100% complete": "1win 네 번째 입금 보너스: 100% 완료",
    "Key facts: fourth deposit bonus": "핵심 사항: 네 번째 입금 보너스",
    "How to claim the fourth deposit bonus": "네 번째 입금 보너스 받는 방법",
    "Best games to use the fourth deposit bonus on": "네 번째 입금 보너스를 사용하기에 최적의 게임",
    "FAQ: fourth deposit bonus": "FAQ: 네 번째 입금 보너스",
    "1win free spins today with XLBONUS": "XLBONUS로 오늘의 1win 무료 스핀",
    "Key facts: 1win free spins": "핵심 사항: 1win 무료 스핀",
    "How to access 1win free spins today": "오늘 1win 무료 스핀에 접근하는 방법",
    "Top slots to use when free spins are active": "무료 스핀이 활성화될 때 사용할 최고 슬롯",
    "Wagering and rules for free spin winnings": "무료 스핀 당첨금에 대한 베팅 및 규칙",
    "FAQ: 1win free spins": "FAQ: 1win 무료 스핀",
    "1win bonus guide: 600% welcome package and beyond": "1win 보너스 가이드: 600% 환영 패키지 및 그 이상",
    "600% welcome package breakdown": "600% 환영 패키지 세부 내역",
    "All 1win bonus pages": "모든 1win 보너스 페이지",
    "First deposit bonus": "첫 번째 입금 보너스",
    "Second deposit bonus": "두 번째 입금 보너스",
    "Third deposit bonus": "세 번째 입금 보너스",
    "Fourth deposit bonus": "네 번째 입금 보너스",
    "Wagering requirements explained": "베팅 요건 설명",
    "Cashback bonus": "캐시백 보너스",
    "How the welcome package works in sequence": "환영 패키지가 순서대로 작동하는 방법",
    "Honest assessment of the wagering": "베팅에 대한 솔직한 평가",
    "FAQ: 1win bonuses": "FAQ: 1win 보너스",
    "Bitcoin deposit and withdrawal at 1win": "1win의 Bitcoin 입금 및 출금",
    "Key facts: Bitcoin at 1win": "핵심 사항: 1win의 Bitcoin",
    "How to deposit Bitcoin at 1win": "1win에 Bitcoin 입금하는 방법",
    "How to withdraw Bitcoin from 1win": "1win에서 Bitcoin 출금하는 방법",
    "Limits and timing for Bitcoin deposits and withdrawals": "Bitcoin 입출금 한도 및 시간",
    "FAQ: Bitcoin at 1win": "FAQ: 1win의 Bitcoin",
    "Ripple (XRP) deposit and withdrawal at 1win": "1win의 Ripple(XRP) 입금 및 출금",
    "Key facts: Ripple at 1win": "핵심 사항: 1win의 Ripple",
    "How to deposit Ripple at 1win": "1win에 Ripple 입금하는 방법",
    "How to withdraw Ripple from 1win": "1win에서 Ripple 출금하는 방법",
    "Limits and timing for Ripple (XRP) deposits and withdrawals": "Ripple(XRP) 입출금 한도 및 시간",
    "FAQ: Ripple at 1win": "FAQ: 1win의 Ripple",
    "Solana deposit and withdrawal at 1win": "1win의 Solana 입금 및 출금",
    "Key facts: Solana at 1win": "핵심 사항: 1win의 Solana",
    "How to deposit Solana at 1win": "1win에 Solana 입금하는 방법",
    "How to withdraw Solana from 1win": "1win에서 Solana 출금하는 방법",
    "Limits and timing for Solana deposits and withdrawals": "Solana 입출금 한도 및 시간",
    "FAQ: Solana at 1win": "FAQ: 1win의 Solana",
    "Tron (TRX) deposit and withdrawal at 1win": "1win의 Tron(TRX) 입금 및 출금",
    "Key facts: Tron at 1win": "핵심 사항: 1win의 Tron",
    "How to deposit Tron at 1win": "1win에 Tron 입금하는 방법",
    "How to withdraw Tron from 1win": "1win에서 Tron 출금하는 방법",
    "Limits and timing for Tron deposits and withdrawals": "Tron 입출금 한도 및 시간",
    "FAQ: Tron at 1win": "FAQ: 1win의 Tron",
    "1win live streaming": "1win 라이브 스트리밍",
    "How toWatchAt 1WIN": "1WIN에서 시청하는 방법",
    "Log In to 1win": "1win에 로그인",
    "Go to the Live Section": "라이브 섹션으로 이동",
    "Click the TV Icon": "TV 아이콘 클릭",
    "Sports available forStreaming": "스트리밍 가능한 스포츠",
    "Football (Soccer)": "축구",
    "Ice Hockey": "아이스 하키",
    "Baseball &amp; Table Tennis": "야구 & 탁구",
    "Get 600% Bonus + Free Live Streaming with XLBONUS": "XLBONUS로 600% 보너스 + 무료 라이브 스트리밍 받기",
    "1win Android App": "1win Android 앱",
    "1win iOS App": "1win iOS 앱",
    "Watch live.Bet live.": "라이브 시청. 라이브 베팅.",
    "Airtel Money deposit at 1win for African players": "아프리카 플레이어를 위한 1win의 Airtel Money 입금",
    "Key facts: Airtel Money at 1win": "핵심 사항: 1win의 Airtel Money",
    "How to deposit at 1win with Airtel Money": "Airtel Money로 1win에 입금하는 방법",
    "How to withdraw from 1win to Airtel Money": "1win에서 Airtel Money로 출금하는 방법",
    "FAQ: Airtel Money at 1win": "FAQ: 1win의 Airtel Money",
    "Easypaisa deposit at 1win for Pakistani players": "파키스탄 플레이어를 위한 1win의 Easypaisa 입금",
    "Key facts: Easypaisa at 1win": "핵심 사항: 1win의 Easypaisa",
    "How to deposit with Easypaisa at 1win": "1win에서 Easypaisa로 입금하는 방법",
    "MuchBetter at 1win: deposit and withdrawal guide": "1win의 MuchBetter: 입금 및 출금 가이드",
    "Key facts: MuchBetter at 1win": "핵심 사항: 1win의 MuchBetter",
    "How to deposit with MuchBetter at 1win": "1win에서 MuchBetter로 입금하는 방법",
    "How to withdraw from 1win to MuchBetter": "1win에서 MuchBetter로 출금하는 방법",
    "FAQ: MuchBetter at 1win": "FAQ: 1win의 MuchBetter",
    "NEFT deposit at 1win for Indian players": "인도 플레이어를 위한 1win의 NEFT 입금",
    "Key facts: NEFT at 1win": "핵심 사항: 1win의 NEFT",
    "How to deposit using NEFT at 1win": "1win에서 NEFT로 입금하는 방법",
    "How to withdraw via NEFT from 1win": "1win에서 NEFT로 출금하는 방법",
    "FAQ: NEFT at 1win": "FAQ: 1win의 NEFT",
    "Net banking deposit at 1win for Indian players": "인도 플레이어를 위한 1win의 인터넷 뱅킹 입금",
    "Key facts: Net banking at 1win": "핵심 사항: 1win의 인터넷 뱅킹",
    "How to deposit via net banking at 1win": "1win에서 인터넷 뱅킹으로 입금하는 방법",
    "How to withdraw to your bank account from 1win": "1win에서 은행 계좌로 출금하는 방법",
    "FAQ: Net banking at 1win": "FAQ: 1win의 인터넷 뱅킹",
    "Neteller at 1win: deposit and withdrawal guide": "1win의 Neteller: 입금 및 출금 가이드",
    "Key facts: Neteller at 1win": "핵심 사항: 1win의 Neteller",
    "How to deposit with Neteller at 1win": "1win에서 Neteller로 입금하는 방법",
    "How to withdraw from 1win to Neteller": "1win에서 Neteller로 출금하는 방법",
    "FAQ: Neteller at 1win": "FAQ: 1win의 Neteller",
    "Orange Money deposit at 1win for Francophone African players": "프랑코폰 아프리카 플레이어를 위한 1win의 Orange Money 입금",
    "Key facts: Orange Money at 1win": "핵심 사항: 1win의 Orange Money",
    "How to deposit at 1win with Orange Money": "Orange Money로 1win에 입금하는 방법",
    "How to withdraw from 1win to Orange Money": "1win에서 Orange Money로 출금하는 방법",
    "FAQ: Orange Money at 1win": "FAQ: 1win의 Orange Money",
    "Paytm deposit at 1win for Indian players": "인도 플레이어를 위한 1win의 Paytm 입금",
    "Key facts: Paytm at 1win": "핵심 사항: 1win의 Paytm",
    "How to deposit with Paytm at 1win": "1win에서 Paytm으로 입금하는 방법",
    "How to withdraw to Paytm from 1win": "1win에서 Paytm으로 출금하는 방법",
    "FAQ: Paytm at 1win": "FAQ: 1win의 Paytm",
    "PhonePe deposit at 1win for Indian players": "인도 플레이어를 위한 1win의 PhonePe 입금",
    "Key facts: PhonePe at 1win": "핵심 사항: 1win의 PhonePe",
    "How to deposit with PhonePe at 1win": "1win에서 PhonePe로 입금하는 방법",
    "How to withdraw via PhonePe from 1win": "1win에서 PhonePe로 출금하는 방법",
    "FAQ: PhonePe at 1win": "FAQ: 1win의 PhonePe",
    "PIX deposit at 1win for Brazilian players": "브라질 플레이어를 위한 1win의 PIX 입금",
    "Key facts: PIX at 1win": "핵심 사항: 1win의 PIX",
    "How to withdraw from 1win via PIX": "1win에서 PIX로 출금하는 방법",
    "FAQ: PIX at 1win": "FAQ: 1win의 PIX",
    "RuPay card deposit at 1win for Indian players": "인도 플레이어를 위한 1win의 RuPay 카드 입금",
    "Key facts: RuPay at 1win": "핵심 사항: 1win의 RuPay",
    "How to deposit with a RuPay card at 1win": "1win에서 RuPay 카드로 입금하는 방법",
    "How to withdraw when using RuPay at 1win": "1win에서 RuPay 사용 시 출금하는 방법",
    "FAQ: RuPay at 1win": "FAQ: 1win의 RuPay",
    "Skrill at 1win: deposit and withdrawal guide": "1win의 Skrill: 입금 및 출금 가이드",
    "Key facts: Skrill at 1win": "핵심 사항: 1win의 Skrill",
    "How to deposit with Skrill at 1win": "1win에서 Skrill로 입금하는 방법",
    "How to withdraw from 1win to Skrill": "1win에서 Skrill로 출금하는 방법",
    "FAQ: Skrill at 1win": "FAQ: 1win의 Skrill",
    "MTN MoMo deposit at 1win": "1win의 MTN MoMo 입금",  # approximate
    "How to deposit at 1win with MTN MoMo": "MTN MoMo로 1win에 입금하는 방법",
    "How to withdraw from 1win to MTN MoMo": "1win에서 MTN MoMo로 출금하는 방법",
    "FAQ: MTN MoMo at 1win": "FAQ: 1win의 MTN MoMo",
    "Boleto deposit at 1win for Brazilian players": "브라질 플레이어를 위한 1win의 Boleto 입금",
    "Key facts: Boleto at 1win": "핵심 사항: 1win의 Boleto",
    "How to deposit with Boleto at 1win": "1win에서 Boleto로 입금하는 방법",
    "How to withdraw from 1win as a Brazilian player (not via Boleto)": "브라질 플레이어로서 1win에서 출금하는 방법(Boleto 제외)",
    "FAQ: Boleto at 1win": "FAQ: 1win의 Boleto",
    "1win cricket betting: IPL, T20 World Cup and every format covered": "1win 크리켓 베팅: IPL, T20 월드컵 및 모든 형식 커버",
    "Arbitrage calculator: guaranteed profit stake split": "차익거래 계산기: 보장된 수익 베팅 배분",
    "2-way arbitrage calculator": "2방향 차익거래 계산기",
    "Bankroll calculator: unit size and risk of ruin": "뱅크롤 계산기: 단위 크기 및 파산 위험",
    "Bankroll management calculator": "뱅크롤 관리 계산기",
    "Each-way calculator: win and place returns": "이치웨이 계산기: 승리 및 순위권 수익",
    "Each-way bet calculator": "이치웨이 베팅 계산기",
    "Hedge calculator: lock in profit or minimise loss": "헤지 계산기: 수익 확보 또는 손실 최소화",
    "Hedge bet calculator": "헤지 베팅 계산기",
    "Today's basketball tips at 1win": "오늘의 1win 농구 팁",
    "Today's basketball tip selections": "오늘의 농구 팁 선택",
    "How these basketball tips are generated": "이 농구 팁이 생성되는 방법",
    "Basketball betting context for today": "오늘의 농구 베팅 맥락",
    "Today's cricket tips at 1win": "오늘의 1win 크리켓 팁",
    "Today's cricket tip selections": "오늘의 크리켓 팁 선택",
    "How these cricket tips are generated": "이 크리켓 팁이 생성되는 방법",
    "Cricket betting context for today": "오늘의 크리켓 베팅 맥락",
    "Today's esports tips at 1win": "오늘의 1win e스포츠 팁",
    "Today's esports tip selections": "오늘의 e스포츠 팁 선택",
    "How these esports tips are generated": "이 e스포츠 팁이 생성되는 방법",
    "Esports betting context for today": "오늘의 e스포츠 베팅 맥락",
    "Today's football tips at 1win": "오늘의 1win 축구 팁",
    "Today's football tip selections": "오늘의 축구 팁 선택",
    "How these football tips are generated": "이 축구 팁이 생성되는 방법",
    "Football betting context for today's markets": "오늘 마켓을 위한 축구 베팅 맥락",
    "Today's tennis tips at 1win": "오늘의 1win 테니스 팁",
    "Today's tennis tip selections": "오늘의 테니스 팁 선택",
    "How these tennis tips are generated": "이 테니스 팁이 생성되는 방법",
    "Tennis betting context for today": "오늘의 테니스 베팅 맥락",
    "1win India: state betting guides and IPL markets": "1win 인도: 주별 베팅 가이드 및 IPL 마켓",
    "India state betting guides": "인도 주별 베팅 가이드",
    "Choose your state": "주 선택",
    "Maharashtra": "마하라슈트라",
    "Tamil Nadu": "타밀나두",
    "Karnataka": "카르나타카",
    "Uttar Pradesh": "우타르프라데시",
    "West Bengal": "웨스트벵골",
    "Rajasthan": "라자스탄",
    "Andhra Pradesh": "안드라프라데시",
    "Telangana": "텔랑가나",
    "IPL coverage at 1win": "1win의 IPL 커버리지",
    "Legal note for Indian players": "인도 플레이어를 위한 법적 안내",
    "1win Karnataka: RCB cricket markets and PhonePe deposits": "1win 카르나타카: RCB 크리켓 마켓 및 PhonePe 입금",
    "Sports markets relevant to Karnataka": "카르나타카와 관련된 스포츠 마켓",
    "How to start betting at 1win from Karnataka": "카르나타카에서 1win 베팅을 시작하는 방법",
    "Legal note for Karnataka players": "카르나타카 플레이어를 위한 법적 안내",
    "1win Kerala: football and Premier League markets": "1win 케랄라: 축구 및 프리미어 리그 마켓",
    "Sports markets relevant to Kerala": "케랄라와 관련된 스포츠 마켓",
    "How to start betting at 1win from Kerala": "케랄라에서 1win 베팅을 시작하는 방법",
    "Legal note for Kerala players": "케랄라 플레이어를 위한 법적 안내",
    "1win Maharashtra: IPL betting and UPI deposits": "1win 마하라슈트라: IPL 베팅 및 UPI 입금",
    "Sports markets relevant to Maharashtra": "마하라슈트라와 관련된 스포츠 마켓",
    "How to start betting at 1win from Maharashtra": "마하라슈트라에서 1win 베팅을 시작하는 방법",
    "Legal note for Maharashtra players": "마하라슈트라 플레이어를 위한 법적 안내",
    "1win Punjab: Punjab Kings IPL and kabaddi markets": "1win 펀자브: 펀자브 킹스 IPL 및 카바디 마켓",
    "Sports markets relevant to Punjab": "펀자브와 관련된 스포츠 마켓",
    "How to start betting at 1win from Punjab": "펀자브에서 1win 베팅을 시작하는 방법",
    "Legal note for Punjab players": "펀자브 플레이어를 위한 법적 안내",
    "1win Rajasthan: Rajasthan Royals IPL markets and UPI deposits": "1win 라자스탄: 라자스탄 로열스 IPL 마켓 및 UPI 입금",
    "Sports markets relevant to Rajasthan": "라자스탄과 관련된 스포츠 마켓",
    "How to start betting at 1win from Rajasthan": "라자스탄에서 1win 베팅을 시작하는 방법",
    "Legal note for Rajasthan players": "라자스탄 플레이어를 위한 법적 안내",
    "1win Tamil Nadu: CSK cricket markets and UPI deposits": "1win 타밀나두: CSK 크리켓 마켓 및 UPI 입금",
    "Sports markets relevant to Tamil Nadu": "타밀나두와 관련된 스포츠 마켓",
    "How to start betting at 1win from Tamil Nadu": "타밀나두에서 1win 베팅을 시작하는 방법",
    "Legal note for Tamil Nadu players": "타밀나두 플레이어를 위한 법적 안내",
    "1win Telangana: Sunrisers Hyderabad markets and USDT deposits": "1win 텔랑가나: 선라이저스 하이데라바드 마켓 및 USDT 입금",
    "Sports markets relevant to Telangana": "텔랑가나와 관련된 스포츠 마켓",
    "How to start betting at 1win from Telangana": "텔랑가나에서 1win 베팅을 시작하는 방법",
    "Legal note for Telangana players": "텔랑가나 플레이어를 위한 법적 안내",
    "1win Uttar Pradesh: Lucknow Super Giants and cricket markets": "1win 우타르프라데시: 럭나우 슈퍼 자이언츠 및 크리켓 마켓",
    "Sports markets relevant to Uttar Pradesh": "우타르프라데시와 관련된 스포츠 마켓",
    "How to start betting at 1win from Uttar Pradesh": "우타르프라데시에서 1win 베팅을 시작하는 방법",
    "Legal note for Uttar Pradesh players": "우타르프라데시 플레이어를 위한 법적 안내",
    "1win West Bengal: KKR cricket and football markets": "1win 웨스트벵골: KKR 크리켓 및 축구 마켓",
    "Sports markets relevant to West Bengal": "웨스트벵골과 관련된 스포츠 마켓",
    "How to start betting at 1win from West Bengal": "웨스트벵골에서 1win 베팅을 시작하는 방법",
    "Legal note for West Bengal players": "웨스트벵골 플레이어를 위한 법적 안내",
    "1win Aviator Bonus News": "1win Aviator 보너스 뉴스",
    "1win Tokens Update": "1win 토큰 업데이트",
    "374k Win at 1win": "1win에서 37만 4천 달러 당첨",
    "45x Aviamasters Win": "45배 Aviamasters 당첨",
    "Free Poker at 1win": "1win의 무료 포커",
    "Mancala Gaming Bonuses": "Mancala Gaming 보너스",
    "Sins Spins at 1win": "1win의 Sins Spins",
    "Why 1win Uzbekistan?": "왜 1win 우즈베키스탄인가?",
    "Step-by-step: 1win Uzbekistan Registration with XLBONUS": "단계별: XLBONUS로 1win 우즈베키스탄 가입",
    "Payment Methods for 1win Uzbekistan": "1win 우즈베키스탄의 결제 수단",
    "Top Sports for Uzbek Players": "우즈베크 플레이어를 위한 주요 스포츠",
    "Accessing 1win in Uzbekistan": "우즈베키스탄에서 1win에 접속하기",
    "Is 1win legal in Uzbekistan?": "우즈베키스탄에서 1win은 합법인가요?",
    "How fast are withdrawals at 1win Uzbekistan?": "1win 우즈베키스탄에서 출금 속도는?",
    "Ready to Join 1win Uzbekistan?": "1win 우즈베키스탄에 가입할 준비가 되셨나요?",
    "About Spribe": "Spribe 소개",
    "Signature Spribe games at 1win": "1win의 주요 Spribe 게임",
    "Game mechanics Spribe is known for": "Spribe로 알려진 게임 메커닉",
    "How to play Spribe games at 1win with XLBONUS": "XLBONUS로 1win에서 Spribe 게임 플레이 방법",
    "Signature BGaming games at 1win": "1win의 주요 BGaming 게임",
    "Game mechanics BGaming is known for": "BGaming으로 알려진 게임 메커닉",
    "How to play BGaming titles at 1win with XLBONUS": "XLBONUS로 1win에서 BGaming 타이틀 플레이 방법",
    "Signature Evolution games at 1win": "1win의 주요 Evolution 게임",
    "Game mechanics Evolution is known for": "Evolution으로 알려진 게임 메커닉",
    "How to play Evolution games at 1win with XLBONUS": "XLBONUS로 1win에서 Evolution 게임 플레이 방법",
    "Signature Hacksaw games at 1win": "1win의 주요 Hacksaw 게임",
    "Game mechanics Hacksaw Gaming is known for": "Hacksaw Gaming으로 알려진 게임 메커닉",
    "How to play Hacksaw Gaming slots at 1win with XLBONUS": "XLBONUS로 1win에서 Hacksaw Gaming 슬롯 플레이 방법",
    "Signature NetEnt games at 1win": "1win의 주요 NetEnt 게임",
    "Game mechanics NetEnt is known for": "NetEnt으로 알려진 게임 메커닉",
    "How to play NetEnt slots at 1win with XLBONUS": "XLBONUS로 1win에서 NetEnt 슬롯 플레이 방법",
    "Signature Play'n GO games at 1win": "1win의 주요 Play'n GO 게임",
    "Game mechanics Play'n GO is known for": "Play'n GO로 알려진 게임 메커닉",
    "How to play Play'n GO slots at 1win with XLBONUS": "XLBONUS로 1win에서 Play'n GO 슬롯 플레이 방법",
    "Signature Pragmatic Play games at 1win": "1win의 주요 Pragmatic Play 게임",
    "Game mechanics Pragmatic Play is known for": "Pragmatic Play로 알려진 게임 메커닉",
    "How to play Pragmatic Play games at 1win with XLBONUS": "XLBONUS로 1win에서 Pragmatic Play 게임 플레이 방법",
    "Signature Relax Gaming games at 1win": "1win의 주요 Relax Gaming 게임",
    "Game mechanics Relax Gaming is known for": "Relax Gaming으로 알려진 게임 메커닉",
    "How to play Relax Gaming slots at 1win with XLBONUS": "XLBONUS로 1win에서 Relax Gaming 슬롯 플레이 방법",
    "For slots with the highest output volume: Pragmatic Play": "최고 생산 볼륨 슬롯: Pragmatic Play",
    "For live casino game shows: Evolution Gaming": "라이브 카지노 게임 쇼: Evolution Gaming",
    "For crash games and provably fair play: Spribe or BGaming": "크래시 게임 및 공정성 증명: Spribe 또는 BGaming",
    "For very high volatility slots: Hacksaw Gaming or Relax Gaming": "초고 변동성 슬롯: Hacksaw Gaming 또는 Relax Gaming",
    "For the broadest regulatory approval record: Play'n GO or NetEnt": "가장 광범위한 규제 승인 기록: Play'n GO 또는 NetEnt",
    "For crypto-native play: BGaming": "크립토 네이티브 플레이: BGaming",
    "Portfolio size comparison": "포트폴리오 크기 비교",
    "How to access all providers at 1win with XLBONUS": "XLBONUS로 1win의 모든 제공업체에 접근하는 방법",
    "Choosing a provider: what differentiates each studio": "제공업체 선택: 각 스튜디오를 차별화하는 것",
    "1win Australia: overview": "1win 호주: 개요",  # approximate
    "1win Malawi: Airtel Money cash in and XLBONUS for sports": "1win 말라위: Airtel Money 입금 및 스포츠를 위한 XLBONUS",
    "Access 1win Malawi": "1win 말라위 접속",
    "Deposit via local Malawi payment methods": "현지 말라위 결제 수단으로 입금",
    "1WIN MALAWI PROMO CODE": "1WIN 말라위 프로모 코드",
    "Airtel Money": "Airtel Money",
    "TNM Mpamba / M-Pesa": "TNM Mpamba / M-Pesa",
    "National Bank / Standard Bank": "내셔널 뱅크 / 스탠다드 뱅크",
    "Is Teen Patti available at 1win Malawi?": "1win 말라위에서 틴 파티를 이용할 수 있나요?",
    "1win Malaysia: MYR play, Touch n Go deposits and XLBONUS": "1win 말레이시아: MYR 플레이, Touch n Go 입금 및 XLBONUS",
    "Access 1win Malaysia": "1win 말레이시아 접속",
    "Deposit via local Malaysia payment methods": "현지 말레이시아 결제 수단으로 입금",
    "1WIN MALAYSIA PROMO CODE": "1WIN 말레이시아 프로모 코드",
    "Touch'n Go eWallet": "Touch'n Go 이월렛",
    "Maybank2u / FPX": "Maybank2u / FPX",
    "Is Teen Patti available at 1win Malaysia?": "1win 말레이시아에서 틴 파티를 이용할 수 있나요?",
    "1win Singapore: SGD play, F1 markets and XLBONUS for casino": "1win 싱가포르: SGD 플레이, F1 마켓 및 카지노를 위한 XLBONUS",
    "Access 1win Singapore": "1win 싱가포르 접속",
    "Deposit via local Singapore payment methods": "현지 싱가포르 결제 수단으로 입금",
    "1WIN SINGAPORE PROMO CODE": "1WIN 싱가포르 프로모 코드",
    "DBS PayLah!": "DBS PayLah!",
    "GrabPay / NETS": "GrabPay / NETS",
    "Is Teen Patti available at 1win Singapore?": "1win 싱가포르에서 틴 파티를 이용할 수 있나요?",
    "1win South Africa: ZAR play, PSL markets and the XLBONUS code": "1win 남아프리카: ZAR 플레이, PSL 마켓 및 XLBONUS 코드",
    "Access 1win South Africa": "1win 남아프리카 접속",
    "Deposit via local South Africa payment methods": "현지 남아프리카 결제 수단으로 입금",
    "1WIN SOUTH AFRICA PROMO CODE": "1WIN 남아프리카 프로모 코드",
    "FNB eWallet": "FNB 이월렛",
    "Capitec Pay / EasyEFT": "Capitec Pay / EasyEFT",
    "Ozow / 1Voucher": "Ozow / 1Voucher",
    "Is Teen Patti available at 1win South Africa?": "1win 남아프리카에서 틴 파티를 이용할 수 있나요?",
    "1win Tanzania: M-Pesa cash in and XLBONUS for sports": "1win 탄자니아: M-Pesa 입금 및 스포츠를 위한 XLBONUS",
    "Access 1win Tanzania": "1win 탄자니아 접속",
    "Deposit via local Tanzania payment methods": "현지 탄자니아 결제 수단으로 입금",
    "1WIN TANZANIA PROMO CODE": "1WIN 탄자니아 프로모 코드",
    "Tigo Pesa / Airtel Money": "Tigo Pesa / Airtel Money",
    "CRDB Bank / NMB Bank": "CRDB 은행 / NMB 은행",
    "Is Teen Patti available at 1win Tanzania?": "1win 탄자니아에서 틴 파티를 이용할 수 있나요?",
    "Complete email/phone verification. 1win will send a code via SMS or email; enter it to confirm.":
        "이메일/전화 인증 완료. 1win이 SMS 또는 이메일로 코드를 보내드립니다. 확인을 위해 입력하세요.",
    "Receive your 600% welcome bonus. Bonus funds appear in your 1win bonus balance within seconds. The 600% is split across four qualifying deposits.":
        "600% 환영 보너스를 받으세요. 보너스 자금이 몇 초 안에 1win 보너스 잔액에 나타납니다. 600%는 네 번의 적격 입금에 걸쳐 분할됩니다.",
    "Complete KYC if required. 1win may require identity verification before large crypto withdrawals.":
        "필요한 경우 KYC를 완료하세요. 1win은 대규모 암호화폐 출금 전에 신원 확인을 요구할 수 있습니다.",
    "Enter the withdrawal amount. 1win deducts a network fee from the amount to cover on-chain transaction costs.":
        "출금 금액을 입력하세요. 1win은 온체인 거래 비용을 충당하기 위해 금액에서 네트워크 수수료를 공제합니다.",
}

# ── Substring-based paragraph replacements (for sentences within paragraphs) ──
# These are applied to the full file content, not just exact matches
SUBSTRING_TRANSLATIONS = [
    # Common UI phrases
    ("Use promo code XLBONUS for a 600% welcome bonus.", "프로모 코드 XLBONUS를 사용하면 600% 환영 보너스를 받을 수 있습니다."),
    ("프로모 코드 XLBONUS for a 600% welcome bonus.", "프로모 코드 XLBONUS로 600% 환영 보너스를 받으세요."),
    ("Enter XLBONUS during registration", "가입 시 XLBONUS를 입력하세요"),
    ("Enter XLBONUS at registration", "가입 시 XLBONUS를 입력하세요"),
    ("Use code XLBONUS", "코드 XLBONUS를 사용하세요"),
    ("Use XLBONUS when registering", "가입 시 XLBONUS를 사용하세요"),
    ("with code XLBONUS", "코드 XLBONUS로"),
    ("promo code XLBONUS", "프로모 코드 XLBONUS"),
    # Deposit/withdrawal common phrases
    ("Go to the Cashier section", "캐셔 섹션으로 이동하세요"),
    ("Navigate to the Cashier", "캐셔로 이동하세요"),
    ("Go to Cashier", "캐셔로 이동"),
    ("instant deposits", "즉시 입금"),
    ("instant withdrawals", "즉시 출금"),
    ("no fees", "수수료 없음"),
    ("zero fees", "수수료 없음"),
    ("minimum deposit", "최소 입금액"),
    ("minimum withdrawal", "최소 출금액"),
    # Sports betting terms
    ("live in-play betting", "라이브 인플레이 베팅"),
    ("in-play betting", "인플레이 베팅"),
    ("pre-match betting", "경기 전 베팅"),
    ("competitive odds", "경쟁력 있는 배당률"),
    ("extensive markets", "광범위한 마켓"),
    ("sportsbook", "스포츠북"),
    ("bet builder", "베팅 빌더"),
    ("cash out", "현금 인출"),
    ("live streaming", "라이브 스트리밍"),
    # Registration
    ("register in seconds", "몇 초 만에 가입"),
    ("sign up in 30 seconds", "30초 만에 가입"),
    ("no VPN required", "VPN 필요 없음"),
    ("no VPN needed", "VPN 필요 없음"),
    # Casino terms
    ("free spins", "무료 스핀"),
    ("welcome bonus", "환영 보너스"),
    ("wagering requirement", "베팅 요건"),
    ("progressive jackpot", "프로그레시브 잭팟"),
    ("live dealer", "라이브 딜러"),
    ("slot games", "슬롯 게임"),
    ("table games", "테이블 게임"),
    ("crash games", "크래시 게임"),
    ("responsible gambling", "책임감 있는 도박"),
    # Countries (for ISP block descriptions)
    ("ISP blocks", "ISP 차단"),
    ("ISP-level blocks", "ISP 수준의 차단"),
    ("mirror links", "미러 링크"),
    ("mirror link", "미러 링크"),
    ("working mirror", "작동하는 미러"),
    ("alternative link", "대체 링크"),
    # Crypto
    ("cryptocurrency", "암호화폐"),
    ("crypto deposits", "암호화폐 입금"),
    ("crypto withdrawals", "암호화폐 출금"),
    ("blockchain", "블록체인"),
    ("provably fair", "공정성 증명"),
    # Common sentence fragments
    ("Click the registration link on this page", "이 페이지의 가입 링크를 클릭하세요"),
    ("all accessible in", "에서 모두 이용 가능합니다"),
    ("no VPN required", "VPN 필요 없음"),
    ("Curaçao gaming license", "Curaçao 게임 라이선스"),
    ("gaming license", "게임 라이선스"),
    ("customer support", "고객 지원"),
    ("account manager", "계정 매니저"),
    ("VIP members", "VIP 회원"),
    ("VIP club", "VIP 클럽"),
    ("Play responsibly", "책임감 있게 플레이하세요"),
    ("gamble responsibly", "책임감 있게 베팅하세요"),
    ("age verification", "나이 확인"),
    ("identity verification", "신원 확인"),
    ("KYC verification", "KYC 인증"),
    ("two-factor authentication", "이중 인증"),
    ("SSL encryption", "SSL 암호화"),
]


def translate_exact_para(text):
    """Try exact match for paragraph content."""
    stripped = text.strip()
    if stripped in PARA_EXACT:
        return PARA_EXACT[stripped]
    return None


def translate_exact_heading(text):
    """Try exact match for heading content."""
    stripped = text.strip()
    if stripped in HEADING_EXACT:
        return HEADING_EXACT[stripped]
    return None


def apply_substring_translations(content):
    """Apply substring-level translations to content."""
    for en, ko in SUBSTRING_TRANSLATIONS:
        content = content.replace(en, ko)
    return content


def translate_paragraph_tag(match):
    """Replace paragraph content if we have an exact translation."""
    full_match = match.group(0)
    # Extract text content
    inner = match.group(1)
    inner_text = re.sub(r'<[^>]+>', '', inner).strip()
    
    ko = translate_exact_para(inner_text)
    if ko:
        # Preserve any wrapping tags in the <p> opening
        p_open = re.match(r'<p[^>]*>', full_match).group(0)
        return f'{p_open}{ko}</p>'
    return full_match


def translate_heading_tag(match):
    """Replace heading content if we have an exact translation."""
    full_match = match.group(0)
    tag = match.group(1)
    inner = match.group(2)
    inner_text = re.sub(r'<[^>]+>', '', inner).strip()
    
    ko = translate_exact_heading(inner_text)
    if ko:
        h_open = re.match(r'<h[1-6][^>]*>', full_match).group(0)
        return f'{h_open}{ko}</{tag}>'
    return full_match


def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Apply exact paragraph translations
    content = re.sub(
        r'<p[^>]*>(.*?)</p>',
        translate_paragraph_tag,
        content,
        flags=re.DOTALL
    )
    
    # Apply exact heading translations
    content = re.sub(
        r'<(h[1-6])[^>]*>(.*?)</\1>',
        translate_heading_tag,
        content,
        flags=re.DOTALL
    )
    
    # Apply substring translations
    content = apply_substring_translations(content)
    
    return content, content != original


def main():
    files = glob.glob(os.path.join(KO_DIR, '**/*.html'), recursive=True)
    print(f"Processing {len(files)} files...")
    
    updated = 0
    para_hits = 0
    heading_hits = 0
    
    for filepath in files:
        content, changed = process_file(filepath)
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
    
    print(f"Updated {updated}/{len(files)} files")


if __name__ == '__main__':
    main()

# This will be imported by the extended translation module
