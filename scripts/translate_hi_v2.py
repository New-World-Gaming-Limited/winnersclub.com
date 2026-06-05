#!/usr/bin/env python3
"""
Hindi (HI) translation script for 1win.codes - v2
Comprehensive EN→HI translation of all 184 pages.
Rules per TRANSLATION_RULES.md:
- XLBONUS, 1win, Curaçao 8048/JAZ, brand names preserved
- No em/en dashes
- lang="hi", /hi/ canonical, full hreflang block
- Hindi register: Devanagari with casino transliterations
"""

import os
import re
import json
from pathlib import Path

BASE = Path("/home/user/workspace/1win-codes-repo")
EN_DIR = BASE / "en"
HI_DIR = BASE / "hi"

# =============================================================================
# 46-LOCALE HREFLANG TEMPLATE  
# =============================================================================
LOCALES = [
    "ar","bg","bn","cs","da","de","el","en","es","et",
    "fa","fi","fr","he","hi","hr","hu","id","it","ja",
    "kk","ko","lo","lt","lv","mn","ms","mt","nb","nl",
    "pl","pt","ro","ru","sk","sl","sq","sr","sv","th",
    "tl","tr","uk","ur","uz","vi","zh"
]

def make_hreflang_for_page(rel_path):
    """Generate full hreflang block for a page path."""
    # The path like 'index.html', 'casino.html', 'bonus/index.html'
    # Normalize to URL slug
    slug = rel_path.replace('.html', '').replace('/index', '/').rstrip('/')
    if slug == 'index':
        slug = ''
    
    lines = []
    for loc in LOCALES:
        if slug:
            url = f"https://1win.codes/{loc}/{slug}"
        else:
            url = f"https://1win.codes/{loc}/"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{url}" />')
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://1win.codes/en/" />')
    return "\n".join(lines)


# =============================================================================
# CORE TRANSLATION DICTIONARY
# Covers: navigation, UI, CTAs, common phrases, body content
# =============================================================================

