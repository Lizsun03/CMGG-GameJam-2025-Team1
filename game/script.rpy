# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("ST3V13", image="stevie.png")
define a = Character("4L3X", image="alex.png")
define artist = Character("xX_ARTIST.152_Xx", image="artist_wink.png")
define artist_surprise = Character("xX_ARTIST.152_Xx", image="artist_surprise.png")
define narrator = Character(None, what_italic=True)
image stevie = "stevie.png"
image alex = "alex.png"
image artist = "artist_wink.png"
image hospital1 = "hospital_1.png"
image hospital2 = "hospital_2.png"
image hospital3 = "hospital_3.png"
image hospital4 = "hospital_4.png"
image hospital5 = "hospital_5.png"
image hospital6 = "hospital_6.png"
image burning = "city.png"
image run1 = "run_1.png"
image run2 = "run_2.png"
image market = "market.png"
image stall1 = "stall1.png"
image stall2 = "stall2.jpg"
image stall3 = "stall3.jpg"
image room = "house a day.png"
image black = "black.jpg"
image art1 = "art1.png"
image art2 = "art2.png"
image art3 = "art3.png"

# The game starts here.
# SCENE 1

transform black:
  zoom 4

label start:
    play sound "background.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    # SCENE 1
    narrator "It’s official: this is definitely the biggest the street market’s ever been. Well – at least since you’ve been coming!"
    narrator "It’s almost impossible to take in everything in one go – so many colors, so many shapes, so many sounds! A true stimulation storm, waiting for you to fly right in."
    
    transform halfsize:
        zoom 0.5

    transform halfsizecenter:
        zoom 0.5
        xalign 0.5 yalign 0.5

    transform midright:
        xalign 0.85 yalign 0.0

    transform midleft:
        xalign 0.2 yalign 0.0

    show stevie at midleft, halfsize
    show alex at midright, halfsize
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
    $ dizzy = True 
    #jump end

label fine_dizzy:
    a "Me? I’m great. And since we’re clearly both great, I guess that means you surely wouldn’t mind checking out the big stalls first?"
    narrator "You giggle nervously. You’ll get over it if you just jump right into the deep end. Plus, imagine if all the good stuff sold out before you got there!"
    
    $ dizzy = False
    
    #jump end

# SCENE 2
transform market:
  zoom 0.75

if dizzy == True:
    scene bg awayfromcrowd
    "Away from the crowds and chaos exploding along the main drag, the two of you find yourselves able to stroll calmly. With fewer people around, you can actually see inside each stall without needing to shove your way forward."

elif dizzy == False:
    scene market at market
    "The two of you throw yourselves head-first into the fray! The crowds are dense, but you and 4L3X are seasoned and stubborn. Darting between giddy customers and awed tourists, you finally find a pocket of air right in front of a few stalls that haven’t opened yet."

show alex at midright, halfsize
a "This is nice. Really nice. I haven’t been to one of these in so long!"
a "I’ve got enough gadgets though – mind if we check out some of the more artsy stuff? I wanna find my Nana something cool for her new bakery. Something that’ll really grab people, y’know?"

#show alex happy
"All you can muster is a nod, which 4L3X jumps on – They grab your hand and pull you along to the closest one, right as the vendor flips a switch."

scene stall1

show artist at halfsize 
artist "Juuuuust in tiiiiiime! Get on over here – Did you know, you’re the first to see my newest collection! How’s that for a great morning, eh?"

hide alex
hide artist
# scene market at market

"Everywhere you look, warmth and happiness beams right back onto you. Paintings, sculptures, holograms… the mediums may vary, but there’s no doubt that every piece was hand-crafted with pure love and joy."

show artist at halfsize
artist "Whatever you want, whatever you want! We don’t mess around here – all originals, all mine! Anything that speaks to you, just let me know, and I’ll tell you aaaall about it."

$ renpy.mark_label_unseen("landscape")
$ renpy.mark_label_unseen("hologram")
$ renpy.mark_label_unseen("twisty")

label painting:
#https://www.reddit.com/r/RenPy/commenyts/prftqd/how_do_i_add_multiple_conversation_choices/
    menu: 
    
        "That landscape is gorgeous! Is it a real place?" if not renpy.seen_label("landscape"):
            jump landscape 

        "Oh my gosh, I’ve never seen a hologram that detailed!" if not renpy.seen_label("hologram"):
            jump hologram

        "Wait, what’s that twisty thing back there? I’ve never seen anything like it!" if not renpy.seen_label("twisty"): 
            jump twisty

label landscape:
        show artist at halfsize
        hide art2 
        hide art3
        show art1 at halfsizecenter
        artist "It is! If you’ve ever been to LuminoCity, there’s this great sushi bar on top of a hotel where you can see out across the entire city! I’ve made a point of eating dinner there every Monday and Thursday just so I can watch the sunset. The way the light catches the buildings… They look so shiny. That view can be all yours!"
        jump painting

