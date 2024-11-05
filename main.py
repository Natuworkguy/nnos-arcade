@namespace
class SpriteKind:
    Pointer_Kind = SpriteKind.create()
    LockBtn_Kind = SpriteKind.create()
    toonsBtn_Kind = SpriteKind.create()
    nonInteractiveIcon = SpriteKind.create()
    hangUpBtn_Kind = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    if controller.A.is_pressed():
        openToonsApp()
sprites.on_overlap(SpriteKind.Pointer_Kind,
    SpriteKind.toonsBtn_Kind,
    on_on_overlap)

def lockDevice():
    global Locked
    if Locked == 0:
        destroyIcons()
        sprites.destroy(Pointer)
    Locked = 1
    scene.set_background_image(assets.image("""
        Lock Screen
    """))
def incomingCall():
    scene.set_background_image(assets.image("""
        Black screen
    """))
    for index in range(10):
        if controller.A.is_pressed():
            lockDevice()
            break
        music.play(music.create_song(assets.song("""
                Ringtone
            """)),
            music.PlaybackMode.UNTIL_DONE)
    lockDevice()
def openToonsApp():
    print("[NNOS SERVICES/toons]: Playing computer noises ambiance")
    while True:
        music.play(music.randomize_sound(music.create_sound_effect(WaveShape.NOISE,
                    5000,
                    0,
                    255,
                    0,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR)),
            music.PlaybackMode.UNTIL_DONE)
def destroyIcons():
    sprites.destroy(lockBtn)
    sprites.destroy(toonsBtn)
def on_combos_attach_combo():
    unlockDevice()
controller.combos.attach_combo("a+b", on_combos_attach_combo)
def on_combos_attach_combo2():
    incomingCall()
controller.combos.attach_combo("d+b", on_combos_attach_combo2)
def unlockDevice():
    global Locked, Pointer, lockBtn, toonsBtn
    if Locked == 1:
        print("[NNOS INFO]: Device has been unlocked.")
        Locked = 0
        scene.set_background_image(assets.image("""
            Background
        """))
        Pointer = sprites.create(assets.image("""
            Cursor
        """), SpriteKind.Pointer_Kind)
        print("[NNOS INFO]: Created Pointer")
        Pointer.set_stay_in_screen(True)
        controller.move_sprite(Pointer, 50, 50)
        print("[NNOS INFO]: Set settings for Pointer")
        lockBtn = sprites.create(assets.image("""
            lockIcon
        """), SpriteKind.LockBtn_Kind)
        print("[NNOS INFO]: Created lockBtn")
        lockBtn.set_position(20, 20)
        print("[NNOS INFO]: Modified position for lockBtn")
        toonsBtn = sprites.create(assets.image("""
                toonsIcon
            """),
            SpriteKind.toonsBtn_Kind)
        print("[NNOS INFO]: Created toonsBtn")
        toonsBtn.set_position(20, 50)
        print("[NNOS INFO]: Modified position for toonsBtn")

def on_on_overlap2(sprite2, otherSprite2):
    if controller.A.is_pressed():
        print("[NNOS INFO]: The device has locked")
        lockDevice()
sprites.on_overlap(SpriteKind.Pointer_Kind,
    SpriteKind.LockBtn_Kind,
    on_on_overlap2)
toonsBtn: Sprite = None
lockBtn: Sprite = None
Pointer: Sprite = None
Locked = 0
lockDevice()