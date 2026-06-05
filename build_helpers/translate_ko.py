#!/usr/bin/env python3
"""
Translate EN → KO for 1win.codes
- Stake CTA swap: all btn-class anchors → playstake.io/landing?c=max3000&offer=max3000
- lang="en" → lang="ko"
- canonical /en/... → /ko/...
- Preserve XLBONUS, 1win, Curaçao 8048/JAZ, brand names, JSON-LD structure
- No em/en dashes
- Register: -ㅂ니다/-습니다 polite Korean
"""

import re
import os
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
import json
import html as html_module

REPO = Path('/home/user/workspace/1win-codes-repo')
EN_DIR = REPO / 'en'
KO_DIR = REPO / 'ko'

STAKE_URL = 'https://playstake.io/landing?c=max3000&offer=max3000'
STAKE_REL = 'nofollow sponsored noopener'
STAKE_TARGET = '_blank'

# Button classes that trigger the Stake CTA swap
BTN_CLASSES = {'btn', 'btn-signup', 'btn-primary', 'btn-gold', 'btn-outline',
               'btn-cta', 'signup-btn', 'register-btn', 'claim-btn', 'cta'}

# Preserve these verbatim (not translated)
PRESERVE_EXACT = ['XLBONUS', '1win', 'Curaçao 8048/JAZ', 'Curaçao', 'Curacao',
                  'Pragmatic Play', 'Evolution Gaming', 'Spribe', 'Hacksaw Gaming',
                  'BGaming', "Play'n GO", 'NetEnt', 'Relax Gaming', 'Aviator',
                  'Lucky Drive', 'JetX', 'Spaceman', 'Sweet Bonanza',
                  'Gates of Olympus', 'Mines', 'Plinko', 'HiLo', 'Aviatrix',
                  'GamCare', 'SSL', 'G-S2MXR8D3HS']

# Known translation dictionary for common EN→KO phrases used in navigation/UI
# The main content will be translated via the TRANSLATIONS map
TRANSLATIONS = {
    # Navigation
    'Promo Code': '프로모 코드',
    'Sports': '스포츠',
    'Casino': '카지노',
    'Bonuses': '보너스',
    'Tools': '도구',
    'More': '더 보기',
    'News': '뉴스',
    'Register': '가입하기',
    'Login': '로그인',
    'Sign Up': '가입하기',
    # Footer
    'Products': '제품',
    'Promos': '프로모션',
    'Support': '지원',
    'Countries': '국가',
    'Sports Betting': '스포츠 베팅',
    'VIP Club': 'VIP 클럽',
    'Promotions': '프로모션',
    'Free Money': '무료 머니',
    'Mirror': '미러',
    'Mirrors': '미러',
    'Review': '리뷰',
    'Website': '웹사이트',
    'Live Streaming': '라이브 스트리밍',
    'Payments': '결제',
    'Download App': '앱 다운로드',
    'FAQ': '자주 묻는 질문',
    'Bangladesh': '방글라데시',
    'India': '인도',
    'Pakistan': '파키스탄',
    'Korea': '한국',
    'Malaysia': '말레이시아',
    'Singapore': '싱가포르',
    'South Africa': '남아프리카',
    'Tanzania': '탄자니아',
    'Malawi': '말라위',
    'Kenya': '케냐',
    'Brazil': '브라질',
    'Ghana': '가나',
    'Russia': '러시아',
    'Turkey': '터키',
    'Vietnam': '베트남',
    # Common UI
    'Home': '홈',
    'Bonus': '보너스',
    'Games': '게임',
    'Instant Crypto': '즉시 암호화폐',
    'Language': '언어',
    'Toggle menu': '메뉴 열기/닫기',
    # Age/disclaimer
    '18+': '18+',
    '18+ | T&C Apply | Play Responsibly.': '만 18세 이상 | 이용약관 적용 | 책임감 있는 게임.',
    '18+ only. New customers only. Terms and conditions apply. Gamble responsibly.': '만 18세 이상. 신규 고객 전용. 이용약관 적용. 책임감 있는 게임.',
    # CTA verbs
    'Register at 1win': '1win 가입하기',
    'Access 1win Registration': '1win 회원가입 접속',
    'Access Your 1win Account': '1win 계정 접속',
    'Login to 1win': '1win 로그인',
    'Join 1win': '1win 가입하기',
    'Claim Bonus': '보너스 받기',
    'Claim Promo Code →': '프로모 코드 받기 →',
    'Register with XLBONUS →': 'XLBONUS로 가입하기 →',
    'Open Account': '계정 열기',
    'Play Now': '지금 플레이',
    'Start Playing': '플레이 시작',
    'Get Bonus': '보너스 받기',
    'Claim Now': '지금 받기',
}


