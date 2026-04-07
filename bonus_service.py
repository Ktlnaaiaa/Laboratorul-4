def calculeaza_bonus(suma: float) -> float:
    """
    Calculează bonusul de fidelitate:
    - suma < 0 sau suma > 10000 -> eroare
    - suma < 100 -> 0 puncte
    - 100 <= suma <= 500 -> 5% bonus
    - suma > 500 -> 10% bonus
    """
    if suma < 0 or suma > 10000:
        raise ValueError("Sumă nevalidă")

    if suma < 100:
        return 0

    if suma <= 500:
        return suma * 0.05

    return suma * 0.10
