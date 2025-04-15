import basicrpg
human = basicrpg.race("Human",0,0,0,0)
commoner = basicrpg.profession("Commoner")
player = basicrpg.character(human,commoner,basicrpg.genname())

class emf_reader(basicrpg.item):
    def use():
        print("Hello world")
emf_reader1 = emf_reader("EMF reader",1,"A device for detecting ghosts")
print(emf_reader1.name)

player.aquire(emf_reader1)

print(hasattr(emf_reader1,"use"))
player.printinvent()
