#!/usr/bin/env python3
"""Round 2: restore Turkish diacritics for words missed by the main pass."""
import os, re, sys, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# Case-preserving replacements (handle Title case via separate entries)
# Each: stripped -> with diacritics
TR_FIXES = {
    "lisansi": "lisansı", "Lisansi": "Lisansı", "LISANSI": "LİSANSI",
    "isletilen": "işletilen", "Isletilen": "İşletilen",
    "kapsaminda": "kapsamında", "Kapsaminda": "Kapsamında",
    "erisim": "erişim", "Erisim": "Erişim",
    "tum": "tüm", "Tum": "Tüm", "TUM": "TÜM",
    "icin": "için", "Icin": "İçin", "ICIN": "İÇİN",
    "gercek": "gerçek", "Gercek": "Gerçek",
    "icinde": "içinde", "Icinde": "İçinde",
    "sirket": "şirket", "Sirket": "Şirket",
    "cogu": "çoğu", "Cogu": "Çoğu",
    "ulkeyi": "ülkeyi", "Ulkeyi": "Ülkeyi",
    "ulkede": "ülkede", "Ulkede": "Ülkede",
    "ulkelerde": "ülkelerde", "Ulkelerde": "Ülkelerde",
    "ulkeler": "ülkeler", "Ulkeler": "Ülkeler",
    "ulke": "ülke", "Ulke": "Ülke",
    "kapsiyor": "kapsıyor", "Kapsiyor": "Kapsıyor",
    "sonrasi": "sonrası", "Sonrasi": "Sonrası",
    "degil": "değil", "Degil": "Değil",
    "degildir": "değildir", "Degildir": "Değildir",
    "gore": "göre", "Gore": "Göre",
    "disinda": "dışında", "Disinda": "Dışında",
    "ayni": "aynı", "Ayni": "Aynı",
    "kisitlamalari": "kısıtlamaları", "Kisitlamalari": "Kısıtlamaları",
    "kisitlamalar": "kısıtlamalar", "Kisitlamalar": "Kısıtlamalar",
    "kisitlama": "kısıtlama", "Kisitlama": "Kısıtlama",
    "bolge": "bölge", "Bolge": "Bölge",
    "bolgeler": "bölgeler", "Bolgeler": "Bölgeler",
    "bolgesinde": "bölgesinde", "Bolgesinde": "Bölgesinde",
    "bolgelerinde": "bölgelerinde", "Bolgelerinde": "Bölgelerinde",
    "onemli": "önemli", "Onemli": "Önemli",
    "onemlidir": "önemlidir", "Onemlidir": "Önemlidir",
    "arasinda": "arasında", "Arasinda": "Arasında",
    "arasi": "arası", "Arasi": "Arası",
    "olusturmak": "oluşturmak", "Olusturmak": "Oluşturmak",
    "olusan": "oluşan", "Olusan": "Oluşan",
    "olusturulan": "oluşturulan", "Olusturulan": "Oluşturulan",
    "olusur": "oluşur", "Olusur": "Oluşur",
    "ornek": "örnek", "Ornek": "Örnek",
    "ornekler": "örnekler", "Ornekler": "Örnekler",
    "ornegin": "örneğin", "Ornegin": "Örneğin",
    "kosul": "koşul", "Kosul": "Koşul",
    "kosullar": "koşullar", "Kosullar": "Koşullar",
    "kosullari": "koşulları", "Kosullari": "Koşulları",
    "dunya": "dünya", "Dunya": "Dünya",
    "dunyanin": "dünyanın", "Dunyanin": "Dünyanın",
    "dunyada": "dünyada", "Dunyada": "Dünyada",
    "guncel": "güncel", "Guncel": "Güncel",
    "kullanim": "kullanım", "Kullanim": "Kullanım",
    "kullanici": "kullanıcı", "Kullanici": "Kullanıcı",
    "kullanicilar": "kullanıcılar", "Kullanicilar": "Kullanıcılar",
    "kullanicilari": "kullanıcıları", "Kullanicilari": "Kullanıcıları",
    "sirketler": "şirketler", "Sirketler": "Şirketler",
    "cogunluk": "çoğunluk", "Cogunluk": "Çoğunluk",
    "cogunlukla": "çoğunlukla", "Cogunlukla": "Çoğunlukla",
    "cevrim": "çevrim", "Cevrim": "Çevrim",
    "cekim": "çekim", "Cekim": "Çekim",
    "cekimler": "çekimler", "Cekimler": "Çekimler",
    "cekimi": "çekimi", "Cekimi": "Çekimi",
    "odeme": "ödeme", "Odeme": "Ödeme",
    "odemeler": "ödemeler", "Odemeler": "Ödemeler",
    "uye": "üye", "Uye": "Üye",
    "uyelik": "üyelik", "Uyelik": "Üyelik",
    "sifre": "şifre", "Sifre": "Şifre",
    "sifresi": "şifresi", "Sifresi": "Şifresi",
    "musteri": "müşteri", "Musteri": "Müşteri",
    "musteriler": "müşteriler", "Musteriler": "Müşteriler",
    "musterileri": "müşterileri", "Musterileri": "Müşterileri",
    "ucret": "ücret", "Ucret": "Ücret",
    "ucretsiz": "ücretsiz", "Ucretsiz": "Ücretsiz",
    "gunluk": "günlük", "Gunluk": "Günlük",
    "aylik": "aylık", "Aylik": "Aylık",
    "yillik": "yıllık", "Yillik": "Yıllık",
    "haftalik": "haftalık", "Haftalik": "Haftalık",
    "yil": "yıl", "Yil": "Yıl",
    "yilinda": "yılında", "Yilinda": "Yılında",
    "sart": "şart", "Sart": "Şart",
    "sartlar": "şartlar", "Sartlar": "Şartlar",
    "sartlari": "şartları", "Sartlari": "Şartları",
    "bircok": "birçok", "Bircok": "Birçok",
    "cunku": "çünkü", "Cunku": "Çünkü",
    "hosgeldin": "hoşgeldin", "Hosgeldin": "Hoşgeldin",
    "farkli": "farklı", "Farkli": "Farklı",
    "guvenle": "güvenle", "Guvenle": "Güvenle",
    "guvenli": "güvenli", "Guvenli": "Güvenli",
    "guvenlik": "güvenlik", "Guvenlik": "Güvenlik",
    "cesitli": "çeşitli", "Cesitli": "Çeşitli",
    "ozel": "özel", "Ozel": "Özel",
    "ozellik": "özellik", "Ozellik": "Özellik",
    "ozellikle": "özellikle", "Ozellikle": "Özellikle",
    "kisi": "kişi", "Kisi": "Kişi",
    "kisisel": "kişisel", "Kisisel": "Kişisel",
    "sehir": "şehir", "Sehir": "Şehir",
    "kucuk": "küçük", "Kucuk": "Küçük",
    "buyuk": "büyük", "Buyuk": "Büyük",
    "baslangic": "başlangıç", "Baslangic": "Başlangıç",
    "sonuc": "sonuç", "Sonuc": "Sonuç",
    "sonuclar": "sonuçlar", "Sonuclar": "Sonuçlar",
    "kurulus": "kuruluş", "Kurulus": "Kuruluş",
    "gecmis": "geçmiş", "Gecmis": "Geçmiş",
    "simdi": "şimdi", "Simdi": "Şimdi",
    "cesit": "çeşit", "Cesit": "Çeşit",
    "sayi": "sayı", "Sayi": "Sayı",
    "sira": "sıra", "Sira": "Sıra",
    "tikla": "tıkla", "Tikla": "Tıkla",
    "tiklayin": "tıklayın", "Tiklayin": "Tıklayın",
    "yardim": "yardım", "Yardim": "Yardım",
    "yardimci": "yardımcı", "Yardimci": "Yardımcı",
    "baslik": "başlık", "Baslik": "Başlık",
    "bagimsiz": "bağımsız", "Bagimsiz": "Bağımsız",
    "hizla": "hızla", "Hizla": "Hızla",
    "hizli": "hızlı", "Hizli": "Hızlı",
    "iceren": "içeren", "Iceren": "İçeren",
    "icerik": "içerik", "Icerik": "İçerik",
    "icerigi": "içeriği", "Icerigi": "İçeriği",
    "bos": "boş", "Bos": "Boş",
    "butun": "bütün", "Butun": "Bütün",
    "cocuk": "çocuk", "Cocuk": "Çocuk",
    "islem": "işlem", "Islem": "İşlem",
    "islemler": "işlemler", "Islemler": "İşlemler",
    "islemleri": "işlemleri", "Islemleri": "İşlemleri",
    "iste": "işte", "Iste": "İşte",
    "cikis": "çıkış", "Cikis": "Çıkış",
    "giris": "giriş", "Giris": "Giriş",
    "girisi": "girişi", "Girisi": "Girişi",
    "kazanc": "kazanç", "Kazanc": "Kazanç",
    "kazanclar": "kazançlar", "Kazanclar": "Kazançlar",
    "haric": "hariç", "Haric": "Hariç",
    "oraninda": "oranında", "Oraninda": "Oranında",
    "orani": "oranı", "Orani": "Oranı",
    "asagidaki": "aşağıdaki", "Asagidaki": "Aşağıdaki",
    "asagida": "aşağıda", "Asagida": "Aşağıda",
    "yukaridaki": "yukarıdaki", "Yukaridaki": "Yukarıdaki",
    "yukarida": "yukarıda", "Yukarida": "Yukarıda",
    "yapilan": "yapılan", "Yapilan": "Yapılan",
    "yapilir": "yapılır", "Yapilir": "Yapılır",
    "yapilmis": "yapılmış", "Yapilmis": "Yapılmış",
    "yapildi": "yapıldı", "Yapildi": "Yapıldı",
    "yapildigi": "yapıldığı", "Yapildigi": "Yapıldığı",
    "dunyanin": "dünyanın", "Dunyanin": "Dünyanın",
    "bolge": "bölge", "Bolge": "Bölge",
    "donus": "dönüş", "Donus": "Dönüş",
    "donusum": "dönüşüm", "Donusum": "Dönüşüm",
    "tikla": "tıkla", "soylenen": "söylenen", "Soylenen": "Söylenen",
    "tasiyor": "taşıyor", "Tasiyor": "Taşıyor",
    "erisimi": "erişimi", "Erisimi": "Erişimi",
    "guc": "güç", "Guc": "Güç",
    "guclu": "güçlü", "Guclu": "Güçlü",
    "turu": "türü", "Turu": "Türü",
    "turler": "türler", "Turler": "Türler",
    "tur": "tür",  # ambiguous - could be English "tur" too, but rare in TR betting context
    # Skip "is" - too ambiguous with English
}

