import basicrpg
human = basicrpg.race("Human",0,0,0,0)
commoner = basicrpg.profession("Commoner")
player = basicrpg.character(human,commoner,basicrpg.genname())
class world(basicrpg.world):
    def __init__(self, world):
        pass
living_room = basicrpg.room("living room","A living room")
class emf_reader(basicrpg.item):
    def use(self,master:basicrpg.character):
        print(self.description)
        master.printinvent()
emf_reader1 = emf_reader("EMF reader",1,"A device for detecting ghosts")
print(emf_reader1.name)

player.aquire(emf_reader1)
player.printinvent()
player.use(emf_reader1)