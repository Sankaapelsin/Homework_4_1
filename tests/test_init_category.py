from classes import Category


def test_init_category():
    assert Category.__init__(name=str, description=str, goods=list) == []