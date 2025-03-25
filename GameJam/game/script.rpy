# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("ST3V13", image="stevie.png")
define a = Character("4L3X", image="alex.png")
define artist = Character("xX_ARTIST.152_Xx")
define narrator = Character(None, what_italic=True)
image stevie = "stevie.png"
image alex = "alex.png"
# The game starts here.

# SCENE 1
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    # SCENE 1
    narrator "It’s official: this is definitely the biggest the street market’s ever been. Well – at least since you’ve been coming!"
    narrator "It’s almost impossible to take in everything in one go – so many colors, so many shapes, so many sounds! A true stimulation storm, waiting for you to fly right in."
    
    transform halfsize:
        zoom 0.5
    show alex at halfsize

    a "Ok, I’m glad it’s not just me! Are you good? You look a little dizzy."
    
    # This ends the game.
menu:
    "Are you dizzy?"
    
    "Maybe a little...":
        jump maybe_dizzy

    "I'm fine! Are you dizzy?":
        jump fine_dizzy

label maybe_dizzy:
    a "Hah! Don’t worry, you’ll get used to it. We can take it easy to start off – there’s a few side stalls on the perimeter we can check out."
    narrator "You sigh with relief. You can always get to the big stuff later – but a warm-up round doesn’t sound half bad. Besides, everyone knows the best items are the ones you have to hunt for!"
    jump end

label fine_dizzy:
    a "Me? I’m great. And since we’re clearly both great, I guess that means you surely wouldn’t mind checking out the big stalls first?"
    narrator "You giggle nervously. You’ll get over it if you just jump right into the deep end. Plus, imagine if all the good stuff sold out before you got there!"
    jump end

# SCENE 2


# SCENE 3


# SCENE 4
label scene4:
    artist " – find it works best to stick to tranquil scenery, calm stuff. It’s much easier to sell, y’know?"

    artist "People wanna feel happy, that’s all."

    artist "People wanna feel happy."