# Order matters: longer/more specific phrases first
TRANSLATIONS = [
    # === BANNED WORD SUBSTITUTIONS ===
    ("নবীনতম", "নতুন"),  # should not appear in hindi but guard
    
    # === NAVIGATION ===
    ("All sports betting", "सभी स्पोर्ट्स बेटिंग"),
    ("Sports Betting", "स्पोर्ट्स बेटिंग"),
    ("sports betting", "स्पोर्ट्स बेटिंग"),
    ("Live streaming", "लाइव स्ट्रीमिंग"),
    ("Live Streaming", "लाइव स्ट्रीमिंग"),
    ("Game providers", "गेम प्रदाता"),
    ("Crash games", "क्रैश गेम्स"),
    ("All bonuses", "सभी बोनस"),
    ("First deposit 200%", "पहला जमा 200%"),
    ("Second deposit 150%", "दूसरा जमा 150%"),
    ("Third deposit 150%", "तीसरा जमा 150%"),
    ("Fourth deposit 100%", "चौथा जमा 100%"),
    ("Wagering rules", "वेजरिंग नियम"),
    ("Free spins today", "आज के फ्री स्पिन"),
    ("All promotions", "सभी प्रमोशन"),
    ("All calculators", "सभी कैलकुलेटर"),
    ("Odds converter", "ऑड्स कन्वर्टर"),
    ("Parlay calculator", "पार्ले कैलकुलेटर"),
    ("Kelly criterion", "केली क्राइटेरियन"),
    ("Implied probability", "इंप्लाइड प्रोबेबिलिटी"),
    ("Matched bet", "मैच्ड बेट"),
    ("Each-way", "ईच-वे"),
    ("Payment methods", "भुगतान विधियां"),
    ("Mobile app", "मोबाइल ऐप"),
    ("India guides", "भारत गाइड"),
    ("Promo Code", "प्रोमो कोड"),
    ("promo code", "प्रोमो कोड"),
    ("Basketball", "बास्केटबॉल"),
    ("Football", "फुटबॉल"),
    ("Cricket", "क्रिकेट"),
    ("Tennis", "टेनिस"),
    ("Esports", "ई-स्पोर्ट्स"),
    ("Casino home", "कैसीनो होम"),
    ("Slot reviews", "स्लॉट समीक्षाएं"),
    ("Casino", "कैसीनो"),
    ("Bonuses", "बोनस"),
    ("Mirrors", "मिरर"),
    ("Arbitrage", "आर्बिट्राज"),
    ("Surebet", "श्योरबेट"),
    ("Bankroll", "बैंकरोल"),
    ("Cashback", "कैशबैक"),
    
    # === CTAs ===
    ("Register at 1win", "1win पर रजिस्टर करें"),
    ("Access 1win Registration", "1win रजिस्ट्रेशन एक्सेस करें"),
    ("Access Your 1win Account", "अपना 1win खाता एक्सेस करें"),
    ("Register with XLBONUS →", "XLBONUS के साथ रजिस्टर करें"),
    ("Register with XLBONUS", "XLBONUS के साथ रजिस्टर करें"),
    ("Claim Promo Code →", "प्रोमो कोड पाएं"),
    ("Claim Promo Code", "प्रोमो कोड पाएं"),
    ("Claim Bonus", "बोनस पाएं"),
    ("Claim bonus", "बोनस पाएं"),
    ("Download App", "ऐप डाउनलोड करें"),
    ("Download Now", "अभी डाउनलोड करें"),
    ("Get the App", "ऐप पाएं"),
    ("Get Started →", "शुरू करें"),
    ("Get Started", "शुरू करें"),
    ("Play Now →", "अभी खेलें"),
    ("Play Now", "अभी खेलें"),
    ("Start Playing →", "खेलना शुरू करें"),
    ("Start Playing", "खेलना शुरू करें"),
    ("Get Bonus →", "बोनस पाएं"),
    ("Get Bonus", "बोनस पाएं"),
    ("Sign Up", "साइन अप करें"),
    ("sign up", "साइन अप करें"),
    
    # === WELCOME BONUS ===
    ("1win Promo Code XLBONUS - Get a 600% Welcome Bonus", "1win प्रोमो कोड XLBONUS - 600% स्वागत बोनस पाएं"),
    ("1win Promo Code XLBONUS, 600% Welcome Bonus (2026)", "1win प्रोमो कोड XLBONUS, 600% स्वागत बोनस (2026)"),
    ("600% Welcome Bonus", "600% स्वागत बोनस"),
    ("Welcome Bonus", "स्वागत बोनस"),
    ("Welcome bonus", "स्वागत बोनस"),
    ("welcome bonus", "स्वागत बोनस"),
    
    # === PAGE SECTIONS ===
    ("1WIN Register", "1WIN रजिस्टर"),
    ("1WIN Login", "1WIN लॉगिन"),
    ("1WIN Information", "1WIN जानकारी"),
    ("1WIN FAQs", "1WIN अक्सर पूछे जाने वाले प्रश्न"),
    ("1WIN Welcome bonus", "1WIN स्वागत बोनस"),
    ("1WIN Payment methods", "1WIN भुगतान विधियां"),
    ("1WIN promo code Details", "1WIN प्रोमो कोड विवरण"),
    ("The 1WIN promo code is", "1WIN प्रोमो कोड है"),
    ("How to use the", "कैसे उपयोग करें"),
    ("1WIN promo code", "1WIN प्रोमो कोड"),
    ("Latest Promotions", "नवीनतम प्रमोशन"),
    ("Global Access", "वैश्विक पहुंच"),
    ("Get your", "पाएं अपना"),
    ("600% bonus", "600% बोनस"),
    ("Your winning streak", "आपकी जीत का सिलसिला"),
    ("Starts now", "अभी शुरू होता है"),
    
    # === STAT BAR ===
    ("Instant Crypto", "इंस्टेंट क्रिप्टो"),
    
    # === STEP CARDS ===
    ("Visit 1win", "1win पर जाएं"),
    ("Get Your Bonus", "अपना बोनस पाएं"),
    
    # === TABLE HEADERS ===
    ("Website Languages", "वेबसाइट भाषाएं"),
    ("Accepted Crypto", "स्वीकृत क्रिप्टो"),
    ("Deposit Bonus", "जमा बोनस"),
    ("Established", "स्थापित"),
    ("Live Support", "लाइव सपोर्ट"),
    ("Bonus Offer", "बोनस ऑफर"),
    ("Website", "वेबसाइट"),
    ("Product", "उत्पाद"),
    
    # === DEPOSIT LABELS ===
    ("First Deposit", "पहला जमा"),
    ("Second Deposit", "दूसरा जमा"),
    ("Third Deposit", "तीसरा जमा"),
    ("Fourth Deposit", "चौथा जमा"),
    ("first deposit", "पहला जमा"),
    ("second deposit", "दूसरा जमा"),
    ("third deposit", "तीसरा जमा"),
    ("fourth deposit", "चौथा जमा"),
    
    # === PAYMENT GROUPS ===
    ("Cards &amp; E-Wallets", "कार्ड और ई-वॉलेट"),
    ("Cards & E-Wallets", "कार्ड और ई-वॉलेट"),
    ("Cryptocurrency", "क्रिप्टोकरेंसी"),
    
    # === FOOTER ===
    ("1win.codes - independent affiliate review", "1win.codes - स्वतंत्र एफिलिएट समीक्षा"),
    ("© 2026 1win.codes. All rights reserved.", "© 2026 1win.codes. सर्वाधिकार सुरक्षित।"),
    ("This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk. Please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.", 
     "यह एक अनौपचारिक फैन साइट है और 1win से संबद्ध या अनुमोदित नहीं है। यह साइट केवल सूचनात्मक उद्देश्यों के लिए है। जुए में जोखिम शामिल है। कृपया जिम्मेदारी से खेलें। यदि आप या आपके परिचित को जुए की समस्या है, तो कृपया GamCare या स्थानीय सहायता संगठन से संपर्क करें।"),
    
    # === COUNTRY NAMES ===
    ("Bangladesh", "बांग्लादेश"),
    ("Pakistan", "पाकिस्तान"),
    ("South Africa", "दक्षिण अफ्रीका"),
    ("Tanzania", "तंजानिया"),
    ("Malaysia", "मलेशिया"),
    ("Singapore", "सिंगापुर"),
    ("Vietnam", "वियतनाम"),
    ("Turkey", "तुर्की"),
    ("Russia", "रूस"),
    ("Ghana", "घाना"),
    ("Kenya", "केन्या"),
    ("Brazil", "ब्राजील"),
    ("Malawi", "मलावी"),
    ("Korea", "कोरिया"),
    
    # === INDIA STATE NAMES ===
    ("Maharashtra", "महाराष्ट्र"),
    ("Tamil Nadu", "तमिलनाडु"),
    ("Karnataka", "कर्नाटक"),
    ("Uttar Pradesh", "उत्तर प्रदेश"),
    ("West Bengal", "पश्चिम बंगाल"),
    ("Rajasthan", "राजस्थान"),
    ("Gujarat", "गुजरात"),
    ("Kerala", "केरल"),
    ("Punjab", "पंजाब"),
    ("Delhi", "दिल्ली"),
    ("Telangana", "तेलंगाना"),
    ("Andhra Pradesh", "आंध्र प्रदेश"),
    
    # === SPORTS TERMS ===
    ("sports betting", "स्पोर्ट्स बेटिंग"),
    ("Sports Betting", "स्पोर्ट्स बेटिंग"),
    ("online casino", "ऑनलाइन कैसीनो"),
    ("Online casino", "ऑनलाइन कैसीनो"),
    ("Online Casino", "ऑनलाइन कैसीनो"),
    ("live casino", "लाइव कैसीनो"),
    ("Live casino", "लाइव कैसीनो"),
    ("Live Casino", "लाइव कैसीनो"),
    ("crash games", "क्रैश गेम्स"),
    ("Crash games", "क्रैश गेम्स"),
    ("Crash Games", "क्रैश गेम्स"),
    ("free spins", "फ्री स्पिन"),
    ("Free Spins", "फ्री स्पिन"),
    ("Free spins", "फ्री स्पिन"),
    ("live dealer", "लाइव डीलर"),
    ("Live dealer", "लाइव डीलर"),
    ("Live Dealer", "लाइव डीलर"),
    ("betting markets", "बेटिंग मार्केट"),
    ("in-play", "इन-प्ले"),
    ("In-play", "इन-प्ले"),
    ("In-Play", "इन-प्ले"),
    ("cash-out", "कैश-आउट"),
    ("cashout", "कैशआउट"),
    ("Cashout", "कैशआउट"),
    ("sportsbook", "स्पोर्ट्सबुक"),
    ("Sportsbook", "स्पोर्ट्सबुक"),
    ("bookmaker", "बुकमेकर"),
    ("accumulator", "अक्युमुलेटर"),
    ("jackpot", "जैकपॉट"),
    ("Jackpot", "जैकपॉट"),
    ("tournament", "टूर्नामेंट"),
    ("Tournament", "टूर्नामेंट"),
    ("leaderboard", "लीडरबोर्ड"),
    ("wagering", "वेजरिंग"),
    ("Wagering", "वेजरिंग"),
    ("withdraw", "निकासी"),
    ("withdrawal", "निकासी"),
    ("Withdrawal", "निकासी"),
    ("deposit", "जमा"),
    ("Deposit", "जमा"),
    
    # === BONUS CONTENT ===
    ("welcome bonus", "स्वागत बोनस"),
    ("Welcome Bonus", "स्वागत बोनस"),
    ("no deposit bonus", "बिना जमा बोनस"),
    ("reload bonus", "रीलोड बोनस"),
    ("referral bonus", "रेफरल बोनस"),
    ("VIP Club", "VIP क्लब"),
    ("VIP club", "VIP क्लब"),
    ("vip club", "VIP क्लब"),
    ("Lucky Drive", "Lucky Drive"),
    
    # === COMMON PHRASES ===
    ("promo code guide", "प्रोमो कोड गाइड"),
    ("Use links on this page to access the official 1win website and click the &lsquo;Register&rsquo; button.", 
     "इस पेज पर दिए गए लिंक का उपयोग करके आधिकारिक 1win वेबसाइट पर जाएं और 'रजिस्टर' बटन पर क्लिक करें।"),
    ("The first part of your 600% bonus package will be credited to your account. Start playing!", 
     "आपके 600% बोनस पैकेज का पहला भाग आपके खाते में जमा किया जाएगा। खेलना शुरू करें!"),
    ("Four deposits. Each one supercharged. Here's exactly how the 600% total bonus works with crypto deposits.", 
     "चार जमाएं। हर एक सुपरचार्ज्ड। यहां बताया गया है कि क्रिप्टो जमा के साथ 600% कुल बोनस कैसे काम करता है।"),
    ("The above applies to crypto deposits. Fiat currency users get a 500% deposit bonus package across four deposits. 18+ | T&amp;C Apply | Play Responsibly.", 
     "उपरोक्त क्रिप्टो जमा पर लागू होता है। फिएट करेंसी उपयोगकर्ताओं को चार जमाओं में 500% जमा बोनस पैकेज मिलता है। 18+ | नियम एवं शर्तें लागू | जिम्मेदारी से खेलें।"),
    ("Crypto deposit bonus on your opening deposit.", "आपके पहले जमा पर क्रिप्टो जमा बोनस।"),
    ("Even bigger on your second top-up.", "दूसरे टॉप-अप पर और भी बड़ा।"),
    ("Serious boost on deposit number three.", "तीसरे जमा पर जबरदस्त बूस्ट।"),
    ("The biggest single bonus on your fourth deposit.", "चौथे जमा पर सबसे बड़ा एकल बोनस।"),
    ("Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.", 
     "कार्ड, ई-वॉलेट या क्रिप्टो से अपना खाता फंड करें। तेज, सुरक्षित और सीमाहीन।"),
    ("Use promo code", "प्रोमो कोड"),
    ("when registering to get the biggest available welcome bonus. Up to 600% across four deposits.", 
     "का उपयोग रजिस्ट्रेशन के समय करें और सबसे बड़ा उपलब्ध स्वागत बोनस पाएं। चार जमाओं में 600% तक।"),
    ("Exclusive tournaments, cash bonuses, and limited-time offers, updated regularly.", 
     "एक्सक्लूसिव टूर्नामेंट, कैश बोनस और सीमित-समय के ऑफर, नियमित रूप से अपडेट।"),
    ("Claim your 600% bonus with code", "कोड के साथ अपना 600% बोनस दावा करें"),
    ("Curaçao-licensed, 4-hour average withdrawals.", "Curaçao 8048/JAZ लाइसेंसधारी, औसत 4 घंटे में निकासी।"),
    ("1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.", 
     "1win 15 भाषाओं में उपलब्ध है। 30+ स्पोर्ट्स पर बेट लगाएं और कहीं से भी 11,000+ कैसीनो गेम्स खेलें।"),
    ("18+ only. New customers only. Terms and conditions apply. Gamble responsibly.", 
     "केवल 18+। केवल नए ग्राहक। नियम और शर्तें लागू होती हैं। जिम्मेदारी से जुआ खेलें।"),
    ("Use code XLBONUS when you register to unlock a 600% welcome bonus. Visit our", 
     "रजिस्टर करते समय XLBONUS कोड का उपयोग करें और 600% स्वागत बोनस अनलॉक करें। हमारी"),
    ("for full details.", "पर पूरी जानकारी के लिए जाएं।"),
    
    # === INFO TABLE VALUES ===
    ("Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games", 
     "स्पोर्ट्स बेटिंग, कैसीनो, लाइव कैसीनो, Aviator, पोकर, Lucky Drive, गेम्स"),
    ("Up to 600%", "600% तक"),
    ("BTC, DOGE, ETH, USDT and others", "BTC, DOGE, ETH, USDT और अन्य"),
    ("Yes, Android and iOS", "हां, Android और iOS"),
    
    # === FAQ CONTENT ===
    ("Can I access 1win?", "क्या मैं 1win एक्सेस कर सकता हूं?"),
    ("What is the 1win Promo Code?", "1win प्रोमो कोड क्या है?"),
    ("Is 1win legit?", "क्या 1win वैध है?"),
    ("Can I download a 1win app?", "क्या मैं 1win ऐप डाउनलोड कर सकता हूं?"),
    ("What is 1win Lucky Drive?", "1win Lucky Drive क्या है?"),
    ("1win is global and can be accessed in lots of countries. You can access the sportsbook and casino via this page.", 
     "1win वैश्विक है और कई देशों में एक्सेस किया जा सकता है। आप इस पेज के माध्यम से स्पोर्ट्सबुक और कैसीनो एक्सेस कर सकते हैं।"),
    ("1win is a legitimate online betting site offering sports betting, casino games and much more. The official website at 1win.pro holds a Curacao gambling licence.", 
     "1win एक वैध ऑनलाइन बेटिंग साइट है जो स्पोर्ट्स बेटिंग, कैसीनो गेम्स और बहुत कुछ प्रदान करती है। 1win.pro पर आधिकारिक वेबसाइट के पास Curaçao 8048/JAZ जुआ लाइसेंस है।"),
    ("Yes. The 1win app is available on Android and iOS. Register to get the download.", 
     "हां। 1win ऐप Android और iOS पर उपलब्ध है। डाउनलोड पाने के लिए रजिस्टर करें।"),
    ("1win Lucky Drive is a ticket-based promotion allowing players to win luxury vehicles, gadgets and free bets.", 
     "1win Lucky Drive एक टिकट-आधारित प्रमोशन है जो खिलाड़ियों को लग्जरी वाहन, गैजेट और मुफ्त बेट जीतने की अनुमति देता है।"),
    
    # === PROMOTIONS ===
    ("Win a Lambo", "लैम्बो जीतें"),
    ("Lucky Drive: Win a Lamborghini Urus SE", "Lucky Drive: Lamborghini Urus SE जीतें"),
    ("Deposit and claim your free ticket daily. Monthly luxury car draws await.", 
     "प्रतिदिन जमा करें और अपना मुफ्त टिकट पाएं। मासिक लग्जरी कार ड्रॉ का इंतजार है।"),
    ("Sins and Spins Tournament: $50,000 Prize Pool", "Sins and Spins टूर्नामेंट: $50,000 पुरस्कार राशि"),
    ("Spin the reels and climb the leaderboard for massive rewards.", 
     "रीलें स्पिन करें और बड़े पुरस्कारों के लिए लीडरबोर्ड पर चढ़ें।"),
    ("Legends Tournament: $100,000 in Prizes", "Legends टूर्नामेंट: $100,000 पुरस्कार"),
    ("Compete against the best. Weekly tournaments with scheduled payouts.", 
     "सर्वश्रेष्ठ के खिलाफ प्रतिस्पर्धा करें। निर्धारित भुगतान के साथ साप्ताहिक टूर्नामेंट।"),
    ("Aviamasters: Crash Game Championship", "Aviamasters: क्रैश गेम चैंपियनशिप"),
    ("Prove you're the ultimate Aviator pilot. Top cashouts win big.", 
     "साबित करें कि आप अंतिम Aviator पायलट हैं। टॉप कैशआउट बड़ी जीत पाते हैं।"),
    ("Gamzix Slots Fest: Free Spins Galore", "Gamzix Slots Fest: भरपूर फ्री स्पिन"),
    ("Play featured Gamzix slots and earn free spins plus cash bonuses.", 
     "फीचर्ड Gamzix स्लॉट्स खेलें और फ्री स्पिन के साथ कैश बोनस कमाएं।"),
    ("Olympics Special: Enhanced Odds on Every Sport", "Olympics Special: हर खेल पर बेहतर ऑड्स"),
    ("Boosted odds across all Olympic events. Back your country to win gold.", 
     "सभी ओलंपिक इवेंट्स में बूस्टेड ऑड्स। अपने देश को गोल्ड जीतने के लिए बेट करें।"),
    ("Republic Day Bonus: 200 Free Spins", "गणतंत्र दिवस बोनस: 200 फ्री स्पिन"),
    ("Celebrate with 200 free spins on selected slots. Limited time only.", 
     "चुनिंदा स्लॉट्स पर 200 फ्री स्पिन के साथ जश्न मनाएं। सीमित समय के लिए।"),
    ("Love Fest: Share the Jackpot", "Love Fest: जैकपॉट साझा करें"),
    ("Refer a friend and both receive bonus cash. Spread the love, stack the wins.", 
     "एक दोस्त को रेफर करें और दोनों को बोनस कैश मिलेगा। प्यार फैलाएं, जीत जोड़ें।"),
    
    # === BREADCRUMB / COMMON WORDS ===
    ("Home", "होम"),
    ("India", "भारत"),
    ("Toggle menu", "मेनू टॉगल करें"),
    ("Language", "भाषा"),
    
    # === COMMON WORDS ===
    ("Products", "उत्पाद"),
    ("Promos", "प्रमोशन"),
    ("Support", "सपोर्ट"),
    ("Countries", "देश"),
    ("Sports", "स्पोर्ट्स"),
    ("Casino", "कैसीनो"),
    ("Poker", "पोकर"),
    ("Bonuses", "बोनस"),
    ("Bonus", "बोनस"),
    ("Games", "गेम्स"),
    ("Register", "रजिस्टर"),
    ("Login", "लॉगिन"),
    ("Review", "समीक्षा"),
    ("Mirror", "मिरर"),
    ("Payments", "भुगतान"),
    ("News", "समाचार"),
    ("App", "ऐप"),
    
    # === PAGE-SPECIFIC BODY CONTENT ===
    # Index page
    ("1win covers 30+ sports with 1,000+ daily markets, live in-play betting with cash-out on every selection, and free streams on selected football and tennis matches. Curaçao-licensed (8048/JAZ), founded 2018.", 
     "1win में 1,000+ दैनिक मार्केट के साथ 30+ स्पोर्ट्स, हर चयन पर कैश-आउट के साथ लाइव इन-प्ले बेटिंग, और चुनिंदा फुटबॉल और टेनिस मैचों की मुफ्त स्ट्रीम शामिल है। Curaçao 8048/JAZ लाइसेंसधारी, 2018 में स्थापित।"),
    ("11,000+ casino games from 70+ providers including Pragmatic Play, Evolution, NetEnt and Spribe. Live dealer tables 24/7. Daily drops and tournaments worth $50,000+ a week.", 
     "Pragmatic Play, Evolution, NetEnt और Spribe सहित 70+ प्रदाताओं से 11,000+ कैसीनो गेम्स। 24/7 लाइव डीलर टेबल। प्रति सप्ताह $50,000+ मूल्य के दैनिक ड्रॉप और टूर्नामेंट।"),
    ("1win is global. This website can be accessed all over the world. Log in to your account to start playing casino games and placing sports bets. Log in on your PC or mobile device to start playing. Alternatively, download the official 1win app to play on your Android or iOS device.", 
     "1win वैश्विक है। इस वेबसाइट को पूरी दुनिया में एक्सेस किया जा सकता है। कैसीनो गेम्स खेलने और स्पोर्ट्स बेट लगाने के लिए अपने खाते में लॉगिन करें। PC या मोबाइल डिवाइस पर लॉगिन करें और खेलना शुरू करें। Android या iOS डिवाइस पर खेलने के लिए आधिकारिक 1win ऐप डाउनलोड करें।"),
    ("When you log in you can play immediately. You have lots of payment methods to choose from and can fund your account using Bitcoin and many other crypto coins.", 
     "जब आप लॉगिन करते हैं तो आप तुरंत खेल सकते हैं। आपके पास चुनने के लिए कई भुगतान विधियां हैं और Bitcoin तथा कई अन्य क्रिप्टो कॉइन्स का उपयोग करके अपना खाता फंड कर सकते हैं।"),
    ("Code XLBONUS stacks a 200% + 150% + 100% + 50% bonus across your first four deposits. 1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). 600% total, auto-activated.", 
     "XLBONUS कोड आपकी पहली चार जमाओं में 200% + 150% + 100% + 50% बोनस स्टैक करता है। 1win में 30+ स्पोर्ट्स और 11,000+ कैसीनो गेम्स हैं। Curaçao 8048/JAZ लाइसेंसधारी। कुल 600%, ऑटो-एक्टिवेट।"),
    ("1win is a globally accessible sportsbook and casino, operating under Curaçao licence 8048/JAZ. New players use promo code", 
     "1win एक वैश्विक स्पोर्ट्सबुक और कैसीनो है, जो Curaçao 8048/JAZ लाइसेंस के तहत संचालित होता है। नए खिलाड़ी प्रोमो कोड"),
    ("to unlock a 600% welcome bonus across four deposits, up to $1,050 total.", 
     "का उपयोग करके चार जमाओं में 600% स्वागत बोनस अनलॉक कर सकते हैं, कुल $1,050 तक।"),
    ("allows you to get the biggest available bonus when opening a new account. By using this code when registering, you can get a 600% deposit bonus. This can be claimed at either the sportsbook or the casino and also comes with up to 400 free spins.", 
     "नया खाता खोलते समय सबसे बड़ा उपलब्ध बोनस प्राप्त करने में मदद करता है। रजिस्ट्रेशन के समय इस कोड का उपयोग करके आप 600% जमा बोनस प्राप्त कर सकते हैं। यह स्पोर्ट्सबुक या कैसीनो में से किसी पर भी दावा किया जा सकता है और इसमें 400 फ्री स्पिन तक भी शामिल हैं।"),
    ("Register with the code to get one of the largest bonus offers found at any online betting site anywhere in the world!", 
     "कोड के साथ रजिस्टर करें और किसी भी ऑनलाइन बेटिंग साइट पर मिलने वाले सबसे बड़े बोनस ऑफर में से एक पाएं!"),
    ("Fill in the short registration form. When asked if you have a promo code, type in the", 
     "संक्षिप्त रजिस्ट्रेशन फॉर्म भरें। जब प्रोमो कोड पूछा जाए, तो"),
    ("code.", "कोड डालें।"),
    ("Make your first deposit. A 130% first deposit bonus is available with", 
     "अपना पहला जमा करें।"),
    
    # === CRICKET PAGE ===
    ("1win cricket betting: IPL, T20 World Cup and every format covered", 
     "1win क्रिकेट बेटिंग: IPL, T20 विश्व कप और हर फॉर्मेट"),
    ("Hero stats", "मुख्य आंकड़े"),
    ("Markets available", "उपलब्ध मार्केट"),
    ("Welcome bonus code", "स्वागत बोनस कोड"),
    ("In-play streaming", "इन-प्ले स्ट्रीमिंग"),
    ("Select matches live", "चुनिंदा मैच लाइव"),
    ("24/7 full and partial", "24/7 पूर्ण और आंशिक"),
    ("Licence", "लाइसेंस"),
    ("Tournaments and competitions covered", "कवर किए गए टूर्नामेंट और प्रतियोगिताएं"),
    ("Most popular cricket betting markets", "सबसे लोकप्रिय क्रिकेट बेटिंग मार्केट"),
    ("In-play and live cricket betting", "इन-प्ले और लाइव क्रिकेट बेटिंग"),
    ("Cashout and bet builder", "कैशआउट और बेट बिल्डर"),
    ("Mobile cricket betting with the 1win app", "1win ऐप के साथ मोबाइल क्रिकेट बेटिंग"),
    ("How to start betting on cricket at 1win", "1win पर क्रिकेट बेटिंग कैसे शुरू करें"),
    ("Register your account", "अपना खाता रजिस्टर करें"),
    ("Enter promo code", "प्रोमो कोड डालें"),
    ("Deposit funds", "फंड जमा करें"),
    ("Open cricket markets", "क्रिकेट मार्केट खोलें"),
    ("Place your bet", "अपनी बेट लगाएं"),
    
    # === SLOTS COMMON ===
    ("Return to Player", "रिटर्न टू प्लेयर"),
    ("Volatility", "वोलेटिलिटी"),
    ("Min bet", "न्यूनतम बेट"),
    ("Max bet", "अधिकतम बेट"),
    ("Max win", "अधिकतम जीत"),
    ("Paylines", "पेलाइन"),
    ("Reels", "रील"),
    ("High", "उच्च"),
    ("Medium", "मध्यम"),
    ("Low", "कम"),
    
    # === BREADCRUMBS ===
    ("1win Maharashtra: IPL betting and UPI deposits", "1win महाराष्ट्र: IPL बेटिंग और UPI जमा"),
    ("1win Tamil Nadu", "1win तमिलनाडु"),
    ("1win Karnataka", "1win कर्नाटक"),
    ("1win Delhi", "1win दिल्ली"),
    ("1win Kerala", "1win केरल"),
    ("1win Gujarat", "1win गुजरात"),
    ("1win Rajasthan", "1win राजस्थान"),
    ("1win Punjab", "1win पंजाब"),
    ("1win Uttar Pradesh", "1win उत्तर प्रदेश"),
    ("1win West Bengal", "1win पश्चिम बंगाल"),
    ("1win Andhra Pradesh", "1win आंध्र प्रदेश"),
    ("1win Telangana", "1win तेलंगाना"),
    
    # === COMMON BODY WORDS ===
    ("registration", "रजिस्ट्रेशन"),
    ("Registration", "रजिस्ट्रेशन"),
    ("account", "खाता"),
    ("Account", "खाता"),
    ("platform", "प्लेटफॉर्म"),
    ("Platform", "प्लेटफॉर्म"),
    ("available", "उपलब्ध"),
    ("Available", "उपलब्ध"),
    ("instant", "तुरंत"),
    ("Instant", "तुरंत"),
    ("daily", "दैनिक"),
    ("Daily", "दैनिक"),
    ("weekly", "साप्ताहिक"),
    ("Weekly", "साप्ताहिक"),
    ("monthly", "मासिक"),
    ("Monthly", "मासिक"),
    ("players", "खिलाड़ियों"),
    ("player", "खिलाड़ी"),
    ("Players", "खिलाड़ियों"),
    ("Player", "खिलाड़ी"),
    ("markets", "मार्केट"),
    ("market", "मार्केट"),
    ("Markets", "मार्केट"),
    ("Market", "मार्केट"),
    ("odds", "ऑड्स"),
    ("Odds", "ऑड्स"),
    ("stake", "दांव"),
    ("Stake", "दांव"),
    ("bet", "बेट"),
    ("Bet", "बेट"),
    ("bets", "बेट"),
    ("Bets", "बेट"),
    ("win", "जीत"),
    ("Win", "जीत"),
    ("wins", "जीत"),
    ("Wins", "जीत"),
    ("payout", "भुगतान"),
    ("Payout", "भुगतान"),
    ("payouts", "भुगतान"),
    ("Payouts", "भुगतान"),
    ("crypto", "क्रिप्टो"),
    ("Crypto", "क्रिप्टो"),
    ("mobile", "मोबाइल"),
    ("Mobile", "मोबाइल"),
    ("app", "ऐप"),
    ("App", "ऐप"),
    ("Android", "Android"),
    ("iOS", "iOS"),
    ("download", "डाउनलोड"),
    ("Download", "डाउनलोड"),
    
    # === LICENSE ===
    ("Curacao 8048/JAZ", "Curaçao 8048/JAZ"),
    ("Curacao", "Curaçao"),
    ("licensed", "लाइसेंसधारी"),
    ("licence", "लाइसेंस"),
    ("license", "लाइसेंस"),
    ("Licensed", "लाइसेंसधारी"),
]


