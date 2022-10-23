"""
This module provides base class for vehicles.
"""


class Vehicle:
    def __init__(self, average_speed, max_passengers):
        self._average_speed = average_speed
        self._max_passengers = max_passengers
        self._passengers = 0
        self._time_in_move = 0

    def get_time_in_move(self):
        return self._time_in_move

    def set_time_in_move(self, time):
        self._time_in_move = time

    def get_average_speed(self):
        return self._average_speed

    def get_passengers(self):
        return self._passengers

    def add_passengers(self, passengers):
        if passengers > self._max_passengers:
            passengers_to_add = self._max_passengers
        else:
            passengers_to_add = passengers

        self._passengers += passengers_to_add

    def drop_off_passengers(self):
        self._passengers = 0
