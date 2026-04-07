import pytest
from bonus_service import calculeaza_bonus


@pytest.mark.parametrize(
    "suma, rezultat",
    [
        (0, 0),
        (1, 0),
        (99, 0),
        (100, 5),
        (250, 12.5),
        (500, 25),
        (501, 50.1),
        (10000, 1000),
    ],
)
def test_bonus_valori_valide(suma, rezultat):
    assert calculeaza_bonus(suma) == rezultat


@pytest.mark.parametrize("suma", [-1, 10001])
def test_bonus_valori_invalide(suma):
    with pytest.raises(ValueError):
        calculeaza_bonus(suma)
