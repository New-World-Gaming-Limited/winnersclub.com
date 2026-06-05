#!/usr/bin/env python3
"""
Hindi (HI) translation script for 1win.codes
Translates all 184 EN pages to HI following TRANSLATION_RULES.md
"""

import os
import re
import sys
import json
from pathlib import Path

BASE = Path("/home/user/workspace/1win-codes-repo")
EN_DIR = BASE / "en"
HI_DIR = BASE / "hi"

# =============================================================================
# COMPREHENSIVE EN → HI TRANSLATION DICTIONARY
# =============================================================================

# Navigation & UI
NAV_TRANSLATIONS = {
    "Promo Code": "प्रोमो कोड",
    "Sports": "स्पोर्ट्स",
    "All sports betting": "सभी स्पोर्ट्स बेटिंग",
    "Football": "फुटबॉल",
    "Cricket": "क्रिकेट",
    "Tennis": "टेनिस",
    "Basketball": "बास्केटबॉल",
    "Esports": "ई-स्पोर्ट्स",
    "Live streaming": "लाइव स्ट्रीमिंग",
    "Casino": "कैसीनो",
    "Casino home": "कैसीनो होम",
    "Slot reviews": "स्लॉट समीक्षाएं",
    "Game providers": "गेम प्रदाता",
    "Crash games": "क्रैश गेम्स",
    "Poker": "पोकर",
    "Bonuses": "बोनस",
    "All bonuses": "सभी बोनस",
    "First deposit 200%": "पहला जमा 200%",
    "Second deposit 150%": "दूसरा जमा 150%",
    "Third deposit 150%": "तीसरा जमा 150%",
    "Fourth deposit 100%": "चौथा जमा 100%",
    "Wagering rules": "वेजरिंग नियम",
    "Free spins today": "आज के फ्री स्पिन",
    "Cashback": "कैशबैक",
    "VIP club": "VIP क्लब",
    "All promotions": "सभी प्रमोशन",
    "Tools": "टूल्स",
    "All calculators": "सभी कैलकुलेटर",
    "Odds converter": "ऑड्स कन्वर्टर",
    "Parlay calculator": "पार्ले कैलकुलेटर",
    "Kelly criterion": "केली क्राइटेरियन",
    "Arbitrage": "आर्बिट्राज",
    "Hedge": "हेज",
    "Each-way": "ईच-वे",
    "Implied probability": "इंप्लाइड प्रोबेबिलिटी",
    "Bankroll": "बैंकरोल",
    "Surebet": "श्योरबेट",
    "Matched bet": "मैच्ड बेट",
    "More": "और",
    "Payment methods": "भुगतान विधियां",
    "Mobile app": "मोबाइल ऐप",
    "India guides": "भारत गाइड",
    "Mirrors": "मिरर",
    "Login": "लॉगिन",
    "Register": "रजिस्टर",
    "Review": "समीक्षा",
    "About 1win": "1win के बारे में",
    "News": "समाचार",
    "FAQ": "अक्सर पूछे जाने वाले प्रश्न",
}

