class Patient:
    def __init__(self,id,hemo,leuko):
        self.id = id
        self.hemo = int(hemo)
        self.leuko = float(leuko)

    def control_hemoglobin(self):
        if self.hemo < 135:
            return "Nízké"
        elif self.hemo >175:
            return "Vysoké"
        else:
            return "Norma"
    def control_leukocyt(self):
        leuko = self.leuko
        if leuko > 10:
            return "Vysoké"
        elif leuko < 4:
            return "Nízké"
        else:
            return "Norma"
    def categorize(self):
        h = self.control_hemoglobin()
        w = self.control_leukocyt()
        cate ={
            ("Norma","Norma"): "1",
            ("Vysoké","Vysoké"): "2",
            ("Nízké","Nízké"): "3",
            ("Norma","Nízké"): "4",
            ("Norma","Vysoké"):"5",
            ("Nízké","Norma"):"6",
            ("Vysoké","Norma"):"7",
            ("Vysoké","Nízké"):"8",
            ("Nízké","Vysoké"):"9",
        }
        return cate.get((h,w))
       
    def __str__(self):
        return f"{self.id}| HGB:{self.hemo} | WBC: {self.leuko}"
