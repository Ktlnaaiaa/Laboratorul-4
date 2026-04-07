def calculeaza_bonus(suma: float) -> float:
    if suma < 0 or suma > 10000:
        raise ValueError("Sumă nevalidă")

    if suma < 100:
        return 0

    # BUG introdus intenționat: ar trebui să fie <= 500
    if suma < 500:
        return suma * 0.05

    return suma * 0.10