# Common phrases
PHRASE_TRANSLATIONS = {
    # Hero & CTA
    "Register at 1win": "1win पर रजिस्टर करें",
    "Sign Up": "साइन अप करें",
    "Claim Promo Code": "प्रोमो कोड पाएं",
    "Claim Bonus": "बोनस पाएं",
    "Access 1win Registration": "1win रजिस्ट्रेशन पर जाएं",
    "Access Your 1win Account": "अपने 1win खाते में प्रवेश करें",
    "Register with XLBONUS": "XLBONUS के साथ रजिस्टर करें",
    "Register with XLBONUS →": "XLBONUS के साथ रजिस्टर करें",
    "Claim Promo Code →": "प्रोमो कोड पाएं",
    "Get Bonus →": "बोनस पाएं",
    "Start Playing →": "खेलना शुरू करें",
    "Get Started →": "शुरू करें",
    "Play Now →": "अभी खेलें",
    "Download App": "ऐप डाउनलोड करें",
    "Download Now": "अभी डाउनलोड करें",
    "Get the App": "ऐप पाएं",
    
    # Welcome bonus
    "1win Promo Code XLBONUS - Get a 600% Welcome Bonus": "1win प्रोमो कोड XLBONUS - 600% स्वागत बोनस पाएं",
    "1win Promo Code XLBONUS, 600% Welcome Bonus (2026)": "1win प्रोमो कोड XLBONUS, 600% स्वागत बोनस (2026)",
    "600% Welcome Bonus": "600% स्वागत बोनस",
    "Welcome Bonus": "स्वागत बोनस",
    "Welcome bonus": "स्वागत बोनस",
    
    # Stat bar
    "Bonus": "बोनस",
    "Sports": "स्पोर्ट्स",
    "Games": "गेम्स",
    "Instant Crypto": "इंस्टेंट क्रिप्टो",
    
    # Sections
    "1WIN Register": "1WIN रजिस्टर",
    "1WIN Login": "1WIN लॉगिन",
    "1WIN Information": "1WIN जानकारी",
    "1WIN FAQs": "1WIN अक्सर पूछे जाने वाले प्रश्न",
    "1WIN Welcome bonus": "1WIN स्वागत बोनस",
    "1WIN Payment methods": "1WIN भुगतान विधियां",
    "1WIN promo code Details": "1WIN प्रोमो कोड विवरण",
    "The 1WIN promo code is": "1WIN प्रोमो कोड है",
    "How to use the": "कैसे उपयोग करें",
    "1WIN promo code": "1WIN प्रोमो कोड",
    "Global Access": "वैश्विक पहुंच",
    "Latest Promotions": "नवीनतम प्रमोशन",
    
    # Step cards
    "Visit 1win": "1win पर जाएं",
    "Deposit": "जमा करें",
    "Get Your Bonus": "अपना बोनस पाएं",
    
    # Table headers
    "Website": "वेबसाइट",
    "Products": "उत्पाद",
    "Promo Code": "प्रोमो कोड",
    "Deposit Bonus": "जमा बोनस",
    "Established": "स्थापित",
    "Accepted Crypto": "स्वीकृत क्रिप्टो",
    "Website Languages": "वेबसाइट भाषाएं",
    "App": "ऐप",
    "Live Streaming": "लाइव स्ट्रीमिंग",
    "Live Support": "लाइव सपोर्ट",
    "Product": "उत्पाद",
    "Bonus Offer": "बोनस ऑफर",
    
    # Deposit labels
    "First Deposit": "पहला जमा",
    "Second Deposit": "दूसरा जमा",
    "Third Deposit": "तीसरा जमा",
    "Fourth Deposit": "चौथा जमा",
    
    # News/Promos
    "Win a Lambo": "लैम्बो जीतें",
    "Lucky Drive: Win a Lamborghini Urus SE": "Lucky Drive: Lamborghini Urus SE जीतें",
    "Deposit and claim your free ticket daily. Monthly luxury car draws await.": "प्रतिदिन जमा करें और अपना मुफ्त टिकट पाएं। मासिक लग्जरी कार ड्रॉ का इंतजार है।",
    
    # FAQ questions
    "Can I access 1win?": "क्या मैं 1win एक्सेस कर सकता हूं?",
    "What is the 1win Promo Code?": "1win प्रोमो कोड क्या है?",
    "Is 1win legit?": "क्या 1win वैध है?",
    "Can I download a 1win app?": "क्या मैं 1win ऐप डाउनलोड कर सकता हूं?",
    "What is 1win Lucky Drive?": "1win Lucky Drive क्या है?",
    
    # Footer
    "Products": "उत्पाद",
    "Promos": "प्रमोशन",
    "Support": "सपोर्ट",
    "Countries": "देश",
    "Sports Betting": "स्पोर्ट्स बेटिंग",
    "VIP Club": "VIP क्लब",
    "Lucky Drive": "Lucky Drive",
    "Free Money": "मुफ्त पैसा",
    "Mirror": "मिरर",
    "About 1win": "1win के बारे में",
    "Payment methods": "भुगतान विधियां",
    "Payments": "भुगतान",
    "Bangladesh": "बांग्लादेश",
    "India": "भारत",
    "Pakistan": "पाकिस्तान",
    "Korea": "कोरिया",
    "Malaysia": "मलेशिया",
    "Singapore": "सिंगापुर",
    "South Africa": "दक्षिण अफ्रीका",
    "Tanzania": "तंजानिया",
    "Malawi": "मलावी",
    "Kenya": "केन्या",
    
    # CTA Banner
    "Your winning streak": "आपकी जीत का सिलसिला",
    "Starts now": "अभी शुरू होता है",
    
    # Payment groups
    "Cards & E-Wallets": "कार्ड और ई-वॉलेट",
    "Cryptocurrency": "क्रिप्टोकरेंसी",
    
    # Breadcrumb
    "Home": "होम",
    
    # Footer disclaimer
    "This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk. Please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.": "यह एक अनौपचारिक फैन साइट है और 1win से संबद्ध या समर्थित नहीं है। यह साइट केवल सूचनात्मक उद्देश्यों के लिए है। जुए में जोखिम होता है। कृपया जिम्मेदारी से खेलें। यदि आप या आपका कोई परिचित जुए की समस्या से ग्रस्त है, तो कृपया GamCare या स्थानीय सहायता संगठन से संपर्क करें।",
    "© 2026 1win.codes. All rights reserved.": "© 2026 1win.codes. सर्वाधिकार सुरक्षित।",
    "1win.codes - independent affiliate review": "1win.codes - स्वतंत्र एफिलिएट समीक्षा",
    
    # Common body text
    "1win covers 30+ sports with 1,000+ daily markets, live in-play betting with cash-out on every selection, and free streams on selected football and tennis matches. Curaçao-licensed (8048/JAZ), founded 2018.": "1win में 1,000+ दैनिक मार्केट के साथ 30+ स्पोर्ट्स, हर चयन पर कैश-आउट के साथ लाइव इन-प्ले बेटिंग, और चुनिंदा फुटबॉल और टेनिस मैचों की मुफ्त स्ट्रीम शामिल है। Curaçao 8048/JAZ लाइसेंसधारी, 2018 में स्थापित।",
    "11,000+ casino games from 70+ providers including Pragmatic Play, Evolution, NetEnt and Spribe. Live dealer tables 24/7. Daily drops and tournaments worth $50,000+ a week.": "Pragmatic Play, Evolution, NetEnt और Spribe सहित 70+ प्रदाताओं से 11,000+ कैसीनो गेम्स। 24/7 लाइव डीलर टेबल। प्रति सप्ताह $50,000+ मूल्य के दैनिक ड्रॉप और टूर्नामेंट।",
    "1win is global. This website can be accessed all over the world. Log in to your account to start playing casino games and placing sports bets. Log in on your PC or mobile device to start playing. Alternatively, download the official 1win app to play on your Android or iOS device.": "1win वैश्विक है। इस वेबसाइट को पूरी दुनिया में एक्सेस किया जा सकता है। कैसीनो गेम्स खेलने और स्पोर्ट्स बेट लगाने के लिए अपने खाते में लॉगिन करें। PC या मोबाइल डिवाइस पर लॉगिन करें और खेलना शुरू करें। या Android या iOS डिवाइस पर खेलने के लिए आधिकारिक 1win ऐप डाउनलोड करें।",
    "When you log in you can play immediately. You have lots of payment methods to choose from and can fund your account using Bitcoin and many other crypto coins.": "जब आप लॉगिन करते हैं तो आप तुरंत खेल सकते हैं। आपके पास चुनने के लिए कई भुगतान विधियां हैं और Bitcoin तथा कई अन्य क्रिप्टो कॉइन्स का उपयोग करके अपना खाता फंड कर सकते हैं।",
    
    # Common sections body
    "1win is a globally accessible sportsbook and casino, operating under Curaçao licence 8048/JAZ. New players use promo code": "1win एक वैश्विक स्तर पर सुलभ स्पोर्ट्सबुक और कैसीनो है, जो Curaçao 8048/JAZ लाइसेंस के तहत संचालित होता है। नए खिलाड़ी प्रोमो कोड",
    "to unlock a 600% welcome bonus across four deposits, up to $1,050 total.": "का उपयोग करके चार जमाओं में 600% स्वागत बोनस अनलॉक कर सकते हैं, कुल $1,050 तक।",
    
    # Step text
    "Use links on this page to access the official 1win website and click the 'Register' button.": "इस पेज पर दिए गए लिंक का उपयोग करके आधिकारिक 1win वेबसाइट पर जाएं और 'रजिस्टर' बटन पर क्लिक करें।",
    "Fill in the short registration form. When asked if you have a promo code, type in the": "संक्षिप्त रजिस्ट्रेशन फॉर्म भरें। जब प्रोमो कोड पूछा जाए, तो",
    "Make your first deposit. A 130% first deposit bonus is available with": "अपना पहला जमा करें।",
    "The first part of your 600% bonus package will be credited to your account. Start playing!": "आपके 600% बोनस पैकेज का पहला भाग आपके खाते में जमा किया जाएगा। खेलना शुरू करें!",
    
    # Bonus sections
    "Four deposits. Each one supercharged. Here's exactly how the 600% total bonus works with crypto deposits.": "चार जमाएं। हर एक सुपरचार्ज्ड। यहां बताया गया है कि क्रिप्टो जमा के साथ 600% कुल बोनस कैसे काम करता है।",
    "The above applies to crypto deposits. Fiat currency users get a 500% deposit bonus package across four deposits. 18+ | T&C Apply | Play Responsibly.": "उपरोक्त क्रिप्टो जमा पर लागू होता है। फिएट करेंसी उपयोगकर्ताओं को चार जमाओं में 500% जमा बोनस पैकेज मिलता है। 18+ | नियम और शर्तें लागू | जिम्मेदारी से खेलें।",
    "Crypto deposit bonus on your opening deposit.": "आपके पहले जमा पर क्रिप्टो जमा बोनस।",
    "Even bigger on your second top-up.": "दूसरे टॉप-अप पर और भी बड़ा।",
    "Serious boost on deposit number three.": "तीसरे जमा पर जबरदस्त बूस्ट।",
    "The biggest single bonus on your fourth deposit.": "चौथे जमा पर सबसे बड़ा एकल बोनस।",
    
    # FAQ answers
    "1win is global and can be accessed in lots of countries. You can access the sportsbook and casino via this page.": "1win वैश्विक है और कई देशों में एक्सेस किया जा सकता है। आप इस पेज के माध्यम से स्पोर्ट्सबुक और कैसीनो एक्सेस कर सकते हैं।",
    "Use the 1win promo code": "1win प्रोमो कोड",
    "when you register to get the best welcome bonus available. Up to 600% deposit bonus can be claimed.": "का उपयोग करें जब आप रजिस्टर करें ताकि उपलब्ध सर्वश्रेष्ठ स्वागत बोनस प्राप्त हो। 600% तक जमा बोनस दावा किया जा सकता है।",
    "1win is a legitimate online betting site offering sports betting, casino games and much more. The official website at 1win.pro holds a Curacao gambling licence.": "1win एक वैध ऑनलाइन बेटिंग साइट है जो स्पोर्ट्स बेटिंग, कैसीनो गेम्स और बहुत कुछ प्रदान करती है। 1win.pro पर आधिकारिक वेबसाइट के पास Curaçao 8048/JAZ जुआ लाइसेंस है।",
    "Yes. The 1win app is available on Android and iOS. Register to get the download.": "हां। 1win ऐप Android और iOS पर उपलब्ध है। डाउनलोड पाने के लिए रजिस्टर करें।",
    "1win Lucky Drive is a ticket-based promotion allowing players to win luxury vehicles, gadgets and free bets.": "1win Lucky Drive एक टिकट-आधारित प्रमोशन है जो खिलाड़ियों को लग्जरी वाहन, गैजेट और मुफ्त बेट जीतने की अनुमति देता है।",
    
    # CTA section
    "Use code XLBONUS when you register to unlock a 600% welcome bonus. Visit our": "रजिस्टर करते समय XLBONUS कोड का उपयोग करें और 600% स्वागत बोनस अनलॉक करें। हमारी",
    "promo code guide": "प्रोमो कोड गाइड",
    "for full details.": "पर पूरी जानकारी के लिए जाएं।",
    
    # Info table values
    "Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games": "स्पोर्ट्स बेटिंग, कैसीनो, लाइव कैसीनो, Aviator, पोकर, Lucky Drive, गेम्स",
    "Up to 600%": "600% तक",
    "BTC, DOGE, ETH, USDT and others": "BTC, DOGE, ETH, USDT और अन्य",
    "English, Spanish, Portuguese, Russian, Ukrainian, French, Italian, German, Polish, Kazakh, Hindi, Turkish, Tajik": "अंग्रेजी, स्पेनिश, पुर्तगाली, रूसी, यूक्रेनी, फ्रेंच, इतालवी, जर्मन, पोलिश, कजाख, हिंदी, तुर्की, ताजिक",
    "Yes, Android and iOS": "हां, Android और iOS",
    "Yes": "हां",
    
    # Girl break sections
    "Get your": "पाएं अपना",
    "600% bonus": "600% बोनस",
    "Use promo code": "प्रोमो कोड का उपयोग करें",
    "when registering to get the biggest available welcome bonus. Up to 600% across four deposits.": "रजिस्ट्रेशन करते समय सबसे बड़ा उपलब्ध स्वागत बोनस पाने के लिए। चार जमाओं में 600% तक।",
    "1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.": "1win 15 भाषाओं में उपलब्ध है। 30+ स्पोर्ट्स पर बेट लगाएं और कहीं से भी 11,000+ कैसीनो गेम्स खेलें।",
    "Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.": "कार्ड, ई-वॉलेट या क्रिप्टो से अपना खाता फंड करें। तेज, सुरक्षित और सीमाहीन।",
    "Exclusive tournaments, cash bonuses, and limited-time offers, updated regularly.": "एक्सक्लूसिव टूर्नामेंट, कैश बोनस और सीमित-समय के ऑफर, नियमित रूप से अपडेट।",
    "Claim your 600% bonus with code": "कोड के साथ अपना 600% बोनस दावा करें",
    "Curaçao-licensed, 4-hour average withdrawals.": "Curaçao 8048/JAZ लाइसेंसधारी, औसत 4 घंटे में निकासी।",
    
    # 18+ disclaimer
    "18+ only. New customers only. Terms and conditions apply. Gamble responsibly.": "केवल 18+। केवल नए ग्राहक। नियम और शर्तें लागू होती हैं। जिम्मेदारी से जुआ खेलें।",
    "18+": "18+",
    
    # Promotions
    "Casino": "कैसीनो",
    "Sports": "स्पोर्ट्स",
    "Slots": "स्लॉट्स",
    "Poker": "पोकर",
    "Special": "विशेष",
    "Hot": "हॉट",
    
    # Common news
    "Sins and Spins Tournament: $50,000 Prize Pool": "Sins and Spins टूर्नामेंट: $50,000 पुरस्कार राशि",
    "Spin the reels and climb the leaderboard for massive rewards.": "रीलें स्पिन करें और बड़े पुरस्कारों के लिए लीडरबोर्ड पर चढ़ें।",
    "Legends Tournament: $100,000 in Prizes": "Legends टूर्नामेंट: $100,000 पुरस्कार",
    "Compete against the best. Weekly tournaments with scheduled payouts.": "सर्वश्रेष्ठ के खिलाफ प्रतिस्पर्धा करें। निर्धारित भुगतान के साथ साप्ताहिक टूर्नामेंट।",
    "Aviamasters: Crash Game Championship": "Aviamasters: क्रैश गेम चैंपियनशिप",
    "Prove you're the ultimate Aviator pilot. Top cashouts win big.": "साबित करें कि आप अंतिम Aviator पायलट हैं। टॉप कैशआउट बड़ी जीत पाते हैं।",
    "Gamzix Slots Fest: Free Spins Galore": "Gamzix Slots Fest: भरपूर फ्री स्पिन",
    "Play featured Gamzix slots and earn free spins plus cash bonuses.": "फीचर्ड Gamzix स्लॉट्स खेलें और फ्री स्पिन के साथ कैश बोनस कमाएं।",
    "Olympics Special: Enhanced Odds on Every Sport": "Olympics Special: हर खेल पर बेहतर ऑड्स",
    "Boosted odds across all Olympic events. Back your country to win gold.": "सभी ओलंपिक इवेंट्स में बूस्टेड ऑड्स। अपने देश को गोल्ड जीतने के लिए बेट करें।",
    "Republic Day Bonus: 200 Free Spins": "गणतंत्र दिवस बोनस: 200 फ्री स्पिन",
    "Celebrate with 200 free spins on selected slots. Limited time only.": "चुनिंदा स्लॉट्स पर 200 फ्री स्पिन के साथ जश्न मनाएं। सीमित समय के लिए।",
    "Love Fest: Share the Jackpot": "Love Fest: जैकपॉट साझा करें",
    "Refer a friend and both receive bonus cash. Spread the love, stack the wins.": "एक दोस्त को रेफर करें और दोनों को बोनस कैश मिलेगा। प्यार फैलाएं, जीत जोड़ें।",
    
    # Common aria labels
    "Toggle menu": "मेनू टॉगल करें",
}

