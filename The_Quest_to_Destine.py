import time
import random

def scene1():
    print("\nWelcome to 'The Quest for Destiny'!")
    print("You stand at the edge of a dense forest, feeling the call of adventure.")
    print("Before you, a fork in the path presents two options.")
    print("Which path will you choose?")
    time.sleep(1)
    print("\n1. Take the left path")
    print("2. Take the right path")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        scene2a()
    elif choice == "2":
        scene2b()
    else:
        print("Invalid choice. Please try again.")
        scene1()

def scene2a():
    print("\nYou forge ahead into the tangled undergrowth, the foliage closing in around you.")
    print("The left path seems to wind deeper into the heart of the forest.")
    print("As you push through the dense foliage, you come across a fork in the trail.")
    print("What will you do?")
    time.sleep(1)
    print("\n1. Follow the faint light in the distance")
    print("2. Explore the hidden cave entrance")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        scene3a1()
    elif choice == "2":
        scene3a2()
    else:
        print("Invalid choice. Please try again.")
        scene2a()

def scene2b():
    print("\nYou set off down the winding road, the mist swirling around your feet.")
    print("The right path leads you deeper into the mist-shrouded forest.")
    print("As you journey onward, you come across a fork in the road.")
    print("What will you do?")
    time.sleep(1)
    print("\n1. Cross the rickety bridge")
    print("2. Venture into the hidden glade")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        scene3b1()
    elif choice == "2":
        scene3b2()
    else:
        print("Invalid choice. Please try again.")
        scene2b()

def scene3a1():
    print("\nYou follow the flickering light, your curiosity piqued by the mysterious glow.")
    print("The light leads you to a small clearing where you find a group of travelers huddled around a campfire.")
    print("They offer you shelter for the night and share tales of their adventures.")
    print("As the fire crackles and sparks dance in the darkness, you feel a sense of camaraderie with your newfound companions.")
    print("\nCongratulations! You have found companionship on your journey. Your adventure continues!")
    time.sleep(1)
    scene4()

def scene3a2():
    print("\nYou decide to explore the hidden cave, its dark entrance beckoning you into the unknown.")
    print("Inside the cave, you stumble upon a treasure trove of ancient artifacts.")
    print("Among the dusty relics, you find a map detailing the location of a long-lost treasure.")
    print("With your newfound discovery in hand, you set out on a quest to uncover the riches hidden within the depths of the forest.")
    print("\nCongratulations! You have discovered a treasure map. Your adventure continues!")
    time.sleep(1)
    scene4()

def scene3b1():
    print("\nYou cautiously approach the rickety bridge, its ancient timbers groaning underfoot.")
    print("With each step, the bridge creaks and sways, threatening to collapse beneath your weight.")
    print("Just as you reach the other side, a sudden gust of wind sends the bridge tumbling into the abyss below.")
    print("You breathe a sigh of relief, grateful to have made it across safely.")
    print("\nCongratulations! You have successfully crossed the bridge. Your adventure continues!")
    time.sleep(1)
    scene4()

def scene3b2():
    print("\nYou veer off the main path and venture into the hidden glade, the air thick with the scent of wildflowers.")
    print("In the heart of the glade, you discover a tranquil pond surrounded by lush greenery.")
    print("As you pause to drink from the crystal-clear waters, you catch sight of a shimmering object at the bottom of the pond.")
    print("With a sense of anticipation, you dive beneath the surface and retrieve the mysterious treasure hidden below.")
    print("\nCongratulations! You have found a mysterious treasure. Your adventure continues!")
    time.sleep(1)
    scene4()

def scene4():
    print("\nAfter your encounter, you continue your journey through the forest,")
    print("the path ahead winding ever deeper into the heart of the wilderness.")
    print("As the day wears on, you come across a fork in the road once more.")
    print("This time, the choices seem even more daunting.")
    print("What will you do?")
    time.sleep(1)
    print("\n1. Follow the path leading uphill")
    print("2. Explore the winding river")
    print("3. Investigate the mysterious ruins")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        scene5a()
    elif choice == "2":
        scene5b()
    elif choice == "3":
        scene5c()
    else:
        print("Invalid choice. Please try again.")
        scene4()

def scene5a():
    print("\nYou decide to take the path leading uphill, curious about what might await you at the summit.")
    print("The trail becomes steeper as you ascend, but you're determined to reach the top.")
    print("As you climb higher, the air grows cooler, and the trees thin out, revealing glimpses of the sky above.")
    print("After what feels like hours of climbing, you finally reach the peak and are greeted by a breathtaking view of the surrounding landscape.")
    print("\nCongratulations! You have reached the summit. Your adventure continues!")
    time.sleep(1)
    ending1()

def scene5b():
    print("\nYou decide to follow the winding river, eager to explore its hidden secrets.")
    print("The river leads you through dense foliage and rocky terrain, its gentle flow soothing your weary soul.")
    print("As you journey alongside the river, you come across a hidden waterfall, its cascading waters a sight to behold.")
    print("Mesmerized by its beauty, you pause to rest and replenish your water supply.")
    print("\nCongratulations! You have discovered a hidden waterfall. Your adventure continues!")
    time.sleep(1)
    ending2()

def scene5c():
    print("\nYou choose to investigate the mysterious ruins, drawn by the allure of ancient secrets.")
    print("The ruins stand tall and imposing, their weathered stones whispering tales of a forgotten past.")
    print("As you explore the crumbling corridors and hidden chambers, you stumble upon a hidden chamber.")
    print("Inside, you find a relic of immense power, its secrets waiting to be unlocked.")
    print("\nCongratulations! You have discovered a powerful relic. Your adventure continues!")
    time.sleep(1)
    ending3()

def ending1():
    print("\nAs you stand atop the summit, you feel a sense of accomplishment wash over you.")
    print("The breathtaking view before you fills you with a renewed sense of purpose.")
    print("With the knowledge that you conquered the mountain, you feel ready to face whatever challenges lie ahead.")
    print("\nCongratulations! You have achieved greatness in your quest for destiny. Your adventure continues!")
    time.sleep(1)

def ending2():
    print("\nThe hidden waterfall fills you with a sense of wonder and awe.")
    print("Its cascading waters seem to wash away all worries and fears, leaving you feeling refreshed and invigorated.")
    print("With newfound strength and determination, you set out to explore more of the world around you.")
    print("\nCongratulations! You have found solace and beauty in your journey. Your adventure continues!")
    time.sleep(1)

def ending3():
    print("\nThe powerful relic pulses with energy as you hold it in your hands.")
    print("Its ancient magic fills you with a sense of purpose and destiny.")
    print("With the relic as your guide, you set out to uncover the mysteries of the world and unlock its hidden secrets.")
    print("\nCongratulations! You have unearthed a source of great power. Your adventure continues!")
    time.sleep(1)

# Start the game
scene1()