# Protected regions: scripts (handle JSON-LD strings separately), styles, attrs, URLs, code
PROTECT_RE = re.compile(
    r'(<script(?![^>]*type=["\']application/ld\+json)[^>]*>.*?</script>'
    r'|<style[^>]*>.*?</style>'
    r'|<!--.*?-->'
    r'|href=\"[^\"]*\"'
    r'|src=\"[^\"]*\"'
    r'|content=\"https?://[^\"]*\"'
    r'|hreflang=\"[^\"]*\"'
    r'|lang=\"[^\"]*\"'
    r'|class=\"[^\"]*\"'
    r'|id=\"[^\"]*\"'
    r'|data-[a-zA-Z-]+=\"[^\"]*\"'
    r'|<code[^>]*>.*?</code>'
    r')',
    re.S | re.I,
)

def compile_fixes():
    out = []
    for k, v in TR_FIXES.items():
        if k == v:
            continue
        out.append((re.compile(r'\b' + re.escape(k) + r'\b'), v))
    return out

def apply_fixes(text, cfixes):
    parts = []
    last = 0
    for m in PROTECT_RE.finditer(text):
        chunk = text[last:m.start()]
        for pat, new in cfixes:
            chunk = pat.sub(new, chunk)
        parts.append(chunk)
        parts.append(m.group(0))
        last = m.end()
    tail = text[last:]
    for pat, new in cfixes:
        tail = pat.sub(new, tail)
    parts.append(tail)
    return "".join(parts)

def main():
    cfixes = compile_fixes()
    n = 0
    tr_dir = os.path.join(ROOT, "tr")
    for root, dirs, files in os.walk(tr_dir):
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(root, f)
            s = open(p, encoding="utf-8").read()
            new_s = apply_fixes(s, cfixes)
            if new_s != s:
                open(p, "w", encoding="utf-8").write(new_s)
                n += 1
    print(f"tr: {n} files updated")

if __name__ == "__main__":
    main()
