from plane import Plane
from train import Train


def get_int_input(message):
    try:
        return int(input(message))
    except ValueError:
        print('Param must be int!')
        quit()


def main():
    passengers = get_int_input(
        'Enter amount of passengers: ')
    distance = get_int_input(
        'Enter distance (km): ')
    plane_service_time = get_int_input(
        'Enter plane service time (minutes): ')
    train_stops_count = get_int_input(
        'Enter amount of stops for train: ')
    train_time_per_stop = get_int_input(
        'Enter stop duration for train (minutes): ')
    plane = Plane(plane_service_time / 60)
    train = Train(train_stops_count, train_time_per_stop / 60)
    vehicles = [plane, train]

    for vehicle in vehicles:
        vehicle_passengers = passengers
        while vehicle_passengers > 0:
            vehicle.add_passengers(vehicle_passengers)
            vehicle_passengers -= vehicle.get_passengers()
            vehicle.move(distance)
            vehicle.drop_off_passengers()
            if vehicle_passengers > 0:
                vehicle.move(distance)
        print('Total time for {} is {:.2f} hours'.format(
            vehicle, vehicle.get_time_in_move()))


if __name__ == '__main__':
    main()
