class fighter:

    # class attribute
    exp = "a powerful fighter"

    # instance attribute
    def __init__(self, name, attack, magic, dexterity, charname):
        self.name = name
        self.attack = attack
        self.magic = magic
        self.dexterity = dexterity
        self.charname = charname

# instantiate the figher class
Warrior = fighter("Warrior", 20, 0, 10, "nada")
Mage = fighter("Mage", 5, 20, 10, "nada")
Rogue = fighter("Rogue", 15, 5, 20, "nada")
Paladin = fighter("Paladin", 15, 15, 15, "nada")

# access the class attributes
print("The warrior is {}".format(Warrior.__class__.exp))
print("The mage is {}".format(Mage.__class__.exp))
print("The rogue is {}".format(Rogue.__class__.exp))
print("The paladin is {}".format(Paladin.__class__.exp))

print("_______________________________________________________")

# access the instance attributes
print("{} has {} strength and {} magic skill and {} dexterity".format( Warrior.name, Warrior.attack,Warrior.magic,Warrior.dexterity ))
print("{} has {} strength and {} magic skill and {} dexterity".format( Mage.name, Mage.attack,Mage.magic,Mage.dexterity ))
print("{} has {} strength and {} magic skill and {} dexterity".format( Rogue.name, Rogue.attack,Rogue.magic,Rogue.dexterity ))
print("{} has {} strength and {} magic skill and {} dexterity".format( Paladin.name, Paladin.attack,Paladin.magic,Paladin.dexterity ))

print("________________________________________________________")

y = str(input("What is thou name traveller?"))
print ("Please to meet you") 
print (y) 
print ( "Tell me, what is your class?       ")
print ("______________________")
x = int(input("(1) for Warrior, (2) for Mage, (3) for Rogue, (4) for Paladin        "))
print (x)


if (x) == 1:
    Warrior.charnname = (y)
    print ("You've chosen the Warrior")
    print("{} has {} strength and {} magic skill and {} dexterity and your name is {}".format( Warrior.name, Warrior.attack,Warrior.magic,Warrior.dexterity, Warrior.charnname ))
elif (x) == 2:
    Mage.charnname = (y)
    print ("You've chosen the Mage")
    print("{} has {} strength and {} magic skill and {} dexterity and your name is {}".format( Mage.name, Mage.attack,Mage.magic,Mage.dexterity, Mage.charnname ))
elif (x) == 3:
    Rogue.charnname = (y)
    print ("You've chosen the Rogue")
    print("{} has {} strength and {} magic skill and {} dexterity and your name is {}".format( Rogue.name, Rogue.attack,Rogue.magic,Rogue.dexterity, Rogue.charnname ))
elif (x) == 4:
    Paladin.charnname = (y)
    print ("You've chosen the Paladin")
    print("{} has {} strength and {} magic skill and {} dexterity and your name is {}".format( Paladin.name, Paladin.attack,Paladin.magic,Paladin.dexterity, Paladin.charnname ))
else:
    print ("Am I a fool? Come back when thouest are serious")