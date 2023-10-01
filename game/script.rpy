image spooktober = "spooktoberlogo.png"

label splashscreen: 
    scene black 
    with Pause(1)

    scene black
    show spooktober:
    with dissolve 
    with Pause(2)

    scene black with dissolve 
    with Pause(1)
    
    return

###MAIN MENU ANIMATION
image main_menu_animated:
    "gui/Thrall-Illustration-1.png"
    pause 0.7
    "gui/Thrall-Illustration-2.png"
    pause 0.7
    repeat

###CHARACTERS
define e = Character("Estrella", color="FFFFFF")
define z = Character("Zane", color="FFFFFF")
define l = Character("Lazarus", color="FFFFFF")
define Unknown = Character("Unknown", color="FFFFFF")
define InternalDialogue = Character(None)
define Novel = Character(None, kind=nvl)

###CGs
image CRE= "cgs/CRE.png"
image CRZ= "cgs/CRZ.png"
image CRL= "cgs/CRL.png"
image CR = "cgs/CR.png"
image EN = "cgs/EN.png"
image LL = "cgs/LL.png"
image LK = "cgs/LK.png"
image ZZ = "cgs/ZZ.png"
image ZK = "cgs/ZK.png"
image WE = "cgs/WE.png"


label start:
    #This needs to go FIRST 
    call generalSetUp
    play music "audio/music/main theme.mp3" fadein 1.0
    "Nothing good ever came from being enthralled by the supernatural."
    "Or, paranormal. Honestly, the distinction doesn't mean much in Crescent City..."
    "Because being enslaved by their bewitching powers has led many astray in the Otherworld."
    "I mean, case in point, I'm speaking from the grave because I got in too deep too fast."
    "In this perilous border city separating the mundane from the magical, I staked my career as a human reporter navigating the seedy underbelly of a world dominated by near immortal monsters."
    "Until I went too far and got ensnared in a trap that cost me my life."
    "Well, that was before I came back from the dead. And now I'm back on the case, uncovering the crime of the century..."
    "My untimely demise by the hands of one, or both, of my lovers."

    scene tomb
    
    show estrella-neutral:
        zoom 0.53 xanchor -0.95

    e "Where am I?"

    menu:
        e "What should I do?"

        "Investigate":
            #$ investigate = True
            jump go_investigate
        "Escape":
            "(Armed with a pen, a notebook, my wits, and what's left of my ghastly body, I roam through the halls of the tomb-line tunnel, searching for an escape route."
            # (Click and Point Doesn't Appear. Only the Key is added to her inventory.)
            #This next line should add the key to the inventory. 
            $ addToInventory(["key"])
            jump go_hexed
        # and more here as well

label go_investigate:
    "(I use my ghastly palm as a flash light in the dark, breathing in the sharp smell of rotton eggs. Sulfur.)"
    # (Click and Point Should be Here.)
    jump setUpUndergroundCenter