def is_btn_class(tag):
    """Check if tag has any button class that requires Stake URL swap."""
    if not hasattr(tag, 'get'):
        return False
    classes = tag.get('class', [])
    if isinstance(classes, str):
        classes = classes.split()
    return bool(set(classes) & BTN_CLASSES)


def swap_cta_url(tag):
    """Swap affiliate /link/ URL to Stake URL if tag has btn class."""
    if tag.name == 'a' and is_btn_class(tag):
        href = tag.get('href', '')
        # Swap any 1win affiliate link to Stake
        if '/link/' in href or '1win' in href.lower() or href == '#':
            tag['href'] = STAKE_URL
            tag['target'] = STAKE_TARGET
            tag['rel'] = STAKE_REL


def swap_all_cta_links(soup):
    """Find all btn-class anchors and swap their hrefs to Stake URL."""
    count = 0
    for tag in soup.find_all('a'):
        if is_btn_class(tag):
            href = tag.get('href', '')
            if href and href != STAKE_URL:
                tag['href'] = STAKE_URL
                tag['target'] = STAKE_TARGET
                tag['rel'] = STAKE_REL
                count += 1
            elif not href:
                tag['href'] = STAKE_URL
                tag['target'] = STAKE_TARGET
                tag['rel'] = STAKE_REL
                count += 1
    return count


def fix_lang_and_canonical(content, path_relative):
    """Fix html lang and canonical URL."""
    # lang="en" → lang="ko"
    content = re.sub(r'<html\s+lang="en"', '<html lang="ko"', content)
    # canonical /en/... → /ko/...
    content = re.sub(
        r'(<link\s+rel="canonical"\s+href="https://1win\.codes)/en/([^"]*")',
        r'\1/ko/\2',
        content
    )
    return content


def remove_lang_redirect(content):
    """Remove lang-redirect.js script tag (not needed in KO)."""
    content = re.sub(r'\s*<script\s+src="/lang-redirect\.js"[^>]*></script>', '', content)
    return content


def fix_em_en_dashes(text):
    """Replace em/en dashes with hyphens."""
    text = text.replace('\u2014', '-')  # em dash
    text = text.replace('\u2013', '-')  # en dash
    return text


def fix_nav_links_en_to_ko(content):
    """Replace /en/ paths with /ko/ in nav/footer links (not in canonical/hreflang)."""
    # Replace href="/en/... with href="/ko/... 
    content = re.sub(r'href="/en/', 'href="/ko/', content)
    return content


def translate_text_node(text):
    """
    Translate a text string from English to Korean.
    Preserves preserved terms, numbers, code strings, URLs.
    """
    if not text or not text.strip():
        return text
    
    # Check exact match in dict first
    stripped = text.strip()
    if stripped in TRANSLATIONS:
        # Preserve surrounding whitespace
        prefix = text[:len(text) - len(text.lstrip())]
        suffix = text[len(text.rstrip()):]
        return prefix + TRANSLATIONS[stripped] + suffix
    
    return text


