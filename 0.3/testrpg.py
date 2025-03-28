import basicrpg
def say_hi():
    print("Hello world")
human = basicrpg.race("human",0,0,0,0)
commoner = basicrpg.profession("commoner")
player = basicrpg.character(human,commoner,basicrpg.genname)
player.create_random()
knife = basicrpg.weapon("Knife",10,"A fine blade",(1,6),1)
dining_room = basicrpg.room("Dining room","You are standing in a dining room")
dining_room.set_contents({"Knife":knife})
dining_room.set_doors({"You cant escape":dining_room})
dining_room.set_actions({"hello":say_hi})
dining_room.execute(player)
