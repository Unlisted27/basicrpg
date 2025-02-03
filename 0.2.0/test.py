import basicrpg
Human = basicrpg.race("Human",0,0,0,0)
Commoner = basicrpg.profession("Commoner")
player = basicrpg.character(Human,Commoner,basicrpg.genname())
gold = basicrpg.items.item("Gold",1,"poop")
fur = basicrpg.items.item("fur",1,"A fur pelt",(gold,1))

#player.aquire(gold)

#shop = basicrpg.shop({"Hello world":1})
#shop.printshop()
#shop.buy(player,"Hello Wolrd",(gold,1))