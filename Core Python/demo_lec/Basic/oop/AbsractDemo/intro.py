#

from abc import ABC , abstractmethod

class Worrior(ABC):

    @abstractmethod
    def fight():
        pass

class ArcheryWorrior(Worrior):
    def fight(self):
        print(" ArcheryWorrior is used archery to fight.")

class MaceWorrior(Worrior):
    def fight(self):
        print(" MaceWorrior is used mace to fight.")

class SwordWorrior(Worrior):
    def fight(self):
        print(" SwordWorrior is used sword to fight.")

arch = ArcheryWorrior()
mace = MaceWorrior()
sword = SwordWorrior()

li_of_object = [arch , mace, sword]

for obj in li_of_object:
    obj.fight()

