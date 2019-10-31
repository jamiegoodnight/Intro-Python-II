# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def __repr__(self):
        return f'{repr(self.name)} {repr(self.description)}'
