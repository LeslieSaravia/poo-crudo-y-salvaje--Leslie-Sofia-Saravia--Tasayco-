class Tasks:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def show(self):
        print(f"Título: {self.title}")
        print(f"Descripción: {self.description}")
        print(f"Prioridad: {self.priority}")


def check_tasks(*Tasks):
    for list_tasks in Tasks:
        list_tasks.show()


def add_list():
    list_tasks = []
    while True:
        print("--- Nueva tarea ---")
        title_task = input("Ingrese el título de la tarea: ")
        description_task = input("Ingrese la descripción: ")
        priority_task = input("Ingrese el nivel de prioridad (bajo/medio/alto): ")
        
        task_new = Tasks(title_task, description_task, priority_task)  
        list_tasks.append(task_new)

        otro = input("¿Deseas ingresar otra tarea? (s/n): ").lower()
        if otro != 's':
            break
    return list_tasks



task1 = Tasks("Estudiar para examen", "Repasar capítulos 1 al 3 de matemáticas", "Alta")
task2 = Tasks("Comprar materiales", "Lápices, cuadernos, carpetas", "Media")
task3 = Tasks("Ordenar habitación", "Limpiar escritorio y organizar libros", "Baja")

nuevos = add_list()
print("--- TO DO LIST ---")
check_tasks(task1, task2, task3, *nuevos)
