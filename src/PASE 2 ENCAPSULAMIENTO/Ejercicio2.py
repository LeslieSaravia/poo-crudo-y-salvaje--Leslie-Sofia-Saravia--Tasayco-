class restaurant_reservation:
    def __init__(self, customer, time, number_people):
        self.__customer = customer
        self.__time = time
        self.__number_people = number_people

    def show(self):
        print(f"Cliente: {self.__customer}")
        print(f"Hora de reserva: {self.__time}")
        print(f"Número de personas: {self.__number_people}")

    def big_group(self):
        # TELL DON'T ASK
        if self.__number_people >= 6:
            print("El grupo es grande.")
        else:
            print("El grupo es pequeño")
    
    def all(self, list_reservations):
            print("Reservas actuales:")
            for reserva in list_reservations:
                reserva.show()
                reserva.big_group()
                print()


res1 = restaurant_reservation("Sofía", "19:00", 2)
res2 = restaurant_reservation("Juan", "20:30", 8)
res3 = restaurant_reservation("Lucía", "18:00", 4)


list_reservations = [res1, res2, res3]


res1.all(list_reservations)