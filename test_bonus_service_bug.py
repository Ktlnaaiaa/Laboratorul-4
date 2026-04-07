from bonus_service_bug import calculeaza_bonus


def test_bug_detectat_la_limita_500():
    assert calculeaza_bonus(500) == 25