def build_ko_header_nav():
    """Returns the Korean navigation HTML."""
    return '''<nav class="header-nav" id="mainNav">
        <a href="/ko/promo-code" class="nav-link">프로모 코드</a>
        <div class="nav-item">
          <a href="/ko/sports-betting" class="nav-link">스포츠 <svg class="nav-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <a href="/ko/sports-betting">전체 스포츠 베팅</a>
            <a href="/ko/sports/football">축구</a>
            <a href="/ko/sports/cricket">크리켓</a>
            <a href="/ko/sports/tennis">테니스</a>
            <a href="/ko/sports/basketball">농구</a>
            <a href="/ko/sports/esports">e스포츠</a>
            <a href="/ko/live-streaming">라이브 스트리밍</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="/ko/casino" class="nav-link">카지노 <svg class="nav-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <a href="/ko/casino">카지노 홈</a>
            <a href="/ko/slots/">슬롯 리뷰</a>
            <a href="/ko/providers/">게임 제공업체</a>
            <a href="/ko/aviator">Aviator</a>
            <a href="/ko/crash/">크래시 게임</a>
            <a href="/ko/poker">포커</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="/ko/bonus/" class="nav-link">보너스 <svg class="nav-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <a href="/ko/bonus/">전체 보너스</a>
            <a href="/ko/bonus/first-deposit-bonus">첫 번째 입금 200%</a>
            <a href="/ko/bonus/second-deposit-bonus">두 번째 입금 150%</a>
            <a href="/ko/bonus/third-deposit-bonus">세 번째 입금 150%</a>
            <a href="/ko/bonus/fourth-deposit-bonus">네 번째 입금 100%</a>
            <a href="/ko/bonus/wagering-requirements">베팅 조건</a>
            <a href="/ko/bonus/free-spins-today">오늘의 무료 스핀</a>
            <a href="/ko/bonus/cashback-bonus">캐시백</a>
            <a href="/ko/vip-club">VIP 클럽</a>
            <a href="/ko/lucky-drive">Lucky Drive</a>
            <a href="/ko/promotions">전체 프로모션</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="/ko/tools/" class="nav-link">도구 <svg class="nav-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <a href="/ko/tools/">전체 계산기</a>
            <a href="/ko/tools/odds-converter">배당률 변환기</a>
            <a href="/ko/tools/parlay-calculator">파라레이 계산기</a>
            <a href="/ko/tools/kelly-criterion-calculator">켈리 기준</a>
            <a href="/ko/tools/arbitrage-calculator">차익거래</a>
            <a href="/ko/tools/hedge-calculator">헤지</a>
            <a href="/ko/tools/each-way-calculator">이치웨이</a>
            <a href="/ko/tools/implied-probability-calculator">내재 확률</a>
            <a href="/ko/tools/bankroll-calculator">뱅크롤</a>
            <a href="/ko/tools/surebet-calculator">슈어벳</a>
            <a href="/ko/tools/matched-bet-calculator">매치드 벳</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="/ko/payments/" class="nav-link">더 보기 <svg class="nav-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <a href="/ko/payments/">결제 방법</a>
            <a href="/ko/app">모바일 앱</a>
            <a href="/ko/india/">인도 가이드</a>
            <a href="/ko/mirrors">미러</a>
            <a href="/ko/access">로그인</a>
            <a href="/ko/register">회원가입</a>
            <a href="/ko/review">리뷰</a>
            <a href="/ko/website">1win 소개</a>
            <a href="/ko/faq">자주 묻는 질문</a>
          </div>
        </div>
        <a href="/ko/news" class="nav-link">뉴스</a>
      </nav>'''


