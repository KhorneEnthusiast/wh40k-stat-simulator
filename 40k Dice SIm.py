import customtkinter as ctk
import random
from CTkMessagebox import CTkMessagebox

## all the gui shit
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.resizable(height= 500, width = 500)


frame = ctk.CTkFrame(master=root)
frame.pack(pady = 20, padx=60,fill = "both" , expand = True)
##placeholder variables for hit/damage/wound functions. Extracts these from entries later
##attacks = 20
##weaponSkill = 4
##enemytoughness= 4
##strength = 4
##enemySave= 2
##invulnSave=4
##armorPen = 4
##hasInvuln = True
##damage = 1

class dataSheet():
    stats = {
            "Attacks" : 0, 
            "WeaponSkill" : 0,
            "Strength":0,
            "ArmorPen":0,
            "Toughness":0,
            "Wounds":0,
            "Damage":0
            }
    
    
unit1 = dataSheet()
unit2 =dataSheet()
    


## function for determining hit rolls
def determineHits(attacks,weaponSkill):
    global successfulHits 
    successfulHits = 0
    for hits in range(attacks):
        roll = random.randint(1,6)
        if roll >= weaponSkill:
            successfulHits += 1
            print("Hit Roll:",roll)
        if roll < weaponSkill:
            pass
            print("Hit Roll:",roll)
    print(f"You landed {successfulHits} hits.")
    return successfulHits



##function to determine wound rolls
def determineWounds(strength,enemytoughness,successfulHits):
    toughness = enemytoughness
    global successfulWounds
    successfulWounds = 0
    woundReq = 0
    if strength == toughness:
        woundReq = 4
    if strength > toughness:
        woundReq = 3
    if strength >= toughness * 2:
        woundReq = 2
    if strength < toughness:
        woundReq = 5
    if strength <= toughness / 2:
        woundReq = 6
    for wounds in range(successfulHits):
        roll = random.randint(1,6)
        if roll >= woundReq:
            successfulWounds += 1
            print("Wound Roll:", roll)
        if roll < woundReq:
            print("Wound Roll:", roll)
            pass
    print(f"You landed {successfulWounds} wounds.")
    return successfulWounds

##Determine if the enemy saves the wounds. Modifys armor save based on AP of weapon, and checks for invuln. if has invuln, enemySave is always == invulnSave

def determineSave(enemySave,invulnSave,armorPen,successfulWounds,damage,toggleInvuln):
    savedWounds = 0
    failedWounds = 0
    enemySave = enemySave - armorPen
    damageTaken = 0
    print(f"Needs {enemySave} to save")
    if toggleInvuln == "1":
        enemySave = invulnSave
        print(f"Invuln save active. {invulnSave}, {enemySave}")
    for saves in range(successfulWounds):
        roll = random.randint(1,6)
        if roll > enemySave:
            savedWounds += 1
            print("Save Roll:",roll)
        if roll <= enemySave:
            failedWounds += 1
            print("Save Roll:",roll)
    damageTaken =  failedWounds * damage
    print(f"Damage Taken:{damageTaken}")
    
###function to make sure only integers are inputted into entry fields. make it dummy proof


    
    
###Grab Vars from entry, with get, assign them to variables, convert variables to int. Might need to find a better way to do this. <- absolutely do, dumbass        
def setVars():
    ## get all vars from entries
    attacks = attackVar.get()
    weaponSkill = weaponSkillVar.get()
    strength = strengthVar.get() 
    armorPen = armorPenVar.get() 
    enemyToughness = enemToughVar.get() 
    enemySave = enemySaveVar.get() 
    invulnSave = enemInvulnVar.get()
    simDuration = simRoundVar.get()
    damage = damageVar.get()
    
    ### set all vars to int
    attacks = int(attacks)
    weaponSkill =int(weaponSkill)
    strength =int(strength) 
    armorPen = int(armorPen) 
    enemyToughness = int(enemyToughness) 
    enemySave = int(enemySave) 
    
    if toggleInvuln.get() == "1":
        invulnSave = int(invulnSave)
    else:
        pass 
    simDuration = int(simDuration)
    damage = int(damage)
    print(f"Num Attacks:{attacks}\nWeapon Skill:{weaponSkill}\nEnemy Toughness:{enemyToughness}\nStrength:{strength}\nEnemy Save:{enemySave}\nInvuln Save:{invulnSave}\nAP:{armorPen}\nDamage:{damage}")
    determineHits(attacks,weaponSkill)
    determineWounds(strength,enemyToughness,successfulHits)
    determineSave(enemySave,invulnSave,armorPen,successfulWounds,damage,toggleInvuln)
    
##def simulateBattle(attacks,weaponSkill,enemyToughness, strength,enemySave,invulnSave,armorPen,damage):         
    ##pass 
        
    
            
 

def validateDigit(var,label):
    x = var.get()
    try:
        x == ['1','2','3','4','5','6','7','8','9'] or int(x)
    except ValueError:
        label.configure(text = f'Only digits 1-9 allowed.',
                     foreground ="red")
        print(f"{var} is not a valid input")
    else:
         label.configure(text = f'Field is empty',
                     foreground ="red")
        
        
  
            
##invuln State check
toggleInvuln = ctk.StringVar()
toggleInvuln.set('0')  