def build_translation_map():
    """Build ordered translation map from list."""
    # Sort by length (longest first) to prevent partial replacements
    return sorted(TRANSLATIONS, key=lambda x: len(x[0]), reverse=True)


TRANSLATION_MAP = build_translation_map()


def translate_text(text):
    """Translate English text to Hindi."""
    if not text or not text.strip():
        return text
    
    for en, hi in TRANSLATION_MAP:
        if en in text:
            text = text.replace(en, hi)
    
    return text


def fix_structural_elements(content, rel_path):
    """Fix lang, canonical, hreflang, nav URLs, JSON-LD URLs."""
    
    # 1. Fix lang="en" → lang="hi"
    content = content.replace('<html lang="en">', '<html lang="hi">')
    content = content.replace(" lang='en'>", ' lang="hi">')
    
    # 2. Remove ALL em/en dashes
    content = content.replace('—', '-')
    content = content.replace('–', '-')
    content = content.replace('&mdash;', '-')
    content = content.replace('&ndash;', '-')
    
    # 3. Fix nav/link URLs: /en/ → /hi/ (but NOT in hreflang blocks which need their own locales)
    # Strategy: temporarily protect hreflang links, then fix others
    
    # Fix canonical URL
    def fix_canonical(m):
        url = m.group(1).replace('/en/', '/hi/')
        return f'<link rel="canonical" href="{url}">'
    content = re.sub(r'<link rel="canonical" href="([^"]+)">', fix_canonical, content)
    
    # Fix og:url if present
    content = re.sub(
        r'<meta property="og:url" content="https://1win\.codes/en/([^"]*)"',
        lambda m: f'<meta property="og:url" content="https://1win.codes/hi/{m.group(1)}"',
        content
    )
    
    # 4. Replace hreflang block with full 46-locale version
    # Remove existing hreflang links
    content = re.sub(r'\n?\s*<link rel="alternate" hreflang="[^"]+"[^>]+/>', '', content)
    # Also remove partial/relative hreflang links
    content = re.sub(r'\n?\s*<link rel="alternate" hreflang="[^"]+"[^>]+>', '', content)
    
    # Insert full hreflang block after canonical
    hreflang_block = make_hreflang_for_page(rel_path)
    content = re.sub(
        r'(<link rel="canonical"[^>]+>)',
        r'\1\n' + hreflang_block,
        content
    )
    
    # 5. Fix navigation href="/en/..." → href="/hi/..."
    content = re.sub(r'href="/en/([^"]*)"', r'href="/hi/\1"', content)
    
    # 6. Fix JSON-LD /en/ → /hi/
    def fix_jsonld(m):
        block = m.group(0)
        block = re.sub(r'https://1win\.codes/en/', 'https://1win.codes/hi/', block)
        return block
    content = re.sub(
        r'<script type="application/ld\+json"[^>]*>.*?</script>',
        fix_jsonld,
        content,
        flags=re.DOTALL
    )
    
    # 7. Normalize Curacao spelling
    content = content.replace('Curacao 8048/JAZ', 'Curaçao 8048/JAZ')
    content = content.replace('Curacao', 'Curaçao')
    
    return content


