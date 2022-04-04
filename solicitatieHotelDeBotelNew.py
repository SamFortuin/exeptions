#99059050, Sam Fortuin

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
personPhysical[0] = input("Wat is uw naam?\n").lower()
if personPhysical[0] == "janice":
    raise NameError('We hebben al een Janice')
personCompitence[0] = input("In welk veld heeft u praktijkervaaring\n").lower().replace(" ", "").replace("-","")
while True:
    personCompitence[1] = input("Hoeveel jaar praktijkervaaring heeft u?\n")
    try:
        personCompitence[1] = int(personCompitence[1])
    except ValueError:
        print('niet een nummer')
        continue
    break
distractions[0] = input("Heeft u de cursus clown ethiek gevolgd?\n")[:1].replace('j','y')
if distractions[0] != 'y':
    raise Exception('Niet ethisch genoeg')
personCompitence[2] = input("Heeft u een MBO Niveau 4 diploma?\n")
personCompitence[3] = input("Heeft u een rijbeweijs D?\n")
distractions[3] = input("Heeft u ooit een Legend of Zelda game gespeeld?\n")[:1].replace("j",'y')
if distractions[3] != 'y':
    raise Exception('U bent hier niet welkom!')
personCompitence[4] = input("Bent u in bezit van een hoge hoed?\n")
personPhysical[1] = input("Wat is uw geslacht?\n").lower()[:1].replace('f','v')
distractions[2] = input("Heeft u ooit geluistered naar eminem?\n")
if personPhysical[1] == "m":
    personPhysical[2] = input("Heeft u een snor?\n")[:1].lower().replace('j','y')
    if personPhysical[2] == 'y':
        while True:
            personPhysical[3] = input("Wat is de lengte van uw snor in centimeters?\n")[:2]
            try:
                personPhysical[3] = int(personPhysical[3])
            except ValueError:
                print('not a number')
                continue
            break
        if personPhysical[3] >= 10:
            hairReqPassed = True
        else:
            hairReqPassed = False
    else:
        physicalReqPassed = False
elif personPhysical[1] == "v":
    while True:
        personPhysical[3] = input("Wat is de lengte van uw haar in centimeters?\n")[:3].replace('c','').replace(" ","")
        try:
            personPhysical[3] = int(personPhysical[3])
        except ValueError:
            print('not a number')
            continue
        break
    personPhysical[2] = input("Wat is uw haarkleur en haartype\n").lower().replace("haar","").replace(" ","")
    
    if personPhysical[2] == "roodkrul" and personPhysical[3] >= 20:
        hairReqPassed = True
    else:
        hairReqPassed = False
else:
    physicalReqPassed = False

while True:
    personPhysical[4] = input("Wat is uw lengte in centimeters\n")[:3]
    try:
        personPhysical[4] = int(personPhysical[4])
    except ValueError:
        print('not a number')
        continue
    break
distractions[2] = input("Wat is de lengte van uw linker grote teen?\n")
personPhysical[5] = int(input("Wat is uw gewicht in kilo's?\n"))
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
    print(f'{personPhysical[0]} u bent geaccepteerd voor een solicitatie gesprek met meneer E.X. Directeaur')
else:
    print(f'{personPhysical[0]} u bent niet geaccepteerd voor een solicitatie gesprek')