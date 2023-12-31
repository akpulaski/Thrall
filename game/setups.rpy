label generalSetUp: 
    default location = 2 

    python: 
        #Disables rollback because it messes with inventory system.
        config.rollback_enabled = False 

        #Sprite Management 
        environmentSM = SpriteManager(event = evironmentEvent)
        inventorySM = SpriteManager(event = inventoryEvent)

        #General Declarations 
        environmentSprites = []
        inventorySprites = []
        evironmentItems = []
        inventoryItems = []
        environmentItemNames = []
        inventoryItemNames = ["Key", "Lock", "Card", "Claw", "Photo"]
        environmentItemsDeleted = []

    return


        

    
label setUpUndergroundCenter: 
    $ environmentItems = ["photo"]

    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []

   
    python: 

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "photo": 
                    environmentSprites[-1].x = 1300 
                    environmentSprites[-1].y = 900 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100

    scene underground bg
    call screen undergroundCenterScene


label setUpUndergroundLeft: 
    $ environmentItems = ["card", "rock1", "rock2"]

    python: 
        for item in environmentSprites: 
            item.destroy() 
            environmentSM.redraw(0)
        environmentSprites = []
        
    python: 

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item)) 
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "card": 
                    environmentSprites[-1].zorder = 1
                    environmentSprites[-1].x = 200 
                    environmentSprites[-1].y = 900
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
                elif item == "rock1": 
                    environmentSprites[-1].zorder = 5
                    environmentSprites[-1].x = 160
                    environmentSprites[-1].y = 860
                    environmentSprites[-1].width = 200  
                    environmentSprites[-1].height = 200
                elif item == "rock2": 
                    environmentSprites[-1].x = 700 
                    environmentSprites[-1].y = 900 
                    environmentSprites[-1].width = 100 
                    environmentSprites[-1].height = 100

    scene underground bg 
    call screen undergroundLeftScene

label setUpUndergroundRight: 
    $ environmentItems = ["claw", "bottle", "rock3"]
    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []
    

    python:

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "claw": 
                    environmentSprites[-1].x = 750 
                    environmentSprites[-1].y = 650 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
                elif item == "bottle":
                    environmentSprites[-1].x = 710
                    environmentSprites[-1].y = 590
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
                elif item == "rock3": 
                    environmentSprites[-1].x = 1500
                    environmentSprites[-1].y = 950 
                    environmentSprites[-1].width = 100 
                    environmentSprites[-1].height = 100 

    scene underground bg 
    call screen undergroundRightScene

label setUpBank: 
    $ environmentItems = ["lock"]

    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []

    python: 
        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "lock": 
                    environmentSprites[-1].x = 1600 
                    environmentSprites[-1].y = 1000 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100 
    
    scene bank bg 
    call screen bankScene

label setUpInventory: 
    
    python: 
        for item in inventoryItems:
            idle_image = Image("items/{}_idle.png".format(item))
            hover_image = Image("items/{}_hover.png".format(item))
            t = Transform(child = idle_image, zoom = .75)
            inventorySprites.append(inventorySM.create(t))
            inventorySprites[-1].type = item 
            inventorySprites[-1].idle_image = idle_image
            inventorySprites[-1].hover_image = hover_image
            if item == "lock": 
                inventorySprites[-1].x = 350 
                inventorySprites[-1].y = 300 
                inventorySprites[-1].width = 150 
                inventorySprites[-1].height = 150 
                hasLock = True 
            elif item == "key": 
                inventorySprites[-1].x = 600
                inventorySprites[-1].y = 300 
                inventorySprites[-1].width = 150 
                inventorySprites[-1].height = 150 
                hasKey = True 
            elif item == "card": 
                inventorySprites[-1].x = 350 
                inventorySprites[-1].y = 500 
                inventorySprites[-1].width = 150 
                inventorySprites[-1].height = 150 
                hasCard = True 
            elif item == "claw": 
                inventorySprites[-1].x = 600 
                inventorySprites[-1].y = 500 
                inventorySprites[-1].width = 150 
                inventorySprites[-1].height = 150 
                hasClaw = True
            elif item == "photo": 
                inventorySprites[-1].x = 400
                inventorySprites[-1].y = 700 
                inventorySprites[-1].width = 150 
                inventorySprites[-1].height = 150 
                hasPhoto = True 
            
    call screen inventoryScene


label selectScene: 
    if location == 1: 
        scene underground bg 
        jump setUpUndergroundLeft
    elif location == 2: 
        scene underground bg 
        jump setUpUndergroundCenter 
    elif location == 3: 
        scene underground bg 
        jump setUpUndergroundRight 
    elif location == 4: 
        scene bank bg 
        jump setUpBank 

label showInventory: 
    show inventory bg 
    jump setUpInventory