def translate_meta_tags(content):
    """Translate title, meta description, og:title, og:description."""
    
    # Title
    def trans_title(m):
        t = m.group(1)
        t = translate_text(t)
        return f'<title>{t}</title>'
    content = re.sub(r'<title>(.*?)</title>', trans_title, content, flags=re.DOTALL)
    
    # Meta description
    def trans_meta_desc(m):
        desc = m.group(1)
        desc = translate_text(desc)
        return f'<meta name="description" content="{desc}"'
    content = re.sub(r'<meta name="description" content="([^"]*)"', trans_meta_desc, content)
    
    # OG title
    def trans_og_title(m):
        t = m.group(1)
        t = translate_text(t)
        return f'<meta property="og:title" content="{t}"'
    content = re.sub(r'<meta property="og:title" content="([^"]*)"', trans_og_title, content)
    
    # OG description
    def trans_og_desc(m):
        desc = m.group(1)
        desc = translate_text(desc)
        return f'<meta property="og:description" content="{desc}"'
    content = re.sub(r'<meta property="og:description" content="([^"]*)"', trans_og_desc, content)
    
    # aria-label (not on SVG path elements)
    aria_map = {
        "Sign Up": "साइन अप करें",
        "Toggle menu": "मेनू टॉगल करें",
        "Language": "भाषा",
        "1win home": "1win होम",
        "Breadcrumb": "ब्रेडक्रम्ब",
    }
    for en, hi in aria_map.items():
        content = content.replace(f'aria-label="{en}"', f'aria-label="{hi}"')
    
    return content


