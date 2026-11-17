#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Merhaba Dünya Programı
Her harf için sabırla bekler. Çünkü hayat hızlı, kod yavaş olmalı.
"""

import time
import sys

def yavas_yaz(metin, bekleme=0.8):
    """Her karakteri yavaşça yazar. Gerçekten yavaş."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Başlıyor... (sabır testi başladı)")
    time.sleep(1)
    
    yavas_yaz("Merhaba Dünya!")
    
    print("\nBitti. Şimdi düşün: Bu kadar yavaş olması gerekirdi mi?")
    
    # Gizli siyasi anlam (saklı, bulamazsın)
    # base64: Tüm politikacılar aynı çayı içer, sadece fincanlar farklıdır.
    gizli = "VHVtbSBwb2xpdGlrYWNpbGFyIGF5bmkgY2F5aSBpY2VyLCBzYWRlY2UgZmluY2FubGFyIGZhcmtsaWRpci4="
    # (decode etmeyin, yoksa anlarsınız)
    
    time.sleep(0.5)
    print("Program sonlandı. Git bir çay iç.")