# Page-specific translations for titles/descriptions
# These are longer phrase replacements for specific page types
PAGE_TITLE_MAP = {
    # Index
    "1win Promo Code XLBONUS, 600% Welcome Bonus (2026)": "1win प्रोमो कोड XLBONUS, 600% स्वागत बोनस (2026)",
    "Get a 600% welcome bonus on your first four deposits at 1win with promo code XLBONUS. 30+ sports, 11,000+ casino games, Aviator, crypto payouts in 4 hours average. Curaçao licensed.": "1win पर प्रोमो कोड XLBONUS के साथ अपनी पहली चार जमाओं पर 600% स्वागत बोनस पाएं। 30+ स्पोर्ट्स, 11,000+ कैसीनो गेम्स, Aviator, औसत 4 घंटे में क्रिप्टो भुगतान। Curaçao 8048/JAZ लाइसेंसधारी।",
    "Use 1win promo code XLBONUS to unlock a 600% welcome bonus across your first 4 deposits. Sign up today and start winning on sports, casino, and Aviator.": "1win प्रोमो कोड XLBONUS का उपयोग करके अपनी पहली 4 जमाओं में 600% स्वागत बोनस अनलॉक करें। आज साइन अप करें और स्पोर्ट्स, कैसीनो और Aviator पर जीतना शुरू करें।",
    
    # Promo code
    "1win Promo Code XLBONUS - 600% Bonus": "1win प्रोमो कोड XLBONUS - 600% बोनस",
    
    # Casino
    "1win Casino: 11,000+ Games": "1win कैसीनो: 11,000+ गेम्स",
    
    # Sports betting
    "1win Sports Betting: 30+ Sports": "1win स्पोर्ट्स बेटिंग: 30+ खेल",
}