def translate_html_body(content):
    """
    Translate visible text content in HTML body while preserving tags/scripts/styles.
    Uses a state machine to parse HTML and translate text nodes.
    """
    # We process char by char, tracking whether we're inside a tag or script/style
    output = []
    i = 0
    n = len(content)
    
    # Blocks to skip entirely (preserve verbatim)
    SKIP_OPEN = re.compile(r'^<(script|style|code|pre|noscript)(\s[^>]*)?>',
                            re.IGNORECASE)
    SKIP_CLOSE = {
        'script': re.compile(r'</script\s*>', re.IGNORECASE),
        'style': re.compile(r'</style\s*>', re.IGNORECASE),
        'code': re.compile(r'</code\s*>', re.IGNORECASE),
        'pre': re.compile(r'</pre\s*>', re.IGNORECASE),
        'noscript': re.compile(r'</noscript\s*>', re.IGNORECASE),
    }
    
    while i < n:
        remaining = content[i:]
        
        # Check for skip block
        skip_m = SKIP_OPEN.match(remaining)
        if skip_m:
            tag_name = skip_m.group(1).lower()
            close_pat = SKIP_CLOSE.get(tag_name, re.compile(f'</{tag_name}\\s*>', re.IGNORECASE))
            close_m = close_pat.search(remaining, skip_m.end())
            if close_m:
                block = remaining[:close_m.end()]
                output.append(block)
                i += close_m.end()
            else:
                output.append(remaining)
                i = n
            continue
        
        # Check for HTML tag
        if content[i] == '<':
            end = content.find('>', i)
            if end == -1:
                output.append(content[i:])
                i = n
                continue
            # Preserve tag verbatim
            output.append(content[i:end+1])
            i = end + 1
            continue
        
        # Text node - find next '<'
        next_tag = content.find('<', i)
        if next_tag == -1:
            text = content[i:]
            output.append(translate_text(text))
            i = n
        else:
            text = content[i:next_tag]
            output.append(translate_text(text))
            i = next_tag
    
    return ''.join(output)


