def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Bir sayı 0'a bölünemez kanka!"
    return a / b

# Senin test çıktıların kalsın, sorun değil
if __name__ == "__main__":
    print(f"4 * 3 sonucu: {carpma(4, 3)}")
    print(f"Bölme Sonucu: {bolme(10, 2)}")
    print(f"Sıfıra Bölme Testi: {bolme(10, 0)}")