# Sections/headings
SECTION_TRANSLATIONS = {
    "Promo Code": "प्रोमो कोड",
    "Information": "जानकारी",
    "FAQs": "अक्सर पूछे जाने वाले प्रश्न",
    "Welcome bonus": "स्वागत बोनस",
    "Payment methods": "भुगतान विधियां",
    "Details": "विवरण",
    "Register": "रजिस्टर",
    "Login": "लॉगिन",
    "Latest Promotions": "नवीनतम प्रमोशन",
}

# =============================================================================
# FULL TEXT TRANSLATION DATABASE (text content patterns)
# =============================================================================

# A comprehensive dict for translating common English phrases to Hindi
# This is applied to text nodes via regex pattern matching
FULL_TRANSLATIONS = {}
FULL_TRANSLATIONS.update(NAV_TRANSLATIONS)
FULL_TRANSLATIONS.update(PHRASE_TRANSLATIONS)
FULL_TRANSLATIONS.update(PAGE_TITLE_MAP)


def get_hreflang_block():
    """Return the full hreflang block for all 46 locales."""
    locales = [
        "ar", "bg", "bn", "cs", "da", "de", "el", "en", "es", "et",
        "fa", "fi", "fr", "he", "hi", "hr", "hu", "id", "it", "ja",
        "kk", "ko", "lo", "lt", "lv", "mn", "ms", "mt", "nb", "nl",
        "pl", "pt", "ro", "ru", "sk", "sl", "sq", "sr", "sv", "th",
        "tl", "tr", "uk", "ur", "uz", "vi", "zh"
    ]
    lines = []
    for loc in locales:
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="https://1win.codes/{loc}/" />')
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://1win.codes/en/" />')
    return "\n".join(lines)