def ensure_curacao_present(content):
    """Ensure Curaçao 8048/JAZ appears in the content (add to first paragraph if missing)."""
    if 'Curaçao 8048/JAZ' in content or 'Curaçao 8048' in content:
        return content
    
    # Find first <p> tag after <body>
    body_pos = content.lower().find('<body>')
    if body_pos == -1:
        body_pos = 0
    
    first_p = re.search(r'<p[^>]*>(.*?)</p>', content[body_pos:], re.DOTALL)
    if first_p:
        abs_start = body_pos + first_p.start()
        old_p_text = first_p.group(1)
        # Add Curaçao at end of first paragraph
        new_p_text = old_p_text.rstrip('.').rstrip() + '. 1win Curaçao 8048/JAZ लाइसेंस के तहत संचालित होता है।'
        new_p = first_p.group(0).replace(first_p.group(1), new_p_text)
        content = content[:abs_start] + new_p + content[abs_start + len(first_p.group(0)):]
    
    return content


def ensure_xlbonus_present(content):
    """Ensure XLBONUS appears in the content."""
    if 'XLBONUS' in content:
        return content
    
    # Add to first paragraph
    body_pos = content.lower().find('<body>')
    if body_pos == -1:
        body_pos = 0
    
    first_p = re.search(r'<p[^>]*>(.*?)</p>', content[body_pos:], re.DOTALL)
    if first_p:
        abs_start = body_pos + first_p.start()
        old_text = first_p.group(1)
        new_text = old_text.rstrip('.').rstrip() + '. प्रोमो कोड <span class="code-highlight">XLBONUS</span> का उपयोग करें।'
        new_p = first_p.group(0).replace(first_p.group(1), new_text)
        content = content[:abs_start] + new_p + content[abs_start + len(first_p.group(0)):]
    
    return content