label end_investigate: 
    show CRE with dissolve
    e "Who are you?"

    ###"Entwined by Eternity" Good End (Vampire)
    show CRL with dissolve
    e "(Lazarus wipes Zane's blood from the wolf's golden claw I recovered in the tomb, grinning at me, eyes demonic, expression serene.)"
    l "Marvelous, darling, isn't it?"
    e "(He offers me his blood soaked hand, and I take it, slowly coming back together again, piece by piece, inch by unforgiving inch.)"
    e "(Power surges through me, as well as fear, memories that don't feel like my own flooding in.)"
    l "Look, sweetheart, I don't have eternity to get entwined with yet another bullshit seance to bring you back from the dead."
    l "Let's take the money and split it two ways. You and me, against the world, baby."
    l "What do you say, Estrella?"
    e "(His voice is like a caress, as his fangs graze my neck, palm resting where a beating heart once hammered against my ghostly chest.)"
    l "My sweet, your bloodsong cries out for me. You were made for me, and I for you."
    e "Ah!"
    e "(I know it's wrong, yet it feels so right to succumb, knowing I have no real choice to reject Lazarus as he tugs on the spiritual tether binding me to his soul.)"
    e "(I am now bound to Lazarus Lockeheart forevermore, a wicked, fallen woman, but most importantly...)"
    e "(His {b}{i}thrall{i}{b}.)"

    ###"By Your Command" Bad End (Vampire)
    show LL with dissolve
    e "(My hands tremble as I'm forced to kill my werewolf lover by his command, using the same golden claw I recovered in the tomb.)"
    show LK with dissolve
    l "Marvelous, darling, isn't it? I don't think my allure alone compelled you to finish him off so spectacularly."
    e "(Lazarus wraps his blood soaked palms around my neck as I shudder, feeling him feed on my soul as I dissolve into the void.)"
    l "Look, sweetheart, I don't have eternity to get entwined with yet another bullshit seance to bring you back from the dead."
    l "You will follow my orders, or I'll crush your pathetic excuse for a soul, Estrella."
    l "I'll drain you dry, sweetheart, after you cough up your secrets. Your bloodsong is sweet, but revenge will be sweeter if you don't obey me!"
    e "(I say nothing, knowing I have no choice as he tugs on the spiritual tether binding me to his soul.)"
    l "Now lead the way to your treasures, and I may allow you to stay in this in-between existence."
    e "(I am now bound to Lazarus Lockeheart forevermore, a wicked, fallen woman, but most importantly...)"
    e "(His {b}{i}thrall{i}{b}.)"

    ###"Imprinted on My Heart" Good End (Werewolf)
    show CRZ with dissolve
    z "A little murder goes a long way to soothe the soul. His damn theatrics were getting on my last nerves."
    e "(I quiver as Zane tosses aside Lazarus' business card, finishing the job of slicing his head off with a coy smile and cold eyes.)"
    e "(He offers me his blood soaked arm, and I place a shaky hand on his elbow, slowly coming back together again, piece by piece, inch by unforgiving inch.)"
    e "(Power surges through me, as well as fear, memories that don't feel like my own flooding in.)"
    z "My sweet little pup, how I've longed to bring you back to my pack."
    z "Let's take the money and split it two ways. You and I, king and queen, of the Pagan MC."
    z "What do you say, Estrella?"
    e "(His rugged voice weaves through my mind, claws grazing my ghostly spine, tugging me into his warm, solid embrace.)"
    z "You and I were made for each other. Fated mates. Corrupted souls. We can rule this wretched world."
    e "Ah!"
    e "(I know it's wrong, yet it feels so right to surrender, as he tips my chin up and captures my lips in a sinister kiss, my spiritual tether binding me to his soul.)"
    e "(I am now mated to Zane Pagan forevermore, a wicked, fallen woman, but most importantly...)"
    e "({b}{i}Enthralled{i}{b} by my alpha, his promises imprinted in my twisted heart, his love inescapable.)"

    ###"Dance of Death" Bad End (Werewolf)
    show ZZ with dissolve
    z "A little murder goes a long way to soothe the soul. His damn theatrics were getting on my last nerves."
    show ZK with dissolve
    e "(I quiver, dropping Lazarus' business card, finishing the job of slicing his head off, compelled by Zane's pheromones.)"
    e "(He grips the back of my neck, growling, transforming as I'm forced to submit.)"
    z "Ah Estrella, former head bitch in charge. I should kill you where you stand. But I'm a generous leader."
    z "You lead me to the money, and I allow you to live. I remain king of the Pagan MC, and maybe I'll offer you some scraps along with your pathetic life."
    z "What do you say, Estrella?"
    e "(There's nothing I can do but fall in line, my spiritual tether binding me to his soul.)"
    e "(I am now Zane Pagan's possession forevermore, a wicked, fallen woman, but most importantly...)"
    e "({b}{i}Enthralled{i}{b} by my alpha, marching lockstep under his command in a dance of death.)"

    ###"Enthralled" Best End
    show CR with dissolve
    e "Yes! Oh... Yes..."
    scene curtains
    show EN with dissolve
    e "(I can feel my body starting to come together, flesh knitting against bone, revived bit by bit, piece by piece, until I'm made whole.)"
    e "(Sighing sweetly, I rest against Zane's broad chest as Lazarus nuzzles my neck, listening to the beautiful rhythmic thudding of their rapidly beating hearts)."
    l "How grand, Zane! Our Mistress of Darkness is back."
    l "We have waited for what felt like an eternity for you to return to us in all your corrupt glory, my queen!"
    z "It's wonderful, alright. Together, we will be unstoppable. Not a single soul won't kneel before us in this world or the next, Estrella."
    e "(Slowly, memories flood my entire being, evoking nostalgia for a life I once lived yet had forgotten, locked away inside of my head, just like they key to my tomb was buried within my soul.)"
    e "(Our tainted love, I thought doomed from the start, blossomed into an empire born in darkness. I walked a tightrope between a twisted vamp and a ravenous werewolf, straying from the path of righteousness.)"
    e "(Before I decided the corrupt bastards I reported on would serve {b}{i}me{i}{b}. My men cashed in on my revenge, so I no longer had to choose between them.)"
    e "(Yes, I was reborn as a queen pin with two monstrous enforcers by my side, sowing fruits of tragedy, using the dirt I dug up as a journalist to destroy my rivals in Crescent City.)"
    e "(I am delighted by my visions of a fallen, wicked woman without morals or limits.)"
    e "(I catch glimpses of a murderer who used the blood of innocents for a dastardly spell. The blood of her own lovers, too.)"
    e "(And that bitch was me, aye?)"
    z "Our princess is back, Lazarus. No, you're right, our {b}{i}queen{i}{b}."
    z "All we ever wanted was for our sweet, corrupted pup to return to her pack. And now you have come back to us. Better than before."
    z "Lead us now to your secrets, the spells of destruction you hid away in your heart and took to the grave, so that we may not only rule Crescent City but this entire wretch world!"
    l "It will be glorious! No more tip-toeing around playing the part of the good little noir cop. Embrace yourself as we have done."
    e "(All six of my senses are heightened as my body rejects the void.)"
    e "Zane...? Lazarus...?"
    e "(My voice is but a whisper as consuming passion ignites my spirit, evil and lust coursing through me as I reclaim first my body, and then my throne.)"
    e "(Nothing good ever came from being enthralled by the supernatural...)"
    e "(But having two {b}{i}thralls{i}{b} at my beck and call is priceless. The greatest gift that could ever been given.)"
    e "Let us enthrall our enemies. The Queen of Darkness has returned."
    e "Ahahahaaha!"

