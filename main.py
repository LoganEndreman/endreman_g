def on_a_pressed():
    info.set_score(1)
    Enderman.say("Sssss")
    music.play_melody("- - G - - E B - ", 120)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

Enderman: Sprite = None
scene.set_background_color(4)
Enderman = sprites.create(img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f a a a a f a a a a f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f
    """),
    SpriteKind.player)