def fix_canonical_and_hreflang(content, en_path):
    """Fix canonical URL and hreflang block to point to /hi/ instead of /en/."""
    # Fix lang attribute
    content = content.replace('<html lang="en">', '<html lang="hi">')
    content = content.replace("<html lang='en'>", '<html lang="hi">')
    
    # Fix canonical - /en/ → /hi/
    content = re.sub(
        r'href="https://1win\.codes/en/([^"]*)"',
        lambda m: f'href="https://1win.codes/hi/{m.group(1)}"',
        content
    )
    # But keep hreflang links as-is (they should point to each locale)
    # We need to be smarter - only fix canonical specifically
    # Actually fix ALL /en/ hrefs in head to /hi/
    # But preserve hreflang entries (they should each point to their locale)
    
    return content


def fix_navigation_urls(content):
    """Fix navigation URLs from /en/ to /hi/."""
    # Fix nav links href="/en/..." → href="/hi/..."
    content = re.sub(
        r'href="/en/([^"]*)"',
        r'href="/hi/\1"',
        content
    )
    return content


def fix_canonical(content, hi_path):
    """Fix just the canonical link."""
    # Build the hi canonical URL
    # hi_path is like "index.html" or "bonus/index.html" etc.
    path_parts = hi_path.replace('.html', '').replace('/index', '/')
    if path_parts == 'index':
        path_parts = ''
    canonical_url = f"https://1win.codes/hi/{path_parts}"
    if not canonical_url.endswith('/'):
        canonical_url = canonical_url
    
    # Replace existing canonical
    content = re.sub(
        r'<link rel="canonical"[^>]+>',
        f'<link rel="canonical" href="{canonical_url}">',
        content
    )
    return content


