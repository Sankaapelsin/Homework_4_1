def test_mixin_info(capsys, first_product):
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product('Samsung Galaxy C23 Ultra', '256B, Серый цвет, 200MP камера', 180000.0, 5)"
    )


def test_mixin_info_sph(capsys, smartphone_for_adding):
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone('Смартфон 1', 'Description of the product', 500.0, 10)"
    )


def test_mixin_print_lg(capsys, lawn_grass_for_adding):
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass('Газонная трава', 'Description of the product', 1000.0, 10)"
    )