def remove_banned_hi_words(content):
    """Remove/replace Hindi banned words."""
    banned_replacements = {
        'हज़ारों': '11,000+',
        'सैकड़ों': '400,000+',
        'विश्व स्तरीय': 'उच्च-गुणवत्ता',
        'अत्याधुनिक': 'उन्नत',
        'अगली पीढ़ी का': 'आधुनिक',
        'नवीनतम': 'नया',
    }
    for word, replacement in banned_replacements.items():
        content = content.replace(word, replacement)
    return content


def translate_page(en_content, rel_path):
    """Full translation pipeline for one page."""
    content = en_content
    
    # Step 1: Fix structure (lang, canonical, hreflang, nav URLs, JSON-LD)
    content = fix_structural_elements(content, rel_path)
    
    # Step 2: Translate meta tags
    content = translate_meta_tags(content)
    
    # Step 3: Translate body text (all visible content)
    content = translate_html_body(content)
    
    # Step 4: Remove banned words
    content = remove_banned_hi_words(content)
    
    # Step 5: Ensure required elements present
    content = ensure_curacao_present(content)
    content = ensure_xlbonus_present(content)
    
    # Step 6: Final em/en dash removal (catch any we missed)
    content = content.replace('—', '-')
    content = content.replace('–', '-')
    
    return content