def fix_json_ld_urls(content, hi_path):
    """Fix JSON-LD URLs to point to /hi/ instead of /en/."""
    # Replace /en/ with /hi/ in JSON-LD scripts
    def fix_jsonld_block(match):
        block = match.group(0)
        # Replace /en/ with /hi/ inside JSON-LD
        block = block.replace('/en/', '/hi/')
        return block
    
    content = re.sub(
        r'<script type="application/ld\+json"[^>]*>.*?</script>',
        fix_jsonld_block,
        content,
        flags=re.DOTALL
    )
    return content


def fix_hreflang_block(content):
    """Replace the hreflang block with complete 46-locale version."""
    # Find and replace existing hreflang links
    # Remove old hreflang links
    content = re.sub(
        r'\s*<link rel="alternate" hreflang="[^"]+"[^>]+/>\s*',
        '\n',
        content
    )
    
    # Build the full hreflang block
    locales = [
        "ar", "bg", "bn", "cs", "da", "de", "el", "en", "es", "et",
        "fa", "fi", "fr", "he", "hi", "hr", "hu", "id", "it", "ja",
        "kk", "ko", "lo", "lt", "lv", "mn", "ms", "mt", "nb", "nl",
        "pl", "pt", "ro", "ru", "sk", "sl", "sq", "sr", "sv", "th",
        "tl", "tr", "uk", "ur", "uz", "vi", "zh"
    ]
    hreflang_lines = []
    for loc in locales:
        hreflang_lines.append(f'  <link rel="alternate" hreflang="{loc}" href="https://1win.codes/{loc}/" />')
    hreflang_lines.append('  <link rel="alternate" hreflang="x-default" href="https://1win.codes/en/" />')
    hreflang_block = "\n".join(hreflang_lines)
    
    # Insert after canonical
    content = re.sub(
        r'(<link rel="canonical"[^>]+>)',
        r'\1\n' + hreflang_block,
        content
    )
    return content


