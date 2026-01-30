from patient import Patient

diagnosis_map = {
    "1": "Zdravý",
    "2": "Oba vysoké",
    "3": "Oba nízké",
    "4": "Nízké leuko",
    "5": "Vysoké leuko",
    "6": "Nízké hemo",
    "7": "Vysoké hemo",
    "8": "Vysoké hemo nizké leuko",
    "9": "Nízké hemo vysoké leuko"
}

diagnose_list = ["1.Zdravý",
                 "2.Oba vysoké",
                 "3.Oba nízké",
                 "4.Nízké leuko",
                 "5.Vysoké leuko",
                 "6.Nízké hemo",
                 "7.Vysoké hemo",
                 "8.Vysoké hemo nizké leuko",
                 "9.Nízké hemo vysoké leuko",
                 "10.Všechn"]

def correct(text):
    while True:
        try:
            selected = str(input(text)).capitalize()
            if not selected.isalpha():
                raise ValueError("Nezadal jste správny formát")
            else:
                return selected
        except ValueError as e:
            print(e)

def load_data(filename):
    sampls_list = []
    try:
        with open(filename,mode = "r", encoding = "utf-8") as f:
            for row in f:
                row_c = row.strip()
                row_c = row_c.split(";")
                id = row_c[0]
                hemo = row_c[1]
                leuko = row_c[2]
                pacient = Patient(id,hemo,leuko)
                sampls_list.append(pacient)
        return sampls_list
    except FileNotFoundError:
        print("Soubor nebyl nalezen")

def save_data(category_name,pacient_list):
    with open("protocol_output.txt", mode = "a", encoding = "utf-8") as f:
        f.write(f"{category_name}|Počet: {len(pacient_list)}\n")
        for pacient in pacient_list:
            f.write(f"{pacient}\n")
        f.write("-"*30)
        f.write("\n")

# Hlavní část programu 
def main(choice):
    sample_list = load_data("patients_data.txt")
    if sample_list:
        category = {}
        for pacient in sample_list:
            state = pacient.categorize()

            if state not in category:
                category[state] = []
            category[state].append(pacient)

        if "10" in choice:
            for category_code,pac in category.items():
                diagnose = diagnosis_map.get(category_code)
                print(f"{diagnose}|Počet: {len(pac)}")   
                for pacient in pac:
                    print(pacient)

        elif choice in category:
            pac = category[choice]
            diagnose = diagnosis_map.get(choice)
            print(f"{diagnose}|Počet: {len(pac)}")
            for pacient in pac:
                print(pacient)
                
            choice_save = correct("Chcete data uložit?: A or N: ").capitalize()
 
            if "A" in choice_save:
                save_data(diagnose,pac)
                print("Uloženo (protocol_output.txt)")
    return category

if __name__ == "__main__":
    while True:
            print("-"*30)
            for i in diagnose_list:
                print(i)
            print("-"*30)
            choise = input("Kterou skupinu chcete zobrazit?: ")
            category = main(choise)
            print("-"*30)
            choise_next = correct("Chcete vidět další: A or N: ").capitalize()
            if "N" in choise_next:
                print("Analyza ukončena")
                break
        
    
  
  