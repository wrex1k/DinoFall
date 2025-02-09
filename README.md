# Dino Fall - Game Design Document

Tento repozitár obsahuje implementáciu hry v Pygame, ktorá kombinuje prvky rýchlej akcie s farebnými mechanizmami a platformovým pohybom. Hráč sa sústredí na dynamické skákanie na platformy, pričom si musí strategicky vyberať farbu dinosaura. Zároveň zbiera coiny a powerupy, pričom sa postupne hra zrýchľuje.

**Vybraná téma**: Color as a gameplay feature (farba ako herná mechanika)

**Autor**: Pavol Pohánka

---

## **1. Úvod**
DinoFall je jednoduchá akčná hra, v ktorej hráč ovláda dinosaura, ktorý padá z platformy na platformu. Počas pádu môže zbierať coiny a powerupy. Musí meniť svoju farbu, aby sa prispôsobil platformám, na ktoré pristáva. Kľúčovým mechanizmom je zmena farby dinosaura, ktorá ovplyvňuje jeho rýchlosť a efektivitu pri zbere coinov. Rýchlosť pádu a náročnosť hry postupne rastie, čím sa zvyšuje intenzita zážitku. Hra skončí, keď sa dinosaur dotkne hranice hernej plochy. Cieľom tejto hry, je dosiahnuť čo najvyššie skóre.


### **1.1 Inšpirácia**
<ins>**Pou - Sky Jump**</ins>

Hra DinoFall sa inšpiruje minihrou Sky Jump z hry Pou, kde hráč ovláda postavu skáčucu z platformy na platformu. Hráč sa tu musí vyhýbať prekážkam, zbierať coiny, pričom sa zvyšuje náročnosť hry.

DinoFall preberá zbieranie coinov a základnú mechaniku pohybu na platformách len v opačnom smere. Pridáva unikátnu farebnú mechaniku, ktorá ovplyvňuje rýchlosť a spôsob hrania.

<p align="center"> <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/Pou%20-%20Sky%20Jump.png" alt="pou - sky jump"> <br> <em>Obrázok 1 Ukážka hry Pou - Sky Jump</em> </p>

### **1.2 Herný zážitok**

Cieľom hry je, aby hráč čo najdlhšie prežil v rýchlo sa zvyšujúcom tempe a vyhýbal sa pádom mimo platformy.

Kľúčové herné mechaniky sú:
- Rýchly a zábavný herný zážitok s rastúcou dynamikou
- Pestrofarebné prostredie s pixel art grafikou
- Neustála motivácia k zlepšovaniu a dosahovaniu vyššieho skóre
  
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
- **Powerupy**: zbieranie powerupov, ktoré automaticky mení farbu hráča podľa farby platformy
- **Coiny**: zbieranie mincí, ktoré zvyšujú skóre
  
### **2.3 Návrh tried**
- **Game**: Hlavná trieda hry, riadi hernú slučku, aktualizáciu a vykresľovanie objektov.
- **Player**: Spravuje pohyb, animáciu dinosaura, zmenu farby a kolízie s platformami a itemami.
- **Platform**: Reprezentuje pohybujúce sa platformy, ukladá ich farbu a rýchlosť.
- **Item**: Reprezentuje predmety v hre, spravuje ich pohyb a animáciu
- **Menu**: Riadi zobrazenie hlavného menu, vrátane tlačidiel a navigácie.

---
## **3. Grafika**

### **3.1 Vizuálny štýl**
Hra využíva minimalistický pixel art štýl, kde boli použité assety [Dino-Characters](https://arks.itch.io/dino-characters) a [Nature Platformer Tileset](https://rottingpixels.itch.io/nature-platformer-tileset) z itch.io, z ktorých som následne vytváral všetky herné prvky. Cieľom bolo vytvoriť príjemne vyzerajúcu hru pre rôzne vekové kategórie.

- **Farebné platformy**: Každá platforma má svoju jedinečnú farbu, pričom som ich upravil tak, aby ladili s hernou mechanikou.
- **Dinosaur**: Jednoduchá postava dinosaura v 4 farbách (zelená, modrá, červená, žltá).
- **Minimalistické prostredie**: Herné pozadie s oblakmi vytvorenými z tilesetu.
- **UI prvky**: Tlačidlá, HUD a ďalšie herné rozhranie som navrhol a vytvoril samostatne, pričom som dbal na ich prehľadnosť a zapadnutie do celkového vizuálu hry.

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/nature-platformer-tileset-16x16.png" alt="nature platformer tileset">
  <br>
  <em>Obrázok 4 Ukážka nature-platformer-tileset-16x16.png</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20keybuttons.png" alt="control button spritesheet">
  <br>
  <em>Obrázok 5 Ukážka spritesheet-control.png</em>
</p>

<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20soundbuttons.png" alt="sound button spritesheet">
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

**Animácia coinu**
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20coin.gif" alt="animacia coinu">
  <br>
  <em>Obrázok 8 Ukážka hry - Animácia coinu</em>
</p>

**Animácia powerupu**
<p align="center">
  <img src="https://github.com/wrex1k/DinoFall/blob/main/readme/DinoFall%20-%20powerup.gif" alt="animacia powerupu">
  <br>
  <em>Obrázok 8 Ukážka hry - Animácia powerupu</em>
</p>

---
## **4. Zvuk**

### **4.1 Hudba**
V menu je použitá príjemná hudba [Emotional Piano Music](https://pixabay.com/music/modern-classical-emotional-piano-music-256262/) ktorá je charakteristická pre menu. Naopak, v hre je akčná 8 bitová hudba [8-bit-menu](https://youtu.be/6r2Z0EGk0D8?si=p1xDEklEOuksgJm3), ktorá perfektne ladí s minimalistickým pixel art štýlom a podporuje dynamiku hry.

### **4.2 Zvukové efekty**
Zvuky v hre pochádzajú z Pixabay[https://pixabay.com/] z ktorých som vybral zvuky pre výber v menu, dopad hráča, zber coinov a powerupov, pričom som sa zameral na to, aby ladili s herným vizuálom a podporovali arkádovú atmosféru.

---
## **5. Herné prostredie**

### **5.1 Používateľské rozhranie**
V menu sa nachádzajú tlačidlá Play, Controls a Exit, spolu s dvoma tlačidlami na zapnutie či vypnutie hudby a zvukov. 

V hre sa nachádzajú ukazovatele:
- Výška skóre
- Stav powerupu
- Počet coinov

Po skončení hry sa zobrazí Game Over obrazovka, z ktorej je možné sa vrátiť do menu alebo hru resetovať.

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
