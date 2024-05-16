def samitleri_al(metin):
    samit = set()
    for simvol in metin:
        if simvol.lower() not in 'aeiou' and simvol.isalpha():
            samit.add(simvol.lower())
    return samit