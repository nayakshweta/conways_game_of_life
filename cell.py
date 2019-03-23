class Cell:
    def __init__(self, coordinate, status):
        self.coordinate = coordinate
        self.status = status

    def calculate_next_status(self, live_neighbour_count):
        next_status = False
        if live_neighbour_count in (2,3) and self.status == True:
            next_status = True
        elif live_neighbour_count == 3 and self.status == False:
            next_status = True
        else:
            next_status = False
        return next_status

    def get_current_status(self):
        return self.status