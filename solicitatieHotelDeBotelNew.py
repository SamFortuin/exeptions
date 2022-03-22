#99059050, Sam Fortuin
import time

#vars
#place holder strings for list
personCompitence = ["0_praktijkErvaaring", "1_praktijkEvaringTijd", "2_mbo4", "3_truckLicense", "4_ownsTopHat", "5_certificate"]
personPhysical = ["0_name", "1_gender", "2_hairTypeOrMustache", "3_hairLength", "4_height", "5_weight"]
distractions = ["0_clownEthics", "1_toeLength", "2_eminem", "3_zelda"]

#var for when user passes the test
physicalReqPassed = False
hairReqPassed = False
compReqPassed = False

#user input for correct compitence & physical list info
personPhysical[0] = input("Wat is uw naam?\n")
personCompitence[0] = input("In welk veld heeft u praktijkervaaring\n")
#cleanup for later if statement
personCompitence[0] = personCompitence[0].lower().replace(" ", "").replace("-","")
personCompitence[1] = int(input("Hoeveel jaar praktijkervaaring heeft u?\n"))
distractions[0] = input("Heeft u de cursus clown ethiek gevolgd?\n")
personCompitence[2] = input("Heeft u een MBO Niveau 4 diploma?\n")
personCompitence[3] = input("Heeft u een rijbeweijs D?\n")
distractions[3] = input("Heeft u ooit een Legend of Zelda game gespeeld?\n")
personCompitence[4] = input("Bent u in bezit van een hoge hoed?\n")
personPhysical[1] = input("Wat is uw geslacht?\n")
distractions[2] = input("Heeft u ooit geluistered naar eminem?\n")
#lower for if statement
personPhysical[1] = personPhysical[1].lower()

if personPhysical[1] == "man" or personPhysical[1] == "m":
    personPhysical[2] = input("Heeft u een snor?\n")
    personPhysical[2] = personPhysical[2].lower()
    if personPhysical[2] == "ja" or personPhysical[2] == "j":
        personPhysical[3] = input("Wat is de lengte van uw snor in centimeters?\n")
        #cleans up input for int conversion
        personPhysical[3] = personPhysical[3].lower().replace("cm","").replace(" ","")
        personPhysical[3] = int(personPhysical[3])
        if personPhysical[3] >= 10:
            hairReqPassed = True
        else:
            hairReqPassed = False
    else:
        physicalReqPassed = False
elif personPhysical[1] == "vrouw" or personPhysical[1] == "v":
    personPhysical[3] = input("Wat is de lengte van uw haar in centimeters?\n")
    personPhysical[2] = input("Wat is uw haarkleur en haartype\n")
    #cleanup for if statement
    personPhysical[2] = personPhysical[2].lower().replace("haar","").replace(" ","")
    personPhysical[3] = personPhysical[3].lower().replace("cm","").replace(" ","")
    personPhysical[3] = int(personPhysical[3])
    if personPhysical[2] == "roodkrul" and personPhysical[3] >= 20:
        hairReqPassed = True
    else:
        hairReqPassed = False
else:
    physicalReqPassed = False

personPhysical[4] = input("Wat is uw lengte in centimeters\n")
personPhysical[4] = personPhysical[4].lower().replace("cm","").replace(" ","")
personPhysical[4] = int(personPhysical[4])
distractions[2] = input("Wat is de lengte van uw linker grote teen?\n")
personPhysical[5] = int(input("Wat is ue gewicht in kilo's?\n"))
personCompitence[5] = input("Heeft u het certificaat Overleven met gevaarlijk personeel?\n")

#if statement for physicalReq
if personPhysical[4] >= 180 and personPhysical[5] >= 90 and hairReqPassed == True:
    physicalReqPassed = True
else:
    physicalReqPassed = False

#if statement for compReg
if (personCompitence[0] == "dierendressuur" and personCompitence[1] >= 4) or (personCompitence[0] == "jongleren" and personCompitence[1] >= 5) or (personCompitence[0] == "acrobatiek" and personCompitence[1] >= 3):
    compReqPassed = True
else:
    compReqPassed = False

#final if statement
if physicalReqPassed == True and compReqPassed == True:
    print(personPhysical[0],"u bent geaccepteerd voor een solicitatie gesprek met meneer E.X. Directeaur")
    time.sleep(0.2)
    exit()
else:
    print(personPhysical[0],"u bent niet geaccepteerd voor een solicitatie gesprek")
    time.sleep(0.2)
    exit()