##Placeholder for future invuln check
def toggle():
    if toggleInvuln.get() == "1":
        print("Target Has Invuln")
        enemInvulnEntry.configure(state="normal",bg_color = "white")
    else: 
        print("Target Does not have Invuln")
        enemInvulnEntry.configure(state="disabled",bg_color = "red")


def test_error():
   CTkMessagebox(title = "Error", message = "Please only enter numbers.", icon = "cancel")

##create labels
def createLabels():
    row = 0
    labels = ["Attacks","Weapon Skill", "Strength","AP","Toughness","Save","Damage"]
    for i in labels:
        i = ctk.CTkLabel(master=frame,text = i,padx = 10,pady=10)
        i.grid(column = 2, row = row)
        row += 1
    row = 0
    for i in labels:
        i = ctk.CTkLabel(master=frame,text = i,padx = 10,pady=10)
        i.grid(column = 0, row = row)
        row += 1
        
        
## create entries        
def createEntry():
    row = 0
    for x in range(7):
        x = ctk.CTkEntry(master = frame,width=60)
        x.grid(column = 3, row = row )
        row += 1
        for key in unit1.stats:
            unit1.stats = {key,x.get()}
            
    row = 0
    for x in range(7):
        x = ctk.CTkEntry(master = frame,width=60)
        x.grid(column = 1, row = row )
        row += 1
        
           
def printStat():
        print(unit1.keys())


createLabels()
createEntry()

"""""
##Label Definitions and parameters
##Labels Are Column 0
attackLabel = ctk.CTkLabel(master=frame, text = "Attacks",anchor="w")
attackLabel.grid(column = 0, row = 0)

weaponSkillLabel = ctk.CTkLabel(master=frame, text = "Weapon Skill")
weaponSkillLabel.grid(column = 0, row = 1)

strengthLabel = ctk.CTkLabel(master=frame, text = "Strength")
strengthLabel.grid(column = 0, row = 2)

armorPenLabel = ctk.CTkLabel(master = frame, text = "AP")
armorPenLabel.grid(column = 0, row = 3)

enemToughnessLabel = ctk.CTkLabel(master=frame, text = "Enemy Toughness")
enemToughnessLabel.grid(column = 0, row = 4)

enemSaveLabel = ctk.CTkLabel(master=frame, text = "Enemy Save")
enemSaveLabel.grid(column = 0, row = 5)

enemInvulnLabel = ctk.CTkLabel(master=frame, text = "Invuln Save")
enemInvulnLabel.grid(column = 0, row = 6)

damageLabel = ctk.CTkLabel(master=frame, text = "Damage")
damageLabel.grid(column = 0, row = 7)

simulationAmmountLabel = ctk.CTkLabel(master=frame, text = "Simulation Rounds")
simulationAmmountLabel.grid(column = 0, row = 8)

##Test for calling variables for assignment for entries
attackVar = ctk.StringVar()
weaponSkillVar = ctk.StringVar()
strengthVar = ctk.StringVar()
armorPenVar = ctk.StringVar()
enemToughVar = ctk.StringVar()
enemySaveVar = ctk.StringVar()
enemInvulnVar = ctk.StringVar()
simRoundVar = ctk.StringVar()
damageVar = ctk.StringVar()

##Entry Definitions and parameters
##Entrys are Column 1


attackEntry = ctk.CTkEntry(master=frame,width=40,textvariable= attackVar)
attackEntry.grid(column = 1, row = 0)


weaponSkillEntry = ctk.CTkEntry(master=frame,width=40,textvariable=weaponSkillVar)
weaponSkillEntry.grid(column = 1, row = 1)


strengthEntry = ctk.CTkEntry(master=frame,width=40,textvariable=strengthVar)
strengthEntry.grid(column = 1, row = 2)


armorPenEntry = ctk.CTkEntry(master=frame,width=40,textvariable=armorPenVar)
armorPenEntry.grid(column = 1, row = 3)


enemToughnessEntry = ctk.CTkEntry(master=frame,width=40,textvariable=enemToughVar)
enemToughnessEntry.grid(column = 1, row = 4)


enemSaveEntry = ctk.CTkEntry(master=frame,width=40,textvariable=enemySaveVar)
enemSaveEntry.grid(column = 1, row = 5)







damageEntry = ctk.CTkEntry(master=frame,width=40,textvariable=damageVar)
damageEntry.grid(column = 1,row = 7)

simulationLengthEntry = ctk.CTkEntry(master=frame,width=40,textvariable=simRoundVar)
simulationLengthEntry.grid(column = 1,row = 8)
"""
enemInvulnEntry = ctk.CTkEntry(master=frame,width=40)#textvariable=enemInvulnVar
enemInvulnEntry.grid(column = 1,row = 6)


##Define checkbox logic for invuln saves
##putting invuln check at bottom, entry and label will go under all the other shit
##for some reason this fucking thing moves when the label for invuln dissapears. whats the point of setting a grid if does whatever it fucking wants anyway? Remeber to fix this eventually 
##(okay actually just made it be disabled instead of dissapear, looks better)
invulnCheckBox = ctk.CTkCheckBox(master=frame,text="Target has Invuln save?",variable=toggleInvuln,onvalue="1",offvalue="0",command=toggle)
invulnCheckBox.grid(column = 0,row=10)

##Define Simulate Button 
SimulateButton = ctk.CTkButton(master=frame,text="Simulate Battle",command = printStat)
SimulateButton.grid(column = 1,row= 15, sticky = 's')
 










##test_error()
           

toggle()
root.mainloop()





