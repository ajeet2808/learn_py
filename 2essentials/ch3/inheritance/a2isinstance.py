class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


if __name__ == "__main__":
    my_vehicle = Vehicle()
    my_land_vehicle = LandVehicle()
    my_tracked_vehicle = TrackedVehicle()

    for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
        for cls in [Vehicle, LandVehicle, TrackedVehicle]:
            print(isinstance(obj, cls), end="\t")
        print()