label go_hexed:
    ###"Hexed by Haints" Worst End
    show WE with dissolve
    e "No no no no no no no!"
    e "(My body is falling apart. I can feel my heart giving out like an unwinding clock.)"
    e "(Tick. Toc. Tick. Toc! The sound of my dying heart, as this wretched, ghostly body of mine drip, drops into a puddle of mush.)"
    l "Oh, pity. Yet again, she can't accept the truth."
    l "How many rare Black Moons must come and pass until Estrella frees herself from her delusion of sainthood, hmm, Zane?"
    e "(My mind is unraveling. False memories flood my entire being, evoking nostalgia for a life I never lived.)"
    e "(Tainted love, doomed from the start, blossoms in the corner of my mind. I'm walking a tightrope between a twisted vamp and a ravenous werewolf, straying from the path of righteousness.)"
    e "(And then there's me as a queen pin with two monstrous enforcers by my side as I sow fruits of tragedy, using the dirt I dug up as a journalist to destroy my rivals in Crescent City.)"
    e "(I am haunted by visions of a fallen, wicked woman without morals or limits.)"
    e "(I catch glimpses of a murderer who used the blood of innocents for a dastardly spell. The blood of her own lovers, too.)"
    e "(But that's not me! It can't be. It can't be. It! Can't! Be! Me!)"
    z "What can I say, Lazarus? Who ever heard of a hexed ghost when this all started? But she's cursed alright, and there's nothing we can do to help her."
    z "All we wanted was for our sweet, corrupted pup to return to her pack."
    z "Now look at her, choosing to die yet again rather than accept herself as the bitch she is."
    l "It was glorious, wasn't it? When she dropped the little noir cop act and embraced herself as a mistress of the night?"
    l "Regardless, I told you to make her stop. That routine of hers drove her crazy. Now it's too late. I'm starting to suspect she's bound to this cruel fate."
    e "(My vision is fading, like a tv tuned to static before being unplugged for good. All six of my senses are melting as my body is surrendered to the void.)"
    e "(I don't want to die. I don't want to die. I don't want to--"
    z "No amount of yapping would have stopped her from fooling around with evil magic beyond her capabilities."
    z "But it's fine. We wait. We watch. And then we strike again."
    l "You're right. What's another fifty or hundred years, give or take, to see the Queen of Darkness in all her glory once again? To have a shot at the treasures she's taken to the grave?"
    z "Nothing, dear friend. It costs us nothing to wait. Estrella is a priceless gem."
    l "Yes. Worth more than the most ancient blood or purest of gold. Even in her most grotesque form."
    e "Zane... Lazarus..."
    e "(My voice is but a whisper as the last bit of my being gives out.)"
    e "Help... me!"
    l "No can do. Last time you tried to slit my throat for trying to tame you. We'll see you soon, sweetheart. Rest easy now."
    z "Yes, little pup. Surrender to the darkness. I hope next time we meet, it's not in hell."
    e "NOOOOOOOOOOOOO!"

    # This ends the game.

    return

