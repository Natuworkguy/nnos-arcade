 


# NNOS Arcade

This is a simple device interface using MakeCode JavaScript, featuring a lock screen, an unlock mechanism, and Apps. The main features include interactive buttons, sound effects, and lock/unlock behavior.

## Features

- **Device Lock and Unlock**: The device can be locked and unlocked with specific button combinations.The default is a+b 
- **Toons App Simulation**: Clicking the "Toons" button will play ambient computer noise.
- **Custom Sprites and Icons**: Lock and app buttons are created as sprites, and the pointer can interact with them.
  
## Controls

- **`A + B`**: Unlocks the device.
- **Pointer**: Controlled with the directional pad to select icons.
- **`A` Button**: Selects the currently highlighted icon (e.g., locking the device or opening the Toons app).

## Code Breakdown

### Sprite Kinds
- **Pointer_Kind**: The sprite that the user controls to interact with on-screen elements.
- **LockBtn_Kind**: The sprite for the lock button, which locks the device.
- **toonsBtn_Kind**: The sprite for the Toons app button.
- **nonInteractiveIcon**: Placeholder for future non-interactive icons.

### Core Functions
- **`lockDevice()`**: Locks the device, hides the icons, and changes the background to the lock screen.
- **`unlockDevice()`**: Unlocks the device, creates the pointer, lock button, and Toons app button, and restores the background.
- **`incomingCall()`**: Plays a ringtone to simulate an incoming call and allows the user to dismiss it by locking the device.
- **`openToonsApp()`**: Plays continuous ambient computer noises to simulate an app running.
- **`destroyIcons()`**: Removes the lock and Toons app buttons from the screen.

### Event Handlers
- **`onOverlap`**: Detects when the pointer overlaps with interactive elements (e.g., Lock button, Toons button) and triggers respective actions when the `A` button is pressed.

## Setup Instructions

1. Import the provided code into your MakeCode Arcade editor.
2. Test the different button combinations to interact with the simulated device.

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/natuworkguy/nnos-arcade** and import

## To edit this project:

To edit this repository in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/natuworkguy/nnos-arcade** and click import

## Future Enhancements

- Add more apps.
- Expand the UI with non-interactive icons for aesthetics.

## To get a demonstration of the software:

- Go to https://natuworkguy.github.io/nnos-arcade/

---
