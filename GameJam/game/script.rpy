# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("ST3V13")
define a = Character("4L3X")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    # SCENE 1
    s "It’s offcial: this is definitely the biggest the street market’s ever been. Well – at least since you’ve been coming!"
    s "It’s almost impossible to take in everything in one go – so many colors, so many shapes, so many sounds! A true stimulation storm, waiting for you to fly right in."
    s "You've created a new Ren'Py game."

    a "Ok, I’m glad it’s not just me! Are you good? You look a little dizzy."

    
    # This ends the game.

    return
