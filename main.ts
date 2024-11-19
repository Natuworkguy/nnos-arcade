namespace SpriteKind {
    export const Pointer_Kind = SpriteKind.create()
    export const LockBtn_Kind = SpriteKind.create()
    export const toonsBtn_Kind = SpriteKind.create()
    export const nonInteractiveIcon = SpriteKind.create()
    export const hangUpBtn_Kind = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Pointer_Kind, SpriteKind.toonsBtn_Kind, function (sprite, otherSprite) {
    if (controller.A.isPressed()) {
        openToonsApp()
    }
})
function lockDevice () {
    if (Locked == 0) {
        destroyIcons()
        sprites.destroy(Pointer)
    }
    Locked = 1
    scene.setBackgroundImage(assets.image`Lock Screen`)
}
sprites.onOverlap(SpriteKind.Pointer_Kind, SpriteKind.LockBtn_Kind, function (sprite2, otherSprite2) {
    if (controller.A.isPressed()) {
        console.log("[NNOS INFO]: The device has locked")
        lockDevice()
    }
})
function openToonsApp () {
    console.log("[NNOS SERVICES/toons]: Playing computer noises ambiance")
    while (true) {
        music.play(music.randomizeSound(music.createSoundEffect(WaveShape.Noise, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear)), music.PlaybackMode.UntilDone)
    }
}
function destroyIcons () {
    sprites.destroy(lockBtn)
    sprites.destroy(toonsBtn)
}
function unlockDevice () {
    if (Locked == 1) {
        console.log("[NNOS INFO]: Device has been unlocked.")
        Locked = 0
        scene.setBackgroundImage(assets.image`Background`)
        Pointer = sprites.create(assets.image`Cursor`, SpriteKind.Pointer_Kind)
        console.log("[NNOS INFO]: Created Pointer")
        Pointer.setStayInScreen(true)
        controller.moveSprite(Pointer, 50, 50)
        console.log("[NNOS INFO]: Set settings for Pointer")
        lockBtn = sprites.create(assets.image`lockIcon`, SpriteKind.LockBtn_Kind)
        console.log("[NNOS INFO]: Created lockBtn")
        lockBtn.setPosition(20, 20)
        console.log("[NNOS INFO]: Modified position for lockBtn")
        toonsBtn = sprites.create(assets.image`toonsIcon`, SpriteKind.toonsBtn_Kind)
        console.log("[NNOS INFO]: Created toonsBtn")
        toonsBtn.setPosition(20, 50)
        console.log("[NNOS INFO]: Modified position for toonsBtn")
    }
}
controller.combos.attachCombo('a+b', function () { // Change unlock combo here
    unlockDevice()
})
let toonsBtn: Sprite = null
let lockBtn: Sprite = null
let Pointer: Sprite = null
let Locked = 0
lockDevice()
