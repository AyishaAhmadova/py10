from packets import samitleri_al

def main():
    metin = input("Zəhmət olmasa bir cümlə daxil edin: ")
    netice = samitleri_al(metin)
    print("Netice:", netice)

if __name__ == "__main__":
    main()