def build_ko_lang_switcher():
    """Returns the Korean lang switcher and signup button."""
    return '''<div class="header-actions"><select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="언어"><option value="../">EN</option><option value="../fr/">FR</option><option value="../de/">DE</option><option value="../es/">ES</option><option value="../pt/">PT</option><option value="../ru/">RU</option><option value="../tr/">TR</option><option value="../hi/">HI</option><option value="../bn/">BN</option><option value="../ar/">AR</option><option value="../ja/">JA</option><option value="" selected>KO</option><option value="../zh/">ZH</option><option value="../vi/">VI</option><option value="../th/">TH</option><option value="../nl/">NL</option><option value="../it/">IT</option><option value="../pl/">PL</option><option value="../ro/">RO</option><option value="../el/">EL</option><option value="../bg/">BG</option><option value="../uk/">UK</option><option value="../cs/">CS</option><option value="../da/">DA</option><option value="../fi/">FI</option><option value="../sv/">SV</option><option value="../nb/">NB</option><option value="../hu/">HU</option><option value="../sk/">SK</option><option value="../sl/">SL</option><option value="../hr/">HR</option><option value="../sr/">SR</option><option value="../sq/">SQ</option><option value="../lt/">LT</option><option value="../lv/">LV</option><option value="../et/">ET</option><option value="../mt/">MT</option><option value="../ms/">MS</option><option value="../id/">ID</option><option value="../tl/">TL</option><option value="../mn/">MN</option><option value="../uz/">UZ</option><option value="../fa/">FA</option><option value="../he/">HE</option><option value="../lo/">LO</option><option value="../ur/">UR</option><option value="../kk/">KK</option></select>
        <a href="''' + STAKE_URL + '''" target="_blank" rel="''' + STAKE_REL + '''" class="btn btn-signup" aria-label="가입하기">가입하기</a>
        <button class="hamburger" id="hamburger" aria-label="메뉴 열기/닫기">
          <span></span><span></span><span></span>
        </button>
      </div>'''


