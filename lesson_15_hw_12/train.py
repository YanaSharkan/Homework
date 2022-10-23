from vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, stops_count, time_per_stop):
        super().__init__(60, 600)
        self._stops_count = stops_count
        self._time_per_stop = time_per_stop

    def __str__(self):
        return 'Train'

    def move(self, distance):
        initial_time = self.get_time_in_move()
        time_in_stops = self._stops_count * self._time_per_stop
        time = distance / self.get_average_speed()
        self.set_time_in_move(initial_time + time + time_in_stops)