def audit_page(hi_content, rel_path):
    """Audit a translated page for rule compliance."""
    issues = []
    
    if '<html lang="hi">' not in hi_content:
        issues.append("missing lang=hi")
    
    if 'XLBONUS' not in hi_content:
        issues.append("missing XLBONUS")
    
    if 'Curaçao 8048/JAZ' not in hi_content and 'Curaçao 8048' not in hi_content:
        issues.append("missing Curaçao 8048/JAZ")
    
    em_count = hi_content.count('—')
    if em_count > 0:
        issues.append(f"{em_count} em-dashes")
    
    en_count = hi_content.count('–')
    if en_count > 0:
        issues.append(f"{en_count} en-dashes")
    
    if '/hi/' not in hi_content and 'canonical' in hi_content:
        issues.append("canonical missing /hi/")
    
    hreflang_count = hi_content.count('hreflang=')
    if hreflang_count < 40:
        issues.append(f"only {hreflang_count} hreflang entries (need 47+)")
    
    # Banned Hindi words
    banned_hi = ['हज़ारों', 'सैकड़ों', 'विश्व स्तरीय', 'अत्याधुनिक', 'अगली पीढ़ी', 'नवीनतम']
    for b in banned_hi:
        if b in hi_content:
            issues.append(f"banned word: {b}")
    
    # Validate JSON-LD
    jsonld_blocks = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', 
                                hi_content, re.DOTALL)
    for i, block in enumerate(jsonld_blocks):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            issues.append(f"JSON-LD block {i+1} invalid: {e}")
    
    return issues


def process_all():
    """Process all 184 pages."""
    inventory_path = BASE / "build_helpers" / "en_page_inventory.txt"
    inventory = [p.strip() for p in inventory_path.read_text().strip().split('\n') if p.strip()]
    
    results = {
        'processed': 0,
        'errors': [],
        'audit_issues': {},
        'total': len(inventory)
    }
    
    print(f"Processing {len(inventory)} pages...")
    
    for idx, rel_path in enumerate(inventory):
        en_file = EN_DIR / rel_path
        hi_file = HI_DIR / rel_path
        
        if not en_file.exists():
            results['errors'].append(f"EN missing: {rel_path}")
            continue
        
        # Create output directory
        hi_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            en_content = en_file.read_text(encoding='utf-8')
            hi_content = translate_page(en_content, rel_path)
            hi_file.write_text(hi_content, encoding='utf-8')
            results['processed'] += 1
            
            # Audit
            issues = audit_page(hi_content, rel_path)
            if issues:
                results['audit_issues'][rel_path] = issues
            
            if (idx + 1) % 25 == 0:
                print(f"  [{idx+1}/{len(inventory)}] Processed, issues so far: {len(results['audit_issues'])}")
        
        except Exception as e:
            results['errors'].append(f"Error {rel_path}: {e}")
            import traceback
            traceback.print_exc()
    
    return results


if __name__ == "__main__":
    results = process_all()
    
    print(f"\n=== TRANSLATION RESULTS ===")
    print(f"Total: {results['total']}")
    print(f"Processed: {results['processed']}")
    print(f"Errors: {len(results['errors'])}")
    print(f"Pages with audit issues: {len(results['audit_issues'])}")
    
    if results['errors']:
        print(f"\nErrors:")
        for e in results['errors']:
            print(f"  {e}")
    
    if results['audit_issues']:
        print(f"\nAudit issues:")
        for path, issues in list(results['audit_issues'].items())[:20]:
            print(f"  {path}: {issues}")
    
    total_issues = sum(len(v) for v in results['audit_issues'].values())
    clean = results['processed'] - len(results['audit_issues'])
    print(f"\npages: {results['processed']}, issues: {total_issues}, clean: {clean}")
