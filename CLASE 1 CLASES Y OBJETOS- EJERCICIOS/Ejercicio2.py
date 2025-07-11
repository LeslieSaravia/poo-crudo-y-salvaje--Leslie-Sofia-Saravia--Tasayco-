class Student:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career

    def show(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Carrera: {self.career}")

    def legal_age(self):
        if self.age >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
            
            
            
def check_student(*Students):
    for Stds_new in Students:
        Stds_new.show()
        Stds_new.legal_age()


def add_Student():
    list_Stds = []
    while True:
        print("--- Nuevo Estudiante ---")
        name_Std = input("Nombre del estudiante: ")
        age_Std = float(input("Edad del estudiante: "))
        career_Std = input("Carrera: ")
        
        Stds_new = Student(name_Std, age_Std, career_Std)  
        list_Stds.append(Stds_new)

        otro = input("¿Deseas ingresar otro estudiante? (s/n): ").lower()
        if otro != 's':
            break
    return list_Stds

            

# Uso de la clase
std1 = Student("Lucía", 20, "Psicología")
std2 = Student("Carlos", 17, "Derecho")
std3 = Student("Ana", 22, "Ingeniería de Sistemas")

nuevos = add_Student()
print("--- Estado de estudiantes ---")
check_student(std1, std2, std3, *nuevos)