label hologram: 
    show artist at halfsize 
    hide art1 
    hide art3
    show art2 at halfsizecenter
    artist "Oh – Ha! Isn’t she pretty? I based her off of the lovely ladies of Tower Town – have you ever been? They’re all so fashionable, so graceful – so I thought to myself, ‘Why not roll them all into one?’ And here she is: Tower-Town Tory! If you swing back next week, I’ll have her best friend ready, too – Tower-Town Tony."
    jump painting 

label twisty:
    show artist at halfsize
    hide art1 
    hide art2
    show art3 at halfsizecenter
    artist "Which one?"
    show alex at midright, halfsize 
    a "I think they're talking about that weird shape-y thing over there. Behind the boxes."
    show artist_surprise at halfsize
    "You’re not quite sure, but something seems to shift in the artist’s face. His smile’s bigger, which is really nice! But… maybe too big? Is that even possible?"

    artist "Oh! That. Yeah. Um. Hmm."
    artist "That's just..."
    artist "..."
    artist "Oh, you know, sometimes you just… Make stuff. Just to make things!"
    artist "...I don’t even really remember when I made that one."

    a "..."
    a "Makes sense! Anyway, I’m not really looking for sculptures – do you think any of your paintings or holograms would look good in a bakery? You know, stuff that would yell ‘Come in here and get some cake?"

    "But… the sculpture! It’s so… different. Unusual. It’s…"
    "…Well, you can’t really describe it. It’s almost like it’s inventing entirely new feelings, new words, new ideas that have never existed before. You wouldn’t call it “joyful…” but “bummed” doesn’t feel… strong enough?"
    "But what feeling could be stronger than a big ol’ bummer?"

    a "...ST3V1E! Dude! Stop looking at that thing! Like, are you seeing these paintings? They’ve got birds in them – you love birds!"

menu: 
    "I just wanna look at it for a sec!":
        "The artist’s smile is HUUUGE now! Ginormous! So, why does it feel… weird?"
        artist "Oh… Oh well! Can’t please them all. As I was saying, nothing says bakery quite like sprawling fields of grain…"
        show scene stall2    
        $ renpy.pause(0.1)
        show scene stall3
        $ renpy.pause(0.1)
        "Your little fists reach out to brush some boxes away, giving you an even better view of the piece. The world around you almost goes quiet… calm…"

        "…Is this what it feels like to be moved? Yes, that must be it. You’re moved! You’re inspired!"

        "You grip the sculpture in your hands – cold, rough, sharp. It’s weird, but weird is ok! Weird is fun, weird can’t hurt—"

    "Touch it.":
        show scene stall2    
        $ renpy.pause(0.1)
        show scene stall3
        $ renpy.pause(0.1)
        "Your little fists reach out to brush some boxes away, giving you an even better view of the piece. The world around you almost goes quiet… calm…"

        "…Is this what it feels like to be moved? Yes, that must be it. You’re moved! You’re inspired!"

        "You grip the sculpture in your hands – cold, rough, sharp. It’s weird, but weird is ok! Weird is fun, weird can’t hurt—"

        

    



# SCENE 3
# scene bg glitchartstall #flick between the glitched ones to look like active glitching
# scene bg glitchartstalltwo
# scene bg glitchartstall
#make it pause/stay on a scene for a few seconds?
play sound "glitch.mp3"


scene black at black

play sound "windows-error.mp3"
$ renpy.pause(3.0)
# scene bg lab 
scene hospital1 
$ renpy.pause(0.1)
scene hospital2 
$ renpy.pause(0.1)
scene hospital3
$ renpy.pause(0.1)
scene hospital4 
$ renpy.pause(0.1)
scene hospital5 
$ renpy.pause(0.1)
scene hospital6 

$ renpy.pause(2.0)

scene black at black

define reals = Character("STEVIE")
define cyber = Character("???", image="cyber.png")

play sound "wind.mp3"
reals "...Uhhhhh."

#(Dialogue box disappears again. Black again for a few seconds)
scene black at black

play sound "glitch.mp3"

#(Sudden cut to the Burning Buildings/People running away background, more glitch noises/sharp noises)
scene burning with fade 
$ renpy.pause(1.0)
scene run1 with fade
$ renpy.pause(1.0)
scene run2 with fade
$ renpy.pause(1.0)
#(Sudden cut to black screen again. Wind white noise)
play sound "wind.mp3"
scene black at black

reals "..."

scene black at black

# scene bg vat

show cyber at halfsizecenter
cyber "...Wait."
cyber "Wait wait wait wait –"
cyber "...Oh. Oh fuck. Shit."
cyber "Can… Can you hear me?"

reals "..."
reals "<ERROR>"

play sound "wind.mp3"
scene black at black
$ renpy.pause(3.0)

# SCENE 4
label scene4:
    scene market at market
    show artist_surprise at halfsize
    show alex at midright, halfsize
    artist " – find it works best to stick to tranquil scenery, calm stuff. It’s much easier to sell, y’know?"

    artist "People wanna feel happy, that’s all."

    artist "People wanna feel happy."
