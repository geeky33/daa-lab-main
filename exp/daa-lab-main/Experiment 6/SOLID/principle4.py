#Clients should not be forced to implement interfaces they do not use. Instead of one large interface, break it into smaller, specific ones.

#Example:
#Bad Design:
#A Worker interface with methods not relevant to all types of workers:

class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        return "Working"

    def eat(self):
        raise NotImplementedError("Robots don't eat")
#Good Design:
#Separate the interfaces:

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Working"

    def eat(self):
        return "Eating"

class Robot(Workable):
    def work(self):
        return "Working"