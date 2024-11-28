def bmi(tinggi, berat):
    return berat / (tinggi ** 2)


def whtr(pinggang, tinggi):
    return pinggang / tinggi


def bfp(bmi, umur, gender):
    if gender == "laki-laki":
        return bmi * (1.2 * bmi + 0.23 (umur - 16.2))
    elif gender == "perempuan":
        return bmi * (1.2 * bmi + 0.23 (umur - 5.4))