def build_ko_footer():
    """Returns a Korean footer."""
    return '''<footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="80" height="38" viewBox="0 0 74 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="1win">
            <path d="M29.1115 10.208C30.1487 10.208 31.0356 10.842 31.0959 12.6963L31.4601 21.4219L35.4465 11.6406C35.8806 10.5914 36.6194 10.208 37.7228 10.208H40.6838C42.2819 10.208 42.6501 11.6798 42.0109 13.1904L36.1096 27.7871C35.5337 29.2101 34.9846 29.9971 33.6701 29.9971L29.0451 30C27.5587 29.9999 26.7382 29.0408 26.7111 27.4277L26.3976 20.1523L23.3039 27.7773C22.7823 29.0196 22.2671 30 20.9797 30L16.924 29.9941C15.3081 29.9941 14.3853 29.1437 14.343 27.2295L14.1144 21.8594L15.3625 15.1953C15.8237 12.3645 14.8889 11.1646 14.093 10.2148L17.5275 10.2109C18.872 10.211 19.4293 10.8084 19.4806 12.4844L19.84 21.4248L23.841 11.5889C24.2119 10.6845 24.906 10.208 26.0969 10.208H29.1115Z" fill="white"/>
            <path d="M7.85174 10.6641C9.28687 9.94345 10.6554 10.0338 11.7619 10.7754C12.9287 11.6226 13.5922 12.9158 13.2336 14.6885L10.924 26.9912C10.5862 28.993 8.65369 30.3133 6.64276 29.9336C4.74922 29.5748 3.35277 27.7988 3.72967 25.6641L5.03826 18.5391L4.22479 18.9072C2.71416 19.5856 0.937298 18.9073 0.261897 17.3877C-0.413447 15.8681 0.262199 14.0858 1.77264 13.4043L7.85174 10.6641Z" fill="white"/>
            <path d="M49.2443 10.2119C51.2703 10.212 51.7946 11.1853 51.3332 13.3047L48.8039 27.1504C48.5479 28.6639 48.1102 29.9969 46.3224 29.9971H43.1476C41.6276 29.9971 41.0944 28.8513 41.3537 27.3799L43.964 12.7324C44.2263 11.1736 44.899 10.212 46.8498 10.2119H49.2443Z" fill="white"/>
            <path d="M67.5851 10.2051C69.5359 10.2051 70.4343 10.5584 71.5197 11.5322C73.3285 13.1514 73.6701 15.5666 73.2629 17.4873L71.466 27.1445C71.2158 28.6069 70.8296 29.9912 69.0656 29.9912L65.9572 29.9941C64.6034 29.9941 63.8884 29.0049 64.1535 27.3135L65.4142 19.7607C65.5949 18.3738 65.3328 17.3905 64.5793 16.7754C63.4065 15.8196 61.7479 16.2354 60.9064 17.2002C60.3638 17.7791 60.1169 18.5663 59.8273 20.1611L58.5607 27.1533C58.3225 28.5342 57.9366 29.9969 56.1037 29.9971H52.9797C51.035 29.9971 50.8989 28.3024 51.1193 27.3164L53.7512 12.7295C54.0076 11.3907 54.4814 10.208 56.6369 10.208L58.8771 10.2051C60.6138 10.2051 61.6483 10.8506 61.1027 13.2988L60.8703 14.5107C62.0672 12.0716 65.0013 10.2052 67.5851 10.2051Z" fill="white"/>
            <path d="M48.5988 1C50.5736 1.00011 52.175 2.60414 52.175 4.58203C52.175 6.55993 50.5736 8.16395 48.5988 8.16406C46.6239 8.16406 45.0226 6.56 45.0226 4.58203C45.0226 2.60407 46.6239 1 48.5988 1Z" fill="white"/>
          </svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin-bottom:16px;text-transform:uppercase;">1win.codes - 독립 제휴 리뷰</p>
          <div class="footer-badges">
            <span class="age-badge">18+</span>
            <span class="cert-badge">GamCare</span>
            <span class="cert-badge">SSL</span>
          </div>
        </div>

        <div class="footer-links-grid">
          <div class="footer-col">
            <h4>제품</h4>
            <a href="/ko/sports-betting">스포츠 베팅</a>
            <a href="/ko/casino">카지노</a>
            <a href="/ko/aviator">Aviator</a>
            <a href="/ko/poker">포커</a>
          </div>
          <div class="footer-col">
            <h4>프로모션</h4>
            <a href="/ko/promo-code">프로모 코드</a>
            <a href="/ko/vip-club">VIP 클럽</a>
            <a href="/ko/lucky-drive">Lucky Drive</a>
            <a href="/ko/promotions">무료 머니</a>
            <a href="/ko/mirrors">미러</a>
          </div>
          <div class="footer-col">
            <h4>지원</h4>
            <a href="/ko/register">회원가입</a>
            <a href="/ko/access">로그인</a>
            <a href="/ko/review">리뷰</a>
            <a href="/ko/website">웹사이트</a>
            <a href="/ko/live-streaming">라이브 스트리밍</a>
            <a href="/ko/payment-methods">결제</a>
            <a href="/ko/app">앱 다운로드</a>
            <a href="/ko/news">뉴스</a>
            <a href="/ko/faq">자주 묻는 질문</a>
            <a href="/ko/mirrors">미러</a>
          </div>
          <div class="footer-col">
            <h4>국가</h4>
            <a href="/ko/country-bangladesh">방글라데시</a>
            <a href="/ko/country-india">인도</a>
            <a href="/ko/country-pakistan">파키스탄</a>
            <a href="/ko/country-korea">한국</a>
            <a href="/ko/country-kenya">케냐</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="footer-disclaimer">이 사이트는 비공식 팬 사이트이며 1win과 제휴하거나 1win의 승인을 받은 사이트가 아닙니다. 이 사이트는 정보 제공 목적으로만 운영됩니다. 도박에는 위험이 따르므로 책임감 있게 플레이하십시오. 도박 문제가 있는 경우 GamCare 또는 지역 지원 기관에 연락하십시오.</p>
        <p class="footer-copyright">&copy; 2026 1win.codes. 모든 권리 보유.</p>
      </div>
    </div>
  </footer>'''


if __name__ == '__main__':
    print("Translation module loaded successfully")
    print(f"EN dir: {EN_DIR}")
    print(f"KO dir: {KO_DIR}")
    print(f"Stake URL: {STAKE_URL}")
