# Dino Fall - Game Design Document

Tento repozitár obsahuje implementáciu hry v Pygame, ktorá kombinuje prvky rýchlej akcie s farebnými mechanizmami a platformovým pohybom. Hráč sa sústredí na dynamické skákanie na platformy, pričom si musí strategicky vyberať farbu dinosaura. Zároveň zbiera mince, pričom sa postupne hra zrýchľuje.

**Vybraná téma**: Color as a gameplay feature (farba ako herná mechanika)

**Autor**: Pavol Pohánka

---

## **1. Úvod**
DinoFall je jednoduchá akčná hra, v ktorej hráč ovláda dinosaura, ktorý padá z platformy na platformu. Počas pádu môže zbierať mince a meniť svoju farbu, aby sa prispôsobil platformám, na ktoré pristáva. Kľúčovým mechanizmom je zmena farby dinosaura, ktorá ovplyvňuje jeho rýchlosť a efektivitu pri zbere mincí. Rýchlosť pádu a náročnosť hry postupne rastie, čím sa zvyšuje intenzita zážitku. Hra skončí, keď dinosaur opustí hernú obrazovku. Cieľom tejto hry, je dosiahnuť čo najvyššie skóre.


### **1.1 Inšpirácia**
<ins>**Pou - Sky Jump**</ins>

Hra DinoFall sa inšpiruje minihrou Sky Jump z hry Pou, kde hráč ovláda postavu skáčucu z platformy na platformu. Hráč sa tu musí vyhýbať prekážkam, zbierať mince, pričom sa zvyšuje náročnosť hry.

DinoFall preberá zbieranie mincí a základnú mechaniku pohybu na platformách len v opačnom smere. Pridáva unikátnu farebnú mechaniku, ktorá ovplyvňuje rýchlosť a spôsob hrania.

<p align="center"> <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/Pou%20-%20Sky%20Jump.png" alt="pou - sky jump"> <br> <em>Obrázok 1 Ukážka hry Pou - Sky Jump</em> </p>

### **1.2 Herný zážitok**

Cieľom hry je, aby hráč čo najdlhšie prežil v rýchlo sa zvyšujúcom tempe a vyhýbal sa pádom mimo platformy.

Kľúčové herné mechaniky sú:
- Rýchly a zábavný herný zážitok s rastúcou dynamikou
- Pestrofarebné prostredie s pixel art grafikou
- Zvýšené napätie s rastúcou rýchlosťou a pohybom platforiem
- Neustála motivácia k zlepšovaniu a dosahovaniu vyšších skóre
  
### **1.3 Vývojový softvér**
- **Visual Studio Code**: vývojové prostredie
- **Pygame (Python)**: herný engine
- **Piskel**: herná grafika
- **SpriteFusion**: herná grafika
- **AudioMass**: úprava zvukových efektov
  
---
## **2. Koncept**

### **2.1 Prehľad hry**
Hráč ovláda dinosaura, ktorý skáče z jednej platformy na druhú. Musí sa prispôsobovať farbe platformy, aby mal vyššiu rýchlosť, ak sa farba platformy a dinosaura zhodujú. Platformy sa zrýchľujú, čím sa zvyšuje náročnosť.

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20menu.gif" alt="dinofall menu">
  <br>
  <em>Obrázok 2 Ukážka hry - Menu</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20game.gif" alt="dinofall game">
  <br>
  <em>Obrázok 3 Ukážka hry DinoFall</em>
</p>

### **2.2 Základné mechaniky**
- **Farba dinosaura**: zmena farby dinosaura
- **Rýchlosť**: zmena rýchlosti na základe farby zhodujúcej sa s platformou
- **Mince**: zbieranie mincí, ktoré zvyšujú skóre
  
### **2.3 Návrh tried**
- **Game**: Hlavná trieda hry, riadi hernú slučku, aktualizáciu a vykresľovanie objektov.
- **Player**: Spravuje pohyb, zmenu farby a kolízie s platformami.
- **Platform**: Reprezentuje pohybujúce sa platformy, ukladá ich farbu a rýchlosť.
- **Coin**: Obsahuje polohu mincí a spracovanie kolízie s hráčom.
- **Menu**: Riadi zobrazenie hlavného menu, vrátane tlačidiel a navigácie.

---
## **3. Grafika**

### **3.1 Vizuálny štýl**
Hra využíva minimalistický pixel art štýl, ktorý som vytvoril úpravou existujúcich tilesetov a tvorbou vlastných spritesheetov.

- **Farebné platformy**: Každá platforma má svoju jedinečnú farbu, pričom som ich upravil tak, aby ladili s hernou mechanikou.
- **Dinosaur**: Jednoduchá, ale dynamická postava dinosaura, ktorá mení farbu podľa aktuálnej platformy.
- **Minimalistické prostredie**: Herné pozadie s oblakmi vytvorenými z tilesetu.
- **UI prvky**: Tlačidlá, HUD a ďalšie herné rozhranie som navrhol a vytvoril samostatne, pričom som dbal na ich prehľadnosť a zapadnutie do celkového vizuálu hry.

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/nature-platformer-tileset-16x16.png" 
       alt="nature platformer tileset" 
       width="250">
  <br>
  <em>Obrázok 4 Ukážka nature-platformer-tileset-16x16.png</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/assets/menu/spritesheet-controls.png" 
       alt="control button spritesheet" 
       style="width: 300px; height: auto;">
  <br>
  <em>Obrázok 5 Ukážka spritesheet-control.png</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/assets/menu/spritesheet-sound.png" 
       alt="sound button spritesheet" 
       style="width: 200px; height: auto;">
  <br>
  <em>Obrázok 6 Ukážka spritesheet-sound.png</em>
</p>

### **3.2 Animácie**
**Animácia postavy**
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20dinos.gif" alt="animacia postavy">
  <br>
  <em>Obrázok 7 Ukážka hry - Animácia postavy</em>
</p>

**Animácia mince**
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20coin.gif" alt="animacia mince">
  <br>
  <em>Obrázok 8 Ukážka hry - Animácia mince</em>
</p>

---
## **4. Zvuk**

### **4.1 Hudba**
- Atmosférická hudba v menu
- Dynamická hudba počas hrania

### **4.2 Zvukové efekty**
- Zvuky v menu
- Zvuky dopadu na platformu
- Zvuky pri zbere mince

---
## **5. Herné prostredie**

### **5.1 Používateľské rozhranie**
- Ukazovateľ výšky skóre
- Ukazovateľ počtu mincí

### **5.2 Ovládanie**

</ins>**Klávesnica**</ins>
- **Enter**: voľba v menu
- **Escape**: návrat do menu
- **Šípky**: výber v menu a pohyb postavy
- **A**: zmena farby postavy na modrú
- **S**: zmena farby postavy na zelenú
- **D**: zmena farby postavy na červenú
- **F**: zmena farby postavy na žltú
- **R**: reštart hry
  

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20controls.png" alt="dinofall controls">
  <br>
  <em>Obrázok 5 Ukážka Hry - Ovládanie </em>
</p>
