class house:
    def __init__(self, bedroom_count, sq_footage, framing_style, num_of_exterior_doors, num_of_interior_doors, num_of_floors, front_door_is_open=False ):
        self.bedroom_count = bedroom_count
        self.sq_footage = sq_footage
        self.framing_style = framing_style
        self.num_of_exterior_doors = num_of_exterior_doors
        self.num_of_interior_doors = num_of_interior_doors
        self.num_of_floors = num_of_floors
        self.front_door_is_open = front_door_is_open

    def print_info(self):
        print(f"**********{self.owner}'s house **********")
        print(f"bedroom_count: {self.bedroom_count}")
        print(f"sq_footage: {self.sq_footage}")
        print(f"framing_style: {self.framing_style}")
        print(f"num_of_exterior_doors: {self.num_of_exterior_doors}")
        print(f"num_of_interior_doors: {self.num_of_interior_doors}")
        print(f"num_of_floors: {self.num_of_floors}")
        print(f"front_door_is_open: {self.front_door_is_open}")
        return self

    def open_front_door(self):
        self.front_door_is_open = True
        return self

    def close_front_door(self):
        self.front_door_is_open = False
        return self

    def toggle_front_door(self, state):
        self.front_door_is_open = state
        return self
    
    @classmethod # -> targets the class itself
    def change_creator(cls, name):
        cls.change_creator = name
    
    # @staticmethod # -> targets nothing

tyler_house = house(3, 400, "A frame", 1, 2, 2)
nolan_house = house(15,1500, "A frame", 5, 10, 3)

# print(tyler_house.all_houses)

tyler_house.toggle_front_door(True).print_info

print(tyler_house.bedroom_count)

nolan_house.bedroom_count = 5
print(nolan_house.bedroom_count)

print(tyler_house)