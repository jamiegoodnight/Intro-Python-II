class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{repr(self.name)} \n{repr(self.description)}'
