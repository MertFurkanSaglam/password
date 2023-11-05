def sifre_kontrol(sifre):
    if len(sifre) < 8:
        return "Şifre çok kısa, en az 8 karakter olmalıdır."
    
    if not any(char.isupper() for char in sifre):
        return "Şifre en az bir büyük harf içermelidir."
    
    if not any(char.islower() for char in sifre):
        return "Şifre en az bir küçük harf içermelidir."
    
    if not any(char.isdigit() for char in sifre):
        return "Şifre en az bir rakam içermelidir."
    
    if not any(char in "!@#$%^&*" for char in sifre):
        return "Şifre özel karakter içermelidir: !@#$%^&* gibi."
    
    return "Şifre kabul edildi."

while True:
    sifre = input("Lütfen bir şifre girin: ")
    sonuc = sifre_kontrol(sifre)
    print(sonuc)
    
    if sonuc == "Şifre kabul edildi.":
        break
