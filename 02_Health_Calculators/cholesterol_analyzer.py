import os

def loading_data ():
    try:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(file_dir,"cholesterol_data.txt")
        with open(filepath, mode = "r", encoding= "utf-8") as f:
            cholesterol_database = {}
            sum  =0
            for row in f:
                row = row.strip()
                divide = row.split(";")
                patient_name = divide[0]
                indicator = divide[1]
                value = divide[2]
                if indicator == "Cholesterol":
                    cholesterol_database[patient_name] = value
                    sum += 1
            return cholesterol_database
    except FileNotFoundError:
        print("File not found")
        return {}

def diagnose (cho_database:dict):
    normal = {}
    increased_risk = {}
    high_risk = {}
    number_of_patients = 0
    num_normal = 0
    num_increased = 0
    num_high = 0
    for name, value in cho_database.items():
        exchange_value  = float(value)
        if exchange_value <= 5:
            normal[name] = value
            num_normal += 1
        elif exchange_value <= 6.5:
            increased_risk[name] = value
            num_increased += 1
        else:
            high_risk[name] = value 
            num_high += 1
        number_of_patients += 1
    return normal, increased_risk, high_risk, number_of_patients,num_normal,num_increased,num_high

def calculate_statistic (data_list:dict):
    value_chool = []
    if data_list:
        for name, i in data_list.items():
            exchange_i = float(i)
            value_chool.append((exchange_i , name))
        max_chol = max(value_chool)
        min_chol = min(value_chool)
        value_chool.sort()
        length_cholesterol = int(len(value_chool) //2)
        median_chol = value_chool[length_cholesterol]
        return max_chol, min_chol,median_chol, value_chool

def save_data(number_of_patients,num_normal,num_increased,num_high,max_chol_all, 
              min_chol_all,median_chol,
              max_chol_normal, min_chol_normal,median_normal, normal_chol,
              max_chol_increased,min_chol_increased,median_increased,increased_risk_chol,
              max_chol_high, min_chol_high,median_high, high_chol):
    try:
        with open("report_cholesterol.txt", mode = "w" ,encoding="utf-8") as f:
            f.write("REPORT CHOLESTEROL")
            f.write(f"\n{num_normal} má hodnoty v normálu  (<=5 mmol/l):\n {normal_chol}\n")
            f.write("-"*30)
            f.write(f"\n{num_increased} má zvýšené riziko (5,1 - 6,5mmol/l):\n {increased_risk_chol}\n")
            f.write("-"*30)
            f.write(f"\n{num_high} má vysoké riziko (> 6.5 mmol/l):\n {high_chol}\n")
            f.write("-"*30)
            f.write(f"\nCelkový počet pacientů: {number_of_patients}\n")
            f.write(f"Celkové maximum: {max_chol_all}\n")
            f.write(f"Celkové minimum: {min_chol_all}\n")
            f.write(f"Median: {median_chol}\n")
            f.write("-"*30)
            f.write("\n----- NORMA ----- \n")
            f.write(f"Celkové maximum: {max_chol_normal}\n")
            f.write(f"Celkové minimum: {min_chol_normal}\n")
            f.write(f"Median: {median_normal}\n")
            f.write("-"*30)
            f.write("\n----- ZVÝŠENÉ RIZIKO----- \n")
            f.write(f"Celkové maximum: {max_chol_increased}\n")
            f.write(f"Celkové minimum: {min_chol_increased}\n")
            f.write(f"Median: {median_increased}\n")
            f.write("-"*30)
            f.write("\n----- VYSOKÉ RIZIKO----- \n")
            f.write(f"Celkové maximum: {max_chol_high}\n")
            f.write(f"Celkové minimum: {min_chol_high}\n")
            f.write(f"Median: {median_high}\n")
            f.write("-"*30)
        print("Soubor byl uložen'report_cholesterol.txt'")
    except FileExistsError:
        print("Složka s tímto jmnem existuje")

        
if __name__ == "__main__":
    cholesterol_database = loading_data()
    if cholesterol_database:
        normal, increased_risk, high_risk, number_of_patients,num_normal,num_increased,num_high = diagnose(cholesterol_database)
        max_chol_all, min_chol_all,median_chol,value_chool = calculate_statistic (cholesterol_database)
        max_chol_normal, min_chol_normal,median_normal, normal_chol = calculate_statistic(normal)
        max_chol_increased,min_chol_increased,median_increased,increased_risk_chol = calculate_statistic(increased_risk)
        max_chol_high, min_chol_high,median_high, high_chol = calculate_statistic(high_risk)


        print(f"\n{num_normal} má hodnoty v normálu  (<=5 mmol/l):\n {normal_chol}\n")
        print("-"*30)
        print(f"\n{num_increased} má zvýšené riziko (5,1 - 6,5mmol/l):\n {increased_risk_chol}\n")
        print("-"*30)
        print(f"\n{num_high} má vysoké riziko (> 6.5 mmol/l):\n {high_chol}\n")
        print("-"*30)
        print(f"Celkový počet pacientů: {number_of_patients}")
        print(f"Celkové maximum: {max_chol_all}")
        print(f"Celkové minimum: {min_chol_all}")
        print(f"Median: {median_chol}")
        print("-"*30)
        print("----- NORMA ----- ")
        print(f"Celkové maximum: {max_chol_normal}")
        print(f"Celkové minimum: {min_chol_normal}")
        print(f"Median: {median_normal}")
        print("-"*30)
        print("----- ZVÝŠENÉ RIZIKO----- ")
        print(f"Celkové maximum: {max_chol_increased}")
        print(f"Celkové minimum: {min_chol_increased}")
        print(f"Median: {median_increased}")
        print("-"*30)
        print("----- VYSKOÉ RIZIKO----- \n")
        print(f"Celkové maximum: {max_chol_high}")
        print(f"Celkové minimum: {min_chol_high}")
        print(f"Median: {median_high}")
        print("-"*30)


        save_data(number_of_patients,num_normal,num_increased,num_high,max_chol_all, 
                    min_chol_all,median_chol,max_chol_normal, min_chol_normal,median_normal, normal_chol,
                    max_chol_increased,min_chol_increased,median_increased,increased_risk_chol,
                    max_chol_high, min_chol_high,median_high, high_chol)


