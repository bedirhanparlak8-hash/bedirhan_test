def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b
# Mevcut fonksiyonların altına ekle
def carp(a, b):
    return a * b

print(f"4 * 3 sonucu: {carp(4, 3)}")
print("Terminalden selamlar!")
def bolme(a, b):
    if b == 0:
        return "Hata: Bir sayı 0'a bölünemez kanka!"
    return a / b

# Test etmek için:
print("Bölme Sonucu:", bolme(10, 2))
print("Sıfıra Bölme Testi:", bolme(10, 0))