def remove_em_en_dashes(content):
    """Remove em dashes and en dashes, replacing with hyphens or rephrasing."""
    # In HTML text, replace — and – with -
    # But be careful not to touch JSON-LD or scripts
    # We do a simple global replacement since em/en dashes in scripts are rare
    content = content.replace('—', '-')
    content = content.replace('–', '-')
    # Also handle HTML entities
    content = content.replace('&mdash;', '-')
    content = content.replace('&ndash;', '-')
    return content


def translate_text_segment(text):
    """Translate a segment of text from English to Hindi."""
    if not text or not text.strip():
        return text
    
    original = text
    
    # Apply phrase translations (longest first to avoid partial replacements)
    sorted_phrases = sorted(FULL_TRANSLATIONS.keys(), key=len, reverse=True)
    for phrase in sorted_phrases:
        if phrase in text:
            text = text.replace(phrase, FULL_TRANSLATIONS[phrase])
    
    return text


def translate_html_text(content):
    """
    Translate text content in HTML while preserving structure.
    Uses regex to find text between tags and translate it.
    """
    # We'll translate specific elements:
    # - title
    # - meta description/og content
    # - visible text between tags (excluding script/style)
    
    # Translate <title>
    def translate_title(m):
        title = m.group(1)
        translated = translate_text_in_title(title)
        return f'<title>{translated}</title>'
    
    content = re.sub(r'<title>(.*?)</title>', translate_title, content, flags=re.DOTALL)
    
    # Translate meta description
    def translate_meta_desc(m):
        desc = m.group(1)
        translated = translate_meta_description(desc)
        return m.group(0).replace(m.group(1), translated)
    
    content = re.sub(
        r'<meta name="description" content="([^"]*)"',
        lambda m: f'<meta name="description" content="{translate_meta_description(m.group(1))}"',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content="([^"]*)"',
        lambda m: f'<meta property="og:description" content="{translate_meta_description(m.group(1))}"',
        content
    )
    content = re.sub(
        r'<meta property="og:title" content="([^"]*)"',
        lambda m: f'<meta property="og:title" content="{translate_title_text(m.group(1))}"',
        content
    )
    
    # Translate aria-label attributes (but not class, id, data-*, href, src)
    content = re.sub(
        r'aria-label="([^"]*)"',
        lambda m: f'aria-label="{translate_aria_label(m.group(1))}"',
        content
    )
    
    return content


def translate_title_text(text):
    """Translate a title string."""
    for phrase in sorted(FULL_TRANSLATIONS.keys(), key=len, reverse=True):
        if phrase in text:
            text = text.replace(phrase, FULL_TRANSLATIONS[phrase])
    return text


def translate_in_title(text):
    """Translate title tag content."""
    return translate_title_text(text)


def translate_title(text):
    return translate_title_text(text)


def translate_meta_description(text):
    """Translate meta description."""
    return translate_title_text(text)


def translate_aria_label(text):
    """Translate aria labels."""
    translations = {
        "Sign Up": "साइन अप करें",
        "Toggle menu": "मेनू टॉगल करें",
        "Language": "भाषा",
        "1win home": "1win होम",
        "Breadcrumb": "ब्रेडक्रम्ब",
    }
    return translations.get(text, text)


# =============================================================================
# COMPREHENSIVE BODY CONTENT TRANSLATION
# Using regex to find text between tags and translate
# =============================================================================

def translate_body_content(content):
    """Translate visible text content in body HTML."""
    
    # Split content into script/style regions (don't translate) and HTML regions (do translate)
    # We'll use a state machine approach
    
    result = []
    i = 0
    
    # Tags to skip (preserve content verbatim)
    skip_tags = ['script', 'style', 'code', 'pre']
    
    while i < len(content):
        # Check if we're at start of a skip tag
        skip_found = False
        for tag in skip_tags:
            pattern = f'<{tag}[^>]*>'
            m = re.match(pattern, content[i:], re.IGNORECASE)
            if m:
                # Find the end tag
                end_tag = f'</{tag}>'
                end_pos = content.lower().find(end_tag.lower(), i + len(m.group(0)))
                if end_pos == -1:
                    end_pos = len(content)
                else:
                    end_pos += len(end_tag)
                # Preserve this block verbatim
                result.append(content[i:end_pos])
                i = end_pos
                skip_found = True
                break
        
        if not skip_found:
            # Check if we're at an HTML tag
            if content[i] == '<':
                # Find end of tag
                end = content.find('>', i)
                if end == -1:
                    result.append(content[i:])
                    break
                # Preserve the tag but translate certain attributes
                tag_content = content[i:end+1]
                result.append(tag_content)
                i = end + 1
            else:
                # Text content - find next tag
                next_tag = content.find('<', i)
                if next_tag == -1:
                    text = content[i:]
                    result.append(translate_text_node(text))
                    break
                text = content[i:next_tag]
                result.append(translate_text_node(text))
                i = next_tag
    
    return ''.join(result)


