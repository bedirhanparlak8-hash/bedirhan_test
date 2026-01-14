import hesapla

def test_toplama():
    # 5 + 3'ün 8 etmesi gerektiğini robota söylüyoruz
    assert hesapla.topla(5, 3) == 8

def test_cikarma():
    # 10 - 4'ün 6 etmesi gerektiğini robota söylüyoruz
    assert hesapla.cikar(10, 4) == 6
