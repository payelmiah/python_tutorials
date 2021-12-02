class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "actor":
            print(self.name, "Hi, I'm an actor")
        elif self.occupation == "tennis player":
            print(self.name, "Hi,I'm a tennis player")

    def speaks(self):
        print(self.name, ":Say how are you guys")


tom = Human("Tom cruise", "actor")
tom.do_work()
tom.speaks()

maria=Human("Maria","tennis player")
maria.do_work()
maria.speaks()