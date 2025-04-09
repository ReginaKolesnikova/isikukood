def arvuta_kontrollarv(kood):
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    summa1 = sum(int(kood[i]) * kaal1[i] for i in range(10))
    jaak = summa1 % 11
    
    if jaak != 10:
        return jaak
    
    summa2 = sum(int(kood[i]) * kaal2[i] for i in range(10))
    jaak = summa2 % 11
    
    if jaak != 10:
        return jaak
    
    return 0

def kontrolli_koodi(kood):
    if len(kood) != 11:
        return False

    if kood[0] not in '123456':
        return False

    kuupaeva_osa = kood[1:7]
    if not kuupaeva_osa.isdigit():
        return False

    kontrollnumber = arvuta_kontrollarv(kood)
    if kontrollnumber != int(kood[-1]):
        return False
    
    return True

def get_gender(kood):
    gender_number = int(kood[0])
    if gender_number in [1, 3, 5]:
        return "man"
    elif gender_number in [2, 4, 6]:
        return "woman"
    return None

def get_birthday(kood):
    gender_number = int(kood[0])
    
    if gender_number in [1, 2]:
        sajand = "18"
    elif gender_number in [3, 4]:
        sajand = "19"
    elif gender_number in [5, 6]:
        sajand = "20"
    
    day = kood[5:7]
    month = kood[3:5]
    year = sajand + kood[1:3] 
    
    return f"{day}.{month}.{year}"

def get_birthplace(kood):
    haigla_kood = int(kood[7:10])
    if 1 <= haigla_kood <= 10:
        return "Kuressaare Haigla"
    elif 11 <= haigla_kood <= 19:
        return "Tartu Ülikooli Naistekliinik"
    elif 21 <= haigla_kood <= 220:
        return "Ida-Tallinna Keskhaigla"
    elif 221 <= haigla_kood <= 270:
        return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= haigla_kood <= 370:
        return "Maarjamõisa Kliinikum (Tartu)"
    elif 371 <= haigla_kood <= 420:
        return "Narva Haigla"
    elif 421 <= haigla_kood <= 470:
        return "Pärnu Haigla"
    elif 471 <= haigla_kood <= 490:
        return "Pelgulinna Sünnitusmaja (Tallinn)"
    elif 491 <= haigla_kood <= 520:
        return "Järvamaa Haigla (Paide)"
    elif 521 <= haigla_kood <= 570:
        return "Rakvere, Tapa haigla"
    elif 571 <= haigla_kood <= 600:
        return "Valga Haigla"
    elif 601 <= haigla_kood <= 650:
        return "Viljandi Haigla"
    elif 651 <= haigla_kood <= 700:
        return "Lõuna-Eesti Haigla (Võru)"
    return "Unknown place"

def main():
    ikoodid = []
    arvud = []
    
    while True:
        kood = input("Enter isikukood (or enter 'exit' to get last statistics): ")
        if kood.lower() == 'exit':
            break
        
        if kontrolli_koodi(kood):
            gender = get_gender(kood)
            birthday = get_birthday(kood)
            birthplace = get_birthplace(kood)
            print(f"It's a {gender}, birthday is {birthday} and birthplace is {birthplace}")
            ikoodid.append((kood, gender))
        else:
            print("Wrong code, try again.")
            arvud.append(int(kood))
    
    ikoodid.sort(key=lambda x: (x[1] == "man", x[0]))
    arvud.sort()

    print("\nList of right codes (sorted by gender):")
    for kood, gender in ikoodid:
        print(kood)
    
    print("\nList of wrong codes (sorted by ascending):")
    for kood in arvud:
        print(kood)
        
        
if __name__ == "__main__":
    main()
