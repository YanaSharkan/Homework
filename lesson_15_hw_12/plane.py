from vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, service_time):
        super().__init__(320, 150)
        self.service_time = service_time

    def __str__(self):
        return 'Plane'

    def move(self, distance):
        initial_time = self.get_time_in_move()
        time = self.service_time + distance / self.get_average_speed()
        self.set_time_in_move(initial_time + time)
