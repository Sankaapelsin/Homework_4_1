def test__init_smartphone(smartphone_for_adding):
    assert smartphone_for_adding.memory == 512
    assert smartphone_for_adding.color == "red"
