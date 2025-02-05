import basicrpg
Human = basicrpg.race("Human",0,0,0,0)
Commoner = basicrpg.profession("Commoner")
player = basicrpg.character(Human,Commoner,basicrpg.genname())

print("You are on a dusty trail")