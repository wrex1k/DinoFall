# Dino Fall - Game Design Document

This repository contains the implementation of a Pygame-based action game that combines fast-paced gameplay with color-based mechanics and platform movement. The player focuses on dynamically jumping between platforms while strategically changing the dinosaur’s color. Along the way, the player collects coins and power-ups as the game gradually speeds up.

**Selected Theme**: Color as a gameplay feature

---

## **1. Introduction**

DinoFall is a simple action game in which the player controls a dinosaur falling from one platform to another. During the fall, the player collects coins and power-ups and must change the dinosaur’s color to match the platforms it lands on.  

The core mechanic is the color-changing system that affects the dinosaur’s speed and efficiency when collecting coins. The falling speed and overall difficulty gradually increase, making the experience more intense. The game ends when the dinosaur touches the bottom boundary of the screen.  
The main goal is to achieve the highest possible score.

### **1.1 Inspiration**
<ins>**Pou - Sky Jump**</ins>

DinoFall is inspired by the mini-game *Sky Jump* from *Pou*, in which the player controls a character jumping from platform to platform while avoiding obstacles and collecting coins as difficulty rises.

DinoFall adapts the coin collection and platform mechanics but reverses the direction of movement. It adds a unique color-based mechanic that influences both speed and strategy.

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/Pou%20-%20Sky%20Jump.png" alt="pou - sky jump">
  <br>
  <em>Figure 1. Example of Pou - Sky Jump</em>
</p>

### **1.2 Gameplay Experience**

The goal is to survive as long as possible while keeping up with the increasing game speed and avoiding missed platforms.

Key gameplay elements:
- Fast and enjoyable arcade experience with increasing intensity
- Colorful pixel-art environment
- Continuous motivation to improve and achieve higher scores

### **1.3 Development Tools**
- **Visual Studio Code**: Development environment  
- **Pygame (Python)**: Game engine  
- **Piskel**: Game graphics  
- **SpriteFusion**: Game graphics  
- **AudioMass**: Sound effect editing  

---

## **2. Concept**

### **2.1 Game Overview**
The player controls a dinosaur jumping from one platform to another. To move efficiently, the player must match the dinosaur’s color with that of the platform, gaining extra speed if the colors match. Platforms accelerate over time, increasing difficulty.

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20menu.gif" alt="dinofall menu">
  <br>
  <em>Figure 2. Game Example - Menu</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20game.gif" alt="dinofall game">
  <br>
  <em>Figure 3. Game Example - DinoFall Gameplay</em>
</p>

### **2.2 Core Mechanics**
- **Dinosaur Color**: The player can change the dinosaur’s color  
- **Speed**: Increases when the dinosaur’s color matches the platform  
- **Power-ups**: Automatically change the dinosaur’s color to match the next platform  
- **Coins**: Collected to increase score  

### **2.3 Class Design**
- **Game**: Main class handling the game loop, updates, and rendering  
- **Player**: Manages dinosaur movement, animation, color changes, and collisions  
- **Platform**: Represents moving platforms with assigned color and speed  
- **Item**: Handles collectible objects and their animations  
- **Menu**: Manages the main menu UI, buttons, and navigation  

---

## **3. Graphics**

### **3.1 Visual Style**
The game uses a minimalist pixel-art style. Assets such as [Dino-Characters](https://arks.itch.io/dino-characters) and [Nature Platformer Tileset](https://rottingpixels.itch.io/nature-platformer-tileset) from itch.io were used as a base for creating all visual elements. The goal was to make a visually pleasant game suitable for all age groups.

- **Colored Platforms**: Each platform has a unique color, adjusted to fit the core mechanic  
- **Dinosaur**: Simple character in four color variants (green, blue, red, yellow)  
- **Minimalistic Environment**: Background with clouds made from tilesets  
- **UI Elements**: Custom-designed buttons and HUD with clean readability and visual consistency  

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/nature-platformer-tileset-16x16.png" alt="nature platformer tileset">
  <br>
  <em>Figure 4. Example - Nature Platformer Tileset</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20keybuttons.png" alt="control button spritesheet">
  <br>
  <em>Figure 5. Example - Spritesheet Control Buttons</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20soundbuttons.png" alt="sound button spritesheet">
  <br>
  <em>Figure 6. Example - Spritesheet Sound Buttons</em>
</p>

### **3.2 Animations**
**Character Animation**  
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20dinos.gif" alt="character animation">
  <br>
  <em>Figure 7. Character Animation Example</em>
</p>

**Coin Animation**  
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20coin.gif" alt="coin animation">
  <br>
  <em>Figure 8. Coin Animation Example</em>
</p>

**Power-up Animation**  
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20powerup.gif" alt="powerup animation">
  <br>
  <em>Figure 9. Power-up Animation Example</em>
</p>

---

## **4. Sound**

### **4.1 Music**
The main menu features calm background music: [Emotional Piano Music](https://pixabay.com/music/modern-classical-emotional-piano-music-256262/).  
During gameplay, fast-paced 8-bit music [8-bit-menu](https://youtu.be/6r2Z0EGk0D8?si=p1xDEklEOuksgJm3) is used to match the pixel-art aesthetic and enhance game dynamics.

### **4.2 Sound Effects**
Sound effects were sourced from [Pixabay](https://pixabay.com). Sounds were chosen for menu selections, player landings, coin pickups, and power-ups. All sounds were selected to match the visual style and reinforce the arcade atmosphere.

---

## **5. Game Environment**

### **5.1 User Interface**
The main menu includes the following buttons: **Play**, **Controls**, and **Exit**, along with two buttons to toggle music and sound effects.

During gameplay, the UI displays:
- Score counter  
- Power-up status  
- Number of collected coins  

After the game ends, a **Game Over** screen appears, allowing the player to return to the menu or restart.

### **5.2 Controls**
<ins>**Keyboard**</ins>
- **Enter**: Select in menu  
- **Escape**: Return to menu  
- **Arrow keys**: Navigate menu and move character  
- **A**: Change dinosaur color to blue  
- **S**: Change dinosaur color to green  
- **D**: Change dinosaur color to red  
- **F**: Change dinosaur color to yellow  
- **R**: Restart the game  

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20controls.png" alt="dinofall controls">
  <br>
  <em>Figure 10. Game Example - Controls</em>
</p>