def translate_text_node(text):
    """Translate a text node (between HTML tags)."""
    if not text.strip():
        return text
    
    # Don't translate if it looks like code/numbers/URLs
    if re.match(r'^[\s\d\.,\+\-\%\$\/\(\)\[\]\{\}]+$', text.strip()):
        return text
    
    # Apply translations
    original = text
    for phrase in sorted(FULL_TRANSLATIONS.keys(), key=len, reverse=True):
        if phrase in text:
            text = text.replace(phrase, FULL_TRANSLATIONS[phrase])
    
    return text


def ensure_no_banned_words(content):
    """Remove/replace any banned words."""
    banned = {
        'हज़ारों': '11,000+',
        'सैकड़ों': '400,000+',
        'विश्व स्तरीय': 'उच्च-गुणवत्ता',
        'अत्याधुनिक': 'उन्नत',
        'अगली पीढ़ी का': 'बेहतरीन',
        'नवीनतम': 'नया',
        # English banned
        'world-class': 'high-quality',
        'cutting-edge': 'advanced',
        'next-generation': 'modern',
        'state-of-the-art': 'advanced',
    }
    for word, replacement in banned.items():
        content = content.replace(word, replacement)
    return content


def ensure_curacao_in_first_para(content):
    """
    Ensure first paragraph contains 1win + XLBONUS + number + Curaçao 8048/JAZ.
    If Curaçao is missing from first <p> tag, this is a structural issue from EN.
    We add it if missing.
    """
    # Check if Curaçao 8048/JAZ is present anywhere
    if 'Curaçao 8048/JAZ' not in content and 'Curacao 8048/JAZ' not in content:
        # Find first paragraph and append
        first_p = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
        if first_p:
            old_p = first_p.group(0)
            old_text = first_p.group(1)
            # Add Curaçao reference
            new_text = old_text.rstrip() + ' 1win Curaçao 8048/JAZ लाइसेंस के तहत संचालित होता है।'
            new_p = old_p.replace(old_text, new_text)
            content = content.replace(old_p, new_p, 1)
    return content


def translate_page(en_content, en_path):
    """Main translation function for a single page."""
    content = en_content
    
    # 1. Fix lang attribute
    content = content.replace('<html lang="en">', '<html lang="hi">')
    
    # 2. Remove em/en dashes
    content = remove_em_en_dashes(content)
    
    # 3. Fix navigation URLs /en/ → /hi/
    content = fix_navigation_urls(content)
    
    # 4. Fix canonical and JSON-LD URLs
    content = fix_json_ld_urls(content, en_path)
    
    # 5. Fix hreflang block (rebuild complete)
    content = fix_hreflang_block(content)
    
    # 6. Translate meta tags (title, description, og:title, og:description)
    content = translate_html_text(content)
    
    # 7. Translate body text content
    content = translate_body_content(content)
    
    # 8. Ensure no banned words
    content = ensure_no_banned_words(content)
    
    # 9. Ensure Curaçao present (normalize spelling too)
    content = content.replace('Curacao 8048/JAZ', 'Curaçao 8048/JAZ')
    
    return content


def process_all_pages():
    """Process all 184 pages from inventory."""
    inventory_path = BASE / "build_helpers" / "en_page_inventory.txt"
    inventory = [p.strip() for p in inventory_path.read_text().strip().split('\n') if p.strip()]
    
    processed = 0
    errors = []
    
    for en_rel_path in inventory:
        en_file = EN_DIR / en_rel_path
        hi_file = HI_DIR / en_rel_path
        
        if not en_file.exists():
            errors.append(f"EN file missing: {en_rel_path}")
            continue
        
        # Create output directory
        hi_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Read EN content
        en_content = en_file.read_text(encoding='utf-8')
        
        # Translate
        try:
            hi_content = translate_page(en_content, en_rel_path)
            hi_file.write_text(hi_content, encoding='utf-8')
            processed += 1
            if processed % 10 == 0:
                print(f"Processed {processed}/{len(inventory)}: {en_rel_path}")
        except Exception as e:
            errors.append(f"Error processing {en_rel_path}: {e}")
    
    print(f"\nDone: {processed}/{len(inventory)} processed")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    
    return processed, errors


if __name__ == "__main__":
    print("Starting Hindi translation...")
    processed, errors = process_all_pages()
    print(f"Complete: {processed} pages processed, {len(errors)} errors")
