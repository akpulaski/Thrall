screen undergroundCenterScene: 
    add environmentSM
    imagebutton:
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500
        action[SetVariable("location", location - 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/right_%s.png"
        xpos 1750 
        ypos 500 
        action[SetVariable("location", location + 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Jump("showInventory")]

screen undergroundLeftScene: 
    add environmentSM
    imagebutton: 
        auto "nav/right_%s.png"
        xpos 1750 
        ypos 500 
        action[SetVariable("location", location + 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Jump("showInventory")]

screen undergroundRightScene: 
    add environmentSM
    imagebutton: 
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500
        action[SetVariable("location", location - 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Jump("showInventory")]

screen bankScene: 
    add environmentSM
    imagebutton: 
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500 
        action[SetVariable("location", 2), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Jump("showInventory")]


screen inventoryScene: 

    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50 
        ypos 50
        action[Hide("infoScene"), Jump("selectScene")]
    for item in inventoryItems: 
        if item == "claw":
            imagebutton: 
                auto "items/claw_%s.png" at smaller 
                xpos 600 
                ypos 700 
                action[Show("infoScene", item = "claw")]
        if item == "lock": 
            imagebutton: 
                auto "items/lock_%s.png" at smaller 
                xpos 350
                ypos 300
                action[Show("infoScene", item ="lock")]
        if item == "key": 
            imagebutton: 
                auto "items/key_%s.png" at smaller 
                xpos 350 
                ypos 700 
                action[Show("infoScene", item = "key")]
        if item == "card": 
            imagebutton: 
                auto "items/card_%s.png" at smaller
                xpos 600 
                ypos 250 
                action [Show("infoScene", item = "card")]
        if item == "photo": 
            imagebutton: 
                auto "items/photo_%s.png" at smaller
                xpos 500
                ypos 500 
                action[Show("infoScene", item = "photo")]
    textbutton "Move On" xalign .75 yalign .75 action[Jump("end_investigate")]

screen infoScene(item = None): 
    if item == "photo": 
        text "Photo" at nameLoc
        text "The description of the photo goes here." at descLoc
    elif item == "claw": 
        text "Claw" at nameLoc
        text "The description of the claw goes here." at descLoc
    elif item == "lock": 
        text "Lock" at nameLoc
        text "The description of the lock goes here." at descLoc 
    elif item == "card": 
        text "Card" at nameLoc
        text "The description of the card goes here." at descLoc
    elif item == "key": 
        text "Key" at nameLoc
        text "The descriptin of the key goes here." at descLoc