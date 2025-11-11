# DinoFall – Game Build

This branch contains the **compiled version** of DinoFall built with **PyInstaller**.  
Use it if you just want to **play the game** without running the Python source code.

---

## How to Run the Game (Windows)

1. Download or clone this branch:
   ```bash
   git clone -b build https://github.com/wrex1k/DinoFall.git
   ```
   or download it as a ZIP file from GitHub.

2. Navigate into the folder:
   ```bash
   cd DinoFall/dist/game
   ```

3. Run the executable:
   ```bash
   DinoFall.exe
   ```

---

## Common Issues and Fixes

### "Failed to execute script game"
This error may occur if some runtime DLLs are missing or blocked.  
Make sure to extract the entire `dist/game` folder before running the `.exe`.  
Do **not** run it directly from inside the ZIP archive.

### Windows Defender warning
Because the game is unsigned, Windows may show “Unknown publisher”.  
Click **“More info → Run anyway”**. The build is safe and locally compiled with PyInstaller.

---

## Included Files
- `dist/game/DinoFall.exe` → main executable  
- `assets/`, `sounds/`, `fonts/` → required resources  
- `_internal/` → runtime libraries automatically bundled by PyInstaller
