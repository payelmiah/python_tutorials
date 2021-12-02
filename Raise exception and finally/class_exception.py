class Accident(Exception):
    def __init__(self,mgs):
        self.mgs=mgs
    def print_exception(self):
        print("User defined exception ",self.mgs)

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()