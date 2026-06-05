#!/usr/bin/env python3
"""
Korean translation batch 2 — comprehensive paragraph/li/heading translations.
Covers all remaining untranslated content from /tmp/untranslated_ko.txt
"""
import os, re
from bs4 import BeautifulSoup, NavigableString

KO_DIR = '/home/user/workspace/1win-codes-repo/ko'

# ─── EXACT PARAGRAPH TRANSLATIONS ───────────────────────────────────────────

PARA_EXACT = {
    # === WELCOME BONUS / PROMO CODE ===
    "After your first deposit, make three additional qualifying deposits to receive the remaining bonus tiers: 140% on the second, 160% on the third, and 170% on the fourth. Each bonus is credited after each deposit. The total of 130+140+160+170 = 600% represents the full XLBONUS welcome package.":
        "첫 입금 후 추가로 3회의 적격 입금을 하시면 나머지 보너스를 받을 수 있습니다: 2번째 입금 시 140%, 3번째 입금 시 160%, 4번째 입금 시 170%. 각 보너스는 해당 입금 후 즉시 지급됩니다. 130+140+160+170 = 600%의 합계가 XLBONUS 웰컴 패키지 전체 금액입니다.",
    "Step 2, Choose your registration method.Select from: Quick Registration (country + currency + password), Phone (enter mobile number, verify with SMS code), Email (email address + password), or Social Media (Google or Facebook one-click). All methods create a full 1win account with identical access to all platform features and bonuses.":
        "2단계: 가입 방법을 선택하세요. 빠른 가입(국가 + 통화 + 비밀번호), 전화번호(휴대폰 번호 입력 후 SMS 인증), 이메일(이메일 주소 + 비밀번호), 소셜 미디어(Google 또는 Facebook 원클릭) 중 선택하실 수 있습니다. 모든 방법으로 가입하면 동일한 1win 계정이 생성되며, 모든 플랫폼 기능과 보너스에 동일하게 접근할 수 있습니다.",
    "Your second qualifying deposit earns a 140% match. At this point, the cumulative bonus value across both deposits already exceeds what most online betting sites offer in their entire welcome package. The 140% tier applies regardless of whether you deposit more or less than your first deposit.":
        "두 번째 적격 입금 시 140% 매칭 보너스를 받습니다. 이 시점에서 두 번의 입금에 걸친 누적 보너스 가치는 대부분의 온라인 베팅 사이트가 전체 웰컴 패키지로 제공하는 것을 이미 초과합니다. 140% 단계는 첫 입금보다 많거나 적게 입금하든 관계없이 적용됩니다.",
    "The third qualifying deposit brings a 160% match bonus. This tier delivers significantly more bonus value per dollar deposited than typical industry standards. Combined with your first two deposit bonuses, the cumulative effect at this stage is already 430%, before the final tier is applied.":
        "세 번째 적격 입금 시 160% 매칭 보너스를 받습니다. 이 단계는 업계 평균보다 입금액당 훨씬 더 많은 보너스 가치를 제공합니다. 첫 두 번의 입금 보너스와 결합하면, 마지막 단계 적용 전 이미 누적 효과가 430%에 달합니다.",
    "1win is available globally. Select your country for a dedicated guide with local payment methods, sports, and registration instructions.":
        "1win은 전 세계적으로 이용 가능합니다. 해당 국가를 선택하시면 현지 결제 수단, 스포츠, 가입 안내가 포함된 전용 가이드를 제공해 드립니다.",
    "This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk, please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.":
        "이 사이트는 비공식 팬 사이트이며, 1win과 제휴 관계에 있지 않고 1win의 승인을 받지 않았습니다. 이 사이트는 정보 제공 목적으로만 운영됩니다. 도박에는 위험이 따르므로 책임감 있게 플레이하시기 바랍니다. 도박 문제가 있으신 분은 GamCare 또는 현지 지원 기관에 문의하시기 바랍니다.",
    "Select one-click (fastest), phone number, email, or social media registration. All methods create an identical full account with access to all 1win products and bonuses.":
        "원클릭(가장 빠름), 전화번호, 이메일 또는 소셜 미디어 가입 방법 중 하나를 선택하세요. 모든 방법으로 동일한 완전한 계정을 생성하며, 모든 1win 상품과 보너스에 접근할 수 있습니다.",
    # === LOGIN / ACCESS ===
    "Aviator is one of the most popular games at 1win and is available immediately after logging in to your account. Once logged in, navigate to the Casino section and search for \"Aviator\", or find it in the Crash Games category. The game is available on desktop and mobile browsers as well as the 1win app.":
        "Aviator는 1win에서 가장 인기 있는 게임 중 하나로, 계정 로그인 즉시 플레이할 수 있습니다. 로그인 후 카지노 섹션으로 이동해 'Aviator'를 검색하거나, 크래시 게임 카테고리에서 찾을 수 있습니다. 이 게임은 PC와 모바일 브라우저, 그리고 1win 앱에서 모두 이용 가능합니다.",
    "Log in to 1win from your phone, tablet, or desktop. The full platform is available on all devices.":
        "스마트폰, 태블릿 또는 PC에서 1win에 로그인하세요. 모든 기기에서 전체 플랫폼을 이용할 수 있습니다.",
    "Download the 1win app for the most reliable login experience on mobile, no mirror required.":
        "모바일에서 가장 안정적인 로그인 경험을 위해 1win 앱을 다운로드하세요. 미러 사이트가 필요 없습니다.",
    "Click \"Forgot Password\" on the 1win login screen. If you registered by phone, you will receive an SMS verification code to reset your password. If you registered by email, a password reset link will be sent to your inbox. If you registered via social media (Google or Facebook), simply log in using that social account, no password is required for social login.":
        "1win 로그인 화면에서 '비밀번호 분실'을 클릭하세요. 전화번호로 가입하셨다면 비밀번호 재설정을 위한 SMS 인증 코드를 받으실 것입니다. 이메일로 가입하셨다면 비밀번호 재설정 링크가 이메일로 발송됩니다. 소셜 미디어(Google 또는 Facebook)로 가입하셨다면, 해당 소셜 계정으로 로그인하시면 됩니다. 소셜 로그인에는 비밀번호가 필요 없습니다.",
    # === ACCESS / MIRROR ===
    "In many countries, internet service providers (ISPs) are required by local regulations to block access to online betting platforms. When an ISP applies a DNS-level block to 1win.pro, your browser simply cannot reach the site, you see a connection error or a blank page. This is not a fault of 1win; it is a network-level restriction applied by your ISP or government.":
        "많은 국가에서 인터넷 서비스 제공업체(ISP)는 현지 규정에 따라 온라인 베팅 플랫폼에 대한 접근을 차단해야 합니다. ISP가 1win.pro에 DNS 수준 차단을 적용하면 브라우저에서 사이트에 접근할 수 없게 되어 연결 오류 또는 빈 페이지가 표시됩니다. 이는 1win의 잘못이 아니라, ISP 또는 정부가 네트워크 수준에서 적용한 제한입니다.",
    "How the three main access methods compare across every factor that matters.":
        "주요 3가지 접근 방법을 모든 관련 요소에서 비교합니다.",
    # === APP ===
    "Open the app, register with codeXLBONUS, and start betting with 600% bonus.":
        "앱을 열고 코드 XLBONUS로 가입한 후 600% 보너스로 베팅을 시작하세요.",
    "The app is engineered specifically for the demands of mobile betting, a context where speed and responsiveness are critical. Live betting requires odds that refresh without noticeable lag, cash-out buttons that respond to touch instantly, and interfaces that remain stable and readable under the stress of fast-moving events. The 1win app meets these requirements with a native architecture (rather than a browser wrapper) that provides the same performance as a desktop session. Face ID and fingerprint biometric login are supported on compatible devices, removing the friction of password entry during fast-paced betting sessions.":
        "이 앱은 속도와 반응성이 매우 중요한 모바일 베팅의 요구에 맞게 특별히 설계되었습니다. 라이브 베팅은 지연 없이 실시간으로 갱신되는 배당률, 즉각적으로 반응하는 캐시아웃 버튼, 빠르게 변화하는 이벤트 상황에서도 안정적이고 읽기 쉬운 인터페이스를 필요로 합니다. 1win 앱은 브라우저 래퍼가 아닌 네이티브 아키텍처로 구축되어 데스크탑과 동일한 성능을 제공합니다. 호환 기기에서는 Face ID 및 지문 생체인식 로그인을 지원하여 빠른 베팅 중 비밀번호 입력 과정을 줄여줍니다.",
    "Push notifications are one of the app's most valued features for active bettors. You can configure notifications for price boosts on upcoming events, results alerts for matches you have bets on, new bonus offers and promotional events, and Aviator jackpot announcements. This means the app works proactively to surface betting opportunities and account-relevant information without requiring you to open the platform and search manually. For casino players, new game release notifications keep you up to date with the latest additions from major providers.":
        "푸시 알림은 활발히 베팅하는 사용자들에게 가장 유용한 앱 기능 중 하나입니다. 예정된 이벤트의 가격 인상 알림, 베팅한 경기 결과 알림, 새로운 보너스 제안 및 프로모션 이벤트, Aviator 잭팟 공지 등을 설정할 수 있습니다. 이 기능으로 플랫폼을 직접 열어 검색하지 않아도 베팅 기회와 계정 관련 정보를 능동적으로 제공받을 수 있습니다. 카지노 플레이어에게는 새 게임 출시 알림이 주요 공급업체의 최신 추가 게임 정보를 전달합니다.",
    "Download the app and register with XLBONUS for up to 600% on your first deposit. Bet on the go.":
        "앱을 다운로드하고 XLBONUS로 가입하여 첫 입금 시 최대 600% 보너스를 받으세요. 언제 어디서나 베팅하세요.",
    "Yes. The 1win app is completely free to download and use on both iOS and Android. There are no subscription fees or in-app purchases required to access any features.":
        "네. 1win 앱은 iOS와 Android 모두에서 완전히 무료로 다운로드하고 사용할 수 있습니다. 모든 기능에 접근하는 데 구독료나 인앱 구매가 필요하지 않습니다.",
    "Yes. The APK is the official 1win application. Download only from the official 1win website to ensure authenticity. The app uses the same security standards as the website.":
        "네. APK는 공식 1win 애플리케이션입니다. 정품을 보장하기 위해 공식 1win 웹사이트에서만 다운로드하세요. 앱은 웹사이트와 동일한 보안 기준을 사용합니다.",
    "The app requires approximately 100MB of storage space. It's optimized for performance and battery life, running smoothly even on older devices.":
        "앱은 약 100MB의 저장 공간이 필요합니다. 구형 기기에서도 원활하게 실행될 수 있도록 성능과 배터리 수명에 최적화되어 있습니다.",
    "This is a fan-made informational site about 1win. Not affiliated with 1win. Gambling involves risk. Only gamble with money you can afford to lose. If you have a gambling problem, please seek help. Must be 18+ to participate.":
        "이 사이트는 1win에 관한 팬 제작 정보 사이트입니다. 1win과 제휴 관계가 없습니다. 도박에는 위험이 따릅니다. 잃어도 감당할 수 있는 금액으로만 도박하세요. 도박 문제가 있으시면 도움을 받으시기 바랍니다. 18세 이상만 참여 가능합니다.",
    # === AVIATOR ===
    "Hit the cash-out button before the plane crashes. Your bet is multiplied by the current multiplier. Miss it, and you lose your stake.":
        "비행기가 추락하기 전에 캐시아웃 버튼을 누르세요. 베팅 금액은 현재 배수로 곱해집니다. 놓치면 베팅 금액을 잃게 됩니다.",
    "Set the number of rounds, bet amount, and let it run. The system places bets automatically every round so you never miss the action.":
        "라운드 수와 베팅 금액을 설정하면 시스템이 자동으로 매 라운드마다 베팅을 진행합니다. 액션을 절대 놓치지 마세요.",
    "Set your target multiplier (e.g. 2.00x) and the system cashes out automatically when it's reached. Remove human emotion from the equation.":
        "목표 배수(예: 2.00x)를 설정하면 시스템이 해당 배수에 도달했을 때 자동으로 캐시아웃합니다. 감정에 좌우되지 않는 베팅이 가능합니다.",
    "Playing Aviator at 1win gives you access to the full feature set: dual simultaneous bets, auto-bet and auto-cashout configuration, real-time chat with other players, and a live history panel showing recent round results. The dual-bet feature is particularly valued by experienced players, as it allows you to run one conservative bet with a fixed low multiplier auto-cashout (such as 1.5x) and one aggressive bet held for a higher target. This combination provides a consistent small income stream from the first bet while leaving the second bet open for the high-multiplier outcomes that produce outsized gains.":
        "1win에서 Aviator를 플레이하면 모든 기능에 접근할 수 있습니다: 동시 이중 베팅, 자동 베팅 및 자동 캐시아웃 설정, 다른 플레이어와의 실시간 채팅, 최근 라운드 결과를 보여주는 실시간 기록 패널. 이중 베팅 기능은 경험 많은 플레이어들이 특히 선호합니다. 고정된 낮은 배수(예: 1.5x) 자동 캐시아웃으로 보수적인 첫 번째 베팅을 유지하면서, 두 번째 베팅은 더 높은 목표를 위해 열어두는 방식입니다. 이 조합은 첫 번째 베팅에서 안정적인 소득을 창출하면서 두 번째 베팅에서 큰 수익을 노릴 수 있게 합니다.",
    "Yes. Every round of Aviator uses a SHA-256 cryptographic hash that can be independently verified. The crash point is determined before the round starts and cannot be manipulated. You can audit any round result using the seed and hash provided.":
        "네. Aviator의 모든 라운드는 독립적으로 검증할 수 있는 SHA-256 암호화 해시를 사용합니다. 크래시 포인트는 라운드 시작 전에 결정되며 조작할 수 없습니다. 제공된 시드와 해시를 사용하여 라운드 결과를 검증할 수 있습니다.",
    "The theoretical maximum multiplier can reach extremely high levels. The highest recorded multiplier on 1win is 47,000x. With even a small bet, this represents a massive potential payout.":
        "이론적 최대 배수는 매우 높은 수준에 달할 수 있습니다. 1win에서 기록된 최고 배수는 47,000x입니다. 소액 베팅으로도 막대한 잠재적 수익을 얻을 수 있습니다.",
    "Yes. Aviator is fully optimized for mobile play on both the 1win app (iOS/Android) and mobile browser. The touch-based cash-out button is responsive and designed for fast-paced gameplay.":
        "네. Aviator는 1win 앱(iOS/Android)과 모바일 브라우저 모두에서 모바일 플레이에 최적화되어 있습니다. 터치 기반 캐시아웃 버튼은 빠른 게임플레이에 맞게 즉각 반응하도록 설계되었습니다.",
    "Aviator round statistics - last 100 rounds, sample":
        "Aviator 라운드 통계 - 최근 100라운드 샘플",
    # === BANGLADESH ===
    "Select Quick registration (fastest), Phone number, or Social media login. Quick registration requires only your country (Bangladesh), preferred currency (BDT), and a password.":
        "빠른 가입(가장 빠름), 전화번호 또는 소셜 미디어 로그인 중 선택하세요. 빠른 가입은 국가(방글라데시), 선호 통화(BDT), 비밀번호만 필요합니다.",
    "1win Bangladesh supports a comprehensive range of local and international payment methods, making it easy to fund your account and withdraw winnings in Bangladeshi Taka. The platform has integrated with the most widely used mobile financial services in Bangladesh to ensure accessible banking for all players.":
        "1win 방글라데시는 현지 및 국제 결제 수단을 폭넓게 지원하여 방글라데시 타카(BDT)로 계정 충전과 출금을 쉽게 할 수 있습니다. 모든 플레이어가 편리하게 이용할 수 있도록 방글라데시에서 가장 널리 사용되는 모바일 금융 서비스와 통합되어 있습니다.",
    "Bangladesh's most popular mobile banking service. Fast, secure deposits directly from your bKash wallet.":
        "방글라데시에서 가장 인기 있는 모바일 뱅킹 서비스입니다. bKash 지갑에서 빠르고 안전하게 입금할 수 있습니다.",
    "Government-backed mobile financial service. Widely used across Bangladesh for instant transfers.":
        "정부 지원 모바일 금융 서비스입니다. 즉시 송금을 위해 방글라데시 전역에서 널리 사용됩니다.",
    "Dutch-Bangla Bank's mobile banking product. Available to millions of Bangladeshi users.":
        "Dutch-Bangla Bank의 모바일 뱅킹 서비스입니다. 수백만 명의 방글라데시 사용자가 이용하고 있습니다.",
    "Bitcoin, Ethereum, USDT and other major cryptocurrencies accepted. Fast processing, low fees.":
        "비트코인, 이더리움, USDT 및 기타 주요 암호화폐를 지원합니다. 빠른 처리, 낮은 수수료.",
    "Direct bank-to-bank transfers supported. Ideal for larger deposit amounts.":
        "직접 은행 간 이체를 지원합니다. 대금액 입금에 적합합니다.",
    "Visa and Mastercard accepted. International card payments processed securely.":
        "Visa 및 Mastercard를 지원합니다. 국제 카드 결제를 안전하게 처리합니다.",
    "1win fully supports Bangladeshi Taka (BDT). Deposits, withdrawals, and account balances are displayed in BDT. No currency conversion is required for Bangladeshi players.":
        "1win은 방글라데시 타카(BDT)를 완전히 지원합니다. 입금, 출금 및 계정 잔액이 BDT로 표시됩니다. 방글라데시 플레이어는 환전이 필요하지 않습니다.",
    # === BRAZIL ===
    "Go to the Cashier and select Pix. Enter the amount and complete the instant transfer using your bank or Pix-enabled app. Your bonus is applied automatically after the first qualifying deposit.":
        "계좌로 이동하여 Pix를 선택하세요. 금액을 입력하고 은행 앱 또는 Pix 지원 앱을 사용하여 즉시 이체를 완료하세요. 첫 번째 적격 입금 후 보너스가 자동으로 적용됩니다.",
    "1win Brazil has integrated with Brazil's modern payment infrastructure, making deposits and withdrawals fast and free for Brazilian players. Pix is the standout option, instant, free, and available 24/7.":
        "1win 브라질은 브라질의 현대적인 결제 인프라와 통합되어 브라질 플레이어의 입출금을 빠르고 무료로 제공합니다. Pix는 즉시, 무료, 24/7 이용 가능한 최고의 옵션입니다.",
    "Direct bank transfers from Brazilian bank accounts. Supported with all major Brazilian banks.":
        "브라질 은행 계좌에서 직접 은행 이체를 지원합니다. 모든 주요 브라질 은행과 호환됩니다.",
    "Cryptocurrency option. Popular with Brazilian players for fast, borderless transactions.":
        "암호화폐 옵션입니다. 빠르고 국경 없는 거래로 브라질 플레이어들에게 인기입니다.",
    "USD-pegged stablecoin. Protects against BRL currency fluctuation for larger transactions.":
        "USD 연동 스테이블코인입니다. 대규모 거래 시 BRL 환율 변동으로부터 보호합니다.",
    "ETH deposits and withdrawals available. Fast processing with reliable liquidity.":
        "ETH 입출금이 가능합니다. 안정적인 유동성으로 빠른 처리가 가능합니다.",
    "Brazilian bank payment slip. Available for players without a bank account or who prefer offline payment.":
        "브라질 은행 결제 전표입니다. 은행 계좌가 없거나 오프라인 결제를 선호하는 플레이어에게 제공됩니다.",
    "Football is Brazil's national religion, and 1win delivers the deepest Brasileirão coverage available. All Serie A and Serie B matches are available with pre-match and live in-play markets. The top clubs, Flamengo, Palmeiras, Corinthians, São Paulo, and Santos, attract the highest betting volumes. The Copa do Brasil knockout tournament adds significant action throughout the season.":
        "축구는 브라질의 국민 스포츠이며, 1win은 가장 심층적인 브라질레이라웅 커버리지를 제공합니다. 모든 세리에 A 및 세리에 B 경기를 사전 베팅 및 라이브 인플레이 시장으로 이용할 수 있습니다. 플라멩구, 팔메이라스, 코린티안스, 상파울루, 산투스 등 최고의 클럽들이 가장 높은 베팅 볼륨을 끌어냅니다. 코파 두 브라질 토너먼트는 시즌 내내 풍성한 베팅 기회를 제공합니다.",
    "MMA is enormously popular in Brazil. 1win covers every UFC event with full card betting including main event, co-main, and undercard bouts. Brazilian fighters dominate the UFC pound-for-pound rankings, and local fans can bet on their heroes with 1win's competitive MMA odds. Volleyball, another Brazilian sporting passion, is available with Superliga coverage and international competition markets.":
        "MMA는 브라질에서 매우 인기가 높습니다. 1win은 메인 이벤트, 코메인, 언더카드 경기 등 모든 UFC 이벤트를 전체 카드 베팅으로 커버합니다. 브라질 선수들이 UFC 파운드-포-파운드 랭킹을 지배하고 있으며, 현지 팬들은 1win의 경쟁력 있는 MMA 배당률로 자신들의 영웅에게 베팅할 수 있습니다. 또 다른 브라질의 스포츠 열정인 배구도 슈퍼리가 커버리지와 국제 대회 시장을 이용할 수 있습니다.",
    "Yes. 1win is fully accessible in Brazil and accepts BRL deposits and withdrawals. Pix is available as the primary payment method for instant, free transactions.":
        "네. 1win은 브라질에서 완전히 이용 가능하며 BRL 입출금을 지원합니다. Pix는 즉시 무료 거래를 위한 주요 결제 수단으로 제공됩니다.",
    # === GHANA ===
    "1win Ghana brings Ghanaian players an international-standard betting platform with deep coverage of the sports and events most popular in Ghana. Football dominates the platform's Ghanaian offering, with full coverage of the Ghana Premier League, the Black Stars' international fixtures, AFCON qualifiers, and all major European leagues. The platform supports Ghanaian Cedi (GHS) and integrates with MTN MoMo and Vodafone Cash for fast, convenient mobile money payments.":
        "1win 가나는 가나 플레이어에게 국제 수준의 베팅 플랫폼을 제공하며, 가나에서 가장 인기 있는 스포츠와 이벤트를 심층적으로 커버합니다. 축구가 플랫폼의 가나 서비스를 지배하며, 가나 프리미어 리그, 블랙스타즈 국제 경기, AFCON 예선, 모든 주요 유럽 리그를 완전히 커버합니다. 플랫폼은 가나 세디(GHS)를 지원하며, 빠르고 편리한 모바일 머니 결제를 위해 MTN MoMo 및 Vodafone Cash와 통합되어 있습니다.",
    "Follow the registration link on this page to access the 1win platform. Registration is open to all Ghanaian players.":
        "이 페이지의 가입 링크를 통해 1win 플랫폼에 접근하세요. 모든 가나 플레이어의 가입이 가능합니다.",
    "Visit the Cashier and select your preferred mobile money method. Follow the on-screen instructions to complete your first deposit and receive your bonus instantly.":
        "계좌 페이지로 이동하여 선호하는 모바일 머니 방법을 선택하세요. 화면 안내에 따라 첫 입금을 완료하고 보너스를 즉시 받으세요.",
    "1win Ghana supports the most popular mobile money platforms in Ghana alongside international payment options. Deposits are processed quickly and withdrawals are reliable across all supported methods.":
        "1win 가나는 국제 결제 옵션과 함께 가나에서 가장 인기 있는 모바일 머니 플랫폼을 지원합니다. 모든 지원 방법에서 입금은 빠르게 처리되고 출금은 안정적입니다.",
    "Ghana's most widely used mobile money platform. Fast deposits and withdrawals directly from your MTN wallet.":
        "가나에서 가장 널리 사용되는 모바일 머니 플랫폼입니다. MTN 지갑에서 직접 빠르게 입출금할 수 있습니다.",
    "Telecom-linked mobile money service. Instant transfers with broad network coverage across Ghana.":
        "통신사 연동 모바일 머니 서비스입니다. 가나 전역 광범위한 네트워크로 즉시 이체가 가능합니다.",
    "Direct bank-to-bank transfers in GHS. Available from major Ghanaian commercial and universal banks.":
        "GHS로 직접 은행 간 이체를 지원합니다. 주요 가나 상업은행 및 유니버설 뱅크에서 이용 가능합니다.",
    "Cryptocurrency option for fast, borderless transactions. Ideal for large deposit amounts.":
        "빠르고 국경 없는 거래를 위한 암호화폐 옵션입니다. 대금액 입금에 이상적입니다.",
    "Stablecoin option. Pegged to USD value for currency-stable transactions.":
        "스테이블코인 옵션입니다. 통화 안정적인 거래를 위해 USD 가치에 연동됩니다.",
    "International debit and credit card payments. Processed securely with full encryption.":
        "국제 직불 및 신용카드 결제를 지원합니다. 완전한 암호화로 안전하게 처리됩니다.",
    "Major European leagues, the English Premier League, La Liga, Bundesliga, Ligue 1, and Serie A, attract strong betting volumes from Ghanaian players. The UEFA Champions League and Europa League are available with boosted odds on knockout matches and finals.":
        "영국 프리미어 리그, 라 리가, 분데스리가, 리그 1, 세리에 A 등 주요 유럽 리그는 가나 플레이어로부터 강한 베팅 볼륨을 유도합니다. UEFA 챔피언스 리그와 유로파 리그는 녹아웃 경기 및 결승전에서 배당률 상향 서비스를 제공합니다.",
    "The 1win casino offers Ghanaian players a rich selection of games. Live dealer roulette, blackjack, and baccarat operate continuously with professional dealers. The slot catalogue covers 12,000+ titles across all volatility levels. The Aviator crash game is particularly popular among Ghanaian users for its simplicity, fast rounds, and potential for high multipliers.":
        "1win 카지노는 가나 플레이어에게 다양한 게임을 제공합니다. 프로 딜러와 함께하는 라이브 딜러 룰렛, 블랙잭, 바카라가 24시간 운영됩니다. 슬롯 카탈로그는 모든 변동성 수준에서 12,000개 이상의 타이틀을 제공합니다. Aviator 크래시 게임은 간편함, 빠른 라운드, 높은 배수 가능성으로 가나 사용자들에게 특히 인기가 높습니다.",
    "Log in to 1win, go to the Cashier section, select MTN MoMo, enter the deposit amount, and complete the transaction using your MTN mobile money PIN. Deposits are credited instantly.":
        "1win에 로그인하고 계좌 섹션으로 이동하여 MTN MoMo를 선택하세요. 입금 금액을 입력하고 MTN 모바일 머니 PIN으로 거래를 완료하세요. 입금은 즉시 처리됩니다.",
    # === INDIA ===
    "1win India is built for the world's largest cricket market. With comprehensive coverage of the Indian Premier League (IPL), ICC World Cup tournaments, bilateral series involving the Indian national team, and domestic competitions, 1win delivers more cricket betting markets than virtually any other international platform accessible to Indian players. The platform supports Indian Rupee (INR) and integrates with UPI, Paytm, and PhonePe, the payment methods used by 12,000+ millions of Indians daily.":
        "1win 인도는 세계 최대의 크리켓 시장을 위해 구축되었습니다. 인디언 프리미어 리그(IPL), ICC 월드컵 토너먼트, 인도 국가대표팀 관련 양자 시리즈, 국내 대회를 종합적으로 커버하며, 인도 플레이어가 접근 가능한 거의 모든 국제 플랫폼보다 더 많은 크리켓 베팅 시장을 제공합니다. 플랫폼은 인도 루피(INR)를 지원하며 수백만 명의 인도인이 매일 사용하는 결제 수단인 UPI, Paytm, PhonePe와 통합되어 있습니다.",
    "1win India offers the widest range of Indian payment methods of any international operator, including the most popular UPI apps and digital wallets used by Indian players daily.":
        "1win 인도는 모든 국제 운영업체 중 가장 다양한 인도 결제 수단을 제공하며, 인도 플레이어가 매일 사용하는 가장 인기 있는 UPI 앱과 디지털 지갑을 포함합니다.",
    "India's most popular digital wallet. Instant deposits with no bank account required for small amounts.":
        "인도에서 가장 인기 있는 디지털 지갑입니다. 소액의 경우 은행 계좌 없이 즉시 입금할 수 있습니다.",
    "Widely used UPI-linked payment app. Fast, secure deposits directly from your PhonePe balance.":
        "널리 사용되는 UPI 연동 결제 앱입니다. PhonePe 잔액에서 빠르고 안전하게 입금할 수 있습니다.",
    "Direct bank transfers via IMPS for instant and NEFT for standard processing. Available with all major Indian banks.":
        "즉시 이체를 위한 IMPS 및 일반 처리를 위한 NEFT를 통한 직접 은행 이체를 지원합니다. 모든 주요 인도 은행에서 이용 가능합니다.",
    "Cryptocurrency option for fast, private transactions. Ideal for larger deposit amounts.":
        "빠르고 프라이빗한 거래를 위한 암호화폐 옵션입니다. 대금액 입금에 이상적입니다.",
    "USD-pegged stablecoin popular with experienced Indian crypto users.":
        "숙련된 인도 암호화폐 사용자들에게 인기 있는 USD 연동 스테이블코인입니다.",
    "ICC tournaments, T20 World Cup, ODI World Cup, and Champions Trophy, are major betting events in India, and 1win offers comprehensive coverage with markets across all group stage, knockout, and final matches. India's bilateral series against England, Australia, Pakistan, and other top teams are also fully covered.":
        "ICC 토너먼트, T20 월드컵, ODI 월드컵, 챔피언스 트로피는 인도의 주요 베팅 이벤트이며, 1win은 모든 조별 예선, 녹아웃, 결승 경기에 걸쳐 종합적인 커버리지와 시장을 제공합니다. 영국, 호주, 파키스탄 등 최고의 팀과의 인도 양자 시리즈도 완전히 커버됩니다.",
    "Go to the 1win Cashier section, select UPI, enter the amount, and scan the QR code or enter the UPI ID using your preferred UPI app (Google Pay, PhonePe, BHIM). Deposits are instant.":
        "1win 계좌 섹션으로 이동하여 UPI를 선택하고, 금액을 입력한 후 선호하는 UPI 앱(Google Pay, PhonePe, BHIM)을 사용하여 QR 코드를 스캔하거나 UPI ID를 입력하세요. 입금은 즉시 처리됩니다.",
    "Yes. Teen Patti is available in the 1win live casino section with dedicated tables and real dealers. Andar Bahar is also available for players who enjoy traditional Indian card games.":
        "네. Teen Patti는 전용 테이블과 실제 딜러와 함께 1win 라이브 카지노 섹션에서 이용 가능합니다. 전통 인도 카드 게임을 즐기는 플레이어를 위해 Andar Bahar도 제공됩니다.",
    # === KENYA ===
    "Kenya's dominant mobile money platform. Instant deposits and fast withdrawals directly from your M-Pesa account.":
        "케냐의 지배적인 모바일 머니 플랫폼입니다. M-Pesa 계좌에서 직접 즉시 입금 및 빠른 출금이 가능합니다.",
    "Direct transfers from Kenyan bank accounts. Suitable for larger transactions with major local banks.":
        "케냐 은행 계좌에서 직접 이체를 지원합니다. 주요 현지 은행을 통한 대규모 거래에 적합합니다.",
    "Cryptocurrency deposits available. Fast, borderless transactions with low processing fees.":
        "암호화폐 입금이 가능합니다. 낮은 처리 수수료로 빠르고 국경 없는 거래를 지원합니다.",
    "ETH deposits and withdrawals supported. Good option for players comfortable with crypto.":
        "ETH 입출금을 지원합니다. 암호화폐에 익숙한 플레이어에게 좋은 옵션입니다.",
    "USD-pegged stablecoin. Protects against currency fluctuation for larger deposit amounts.":
        "USD 연동 스테이블코인입니다. 대금액 입금 시 환율 변동으로부터 보호합니다.",
    "International card payments accepted. Processed securely with full fraud protection.":
        "국제 카드 결제를 지원합니다. 완전한 사기 방지 보호와 함께 안전하게 처리됩니다.",
    "Rugby union is hugely popular in Kenya. The Kenya Sevens team is one of the most successful on the World Rugby Sevens Series circuit, and 1win covers international sevens rugby tournaments with dedicated betting markets. The Kenya Cup domestic competition is also available for betting.":
        "럭비 유니언은 케냐에서 매우 인기가 높습니다. 케냐 세번스 팀은 월드 럭비 세번스 시리즈 서킷에서 가장 성공적인 팀 중 하나이며, 1win은 전용 베팅 시장으로 국제 세번스 럭비 토너먼트를 커버합니다. 케냐 컵 국내 대회도 베팅 가능합니다.",
    # === KOREA ===
    "Select Quick registration for the fastest account setup. Enter your country (South Korea), preferred currency (KRW), and a secure password.":
        "가장 빠른 계정 설정을 위해 빠른 가입을 선택하세요. 국가(대한민국), 선호 통화(KRW), 안전한 비밀번호를 입력하세요.",
    "Direct transfers from Korean bank accounts. Supported for both deposits and withdrawals in KRW.":
        "한국 은행 계좌에서 직접 이체를 지원합니다. KRW로 입금 및 출금 모두 가능합니다.",
    "Second most popular crypto option. Smart contract-based transfers with excellent speed.":
        "두 번째로 인기 있는 암호화폐 옵션입니다. 스마트 계약 기반 이체로 탁월한 속도를 제공합니다.",
    "Stablecoin option for players who prefer stable value. USDT TRC-20 and ERC-20 supported.":
        "안정적인 가치를 선호하는 플레이어를 위한 스테이블코인 옵션입니다. USDT TRC-20 및 ERC-20을 지원합니다.",
    "Various international e-wallet providers supported. Check the cashier section for current availability.":
        "다양한 국제 전자 지갑 제공업체를 지원합니다. 현재 이용 가능 여부는 계좌 섹션을 확인하세요.",
    "Korean Baseball Organization (KBO) games are available with comprehensive pre-match and in-play markets including run lines, totals, player props, and first-inning betting. The KBO season runs from April to November, providing months of continuous baseball betting opportunities for Korean players.":
        "한국야구위원회(KBO) 경기는 런라인, 합계, 선수 소품, 첫 회 베팅을 포함한 종합적인 사전 베팅 및 인플레이 시장을 제공합니다. KBO 시즌은 4월부터 11월까지 진행되어 한국 플레이어에게 수개월간 지속적인 야구 베팅 기회를 제공합니다.",
    "Esports betting is a major draw for Korean 1win players. League of Legends (LCK), StarCraft II, Valorant, Dota 2, and CS2 are all covered. Korea's dominance in competitive gaming means Korean players can watch and bet on top-level esports action with genuine insight into team and player performance.":
        "e스포츠 베팅은 한국 1win 플레이어들에게 큰 매력입니다. 리그 오브 레전드(LCK), 스타크래프트 II, 발로란트, 도타 2, CS2 모두 커버됩니다. 한국이 e스포츠에서 지배적인 위치를 차지하고 있어 한국 플레이어들은 팀과 선수 성적에 대한 깊은 이해를 바탕으로 최고 수준의 e스포츠를 시청하고 베팅할 수 있습니다.",
    "The 1win casino is a major attraction for Korean players. Live dealer baccarat is the standout offering, Korean players have a strong cultural affinity for baccarat, and 1win's live tables feature real dealers in real-time HD streams. Live blackjack, roulette, and dragon tiger are also available 24/7. The slots catalogue covers over 10,000 titles from leading providers including Pragmatic Play, BGaming, and Hacksaw Gaming.":
        "1win 카지노는 한국 플레이어들에게 큰 매력입니다. 라이브 딜러 바카라가 핵심 서비스로, 한국 플레이어들은 바카라에 강한 문화적 친밀감을 가지고 있으며, 1win의 라이브 테이블은 실제 딜러와 HD 실시간 스트림을 제공합니다. 라이브 블랙잭, 룰렛, 드래곤 타이거도 24/7 이용 가능합니다. 슬롯 카탈로그는 Pragmatic Play, BGaming, Hacksaw Gaming 등 선도적인 공급업체로부터 10,000개 이상의 타이틀을 제공합니다.",
    # === PAKISTAN ===
    "1win Pakistan is the betting platform of choice for Pakistani players seeking comprehensive cricket coverage, an extensive casino, and local payment options. The platform supports Pakistani Rupee (PKR) and integrates with Easypaisa and JazzCash, Pakistan's most popular mobile money services, making it straightforward for players across the country to deposit and withdraw funds without the complications of international banking.":
        "1win 파키스탄은 종합적인 크리켓 커버리지, 광범위한 카지노, 현지 결제 옵션을 원하는 파키스탄 플레이어들의 선호 베팅 플랫폼입니다. 플랫폼은 파키스탄 루피(PKR)를 지원하며 파키스탄에서 가장 인기 있는 모바일 머니 서비스인 Easypaisa 및 JazzCash와 통합되어 국제 은행 거래의 복잡함 없이 전국 플레이어가 쉽게 입출금할 수 있습니다.",
    "Choose Quick registration for instant account creation. Select Pakistan as your country and PKR as your currency.":
        "즉시 계정 생성을 위해 빠른 가입을 선택하세요. 국가는 파키스탄, 통화는 PKR로 선택하세요.",
    "Pakistan's leading mobile money platform. Deposit directly from your Easypaisa account, fast, secure, and widely available.":
        "파키스탄의 선도적인 모바일 머니 플랫폼입니다. Easypaisa 계좌에서 직접 입금하세요. 빠르고, 안전하며, 광범위하게 이용 가능합니다.",
    "Telecom-linked mobile wallet from Jazz. Instant deposits with no bank account required.":
        "Jazz의 통신사 연동 모바일 지갑입니다. 은행 계좌 없이 즉시 입금할 수 있습니다.",
    "Direct transfers from Pakistani bank accounts. Supported via major national and commercial banks.":
        "파키스탄 은행 계좌에서 직접 이체를 지원합니다. 주요 국내 및 상업 은행을 통해 이용 가능합니다.",
    "Stablecoin option denominated in USD equivalent. Popular for larger transaction amounts.":
        "USD 등가액으로 표시된 스테이블코인 옵션입니다. 대규모 거래 금액에 인기가 있습니다.",
    "International debit and credit cards accepted. Transactions processed in PKR.":
        "국제 직불 및 신용카드를 지원합니다. 거래는 PKR로 처리됩니다.",
    "Football is the second most popular sport for Pakistani bettors. The English Premier League, UEFA Champions League, and La Liga attract strong betting volumes from Pakistani players. Kabaddi, available in Pro Kabaddi League format, is also covered, as are virtual sports markets for players who want action at any hour.":
        "축구는 파키스탄 베터들에게 두 번째로 인기 있는 스포츠입니다. 영국 프리미어 리그, UEFA 챔피언스 리그, 라 리가는 파키스탄 플레이어로부터 강한 베팅 볼륨을 유도합니다. Pro Kabaddi League 형식의 카바디도 커버되며, 언제든지 베팅을 원하는 플레이어를 위한 가상 스포츠 시장도 제공됩니다.",
    # === RUSSIA ===
    "1win is one of the most established international betting platforms for Russian players, with a deep sports catalogue covering the Russian Premier League (RPL), Kontinental Hockey League (KHL), MMA events including UFC and local promotions, and dozens of other sports. The platform supports Russian Ruble (RUB) and accepts popular Russian payment methods including bank cards, Qiwi, and YooMoney, ensuring straightforward deposits and withdrawals for all Russian players.":
        "1win은 러시아 플레이어를 위한 가장 확고히 자리잡은 국제 베팅 플랫폼 중 하나로, 러시아 프리미어 리그(RPL), 콘티넨탈 하키 리그(KHL), UFC를 포함한 MMA 이벤트, 수십 가지 기타 스포츠를 포함한 광범위한 스포츠 카탈로그를 제공합니다. 플랫폼은 러시아 루블(RUB)을 지원하며 은행 카드, Qiwi, YooMoney 등 인기 있는 러시아 결제 수단을 지원하여 모든 러시아 플레이어의 입출금을 원활하게 합니다.",
    "1win Russia supports the main payment systems used by Russian players. The platform has adapted to changing payment conditions and maintains a range of reliable deposit and withdrawal options.":
        "1win 러시아는 러시아 플레이어가 사용하는 주요 결제 시스템을 지원합니다. 플랫폼은 변화하는 결제 조건에 적응하여 다양한 안정적인 입출금 옵션을 유지합니다.",
    "Russian bank cards accepted for deposits. MIR cards supported alongside Visa and Mastercard.":
        "러시아 은행 카드 입금을 지원합니다. Visa 및 Mastercard와 함께 MIR 카드도 지원됩니다.",
    "Popular Russian e-wallet. Fast deposits directly from your Qiwi account.":
        "인기 있는 러시아 전자 지갑입니다. Qiwi 계좌에서 직접 빠르게 입금할 수 있습니다.",
    "Widely used Russian payment service. Instant deposits and reliable withdrawals.":
        "널리 사용되는 러시아 결제 서비스입니다. 즉시 입금과 안정적인 출금이 가능합니다.",
    "Cryptocurrency option for private, fast transactions. Unaffected by banking restrictions.":
        "프라이빗하고 빠른 거래를 위한 암호화폐 옵션입니다. 은행 제한의 영향을 받지 않습니다.",
    "Stablecoin option. Highly popular with Russian players for its stability and fast processing.":
        "스테이블코인 옵션입니다. 안정성과 빠른 처리로 러시아 플레이어들에게 매우 인기가 높습니다.",
    "ETH deposits available. Second most popular crypto option for Russian users.":
        "ETH 입금이 가능합니다. 러시아 사용자에게 두 번째로 인기 있는 암호화폐 옵션입니다.",
    "The Russian Premier League (RPL) is covered in full at 1win Russia. Matches involving CSKA Moscow, Spartak Moscow, Zenit Saint Petersburg, and Lokomotiv Moscow attract the highest betting volumes. Pre-match and live in-play markets including match winner, handicap, over/under, clean sheet, and first goalscorer are available for every RPL fixture. Russian Cup and lower-division matches are also covered.":
        "러시아 프리미어 리그(RPL)는 1win 러시아에서 완전히 커버됩니다. CSKA 모스크바, 스파르타크 모스크바, 제니트 상트페테르부르크, 로코모티프 모스크바가 포함된 경기가 가장 높은 베팅 볼륨을 끌어냅니다. 모든 RPL 경기에서 승자, 핸디캡, 오버/언더, 무실점, 첫 골 득점자를 포함한 사전 베팅 및 라이브 인플레이 시장이 제공됩니다. 러시아 컵 및 하위 리그 경기도 커버됩니다.",
    "Ice hockey is Russia's second most popular betting sport. The Kontinental Hockey League (KHL) season from September to April provides a constant stream of betting opportunities. 1win covers all KHL games with markets including match winner, puck line, total goals, and first period betting. CSKA Moscow, SKA Saint Petersburg, and Metallurg Magnitogorsk are the most-bet teams.":
        "아이스하키는 러시아에서 두 번째로 인기 있는 베팅 스포츠입니다. 9월부터 4월까지 진행되는 콘티넨탈 하키 리그(KHL) 시즌은 지속적인 베팅 기회를 제공합니다. 1win은 모든 KHL 경기를 승자, 퍽 라인, 총 골, 1피리어드 베팅을 포함한 시장으로 커버합니다. CSKA 모스크바, SKA 상트페테르부르크, 마그니토고르스크 메탈루르그가 가장 많이 베팅되는 팀입니다.",
    "MMA is hugely popular in Russia. 1win covers all UFC events with full card coverage including main event, co-main, and undercard bouts. Russian fighters competing in the UFC and other major promotions always attract strong local betting interest. Bellator, ONE Championship, and Russian domestic MMA events are also available.":
        "MMA는 러시아에서 매우 인기가 높습니다. 1win은 메인 이벤트, 코메인, 언더카드 경기 등 전체 카드 커버리지로 모든 UFC 이벤트를 커버합니다. UFC 및 기타 주요 프로모션에서 활동하는 러시아 선수들은 항상 강한 현지 베팅 관심을 끌어냅니다. Bellator, ONE Championship, 러시아 국내 MMA 이벤트도 이용 가능합니다.",
    "The 1win casino is one of the strongest offerings on the platform for Russian players. Live dealer tables with Russian-speaking dealers are available for baccarat, blackjack, roulette, and poker. The slots section covers over 10,000 titles. Aviator is the most played crash game among Russian users. The casino is available 24/7 via browser and the 1win app.":
        "1win 카지노는 러시아 플레이어를 위한 플랫폼의 가장 강력한 서비스 중 하나입니다. 러시아어를 구사하는 딜러와 함께 바카라, 블랙잭, 룰렛, 포커 라이브 딜러 테이블을 이용할 수 있습니다. 슬롯 섹션은 10,000개 이상의 타이틀을 커버합니다. Aviator는 러시아 사용자 사이에서 가장 많이 플레이되는 크래시 게임입니다. 카지노는 브라우저와 1win 앱을 통해 24/7 이용 가능합니다.",
    # === TURKEY ===
    "Turkey's most popular digital wallet for online transactions. Fast, secure deposits and withdrawals in TRY.":
        "온라인 거래를 위한 터키에서 가장 인기 있는 디지털 지갑입니다. TRY로 빠르고 안전하게 입출금할 수 있습니다.",
    "Direct Turkish bank transfers via Havale (same bank) or EFT (inter-bank). Available with all major Turkish banks.":
        "Havale(동일 은행) 또는 EFT(은행 간) 방식으로 직접 터키 은행 이체를 지원합니다. 모든 주요 터키 은행에서 이용 가능합니다.",
    "USD-pegged stablecoin. Protects against TRY currency fluctuation for larger transactions.":
        "USD 연동 스테이블코인입니다. 대규모 거래 시 TRY 환율 변동으로부터 보호합니다.",
    "ETH deposits and withdrawals available. Reliable crypto option with strong liquidity.":
        "ETH 입출금이 가능합니다. 강한 유동성을 갖춘 안정적인 암호화폐 옵션입니다.",
    "International card payments accepted subject to card issuer approval.":
        "국제 카드 결제는 카드 발급사 승인에 따라 지원됩니다.",
    "Turkish clubs competing in European competitions, the UEFA Champions League and Europa League, receive special attention at 1win, with boosted odds and enhanced markets during matchweeks. The Turkish national team's qualifying campaigns and major tournaments are covered with dedicated promotional periods.":
        "UEFA 챔피언스 리그와 유로파 리그 등 유럽 대회에 참가하는 터키 클럽들은 1win에서 특별한 관심을 받으며, 경기 주간에 배당률 상향 및 향상된 시장을 제공합니다. 터키 국가대표팀의 예선 캠페인과 주요 토너먼트는 전용 프로모션 기간으로 커버됩니다.",
    "Basketball is Turkey's second most popular sport for betting. The BSL (Basketbol Süper Ligi) is fully covered, as is the EuroLeague, which features Turkish teams Anadolu Efes and Fenerbahçe Beko. Tennis, volleyball, and MMA markets are also available for Turkish players seeking variety.":
        "농구는 터키에서 두 번째로 인기 있는 베팅 스포츠입니다. 터키 팀 아나돌루 에페스와 페네르바체 베코가 참가하는 유로리그뿐만 아니라 BSL(바스켓볼 쉬퍼 리기)도 완전히 커버됩니다. 다양한 베팅을 원하는 터키 플레이어를 위해 테니스, 배구, MMA 시장도 제공됩니다.",
    "The 1win live casino is a major attraction for Turkish players. Live dealer roulette, blackjack, and baccarat tables run 24/7. The casino section also features Turkish-language slots and Aviator, the crash game that has become one of the most played titles across Turkey. Live casino cashback promotions are available weekly for active players.":
        "1win 라이브 카지노는 터키 플레이어들에게 큰 매력입니다. 라이브 딜러 룰렛, 블랙잭, 바카라 테이블이 24/7 운영됩니다. 카지노 섹션에는 터키어 슬롯과 터키 전역에서 가장 많이 플레이되는 타이틀 중 하나가 된 크래시 게임 Aviator도 제공됩니다. 활성 플레이어를 위한 라이브 카지노 캐시백 프로모션이 매주 제공됩니다.",
    # === VIETNAM ===
    "Go to the Cashier, select MoMo or ZaloPay, and complete the transfer. Your bonus is credited immediately after the first qualifying deposit.":
        "계좌로 이동하여 MoMo 또는 ZaloPay를 선택하고 이체를 완료하세요. 첫 번째 적격 입금 후 즉시 보너스가 지급됩니다.",
    "Vietnam's leading mobile e-wallet. Instant deposits and withdrawals directly from your MoMo account.":
        "베트남의 선도적인 모바일 전자 지갑입니다. MoMo 계좌에서 직접 즉시 입출금할 수 있습니다.",
    "Zalo-linked digital wallet widely used in Vietnam. Fast transactions integrated with the Zalo super-app.":
        "베트남에서 널리 사용되는 Zalo 연동 디지털 지갑입니다. Zalo 슈퍼앱과 통합된 빠른 거래를 지원합니다.",
    "Direct transfers from Vietnamese banks including Vietcombank, BIDV, Techcombank, and others.":
        "Vietcombank, BIDV, Techcombank 등 베트남 은행에서 직접 이체를 지원합니다.",
    "Stablecoin option. Protects against VND fluctuation and popular for larger transactions.":
        "스테이블코인 옵션입니다. VND 환율 변동으로부터 보호하며 대규모 거래에 인기가 있습니다.",
    "Esports is one of the fastest-growing betting categories in Vietnam. 1win covers the VCS (Vietnam Championship Series for League of Legends), regional Mobile Legends: Bang Bang tournaments, Dota 2 international competitions, Valorant, and CS2. Table tennis, a sport with enormous betting volumes across Southeast Asia, is also available with 24/7 market coverage at 1win.":
        "e스포츠는 베트남에서 가장 빠르게 성장하는 베팅 카테고리 중 하나입니다. 1win은 VCS(베트남 리그 오브 레전드 챔피언십 시리즈), 지역 모바일 레전드: 뱅뱅 토너먼트, 도타 2 국제 대회, 발로란트, CS2를 커버합니다. 동남아시아 전역에서 막대한 베팅 볼륨을 가진 탁구도 1win에서 24/7 시장 커버리지로 이용 가능합니다.",
    "The 1win casino is particularly strong for Vietnamese players. Live dealer baccarat, the most popular casino game in Vietnam, operates continuously with real dealers in HD streams. Sicbo, dragon tiger, and roulette are also available live. The Aviator crash game has become one of the most-played games at 1win Vietnam for its simplicity and fast-paced action. The slots section includes 12,000+ games from international providers.":
        "1win 카지노는 베트남 플레이어에게 특히 강력합니다. 베트남에서 가장 인기 있는 카지노 게임인 라이브 딜러 바카라가 HD 스트림의 실제 딜러와 함께 지속적으로 운영됩니다. 식보, 드래곤 타이거, 룰렛도 라이브로 이용 가능합니다. Aviator 크래시 게임은 간편함과 빠른 게임플레이로 1win 베트남에서 가장 많이 플레이되는 게임 중 하나가 되었습니다. 슬롯 섹션은 국제 공급업체의 12,000개 이상의 게임을 포함합니다.",
    "Log in to 1win, go to the Cashier, select MoMo, enter the deposit amount, and complete the transfer through your MoMo app. Deposits are credited instantly.":
        "1win에 로그인하고 계좌로 이동하여 MoMo를 선택하세요. 입금 금액을 입력하고 MoMo 앱을 통해 이체를 완료하세요. 입금은 즉시 처리됩니다.",
    # === GLOBAL FAQ ===
    "1win is available in over 50 countries across Asia, Africa, Latin America, Europe, and CIS regions. Some countries may have restrictions based on local gambling regulations. Check the 1win website for your country's availability.":
        "1win은 아시아, 아프리카, 라틴 아메리카, 유럽, CIS 지역의 50개국 이상에서 이용 가능합니다. 일부 국가는 현지 도박 규정에 따라 제한이 있을 수 있습니다. 귀하의 국가 이용 가능 여부는 1win 웹사이트를 확인하세요.",
    "You must be at least 18 years old to register and play on 1win. Age verification is required during the KYC process, and underage gambling is strictly prohibited.":
        "1win에 가입하고 플레이하려면 최소 18세 이상이어야 합니다. KYC 프로세스에서 연령 확인이 필요하며, 미성년자 도박은 엄격히 금지됩니다.",
    "1win supports over 15 languages including English, Hindi, Portuguese, Spanish, French, Turkish, Russian, and many more. The interface automatically detects your browser language.":
        "1win은 영어, 힌디어, 포르투갈어, 스페인어, 프랑스어, 터키어, 러시아어 등 15개 이상의 언어를 지원합니다. 인터페이스는 브라우저 언어를 자동으로 감지합니다.",
    "Live (in-play) betting allows you to place bets on events that are currently in progress. Odds update in real-time based on game action. You can bet on goals, points, cards, corners, and 12,000+ other live markets.":
        "라이브(인플레이) 베팅은 현재 진행 중인 이벤트에 베팅할 수 있습니다. 배당률은 경기 상황에 따라 실시간으로 업데이트됩니다. 골, 포인트, 카드, 코너 및 12,000개 이상의 기타 라이브 시장에 베팅할 수 있습니다.",
    "An accumulator (parlay/express) combines multiple selections into one bet. All selections must win for the bet to pay out, but the odds multiply together for much higher potential returns. For example, 4 selections at 2.0 odds each = 16.0 combined odds.":
        "어큐뮬레이터(파를레이/익스프레스)는 여러 선택을 하나의 베팅으로 결합합니다. 베팅이 지급되려면 모든 선택이 적중해야 하지만, 배당률이 곱해져 훨씬 높은 잠재 수익을 제공합니다. 예를 들어, 각 2.0 배당의 4개 선택 = 16.0 결합 배당률.",
    "Cash out allows you to settle a bet early, before the event ends. If your bet is winning, you can lock in a profit. If it's losing, you can minimize your losses. The cash-out amount is calculated based on current odds.":
        "캐시아웃을 통해 이벤트가 끝나기 전에 일찍 베팅을 정산할 수 있습니다. 베팅이 이기고 있다면 수익을 확정할 수 있습니다. 지고 있다면 손실을 최소화할 수 있습니다. 캐시아웃 금액은 현재 배당률을 기준으로 계산됩니다.",
    "1win supports decimal, fractional, American, and Hong Kong odds formats. You can switch between formats in your account settings at any time.":
        "1win은 소수형, 분수형, 미국형, 홍콩형 배당률 형식을 지원합니다. 계정 설정에서 언제든지 형식을 변경할 수 있습니다.",
    "1win features over 10,000 casino games from 100+ providers including Pragmatic Play, Evolution, NetEnt, Play'n GO, Microgaming, and many more. New games are added weekly.":
        "1win은 Pragmatic Play, Evolution, NetEnt, Play'n GO, Microgaming 등 100개 이상의 공급업체로부터 10,000개 이상의 카지노 게임을 제공합니다. 새 게임이 매주 추가됩니다.",
    "Top slots include: Gates of Olympus (Pragmatic Play), Sweet Bonanza (Pragmatic Play), Book of Dead (Play'n GO), Starburst (NetEnt), and The Dog House Megaways. The \"Popular\" section shows the most-played games in real time.":
        "인기 슬롯: Gates of Olympus(Pragmatic Play), Sweet Bonanza(Pragmatic Play), Book of Dead(Play'n GO), Starburst(NetEnt), The Dog House Megaways. '인기' 섹션에서 실시간 최다 플레이 게임을 확인할 수 있습니다.",
    "RTP (Return to Player) varies by game. Most slots have RTPs between 95-97%. Blackjack can reach 99%+ with optimal strategy. Aviator has a 97% RTP. Each game displays its RTP in the info section.":
        "RTP(플레이어 환수율)는 게임마다 다릅니다. 대부분의 슬롯은 95-97% RTP를 갖습니다. 블랙잭은 최적 전략 사용 시 99%+에 달할 수 있습니다. Aviator의 RTP는 97%입니다. 각 게임의 정보 섹션에서 RTP를 확인할 수 있습니다.",
    "Crypto transactions are 100% free (0% fees). Card payments have a 2.5% processing fee. Bank transfers, PIX, and UPI are free. Always check the cashier section for the latest fee information.":
        "암호화폐 거래는 100% 무료(0% 수수료)입니다. 카드 결제에는 2.5% 처리 수수료가 부과됩니다. 은행 이체, PIX, UPI는 무료입니다. 최신 수수료 정보는 항상 계좌 섹션을 확인하세요.",
    "Yes. 1win supports 20+ currencies including USD, EUR, INR, BRL, NGN, KES, and more. Deposits are automatically converted to your account currency at competitive exchange rates.":
        "네. 1win은 USD, EUR, INR, BRL, NGN, KES 등 20개 이상의 통화를 지원합니다. 입금액은 경쟁력 있는 환율로 계정 통화로 자동 환전됩니다.",
    "Go to Account → Verification. Upload a clear photo of your government-issued ID (passport, driver's license, or national ID) and a proof of address (utility bill or bank statement dated within 3 months). Verification is typically completed within 24 hours.":
        "계정 → 인증으로 이동하세요. 정부 발급 신분증(여권, 운전면허증 또는 주민등록증) 사진과 주소 증명(3개월 이내 공과금 청구서 또는 은행 명세서)을 업로드하세요. 인증은 일반적으로 24시간 이내에 완료됩니다.",
    "Click \"Forgot Password\" on the login page. Enter your registered email address or phone number. You'll receive a reset link via email or SMS. Follow the link to create a new password.":
        "로그인 페이지에서 '비밀번호 분실'을 클릭하세요. 등록된 이메일 주소 또는 전화번호를 입력하세요. 이메일 또는 SMS로 재설정 링크를 받으실 것입니다. 링크를 클릭하여 새 비밀번호를 설정하세요.",
    "No. Each person is allowed only one account on 1win. Creating multiple accounts violates the terms of service and may result in all accounts being permanently suspended and funds forfeited.":
        "아니요. 1win에서는 1인당 하나의 계정만 허용됩니다. 여러 계정 생성은 서비스 약관을 위반하며 모든 계정이 영구 정지되고 자금이 몰수될 수 있습니다.",
    "Cashback is a percentage of your net losses returned to your account. The percentage depends on your VIP 등급 (3%-15%). Cashback is calculated weekly and credited automatically every Monday. It's essentially a safety net on losing weeks.":
        "캐시백은 순손실의 일정 비율을 계정으로 반환하는 것입니다. 비율은 VIP 등급(3%-15%)에 따라 달라집니다. 캐시백은 매주 계산되어 매주 월요일 자동으로 지급됩니다. 손실이 있는 주의 안전망 역할을 합니다.",
    "Yes, official 1win mirrors are completely safe. They use the same SSL/TLS encryption and security infrastructure as the main site. Your personal data, deposits, winnings, and bonuses are protected by the same systems. The key is to use mirrors from verified, trusted sources, like the links listed on ourmirror page, rather than unknown links you may find on unverified third-party sites.":
        "네, 공식 1win 미러 사이트는 완전히 안전합니다. 메인 사이트와 동일한 SSL/TLS 암호화 및 보안 인프라를 사용합니다. 개인 데이터, 입금, 당첨금, 보너스가 동일한 시스템으로 보호됩니다. 핵심은 검증되지 않은 타사 사이트에서 찾을 수 있는 알 수 없는 링크가 아닌, 미러 페이지에 나열된 링크와 같이 검증된 신뢰할 수 있는 소스의 미러를 사용하는 것입니다.",
    # === LIVE STREAMING ===
    "Accessing live sports streams at 1win takes three steps and less than a minute.":
        "1win에서 라이브 스포츠 스트림에 접근하는 데는 3단계, 1분도 채 걸리지 않습니다.",
    "Click the TV icon next to any streamable event to open the live video player. The stream loads within the page, no redirects, no external sites. Watch in the same window as the odds, place bets in real time, and follow the action as it happens. Stream quality is automatically adjusted to your connection speed.":
        "스트리밍 가능한 이벤트 옆의 TV 아이콘을 클릭하면 라이브 비디오 플레이어가 열립니다. 스트림은 페이지 내에서 로드되며, 리디렉션이나 외부 사이트가 필요 없습니다. 배당률과 같은 창에서 시청하고, 실시간으로 베팅을 배치하고, 진행 상황을 따라가세요. 스트림 품질은 연결 속도에 따라 자동으로 조정됩니다.",
    "All four Grand Slams, Australian Open, French Open, Wimbledon, and the US Open, are streamed when available, alongside ATP and WTA tour events throughout the calendar year. Live betting markets include set betting, game handicaps, next point winner, and break of serve. Tennis streams run 24/7 during major tournaments with multiple courts covered simultaneously.":
        "호주 오픈, 프랑스 오픈, 윔블던, US 오픈 등 4대 그랜드슬램이 이용 가능할 때 스트리밍되며, 연중 ATP 및 WTA 투어 이벤트도 제공됩니다. 라이브 베팅 시장에는 세트 베팅, 게임 핸디캡, 다음 포인트 승자, 서비스 브레이크가 포함됩니다. 주요 토너먼트 중에는 여러 코트가 동시에 커버되며 테니스 스트림이 24/7 진행됩니다.",
    "NBA regular season and playoff games are streamed live, along with EuroLeague, national championship leagues across Europe, and international competitions including FIBA World Cup qualifiers. Quarter-by-quarter betting, player props, and live point spread markets are all available alongside the stream for comprehensive in-play wagering.":
        "NBA 정규 시즌 및 플레이오프 경기가 라이브로 스트리밍되며, 유로리그, 유럽 전역의 국가 챔피언십 리그, FIBA 월드컵 예선 등 국제 대회도 제공됩니다. 쿼터별 베팅, 선수 소품, 라이브 포인트 스프레드 시장이 모두 스트림과 함께 제공되어 종합적인 인플레이 베팅이 가능합니다.",
    "NHL regular season and playoff games are covered, together with the KHL (Kontinental Hockey League), SHL, Finnish Liiga, Czech Extraliga, and international tournaments including the IIHF World Championship. Live betting includes period betting, puck line, and total goals markets running alongside the live stream feed.":
        "NHL 정규 시즌 및 플레이오프 경기가 KHL(콘티넨탈 하키 리그), SHL, 핀란드 리가, 체코 엑스트라리가, IIHF 세계선수권대회 등 국제 토너먼트와 함께 커버됩니다. 라이브 베팅에는 피리어드 베팅, 퍽 라인, 라이브 스트림 피드와 함께 진행되는 총 골 시장이 포함됩니다.",
    "ESports is one of the fastest-growing streaming categories at 1win. CS:GO, Dota 2, League of Legends, Valorant, FIFA, and NBA 2K are all covered with live streams of major tournaments including ESL, BLAST Premier, The International, and regional championships. ESports markets include map winner, round handicap, total maps, and first blood betting.":
        "e스포츠는 1win에서 가장 빠르게 성장하는 스트리밍 카테고리 중 하나입니다. CS:GO, Dota 2, 리그 오브 레전드, 발로란트, FIFA, NBA 2K 등 ESL, BLAST Premier, The International, 지역 챔피언십을 포함한 주요 토너먼트의 라이브 스트림이 제공됩니다. e스포츠 시장에는 맵 승자, 라운드 핸디캡, 총 맵 수, 퍼스트 블러드 베팅이 포함됩니다.",
    "MLB games are streamed throughout the regular season and postseason, along with Japanese NPB and Korean KBO leagues. Table tennis is streamed round the clock from professional leagues in China, Germany, and Russia, making it one of the most consistently available streaming sports on the platform, ideal for players in any time zone looking for live action at any hour.":
        "MLB 경기는 정규 시즌과 포스트시즌 내내 스트리밍되며, 일본 NPB 및 한국 KBO 리그도 제공됩니다. 탁구는 중국, 독일, 러시아의 프로 리그에서 24시간 스트리밍되어 플랫폼에서 가장 일관되게 이용 가능한 스트리밍 스포츠 중 하나로, 어느 시간대에서든 라이브 액션을 원하는 플레이어에게 이상적입니다.",
    "Watch live sports on your phone or tablet, on the app or in your mobile browser.":
        "스마트폰이나 태블릿에서 앱 또는 모바일 브라우저로 라이브 스포츠를 시청하세요.",
    "For the best mobile streaming experience, the 1win app is recommended. Available for Android as a direct APK download and for iOS from the App Store, the app provides faster stream loading times, lower battery consumption, and push notifications for match events that you have placed bets on. The app interface is specifically designed for one-handed use, browsing live events, switching between streams, and placing bets are all achievable with a single thumb.":
        "최고의 모바일 스트리밍 경험을 위해 1win 앱을 권장합니다. Android는 직접 APK 다운로드로, iOS는 App Store에서 이용 가능한 앱은 더 빠른 스트림 로딩 시간, 낮은 배터리 소비, 베팅한 경기 이벤트에 대한 푸시 알림을 제공합니다. 앱 인터페이스는 한 손 사용에 맞게 설계되어 라이브 이벤트 검색, 스트림 전환, 베팅 배치가 모두 엄지 하나로 가능합니다.",
    "Download the 1win Android APK directly from the website. The app supports all streaming features, includes live score overlays, and sends push alerts for goals, cards, and odds movements on your active bets. Installation takes under two minutes and the app does not require Google Play, download directly for any Android device.":
        "1win Android APK를 웹사이트에서 직접 다운로드하세요. 앱은 모든 스트리밍 기능을 지원하고, 라이브 스코어 오버레이를 포함하며, 활성 베팅의 골, 카드, 배당률 변동에 대한 푸시 알림을 전송합니다. 설치는 2분 이내에 완료되며, 앱은 Google Play 없이 모든 Android 기기에서 직접 다운로드할 수 있습니다.",
    "Live streams integrated directly into the betting interface. Watch the match and place bets in the same window, no tab switching.":
        "라이브 스트림이 베팅 인터페이스에 직접 통합되어 있습니다. 탭을 전환할 필요 없이 같은 창에서 경기를 시청하고 베팅을 배치하세요.",
    "Yes. Live streaming is fully supported on the 1win mobile app (Android and iOS) and on the mobile-optimised website accessible in any smartphone browser. The video player automatically adapts to your screen size and supports landscape mode for full-screen viewing. For the best experience, the 1win app is recommended. Download it via ourapp page.":
        "네. 라이브 스트리밍은 1win 모바일 앱(Android 및 iOS)과 스마트폰 브라우저에서 접근 가능한 모바일 최적화 웹사이트에서 완전히 지원됩니다. 비디오 플레이어는 화면 크기에 자동으로 적응하며 전체 화면 시청을 위한 가로 모드를 지원합니다. 최고의 경험을 위해 1win 앱을 권장합니다. 앱 페이지를 통해 다운로드하세요.",
    # === LUCKY DRIVE ===
    "The world's first Super Sport Utility Vehicle. Hybrid power meets Italian craftsmanship in a $240,000 package of pure dominance.":
        "세계 최초의 슈퍼 스포츠 유틸리티 차량. 하이브리드 동력과 이탈리아 장인 정신이 결합된 240,000달러의 순수한 지배력.",
    "Every real-money bet you place on 1win earns you automatic raffle tickets. The more you play, the more tickets you accumulate. When the draw date hits, one lucky player drives away in a brand-new Lambo. No separate entry needed, just play and win.":
        "1win에서 실제 돈으로 베팅할 때마다 자동으로 추첨 티켓이 지급됩니다. 더 많이 플레이할수록 더 많은 티켓을 쌓을 수 있습니다. 추첨일이 되면 행운의 플레이어 한 명이 새 람보르기니를 받아갑니다. 별도의 참가 신청 없이 그냥 플레이하고 당첨되세요.",
    "Past draws have given away Porsche 911s, Tesla Model Xs, and over $1,000,000 in combined cash prizes. Lucky Drive is the single biggest promotion in online betting, and it's exclusive to 1win.":
        "과거 추첨에서 포르쉐 911, 테슬라 모델 X, 총 100만 달러 이상의 현금 상금이 지급되었습니다. Lucky Drive는 온라인 베팅 업계에서 가장 큰 단일 프로모션으로 1win 독점 제공입니다.",
    "Bet on sports, spin slots, play Aviator, or hit the poker tables. Every $10 wagered earns you 1 Lucky Drive ticket.":
        "스포츠에 베팅하고, 슬롯을 돌리고, Aviator를 플레이하거나, 포커 테이블에 앉으세요. $10 베팅마다 Lucky Drive 티켓 1장이 지급됩니다.",
    "Sit back and watch the live draw. If your ticket is pulled, you win. More tickets = higher chances. It's that simple.":
        "편안하게 앉아 라이브 추첨을 시청하세요. 귀하의 티켓이 뽑히면 당첨됩니다. 티켓이 많을수록 당첨 확률이 높아집니다. 그만큼 간단합니다.",
    "A brand-new Lamborghini Urus SE. Every $100 wagered earns you a ticket. The more you play, the closer you get.":
        "새 람보르기니 Urus SE. $100 베팅마다 티켓 1장이 지급됩니다. 더 많이 플레이할수록 당첨에 가까워집니다.",
    "Even if you don't win the Lambo, there are massive cash prizes and bonuses up for grabs.":
        "람보르기니를 못 당첨되더라도 수많은 현금 상금과 보너스를 받을 기회가 있습니다.",
    "Real players. Real prizes. Real life-changing moments.":
        "실제 플레이어. 실제 상금. 실제 인생을 바꾸는 순간들.",
    "Past winners have taken home supercars, luxury watches, and 12,000+ thousands in cash. Your turn is coming.":
        "과거 당첨자들은 슈퍼카, 명품 시계, 수천 달러의 현금을 가져갔습니다. 당신의 차례가 곧 올 것입니다.",
    "Lucky Drive is one of the most distinctive promotions in the 1win ecosystem, a recurring prize draw that awards physical and cash prizes including luxury cars, watches, electronics, and cash payouts worth 12,000+ 1,000+ dollars. Unlike a simple random prize draw, Lucky Drive ties ticket accumulation to your genuine betting and gaming activity on the platform. Every bet you place, whether on sports, casino games, Aviator, or poker, generates tickets that enter you into the draw. The more active you are, the more tickets you accumulate, and the higher your statistical probability of winning.":
        "Lucky Drive는 1win 생태계에서 가장 독특한 프로모션 중 하나로, 명품 자동차, 시계, 전자기기, 현금 등 실물 및 현금 상금을 주는 정기 추첨 이벤트입니다. 단순한 랜덤 추첨과 달리, Lucky Drive는 티켓 적립을 플랫폼에서의 실제 베팅 및 게임 활동과 연결합니다. 스포츠, 카지노 게임, Aviator, 포커 등 어디서든 베팅할 때마다 추첨 티켓이 생성됩니다. 더 활발히 활동할수록 더 많은 티켓을 쌓고 당첨 확률이 높아집니다.",
    "Lucky Drive draws are announced in advance through the 1win platform and via ourpromotions page. Prize winners are verified and notified directly through their 1win accounts. Physical prizes including cars and luxury goods are arranged for delivery or collection. Cash prizes are credited to the winner's 1win account and are withdrawable using any supported method. Visit thepayments pageto see all available withdrawal options.":
        "Lucky Drive 추첨은 1win 플랫폼과 프로모션 페이지를 통해 사전에 공지됩니다. 상금 당첨자는 검증되며 1win 계정을 통해 직접 통보받습니다. 자동차 및 명품을 포함한 실물 상품은 배송 또는 수령이 준비됩니다. 현금 상금은 당첨자의 1win 계정에 지급되며 지원되는 방법으로 출금 가능합니다. 모든 출금 옵션은 결제 페이지를 방문하세요.",
    "Lucky Drive draws happen quarterly. The next draw is scheduled for the end of Q2 2026. Check the 1win promotions page for the exact date and live stream details.":
        "Lucky Drive 추첨은 분기별로 진행됩니다. 다음 추첨은 2026년 2분기 말로 예정되어 있습니다. 정확한 날짜와 라이브 스트림 세부 사항은 1win 프로모션 페이지를 확인하세요.",
    "Yes. Grand prize winners have the option to receive the cash equivalent ($240,000) instead of the vehicle. The choice is entirely up to you.":
        "네. 대상 당첨자는 차량 대신 현금 동가액($240,000)을 받는 옵션을 선택할 수 있습니다. 선택은 전적으로 귀하에게 달려 있습니다.",
    "No. There is no cap on how many tickets you can earn. The more you play, the more tickets you collect, and the higher your chances of winning.":
        "아니요. 획득 가능한 티켓 수에 제한이 없습니다. 더 많이 플레이할수록 더 많은 티켓을 수집하고 당첨 확률이 높아집니다.",
    "Lucky Drive is available to all registered 1win users in eligible countries (50+ countries). Check 1win's terms for a full list of supported regions.":
        "Lucky Drive는 적격 국가(50개국 이상)의 모든 등록된 1win 사용자에게 제공됩니다. 지원 지역 전체 목록은 1win의 약관을 확인하세요.",
    # === MIRROR ===
    "Mirrors for 1win can change from time to time. It is common to find a new URL created for a mirror site. A new mirror may be created when a previously used one is blocked. You will find the latest 1win mirror URLs on this page. Alternatively, players can access 1win by using a VPN service.":
        "1win의 미러 사이트는 때때로 변경될 수 있습니다. 미러 사이트에 새로운 URL이 생성되는 것은 일반적입니다. 이전에 사용했던 미러가 차단되면 새로운 미러가 생성될 수 있습니다. 이 페이지에서 최신 1win 미러 URL을 찾을 수 있습니다. 또는 VPN 서비스를 사용하여 1win에 접근할 수도 있습니다.",
    "Access the 1win mirror from any device, PC, smartphone, or tablet.":
        "PC, 스마트폰, 태블릿 등 모든 기기에서 1win 미러에 접근하세요.",
    "Access the 1win mirror directly in your browser on Windows or Mac. No download required, simply navigate to the current mirror URL and log in with your existing credentials. The full desktop experience is available including all sports betting, casino, and poker features.":
        "Windows 또는 Mac 브라우저에서 직접 1win 미러에 접근하세요. 다운로드 없이 현재 미러 URL로 이동하여 기존 자격 증명으로 로그인하면 됩니다. 모든 스포츠 베팅, 카지노, 포커 기능을 포함한 전체 데스크탑 경험을 이용할 수 있습니다.",
    "The 1win mirror is fully optimised for mobile browsers on Android and iOS. Visit the mirror URL from Safari, Chrome, or any mobile browser for instant access. Alternatively, download the dedicated 1win app for the best mobile experience with push notifications and fast loading.":
        "1win 미러는 Android와 iOS의 모바일 브라우저에 완전히 최적화되어 있습니다. Safari, Chrome 또는 모바일 브라우저에서 미러 URL을 방문하면 즉시 접근할 수 있습니다. 또는 전용 1win 앱을 다운로드하여 푸시 알림과 빠른 로딩의 최고의 모바일 경험을 누리세요.",
    "Sign up instantly using your existing Google, Facebook, or other social media account. One click to connect and you're ready to play. No forms to fill, no email confirmation required.":
        "기존 Google, Facebook 또는 기타 소셜 미디어 계정을 사용하여 즉시 가입하세요. 한 번의 클릭으로 연결하면 플레이할 준비가 됩니다. 양식 작성이나 이메일 확인이 필요 없습니다.",
    "Deposit using any supported payment method, card, crypto, or e-wallet. The bonus up to $500 is credited to your account instantly.":
        "카드, 암호화폐 또는 전자 지갑 등 지원되는 결제 수단을 사용하여 입금하세요. 최대 $500의 보너스가 즉시 계정에 지급됩니다.",
    "Download the official 1win app for seamless access, no mirror required on mobile.":
        "모바일에서 미러 없이 원활하게 접근하려면 공식 1win 앱을 다운로드하세요.",
    "In a growing number of countries, internet service providers (ISPs) are required by local regulations to block access to online betting platforms. When your ISP applies a DNS-level block on 1win.pro, attempting to visit the main domain simply fails, you receive a connection error or a blank page. This is not a problem with the website itself; it is a regulatory measure applied at the network level. A 1win mirror site is the direct solution to this problem, giving you instant access without any additional software or configuration.":
        "점점 더 많은 국가에서 인터넷 서비스 제공업체(ISP)는 현지 규정에 따라 온라인 베팅 플랫폼에 대한 접근을 차단해야 합니다. ISP가 1win.pro에 DNS 수준 차단을 적용하면 메인 도메인 방문이 실패하여 연결 오류 또는 빈 페이지가 표시됩니다. 이는 웹사이트 자체의 문제가 아니라 네트워크 수준에서 적용된 규제 조치입니다. 1win 미러 사이트는 이 문제의 직접적인 해결책으로, 추가 소프트웨어나 설정 없이 즉시 접근을 제공합니다.",
    "A mirror is an exact, live replica of the official 1win website hosted on a different domain name. It connects to the same servers, the same database, and the same user accounts as 1win.pro. When you log in on a mirror using your existing 1win credentials, you see your real balance, your open bets, your bonus funds, and your complete bet history, exactly as they appear on the main site. The mirror is not a separate platform; it is the same platform accessed through a different address.":
        "미러는 다른 도메인 이름에 호스팅된 공식 1win 웹사이트의 정확한 실시간 복제본입니다. 1win.pro와 동일한 서버, 동일한 데이터베이스, 동일한 사용자 계정에 연결됩니다. 기존 1win 자격 증명으로 미러에 로그인하면 메인 사이트와 동일하게 실제 잔액, 오픈 베팅, 보너스 자금, 전체 베팅 기록을 확인할 수 있습니다. 미러는 별도의 플랫폼이 아니라 다른 주소를 통해 접근하는 동일한 플랫폼입니다.",
    "Yes, official 1win mirrors are completely safe. The safety of a mirror site depends entirely on its source. Mirrors distributed by 1win and listed on trusted fan information pages like this one are genuine replicas of the official platform, operated under the same technical and regulatory framework. They are not third-party sites, not phishing pages, and not alternative platforms with different rules or different game providers. They are the same platform on a different URL.":
        "네, 공식 1win 미러는 완전히 안전합니다. 미러 사이트의 안전성은 전적으로 소스에 달려 있습니다. 1win이 배포하고 이 페이지와 같은 신뢰할 수 있는 팬 정보 페이지에 나열된 미러는 동일한 기술 및 규제 프레임워크 하에 운영되는 공식 플랫폼의 진정한 복제본입니다. 타사 사이트, 피싱 페이지, 또는 다른 규칙이나 다른 게임 공급업체를 가진 대체 플랫폼이 아닙니다. 다른 URL의 동일한 플랫폼입니다.",
    "Every official 1win mirror uses the same security infrastructure as 1win.pro. This includes industry-standard AES-256 encryption for data at rest and TLS 1.3 for data in transit. Your personal information, name, email, payment details, is encrypted before storage and never transmitted in plaintext. Payment processing uses the same verified gateways as the main site, with the same fraud detection and verification layers. When you make a deposit or request a withdrawal on a mirror, you are using exactly the same financial systems.":
        "모든 공식 1win 미러는 1win.pro와 동일한 보안 인프라를 사용합니다. 이에는 저장 데이터를 위한 업계 표준 AES-256 암호화와 전송 중 데이터를 위한 TLS 1.3이 포함됩니다. 이름, 이메일, 결제 세부 정보 등 개인 정보는 저장 전에 암호화되며 평문으로 전송되지 않습니다. 결제 처리는 메인 사이트와 동일한 검증된 게이트웨이를 사용하며, 동일한 사기 탐지 및 검증 레이어를 갖추고 있습니다. 미러에서 입금하거나 출금을 요청할 때 정확히 동일한 금융 시스템을 사용하는 것입니다.",
    "Three reliable methods to always have access to a working 1win mirror URL.":
        "항상 작동하는 1win 미러 URL에 접근할 수 있는 3가지 신뢰할 수 있는 방법.",
    "The 1win mobile app for Android and iOS connects to the platform automatically, bypassing the need for a mirror entirely. The app routes your connection independently of your ISP's DNS settings. Download the app once and you always have unrestricted access, no mirror URL needed. See our1win app pagefor the download link.":
        "Android 및 iOS용 1win 모바일 앱은 자동으로 플랫폼에 연결되어 미러가 전혀 필요 없습니다. 앱은 ISP의 DNS 설정과 독립적으로 연결을 라우팅합니다. 앱을 한 번 다운로드하면 항상 제한 없이 접근할 수 있으며, 미러 URL이 필요 없습니다. 다운로드 링크는 1win 앱 페이지를 참조하세요.",
    "Push notifications have been enhanced, you'll get instant alerts for goals, match results, and when your bets land. The cashout feature is now available directly from notifications.":
        "푸시 알림이 강화되어 골, 경기 결과, 베팅 결과에 대한 즉각적인 알림을 받을 수 있습니다. 이제 알림에서 직접 캐시아웃 기능을 이용할 수 있습니다.",
    # === NEWS ===
    "1win offers one of the best Aviator experiences in the industry, with live chat during rounds, detailed statistics, and auto-bet features that let you set strategies and walk away.":
        "1win은 업계 최고의 Aviator 경험을 제공합니다. 라운드 중 라이브 채팅, 상세 통계, 전략을 설정하고 자리를 비울 수 있는 자동 베팅 기능을 갖추고 있습니다.",
    "Every user who places a qualifying bet of $10+ on any quarter-final match will receive a $5 free bet for the next round. Accumulator bets across multiple matches are eligible for an additional 40% profit boost.":
        "모든 쿼터파이널 경기에 $10 이상의 적격 베팅을 하는 모든 사용자는 다음 라운드를 위한 $5 무료 베팅을 받습니다. 여러 경기에 걸친 어큐뮬레이터 베팅은 추가 40% 수익 부스트를 받을 수 있습니다.",
    "Pre-match betting markets include match result, both teams to score, over/under goals, correct score, first goalscorer, and dozens more. Asian handicap and draw no bet markets are also available.":
        "사전 베팅 시장에는 경기 결과, 양 팀 득점, 오버/언더 골, 정확한 스코어, 첫 골 득점자 등 수십 가지가 포함됩니다. 아시안 핸디캡 및 무승부 없음 시장도 이용 가능합니다.",
    "1win also supports traditional payment methods including Visa, Mastercard, bank transfer, Perfect Money, Skrill, and regional options like UPI and Paytm for Indian players.":
        "1win은 또한 Visa, Mastercard, 은행 이체, Perfect Money, Skrill, 인도 플레이어를 위한 UPI 및 Paytm 등 지역 옵션을 포함한 전통적인 결제 수단을 지원합니다.",
    "The Q2 2026 Lucky Drive draw is officially open at 1win. Every $100 wagered across any game type, sports betting, casino, poker, or Aviator, earns one entry ticket into the draw.":
        "2026년 2분기 Lucky Drive 추첨이 1win에서 공식적으로 시작되었습니다. 스포츠 베팅, 카지노, 포커, Aviator 등 모든 게임 유형에서 $100 베팅마다 추첨 참가 티켓 1장이 지급됩니다.",
    "The grand prize is a brand-new Lamborghini Urus SE valued at $230,000, or its cash equivalent if you prefer. VIP Platinum members receive 3x tickets per $100 wagered, and Diamond members receive 5x tickets.":
        "대상은 $230,000 상당의 새 람보르기니 Urus SE이며, 원하시면 현금 동가액을 받을 수 있습니다. VIP 플래티넘 회원은 $100 베팅마다 티켓 3장, 다이아몬드 회원은 티켓 5장을 받습니다.",
    "In addition to the Lamborghini, there are 12,000+ secondary prizes including luxury watches (Rolex, Omega), the latest iPhones and MacBooks, and substantial cash prizes ranging from $500 to $50,000.":
        "람보르기니 외에도 명품 시계(롤렉스, 오메가), 최신 iPhone 및 MacBook, $500에서 $50,000에 달하는 상당한 현금 상금을 포함한 2등 이하 상품이 있습니다.",
    "The live draw will be streamed on the 1win platform on June 30, 2026. Previous Lucky Drive winners have walked away with supercars, luxury holidays, and six-figure cash prizes.":
        "라이브 추첨은 2026년 6월 30일 1win 플랫폼에서 스트리밍됩니다. 이전 Lucky Drive 당첨자들은 슈퍼카, 명품 휴가, 6자리 현금 상금을 받아갔습니다.",
    "1win Poker has launched a new weekly freeroll series with a guaranteed $10,000 prize pool every Sunday. The tournament is open to all registered players with absolutely no buy-in required.":
        "1win 포커가 매주 일요일 $10,000 보장 상금 풀의 새로운 위클리 프리롤 시리즈를 시작했습니다. 토너먼트는 바이인 없이 모든 등록 플레이어에게 개방됩니다.",
    "The freeroll runs every Sunday at 18:00 UTC with late registration available for the first hour. Top 100 finishers receive cash prizes, and the overall weekly champion earns a seat in the monthly $100K GTD tournament.":
        "프리롤은 매주 일요일 UTC 18:00에 진행되며 첫 한 시간 동안 늦은 등록이 가능합니다. 상위 100명이 현금 상금을 받으며, 위클리 챔피언은 월간 $100K GTD 토너먼트 시드를 획득합니다.",
    "1win Poker offers Texas Hold'em and Omaha cash games running 24/7, plus a full tournament schedule with buy-ins starting from just $0.50. The poker room features multi-table support, hand histories, and player statistics.":
        "1win 포커는 24/7 운영되는 텍사스 홀덤과 오마하 캐시 게임, 단 $0.50부터 시작하는 바이인의 전체 토너먼트 일정을 제공합니다. 포커 룸은 멀티 테이블 지원, 핸드 기록, 플레이어 통계 기능을 갖추고 있습니다.",
    "High-stakes players can access VIP tables with unlimited buy-ins and personal dealer support. 1win's poker software supports desktop, mobile app, and browser play.":
        "고액 플레이어는 무제한 바이인과 개인 딜러 지원이 있는 VIP 테이블에 접근할 수 있습니다. 1win 포커 소프트웨어는 데스크탑, 모바일 앱, 브라우저 플레이를 지원합니다.",
    "1win has announced the biggest tournament series of the year, the Spring Showdown. Running from April 1 through May 15, this event features over 150 individual tournaments across casino, poker, and sports betting verticals with a combined guaranteed prize pool exceeding $2,000,000.":
        "1win이 올해 최대 토너먼트 시리즈인 스프링 쇼다운을 발표했습니다. 4월 1일부터 5월 15일까지 진행되는 이 이벤트는 카지노, 포커, 스포츠 베팅 부문에 걸쳐 150개 이상의 개별 토너먼트를 포함하며, 총 보장 상금 풀이 $2,000,000를 초과합니다.",
    "The overall champion takes home a Lamborghini Urus SE in addition to the cash prize. This makes it the richest tournament series ever hosted on the 1win platform.":
        "종합 챔피언은 현금 상금 외에 람보르기니 Urus SE를 받습니다. 이는 1win 플랫폼에서 개최된 역대 가장 풍성한 토너먼트 시리즈입니다.",
    "Daily satellite events start at just $1 buy-in, making the series accessible to players of all bankroll sizes. The Grand Final on May 15 has a guaranteed $500,000 prize pool.":
        "일일 위성 이벤트는 단 $1 바이인으로 시작하여 모든 규모의 뱅크롤을 가진 플레이어가 참가할 수 있습니다. 5월 15일 그랜드 파이널의 보장 상금 풀은 $500,000입니다.",
    "For crypto depositors, the full 600% package is available. Players depositing with fiat currencies (Visa, Mastercard, bank transfer) receive a 500% bonus package across four deposits.":
        "암호화폐 입금자는 전체 600% 패키지를 이용할 수 있습니다. 법정화폐(Visa, Mastercard, 은행 이체)로 입금하는 플레이어는 4번의 입금에 걸쳐 500% 보너스 패키지를 받습니다.",
    "This is the best time to join 1win, the extended bonus period means you have more time to take advantage of the most generous welcome offer in the industry.":
        "지금이 1win에 가입하기 가장 좋은 시기입니다. 연장된 보너스 기간은 업계에서 가장 관대한 웰컴 오퍼를 활용할 더 많은 시간을 의미합니다.",
    "UFC 315 is set for this Saturday and 1win has the best pre-fight odds on the market. The main event features the middleweight title bout with 1win offering +185 on the challenger, the most generous line available. Live in-play round betting will be available, and all UFC bets this weekend qualify for the accumulator bonus of up to 40% extra profit.":
        "UFC 315가 이번 토요일로 예정되어 있으며 1win이 시장 최고의 경기 전 배당률을 제공합니다. 메인 이벤트는 미들급 타이틀 전으로 1win이 도전자에게 +185를 제공하며, 가장 관대한 라인입니다. 라이브 인플레이 라운드 베팅이 제공되며, 이번 주말 모든 UFC 베팅은 최대 40% 추가 수익의 어큐뮬레이터 보너스를 받습니다.",
    "Join 1win today and get instant access to the latest promotions, tournaments, and exclusive bonuses. Use codeXLBONUSfor 600% on your first deposit.":
        "오늘 1win에 가입하고 최신 프로모션, 토너먼트, 독점 보너스에 즉시 접근하세요. 코드 XLBONUS를 사용하여 첫 입금 시 600% 보너스를 받으세요.",
    "Crypto deposits and withdrawals are completely free (0% fees). Card payments have a 2.5% processing fee. Bank transfers and regional methods (PIX, UPI) are free.":
        "암호화폐 입출금은 완전히 무료(0% 수수료)입니다. 카드 결제에는 2.5% 처리 수수료가 부과됩니다. 은행 이체 및 지역 방법(PIX, UPI)은 무료입니다.",
    # === POKER ===
    "Visa, Mastercard, crypto, e-wallets, choose how you play. All transactions secured with bank-grade encryption.":
        "Visa, Mastercard, 암호화폐, 전자 지갑 - 원하는 결제 방법을 선택하세요. 모든 거래는 은행 수준의 암호화로 보안됩니다.",
    "Whether you're a Texas Hold'em purist or an Omaha action junkie, we've got your game.":
        "텍사스 홀덤 순수주의자든 오마하 액션 매니아든, 귀하를 위한 게임이 있습니다.",
    "The king of poker. Two hole cards, five community cards, and infinite strategic depth. Cash games from micro-stakes $0.01/$0.02 all the way to high-roller $50/$100 tables.":
        "포커의 왕. 두 장의 홀 카드, 다섯 장의 커뮤니티 카드, 무한한 전략적 깊이. $0.01/$0.02 마이크로 스테이크에서 $50/$100 하이 롤러 테이블까지의 캐시 게임.",
    "Four hole cards, bigger pots, wilder action. Pot-Limit Omaha (PLO) is the game of choice for action junkies who love big swings and complex decisions.":
        "네 장의 홀 카드, 더 큰 팟, 더 격렬한 액션. 팟 리밋 오마하(PLO)는 큰 변동과 복잡한 결정을 좋아하는 액션 매니아들의 선호 게임입니다.",
    "All cards below 6 removed. Faster action, bigger hands, more drama. Flush beats a full house. The format that's taking over the poker world.":
        "6 이하의 모든 카드가 제거됩니다. 더 빠른 액션, 더 강한 패, 더 많은 드라마. 플러시가 풀하우스를 이깁니다. 포커 세계를 장악하고 있는 형식입니다.",
    "Freerolls, sit-and-go, and multi-table tournaments running every hour. Scheduled prize pools daily.":
        "매 시간 진행되는 프리롤, 싯앤고, 멀티 테이블 토너먼트. 매일 예정된 상금 풀.",
    "Large-field tournaments with massive scheduled prize pools. Deep stacks, structured blind levels, and satellite qualifiers available.":
        "대규모 보장 상금 풀의 대규모 토너먼트. 딥 스택, 구조화된 블라인드 레벨, 위성 예선 이용 가능.",
    "Jump in, play fast, win big. Single-table tournaments that start the moment enough players register. Quick action, quick payouts.":
        "바로 시작하고, 빠르게 플레이하고, 크게 이기세요. 충분한 플레이어가 등록되는 즉시 시작되는 단일 테이블 토너먼트. 빠른 액션, 빠른 지급.",
    "Zero buy-in, real prize pools. Perfect for building your bankroll from nothing. Multiple freerolls running every single day.":
        "제로 바이인, 실제 상금 풀. 아무것도 없는 상태에서 뱅크롤을 구축하기에 완벽합니다. 매일 여러 프리롤이 진행됩니다.",
    "Texas Hold'em, Omaha, tournaments with massive prize pools. Outsmart, outplay, outlast.":
        "텍사스 홀덤, 오마하, 대규모 상금 풀의 토너먼트. 더 영리하게, 더 잘 플레이하고, 더 오래 버티세요.",
    "Pick your stakes. From micro-grind to high-roller, there's always a seat waiting.":
        "스테이크를 선택하세요. 마이크로 그라인드부터 하이 롤러까지, 항상 자리가 기다리고 있습니다.",
    "Play up to 8 tables simultaneously. Maximize your volume and your win rate across multiple games.":
        "최대 8개 테이블을 동시에 플레이하세요. 여러 게임에 걸쳐 볼륨과 승률을 극대화하세요.",
    "Full hand history for every session. Review your play, analyze your decisions, and find your leaks.":
        "모든 세션의 전체 핸드 기록. 플레이를 검토하고, 결정을 분석하고, 약점을 찾으세요.",
    "Built-in HUD stats and session tracking. VPIP, PFR, and more, all the data you need to crush.":
        "내장된 HUD 통계 및 세션 추적. VPIP, PFR 등 크러시하는 데 필요한 모든 데이터.",
    "Play without being tracked. Anonymous tables prevent HUD mining and keep the games fair for everyone.":
        "추적 없이 플레이하세요. 익명 테이블은 HUD 마이닝을 방지하고 모든 사람에게 공정한 게임을 보장합니다.",
    "Every hand you play earns you money back. The more you grind, the more you earn, up to 50% rakeback.":
        "플레이하는 모든 핸드에서 돈을 돌려받습니다. 더 많이 그라인드할수록 더 많이 벌 수 있으며, 최대 50% 레이크백을 받습니다.",
    "1win's rakeback program returns a percentage of every pot's rake directly to your account. Higher volume = higher rakeback percentage. Grind harder, earn more.":
        "1win의 레이크백 프로그램은 모든 팟의 레이크 일정 비율을 계정으로 직접 반환합니다. 더 높은 볼륨 = 더 높은 레이크백 비율. 더 열심히 그라인드할수록 더 많이 벌 수 있습니다.",
    "On top of standard rakeback, weekly bonuses reward consistent play. Active players receive additional percentage boosts and exclusive tournament tickets.":
        "표준 레이크백 외에, 위클리 보너스가 지속적인 플레이를 보상합니다. 활성 플레이어는 추가 비율 부스트와 독점 토너먼트 티켓을 받습니다.",
    "1win Poker occupies a distinct position in the platform's product suite, it is not an afterthought added alongside slots and sports, but a fully developed poker room that caters to both recreational players and serious grinders. The room runs on a dedicated poker client with cash tables operating 24 hours a day at stakes ranging from micro to high, and a structured tournament calendar that includes scheduled prize pool events every day of the week. The Sunday $10,000 freeroll is a recurring fixture that draws significant participation and provides a low-risk way for new players to build a bankroll without an initial investment.":
        "1win 포커는 플랫폼의 제품군에서 독특한 위치를 차지합니다. 슬롯과 스포츠 옆에 덧붙인 것이 아니라, 레크리에이션 플레이어와 진지한 그라인더 모두를 위해 완전히 개발된 포커 룸입니다. 룸은 마이크로에서 하이까지 스테이크 범위의 캐시 테이블이 24시간 운영되는 전용 포커 클라이언트와 매주 매일 보장 상금 이벤트를 포함한 구조화된 토너먼트 캘린더로 운영됩니다. 일요일 $10,000 프리롤은 상당한 참여를 끌어내고 신규 플레이어가 초기 투자 없이 뱅크롤을 구축할 수 있는 저위험 방법을 제공하는 정기 이벤트입니다.",
    "Texas Hold'em is the primary game variant at 1win Poker, with No Limit cash tables and tournaments available across all stake levels. Omaha and Omaha Hi-Lo tables run alongside the main Hold'em offering, giving experienced players the option to switch formats based on traffic and preference. The table software includes hand history tracking, customizable table themes, four-color deck options, and multi-table support, allowing serious players to run multiple tables simultaneously from the same account. Sit-and-Go tournaments fire regularly throughout the day at all buy-in levels.":
        "텍사스 홀덤은 1win 포커의 주요 게임 변형으로, 모든 스테이크 레벨에서 노 리밋 캐시 테이블과 토너먼트를 이용할 수 있습니다. 오마하 및 오마하 하이-로 테이블이 메인 홀덤 제공과 함께 운영되어 경험 있는 플레이어가 트래픽과 선호도에 따라 형식을 전환할 수 있습니다. 테이블 소프트웨어에는 핸드 기록 추적, 사용자 지정 테이블 테마, 4색 덱 옵션, 멀티 테이블 지원이 포함되어 있어 진지한 플레이어가 동일한 계정에서 여러 테이블을 동시에 운영할 수 있습니다. 싯앤고 토너먼트는 모든 바이인 레벨에서 하루 종일 정기적으로 시작됩니다.",
    "1win offers Texas Hold'em, Omaha (PLO), and Short Deck poker. Both cash games and tournaments are available, with stakes ranging from micro ($0.01/$0.02) to high-roller ($5/$10+). Sit & Go, MTT, and freeroll tournaments run around the clock.":
        "1win은 텍사스 홀덤, 오마하(PLO), 숏 덱 포커를 제공합니다. 캐시 게임과 토너먼트 모두 이용 가능하며, 스테이크는 마이크로($0.01/$0.02)에서 하이 롤러($5/$10+)까지 다양합니다. 싯앤고, MTT, 프리롤 토너먼트가 24시간 운영됩니다.",
    "Yes. 1win offers up to 50% rakeback depending on your playing volume. Rakeback is calculated on every hand you play and credited to your account. Higher volume players unlock higher rakeback percentages plus weekly bonuses.":
        "네. 1win은 플레이 볼륨에 따라 최대 50% 레이크백을 제공합니다. 레이크백은 플레이하는 모든 핸드에 대해 계산되어 계정에 지급됩니다. 더 높은 볼륨 플레이어는 더 높은 레이크백 비율과 위클리 보너스를 잠금 해제합니다.",
    "Absolutely. 1win poker supports multi-tabling up to 8 tables simultaneously on desktop, and up to 4 tables on mobile. This lets you maximize your volume and win rate across multiple games.":
        "물론입니다. 1win 포커는 데스크탑에서 최대 8개 테이블, 모바일에서 최대 4개 테이블을 동시에 지원합니다. 이를 통해 여러 게임에 걸쳐 볼륨과 승률을 극대화할 수 있습니다.",
    "Yes. 1win runs multiple freeroll tournaments every day with real money prize pools and zero buy-in. They're the perfect way to build a bankroll from scratch or practice tournament strategy no-buy-in.":
        "네. 1win은 실제 돈 상금 풀과 제로 바이인으로 매일 여러 프리롤 토너먼트를 운영합니다. 아무것도 없는 상태에서 뱅크롤을 구축하거나 바이인 없이 토너먼트 전략을 연습하기에 완벽합니다.",
    # === REGISTRATION ===
    "Select from four registration options: one-click (fastest), mobile phone, email address, or social media login via Google or Facebook. All methods create a full 1win account with access to all products, bonuses, and payment options.":
        "네 가지 가입 옵션 중 하나를 선택하세요: 원클릭(가장 빠름), 휴대폰, 이메일 주소, Google 또는 Facebook을 통한 소셜 미디어 로그인. 모든 방법으로 모든 상품, 보너스, 결제 옵션에 접근 가능한 완전한 1win 계정을 생성합니다.",
    "Forgot your password? Use the \"Forgot Password\" link on the login screen. If you registered by phone, you will receive an SMS code to reset. If you registered by email, a reset link will be sent to your inbox. If you registered via social media, simply log in with that social account again, no password is required. For further login help, visit the1win login page.":
        "비밀번호를 잊으셨나요? 로그인 화면의 '비밀번호 분실' 링크를 사용하세요. 전화번호로 가입하셨다면 재설정을 위한 SMS 코드를 받으실 것입니다. 이메일로 가입하셨다면 재설정 링크가 이메일로 발송됩니다. 소셜 미디어로 가입하셨다면, 해당 소셜 계정으로 다시 로그인하시면 됩니다. 비밀번호가 필요 없습니다. 추가 로그인 도움이 필요하시면 1win 로그인 페이지를 방문하세요.",
    "Your second deposit earns a 140% bonus. Continue building your bankroll with this boosted second deposit. All four deposits in the welcome package are eligible, giving you maximum value from your initial funding.":
        "두 번째 입금 시 140% 보너스를 받습니다. 이 향상된 두 번째 입금으로 뱅크롤을 계속 구축하세요. 웰컴 패키지의 4번의 입금 모두 적격하여 초기 자금에서 최대 가치를 얻을 수 있습니다.",
    # === REVIEW ===
    "Live betting is a particular strength. The in-play section updates in real time with current scores, match timelines, and constantly refreshing odds. Live cash-out is available on selected markets, giving you control over your open bets. Live streaming is integrated directly into the betting interface, watch the event and bet simultaneously on the same screen. See our dedicatedsports betting pagefor a full breakdown.":
        "라이브 베팅은 특히 강점입니다. 인플레이 섹션은 현재 스코어, 경기 타임라인, 지속적으로 갱신되는 배당률로 실시간 업데이트됩니다. 선택된 시장에서 라이브 캐시아웃이 가능하여 오픈 베팅을 제어할 수 있습니다. 라이브 스트리밍이 베팅 인터페이스에 직접 통합되어 같은 화면에서 동시에 이벤트를 시청하고 베팅할 수 있습니다. 전체 분석은 스포츠 베팅 전용 페이지를 참조하세요.",
    "The 1win website uses a dark-themed design with blue and gold accents. Navigation is clean and logical, the main menu provides one-click access to Sport, Live, Casino, Poker, Aviator, and Promotions. Finding specific events or games is easy through the search function and genre/provider filters in the casino.":
        "1win 웹사이트는 파란색과 금색 액센트의 다크 테마 디자인을 사용합니다. 내비게이션은 깔끔하고 논리적이며, 메인 메뉴에서 스포츠, 라이브, 카지노, 포커, Aviator, 프로모션에 원클릭으로 접근할 수 있습니다. 검색 기능과 카지노의 장르/공급업체 필터를 통해 특정 이벤트나 게임을 쉽게 찾을 수 있습니다.",
    "The desktop version provides the most complete view, with a three-column layout showing the sports navigation, the event list, and the betslip simultaneously. The mobile website is fully responsive and retains all functionality, you can place bets, make deposits, play casino games, and manage your account entirely from a mobile browser without needing to download the app.":
        "데스크탑 버전은 스포츠 내비게이션, 이벤트 목록, 베팅 슬립을 동시에 보여주는 3열 레이아웃으로 가장 완전한 뷰를 제공합니다. 모바일 웹사이트는 완전히 반응형이며 모든 기능을 유지하여, 앱 다운로드 없이도 모바일 브라우저에서 완전히 베팅, 입금, 카지노 게임, 계정 관리를 할 수 있습니다.",
    "Beyond traditional sports, 1win covers eSports with similar depth, CS2, Dota 2, and League of Legends matches include map winner markets, kill totals, and player performance props. Political betting and entertainment markets (awards ceremonies, TV show outcomes) are also available, broadening the appeal beyond traditional sports bettors.":
        "전통적인 스포츠 외에도 1win은 e스포츠를 유사한 깊이로 커버합니다. CS2, Dota 2, 리그 오브 레전드 경기에는 맵 승자 시장, 킬 합계, 플레이어 성과 소품이 포함됩니다. 정치 베팅과 엔터테인먼트 시장(시상식, TV 쇼 결과)도 이용 가능하여 전통적인 스포츠 베터 이상으로 매력을 넓힙니다.",
    "1win supports over 50 payment methods for deposits and withdrawals. Options include Visa and Mastercard bank cards, e-wallets (Skrill, Neteller, Perfect Money), mobile banking (bKash, Nagad, Easypaisa, JazzCash, M-Pesa, MTN MoMo), and over 20 cryptocurrencies (Bitcoin, Ethereum, USDT, Litecoin, XRP, BNB, Tron, and more).":
        "1win은 입출금을 위해 50개 이상의 결제 수단을 지원합니다. Visa 및 Mastercard 은행 카드, 전자 지갑(Skrill, Neteller, Perfect Money), 모바일 뱅킹(bKash, Nagad, Easypaisa, JazzCash, M-Pesa, MTN MoMo), 20개 이상의 암호화폐(비트코인, 이더리움, USDT, 라이트코인, XRP, BNB, 트론 등)가 포함됩니다.",
    "An extensive FAQ section covers the most common questions and is a good first stop before contacting support. The FAQ covers registration, login, deposits, withdrawals, sports betting rules, casino game rules, and bonus terms in detail.":
        "광범위한 FAQ 섹션이 가장 일반적인 질문을 다루며 지원 문의 전 첫 번째 방문지로 좋습니다. FAQ는 가입, 로그인, 입금, 출금, 스포츠 베팅 규칙, 카지노 게임 규칙, 보너스 약관을 상세히 커버합니다.",
    "Yes. 1win is fully accessible on mobile via the browser (fully responsive design) or the dedicated app available for Android and iOS. The app offers the best mobile experience with Face ID login, push notifications, and fast performance. Download details are on the1win app page.":
        "네. 1win은 브라우저(완전 반응형 디자인) 또는 Android 및 iOS용 전용 앱을 통해 모바일에서 완전히 이용 가능합니다. 앱은 Face ID 로그인, 푸시 알림, 빠른 성능으로 최고의 모바일 경험을 제공합니다. 다운로드 세부 사항은 1win 앱 페이지에서 확인하세요.",
    # === SPORTS ===
    "From the world's biggest leagues to underground fight cards, every sport, every market, every edge.":
        "세계 최대 리그부터 언더그라운드 파이트 카드까지, 모든 스포츠, 모든 시장, 모든 엣지.",
    "Premier League, Champions League, La Liga, Serie A, Bundesliga, every match, every market. Pre-match and live in-play with cash-out.":
        "프리미어 리그, 챔피언스 리그, 라 리가, 세리에 A, 분데스리가 - 모든 경기, 모든 시장. 캐시아웃 기능의 사전 베팅 및 라이브 인플레이.",
    "NBA, EuroLeague, NCAA, spreads, totals, player props, and quarter-by-quarter live betting. Slam dunk your bankroll.":
        "NBA, 유로리그, NCAA - 스프레드, 합계, 선수 소품, 쿼터별 라이브 베팅. 뱅크롤을 슬램 덩크하세요.",
    "Grand Slams, ATP, WTA, match winners, set betting, game-by-game live markets. Ace every bet.":
        "그랜드 슬램, ATP, WTA - 경기 승자, 세트 베팅, 게임별 라이브 시장. 모든 베팅을 에이스로 마무리하세요.",
    "UFC, Bellator, ONE Championship, method of victory, round betting, fight props. Get in the cage.":
        "UFC, Bellator, ONE Championship - 승리 방법, 라운드 베팅, 파이트 소품. 케이지에 들어가세요.",
    "CS2, Dota 2, League of Legends, Valorant, map betting, kill totals, tournament outrights. Level up your bets.":
        "CS2, Dota 2, 리그 오브 레전드, 발로란트 - 맵 베팅, 킬 합계, 토너먼트 아웃라이트. 베팅을 레벨업하세요.",
    "IPL, T20 World Cup, Test Matches, top batsman, session runs, match outcomes. Six it to the boundary.":
        "IPL, T20 월드컵, 테스트 매치 - 최다 타자, 세션 런, 경기 결과. 경계선까지 식스를 날리세요.",
    "The game is on. Odds shift every second. Seize the moment or watch it slip away, this is where the sharpest bettors make their money.":
        "경기가 시작됩니다. 배당률이 매초 변합니다. 순간을 포착하거나 놓쳐버리거나 - 여기가 가장 날카로운 베터들이 돈을 버는 곳입니다.",
    "Odds update every second during live play. 1,000+ markets open simultaneously across multiple events. React faster, win bigger.":
        "라이브 플레이 중 매초 배당률이 업데이트됩니다. 여러 이벤트에 걸쳐 1,000개 이상의 시장이 동시에 열립니다. 더 빠르게 반응하고, 더 크게 이기세요.",
    "Lock in profits or cut your losses before the final whistle. Full or partial cash-out available on most live markets. Total control.":
        "최종 휘슬 전에 수익을 확정하거나 손실을 줄이세요. 대부분의 라이브 시장에서 전체 또는 부분 캐시아웃이 가능합니다. 완전한 제어.",
    "Watch and bet simultaneously on 1,000+ events streamed free directly within the 1win platform. No third-party apps needed.":
        "1win 플랫폼 내에서 직접 무료로 스트리밍되는 1,000개 이상의 이벤트를 동시에 시청하고 베팅하세요. 타사 앱이 필요 없습니다.",
    "Push notifications for score changes, goal alerts, and odds movements. Never miss a betting opportunity, whether you're on desktop or mobile.":
        "스코어 변경, 골 알림, 배당률 변동에 대한 푸시 알림. 데스크탑이든 모바일이든 베팅 기회를 절대 놓치지 마세요.",
    "Singles, accumulators, system bets, choose your weapon and go all in.":
        "단식, 어큐뮬레이터, 시스템 베팅 - 무기를 선택하고 올인하세요.",
    "One selection, one outcome. The simplest and most reliable way to bet. Back a single event and collect.":
        "하나의 선택, 하나의 결과. 가장 간단하고 신뢰할 수 있는 베팅 방법. 단일 이벤트에 베팅하고 수금하세요.",
    "Combine multiple selections for multiplied payouts. 5-fold, 10-fold, 20-fold, stack the odds in your favor.":
        "여러 선택을 결합하여 배수 지급을 받으세요. 5배, 10배, 20배 - 유리하게 배당률을 쌓으세요.",
    "Cover multiple combinations within your selections. Win even if not every pick hits. Strategic flexibility.":
        "선택 내에서 여러 조합을 커버하세요. 모든 픽이 맞지 않아도 이길 수 있습니다. 전략적 유연성.",
    "Lightning-fast combo bets on live events. Quick picks for instant action when the game is heating up.":
        "라이브 이벤트에서 번개처럼 빠른 콤보 베팅. 경기가 달아오를 때 즉각적인 액션을 위한 빠른 픽.",
    "Three steps to your first winning bet. It's that simple.":
        "첫 번째 당첨 베팅을 위한 3단계. 정말 그만큼 간단합니다.",
    "Enter your stake, confirm your bet, and watch the action. Cash out anytime or ride it to the final whistle.":
        "스테이크를 입력하고, 베팅을 확인하고, 액션을 지켜보세요. 언제든지 캐시아웃하거나 최종 휘슬까지 홀드하세요.",
    "Beyond the welcome offer, 1win provides ongoing value through accumulator bonuses, cashback on losses, reload promotions, and tournament-specific boosts around major events like the Champions League, the World Cup, Grand Slams, and UFC fight nights. The1win VIP Clubadds another layer of long-term value, with loyal bettors receiving personal managers, exclusive odds, higher withdrawal limits, and invitations to private tournaments. View the full list of available offers on ourpromotions page.":
        "웰컴 오퍼 외에도 1win은 어큐뮬레이터 보너스, 손실 캐시백, 리로드 프로모션, 챔피언스 리그, 월드컵, 그랜드 슬램, UFC 파이트 나이트 등 주요 이벤트 관련 토너먼트별 부스트를 통해 지속적인 가치를 제공합니다. 1win VIP 클럽은 충성 베터들에게 개인 매니저, 독점 배당률, 높은 출금 한도, 프라이빗 토너먼트 초대를 제공하는 장기적 가치의 또 다른 레이어를 추가합니다. 이용 가능한 오퍼 전체 목록은 프로모션 페이지에서 확인하세요.",
    "The minimum bet at 1win is typically $0.10 (or equivalent in your currency). Maximum bet limits vary by sport, league, and market, high-roller limits are available for popular events.":
        "1win의 최소 베팅은 일반적으로 $0.10(또는 통화 등가액)입니다. 최대 베팅 한도는 스포츠, 리그, 시장에 따라 다르며, 인기 이벤트에는 하이 롤러 한도가 제공됩니다.",
    "Absolutely. 1win has a dedicated esports section covering CS2, Dota 2, League of Legends, Valorant, and more. Markets include match winner, map betting, kill totals, and tournament outrights.":
        "물론입니다. 1win에는 CS2, Dota 2, 리그 오브 레전드, 발로란트 등을 커버하는 전용 e스포츠 섹션이 있습니다. 시장에는 경기 승자, 맵 베팅, 킬 합계, 토너먼트 아웃라이트가 포함됩니다.",
    # === VIP ===
    "Every bet moves you up. The higher your tier, the bigger your perks.":
        "모든 베팅이 등급을 높입니다. 등급이 높을수록 혜택이 커집니다.",
    "Weekly cashback 3%Standard supportBasic bonuses":
        "위클리 캐시백 3% | 기본 지원 | 기본 보너스",
    "Weekly cashback 5%Priority supportBirthday bonus":
        "위클리 캐시백 5% | 우선 지원 | 생일 보너스",
    "Weekly cashback 8%Personal managerHigher limits":
        "위클리 캐시백 8% | 개인 매니저 | 높은 한도",
    "Weekly cashback 10%VIP events accessLuxury gifts":
        "위클리 캐시백 10% | VIP 이벤트 접근 | 명품 선물",
    "Weekly cashback 15%Unlimited withdrawalsConcierge service":
        "위클리 캐시백 15% | 무제한 출금 | 컨시어지 서비스",
    "Personal managers, unlimited withdrawals, luxury gifts, and invitations to exclusive events. This is the VIP life.":
        "개인 매니저, 무제한 출금, 명품 선물, 독점 이벤트 초대. 이것이 VIP 라이프입니다.",
    "Increased deposit, withdrawal, and bet limits. Diamond members enjoy virtually unlimited betting capacity.":
        "높아진 입금, 출금, 베팅 한도. 다이아몬드 회원은 사실상 무제한 베팅 용량을 즐길 수 있습니다.",
    "VIP-only tournaments, live events, and experiences. From private poker tables to luxury sporting events.":
        "VIP 전용 토너먼트, 라이브 이벤트, 경험. 프라이빗 포커 테이블부터 명품 스포츠 이벤트까지.",
    "Rolex watches, sports cars, VIP travel packages, and yacht party invitations. The higher your tier, the bigger the gifts.":
        "롤렉스 시계, 스포츠카, VIP 여행 패키지, 요트 파티 초대. 등급이 높을수록 선물이 커집니다.",
    "A generous cash bonus on your birthday. Up to $1,000 for Diamond members, because winners celebrate big.":
        "생일에 풍성한 현금 보너스. 다이아몬드 회원에게는 최대 $1,000, 승자는 크게 축하하니까요.",
    "There's no application. Just play. Your VIP status is earned automatically.":
        "신청서가 없습니다. 그냥 플레이하세요. VIP 상태는 자동으로 획득됩니다.",
    "Every wager accumulates VIP points. Hit the tier threshold and you're automatically upgraded.":
        "모든 베팅이 VIP 포인트를 쌓습니다. 등급 임계값에 도달하면 자동으로 업그레이드됩니다.",
    "Your benefits activate instantly upon tier promotion. Personal manager contacts you within 24 hours.":
        "등급 승급 시 즉시 혜택이 활성화됩니다. 개인 매니저가 24시간 이내에 연락합니다.",
    "Platinum and Diamond members receive premium gifts that match their lifestyle.":
        "플래티넘 및 다이아몬드 회원은 라이프스타일에 맞는 프리미엄 선물을 받습니다.",
    "Submariner, Daytona, and GMT-Master II models for top-tier players.":
        "최상위 등급 플레이어를 위한 서브마리너, 데이토나, GMT-마스터 II 모델.",
    "Porsche, Ferrari, and Lamborghini deliveries for Diamond members.":
        "다이아몬드 회원을 위한 포르쉐, 페라리, 람보르기니 배달.",
    "All-expenses-paid trips to Monaco, Las Vegas, Dubai, and Macau.":
        "모나코, 라스베가스, 두바이, 마카오로의 모든 비용 포함 여행.",
    "Exclusive VIP yacht events in Ibiza, Miami, and the French Riviera.":
        "이비자, 마이애미, 프랑스 리비에라의 독점 VIP 요트 이벤트.",
    "5 tiers of escalating luxury. Diamond members get 5x Lucky Drive tickets, priority support, and bespoke experiences.":
        "5단계의 점진적 명품. 다이아몬드 회원은 Lucky Drive 티켓 5배, 우선 지원, 맞춤형 경험을 받습니다.",
    "The 1win VIP Club is a structured loyalty program that rewards consistent activity with progressively more valuable benefits across five tiers: Bronze, Silver, Gold, Platinum, and Diamond. Entry to the VIP program is automatic, every registered player starts accumulating loyalty points from their first bet, and advancement through the tiers is determined entirely by your volume of play over time. There are no invitation requirements and no manual application process. The more you bet across sports, casino, poker, and Aviator, the faster you advance through the tier system.":
        "1win VIP 클럽은 브론즈, 실버, 골드, 플래티넘, 다이아몬드의 5단계에 걸쳐 점진적으로 더 가치 있는 혜택으로 지속적인 활동을 보상하는 구조적 충성도 프로그램입니다. VIP 프로그램 입회는 자동이며, 모든 등록 플레이어는 첫 번째 베팅부터 충성도 포인트를 쌓기 시작하고, 등급 상승은 전적으로 시간에 따른 플레이 볼륨에 의해 결정됩니다. 초대 요건이 없고 수동 신청 과정이 없습니다. 스포츠, 카지노, 포커, Aviator에서 더 많이 베팅할수록 등급 시스템을 더 빠르게 올라갑니다.",
    "Diamond tier, the highest level of the 1win VIP Club, provides the most comprehensive package available: a personal VIP manager assigned exclusively to your account, completely customized bonus structures negotiated to match your playing style, the highest available withdrawal limits, invitation to 1win-sponsored events and real-world experiences, and 5x multipliers on Lucky Drive ticket accumulation. Diamond players also receive preferential odds adjustments on major sports events and access to private high-limit casino tables not available to the general player pool.":
        "다이아몬드 등급, 1win VIP 클럽의 최고 수준은 가장 포괄적인 패키지를 제공합니다: 계정에 독점적으로 배정된 개인 VIP 매니저, 플레이 스타일에 맞게 협상된 완전히 맞춤화된 보너스 구조, 최고 가능한 출금 한도, 1win 후원 이벤트 및 실세계 경험 초대, Lucky Drive 티켓 적립 5배 배수. 다이아몬드 플레이어는 또한 주요 스포츠 이벤트에서 우선적인 배당률 조정과 일반 플레이어 풀에서 이용할 수 없는 프라이빗 고한도 카지노 테이블에 접근할 수 있습니다.",
    "There's no application or invitation required. Simply play on 1win and your VIP status is calculated automatically based on your total wagering volume. You start at Bronze and progress upward.":
        "신청서나 초대가 필요 없습니다. 1win에서 그냥 플레이하면 VIP 상태가 총 베팅 볼륨을 기준으로 자동으로 계산됩니다. 브론즈에서 시작하여 위로 올라갑니다.",
    "VIP status is reviewed monthly. To maintain your tier, you need to keep playing regularly. Inactive accounts may be downgraded after 90 days of no activity.":
        "VIP 상태는 월별로 검토됩니다. 등급을 유지하려면 정기적으로 플레이해야 합니다. 비활성 계정은 90일 활동 없이 다운그레이드될 수 있습니다.",
    "Personal managers are assigned at Gold tier and above. Once you reach Gold status, your dedicated manager will contact you within 24 hours via your preferred communication channel.":
        "개인 매니저는 골드 등급 이상에서 배정됩니다. 골드 상태에 도달하면 전담 매니저가 24시간 이내에 선호하는 커뮤니케이션 채널을 통해 연락합니다.",
    "Cashback is calculated weekly on your net losses. The percentage depends on your VIP tier (3% for Bronze up to 15% for Diamond). It's credited automatically every Monday.":
        "캐시백은 순손실에 대해 매주 계산됩니다. 비율은 VIP 등급에 따라 달라집니다(브론즈 3%에서 다이아몬드 15%까지). 매주 월요일 자동으로 지급됩니다.",
    "Absolutely not. The VIP Club is completely free. There are no membership fees, hidden charges, or subscription costs. Your VIP status is earned through play, not purchased.":
        "전혀 그렇지 않습니다. VIP 클럽은 완전히 무료입니다. 회원비, 숨겨진 요금, 구독 비용이 없습니다. VIP 상태는 플레이를 통해 획득하는 것이지 구매하는 것이 아닙니다.",
    # === WEBSITE ===
    "Everything you need to know about the 1win website at a glance.":
        "1win 웹사이트에 대해 알아야 할 모든 것을 한눈에.",
    "Logging in to the 1win website is straightforward. Click the Login button in the top right corner of the homepage. Enter your registered phone number or email address along with your password. If you signed up through a social account, simply click the corresponding social login button (Google, Facebook) and you will be authenticated automatically. Two-factor authentication is available for additional security, we recommend enabling it from your account settings.":
        "1win 웹사이트 로그인은 간단합니다. 홈페이지 오른쪽 상단의 로그인 버튼을 클릭하세요. 등록된 전화번호 또는 이메일 주소와 비밀번호를 입력하세요. 소셜 계정으로 가입하셨다면, 해당 소셜 로그인 버튼(Google, Facebook)을 클릭하면 자동으로 인증됩니다. 추가 보안을 위해 이중 인증을 사용할 수 있으며, 계정 설정에서 활성화하는 것을 권장합니다.",
    "One platform. Seven product verticals. Everything under one login.":
        "하나의 플랫폼. 7개의 제품 버티컬. 하나의 로그인으로 모든 것.",
    "The 1win poker room offers Texas Hold'em and Omaha at a range of stakes, from micro-limit tables for new players to high-stakes rooms for experienced players. Scheduled tournaments run daily with scheduled prize pools. The poker client is available directly in the browser or via the 1win app, no separate software download required. Sit-and-go tournaments are available around the clock.":
        "1win 포커 룸은 신규 플레이어를 위한 마이크로 리밋 테이블부터 경험 있는 플레이어를 위한 하이 스테이크 룸까지 다양한 스테이크의 텍사스 홀덤과 오마하를 제공합니다. 보장 상금 풀의 예정된 토너먼트가 매일 운영됩니다. 포커 클라이언트는 브라우저에서 직접 또는 1win 앱을 통해 이용 가능하며, 별도의 소프트웨어 다운로드가 필요 없습니다. 싯앤고 토너먼트는 24시간 이용 가능합니다.",
    "Your first deposit to the 1win website receives a 130% match bonus. Deposit $100 and receive $130 in bonus funds, giving you $230 total to play with on day one.":
        "1win 웹사이트에 첫 입금 시 130% 매칭 보너스를 받습니다. $100 입금 시 $130의 보너스 자금을 받아, 첫날 총 $230으로 플레이할 수 있습니다.",
    "Your second deposit on the 1win website earns a 140% bonus. This builds on the foundation of your first deposit bonus, extending your bankroll significantly.":
        "1win 웹사이트에 두 번째 입금 시 140% 보너스를 받습니다. 첫 번째 입금 보너스의 기반 위에 쌓여 뱅크롤을 크게 확장합니다.",
    "The third deposit earns a 160% match. At this stage the cumulative bonus value becomes substantial, a compelling reason to keep coming back to the 1win website.":
        "세 번째 입금 시 160% 매칭 보너스를 받습니다. 이 단계에서 누적 보너스 가치가 상당해지며, 1win 웹사이트로 계속 돌아오게 하는 강력한 이유가 됩니다.",
    "The fourth and final welcome deposit earns the highest single-deposit rate at 170%. Combined with crypto payments, the total across all four deposits reaches 600%.":
        "네 번째이자 마지막 웰컴 입금은 170%의 단일 입금 최고 비율을 받습니다. 암호화폐 결제와 결합하면 4번의 입금 총합이 600%에 달합니다.",
    "Accessing the 1win website depends on your location. In most countries, the platform is fully accessible by visiting 1win.pro directly in your browser. However, in some regions internet service providers block the main domain due to local gambling regulations. In these cases, there are three reliable ways to continue using the platform without interruption.":
        "1win 웹사이트 접근은 위치에 따라 다릅니다. 대부분의 국가에서 브라우저에서 직접 1win.pro를 방문하여 플랫폼에 완전히 접근할 수 있습니다. 그러나 일부 지역에서는 현지 도박 규정으로 인해 인터넷 서비스 제공업체가 메인 도메인을 차단합니다. 이 경우 중단 없이 플랫폼을 계속 사용할 수 있는 3가지 신뢰할 수 있는 방법이 있습니다.",
    "The second option is to download the 1win mobile app. Available for both Android (APK direct download) and iOS (App Store), the app bypasses ISP-level domain blocks entirely. It connects via its own routing infrastructure, making it the most reliable long-term access method. The app supports all website features including sports betting, casino, Aviator, poker, and full account management.":
        "두 번째 옵션은 1win 모바일 앱을 다운로드하는 것입니다. Android(APK 직접 다운로드) 및 iOS(App Store) 모두 이용 가능한 앱은 ISP 수준 도메인 차단을 완전히 우회합니다. 자체 라우팅 인프라를 통해 연결되어 가장 신뢰할 수 있는 장기 접근 방법입니다. 앱은 스포츠 베팅, 카지노, Aviator, 포커, 전체 계정 관리를 포함한 모든 웹사이트 기능을 지원합니다.",
    "Yes. The 1win website operates under a Curacao eGaming license, which requires the platform to meet regulatory standards for fairness, data security, and financial protection. The site uses SSL/TLS encryption for all connections. Game outcomes are certified by independent RNG auditors. 1win has operated since 2016 and processes millions of bets annually across its global player base.":
        "네. 1win 웹사이트는 Curaçao 8048/JAZ 라이선스 하에 운영되며, 플랫폼이 공정성, 데이터 보안, 금융 보호를 위한 규제 기준을 충족해야 합니다. 사이트는 모든 연결에 SSL/TLS 암호화를 사용합니다. 게임 결과는 독립적인 RNG 감사자에 의해 인증됩니다. 1win은 2016년부터 운영되어 전 세계 플레이어 기반에서 연간 수백만 건의 베팅을 처리합니다.",
    "Yes. The 1win website is fully optimised for mobile browsers on both Android and iOS. Alternatively, download the dedicated 1win mobile app for the best experience, it loads faster, supports push notifications, and includes all the same features as the desktop website. The Android APK is available directly from the 1win website; iOS users can download from the App Store.":
        "네. 1win 웹사이트는 Android와 iOS의 모바일 브라우저에 완전히 최적화되어 있습니다. 또는 최고의 경험을 위해 전용 1win 모바일 앱을 다운로드하세요. 더 빠르게 로드되고, 푸시 알림을 지원하며, 데스크탑 웹사이트와 동일한 모든 기능을 포함합니다. Android APK는 1win 웹사이트에서 직접 이용 가능하며, iOS 사용자는 App Store에서 다운로드할 수 있습니다.",
    "Lucky Drive is a unique promotional game exclusive to the 1win website. Players complete daily tasks and accumulate points that contribute to a progress bar. When the bar fills, players spin a wheel for prizes including cash bonuses, free bets, and merchandise, including the chance to win a luxury car. It is one of the most distinctive features of the 1win platform and is available to all registered players. Visit theLucky Drive pageto learn more.":
        "Lucky Drive는 1win 웹사이트 독점 고유 프로모션 게임입니다. 플레이어는 일일 작업을 완료하고 진행 바에 기여하는 포인트를 적립합니다. 바가 가득 차면 플레이어는 현금 보너스, 무료 베팅, 상품을 위한 휠을 돌리며, 명품 자동차를 당첨받을 기회가 있습니다. 1win 플랫폼에서 가장 독특한 기능 중 하나로 모든 등록 플레이어에게 제공됩니다. Lucky Drive 페이지를 방문하여 자세히 알아보세요.",
    # === MALAWI / MALAYSIA / SINGAPORE / SOUTH AFRICA / TANZANIA ===
    "1win Malawi is built for the world's largest cricket market. With comprehensive coverage of the Indian Premier League (IPL), ICC World Cup tournaments, bilateral series involving the Indian national team, and domestic competitions, 1win delivers more cricket betting markets than virtually any other international platform accessible to Indian players. The platform supports Indian Rupee (INR) and integrates with UPI, Paytm, and PhonePe, the payment methods used by 12,000+ millions of Indians daily.":
        "1win 말라위는 현지 결제 수단, 크리켓 베팅, 스포츠 시장을 지원하는 플랫폼입니다. 1win은 Curaçao 8048/JAZ 라이선스로 운영되며 광범위한 스포츠 베팅 및 카지노 게임을 제공합니다. XLBONUS 코드를 사용하여 최대 600% 보너스를 받으세요.",
    "1win Malawi offers the widest range of Indian payment methods of any international operator, including the most popular UPI apps and digital wallets used by Indian players daily.":
        "1win 말라위는 현지 모바일 머니 및 암호화폐를 포함한 다양한 결제 수단을 지원합니다.",
    "Airtel Money deposits arrive instantly via the Airtel mobile money platform. Malawi's most-used payment method. Withdrawals back to Airtel Money clear in minutes during business hours.":
        "Airtel Money 입금은 Airtel 모바일 머니 플랫폼을 통해 즉시 도착합니다. 말라위에서 가장 많이 사용되는 결제 수단입니다. Airtel Money 출금은 영업 시간 중 몇 분 내에 처리됩니다.",
    "Direct bank transfer from any Malawian bank account via National Bank of Malawi or Standard Bank. Suitable for larger deposits. Withdrawals clear in 1-3 business days.":
        "National Bank of Malawi 또는 Standard Bank를 통한 모든 말라위 은행 계좌에서 직접 은행 이체. 대금액 입금에 적합합니다. 출금은 1-3 영업일 이내에 처리됩니다.",
    "BTC, ETH, USDT TRC-20 and more. Fastest option overall, 5 minute deposits, no Reserve Bank of Malawi reporting required. Recommended for larger balances.":
        "BTC, ETH, USDT TRC-20 등. 전체적으로 가장 빠른 옵션으로 5분 입금이 가능합니다. 말라위 중앙은행 신고 불필요. 대금액에 권장됩니다.",
    "1win Malaysia is built for the world's largest cricket market. With comprehensive coverage of the Indian Premier League (IPL), ICC World Cup tournaments, bilateral series involving the Indian national team, and domestic competitions, 1win delivers more cricket betting markets than virtually any other international platform accessible to Indian players. The platform supports Indian Rupee (INR) and integrates with UPI, Paytm, and PhonePe, the payment methods used by 12,000+ millions of Indians daily.":
        "1win 말레이시아는 현지 결제 수단, 스포츠 베팅, 카지노 게임을 지원하는 플랫폼입니다. 1win은 Curaçao 8048/JAZ 라이선스로 운영됩니다. XLBONUS 코드로 최대 600% 보너스를 받으세요.",
    "1win Malaysia offers the widest range of Indian payment methods of any international operator, including the most popular UPI apps and digital wallets used by Indian players daily.":
        "1win 말레이시아는 Touch 'n Go, Boost 지갑, 은행 이체를 포함한 다양한 현지 결제 수단을 지원합니다.",
    "Malaysia's most popular e-wallet. Instant deposits via TnG QR code or linked card. Withdrawals back to TnG within minutes.":
        "말레이시아에서 가장 인기 있는 전자 지갑입니다. TnG QR 코드 또는 연동 카드를 통해 즉시 입금할 수 있습니다. TnG 출금은 몇 분 이내에 처리됩니다.",
    "Boost wallet deposits work instantly. A common choice for Malaysian mobile-first players who want fast top-ups.":
        "Boost 지갑 입금은 즉시 처리됩니다. 빠른 충전을 원하는 말레이시아 모바일 우선 플레이어들에게 일반적인 선택입니다.",
    "Direct bank transfer from any Malaysian bank via FPX. Withdraw to your Maybank, CIMB, Public Bank or RHB account in 1, 3 business days.":
        "FPX를 통한 모든 말레이시아 은행에서 직접 은행 이체. Maybank, CIMB, Public Bank 또는 RHB 계좌로 1-3 영업일 이내에 출금할 수 있습니다.",
    "BTC, ETH, USDT TRC-20 and more. Fastest option, 5 minute deposits, no Bank Negara reporting required. Recommended for larger balances.":
        "BTC, ETH, USDT TRC-20 등. 가장 빠른 옵션으로 5분 입금 가능. Bank Negara 신고 불필요. 대금액에 권장됩니다.",
    "1win Singapore is built for the world's largest cricket market. With comprehensive coverage of the Indian Premier League (IPL), ICC World Cup tournaments, bilateral series involving the Indian national team, and domestic competitions, 1win delivers more cricket betting markets than virtually any other international platform accessible to Indian players. The platform supports Indian Rupee (INR) and integrates with UPI, Paytm, and PhonePe, the payment methods used by 12,000+ millions of Indians daily.":
        "1win 싱가포르는 현지 결제 수단, 스포츠 베팅, 카지노를 지원하는 플랫폼입니다. 1win은 Curaçao 8048/JAZ 라이선스로 운영됩니다. XLBONUS 코드로 최대 600% 보너스를 받으세요.",
    "1win Singapore offers the widest range of Indian payment methods of any international operator, including the most popular UPI apps and digital wallets used by Indian players daily.":
        "1win 싱가포르는 PayNow, GrabPay, NETS 등 현지 결제 수단을 지원합니다.",
    "Singapore's instant interbank transfer system. Deposits arrive in seconds via QR or mobile number. Withdrawals back to your linked bank account within minutes during business hours.":
        "싱가포르의 즉시 은행 간 이체 시스템. QR 코드 또는 휴대폰 번호를 통해 초 단위로 입금됩니다. 영업 시간 중 연결된 은행 계좌로 출금은 몇 분 이내에 처리됩니다.",
    "GrabPay deposits work instantly across Singapore. NETS provides direct bank-account top-ups via the NETS network used at ATMs and POS terminals across the country.":
        "GrabPay 입금은 싱가포르 전역에서 즉시 처리됩니다. NETS는 전국 ATM 및 POS 단말기에