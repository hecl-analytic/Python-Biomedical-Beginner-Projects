import os

def load_data ():
    try:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(file_dir,"bmi_data.txt")
        with open(filepath, mode = "r" , encoding= "utf-8") as f:
            bmi_database = {}
            for row in f:
                row = row.strip()
                divide = row.split(";")
                patient_name  = divide[0]
                weight = divide[1]
                height = divide[2]
                bmi_database[patient_name] = weight,height
            return bmi_database
            
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
        return {}

def bmi_call (bmi_database:dict):
    bmi_results = []
    for name, measurement in bmi_database.items():
        weight_str = measurement [0]
        height_str = measurement [1]
        weight = float(weight_str)
        height = float(height_str)
        height_m = height / 100
        bmi = round((weight /(height_m * height_m)),2)
        bmi_results.append((bmi,name))
    return bmi_results

def average_bmi (bmi_results):
    sum = 0
    for count  in bmi_results:
        sum += count[0]
    avg_BMI = sum / len(bmi_results)
    return avg_BMI

def median_bmi (bmi_results:list):
    bmi_results.sort()
    mid = len(bmi_results)//2
    med_BMI = bmi_results[mid]
    return med_BMI

def bmi_diagnosis(bmi_results):

    Underweight = []
    Normal_weight = []
    Overweight = []
    Obesity_Class_I = []
    Obesity_Class_II = []
    Obesity_Class_III= []
    number_patients = 0

    for value, name in bmi_results:
        number_patients += 1

        if value < 18.5:
            Underweight.append((name,value))
        elif value <= 24.9:
            Normal_weight.append((name,value))
        elif value <= 29.9:
            Overweight.append((name,value))
        elif value <= 34.9:
            Obesity_Class_I.append((name,value))
        elif value <= 39.9:
            Obesity_Class_II.append((name,value))
        elif value > 39.9:
            Obesity_Class_III.append((name,value))

    return Underweight,Normal_weight,Overweight,Obesity_Class_I,Obesity_Class_II,Obesity_Class_III,number_patients


def save_data(bmi_results,med_BMI,avg_BMI,min_BMI,max_BMI,under,num_pat,normal,over,clasI,clasII,clasIII):
    with open("report_bmi_data.txt", mode= "w", encoding = "utf-8") as f:
        f.write(f"Výsledky BMI pro dataset\n")
        f.write("-"*60)
        f.write(f"\nSeřazený hodnoty pacientů:\n {bmi_results}\n")
        f.write(f"Celkový je v datasetu {num_pat} pacientů\n")
        f.write(f"Medián: {med_BMI}\n")
        f.write(f"Průměrná hodnota: {avg_BMI}\n")
        f.write(f"Maximální hodnota: {max_BMI}\n")
        f.write(f"Minimální hodnota: {min_BMI}\n")
        f.write("-"*60)
        f.write(f"\n{len(under)} pacientů má podváhu: {under}\n")
        f.write(f"\n{len(normal)} pacientů má zdravou(normální) váhu:\n {normal}")
        f.write(f"\n{len(over)} pacientů má lehkou nadváhu:\n {over}")
        f.write(f"\n{len(clasI)} pacientů má obesitu 1. stupně\n {clasI}")
        f.write(f"\n{len(clasII)} pacientů má obesitu 2. stupně\n {clasII}")
        f.write(f"\n{len(clasIII)} pacientů je morbidně obezních\n {clasIII}\n")
        f.write("-"*60)
        f.write("-"*60)
    print("-"*60)
    print("\nData byly uloženy\n")


if __name__ == "__main__":
    bmi_database = load_data()
    if bmi_database:
        bmi_results = bmi_call(bmi_database)
        max_BMI = max(bmi_results)
        min_BMI = min(bmi_results)
        avg_BMI = average_bmi(bmi_results)
        med_BMI = median_bmi(bmi_results)
        under,normal,over,clasI,clasII,clasIII,num_pat= bmi_diagnosis(bmi_results)
        bmi_results.sort()

        print("\nVýsledky BMI pro dataset")
        print("-"*60)
        print(f"Seřazený hodnoty pacientů:\n {bmi_results}\n")
        print(f"Median: {med_BMI}")
        print(f"Průměrná hodnota: {avg_BMI}")
        print(f"Maximální hodnota: {max_BMI}")
        print(f"Minimální hodnota: {min_BMI}")
        print("-"*60)
        print(f"\nZ celkového počtu {num_pat} pacientů\n")
        print(f"\n{len(under)} pacientů má podváhu: {under}\n")
        print(f"{len(normal)} pacientů má zdravou(normální) váhu:\n {normal}")
        print(f"{len(over)} pacientů má lehkou nadváhu:\n {over}")
        print(f"{len(clasI)} pacientů má obesitu 1. stupně\n {clasI}")
        print(f"{len(clasII)} pacientů má obesitu 2. stupně\n {clasII}")
        print(f"{len(clasIII)} pacientů je morbidně obezních\n {clasIII}")

        save_data(bmi_results,med_BMI,avg_BMI,min_BMI,max_BMI,under,num_pat,normal,over,clasI,clasII,clasIII)
