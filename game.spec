# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['game.py'],
    pathex=[],
    binaries=[],
    datas=[('sounds/menu.mp3', 'sounds'), ('sounds/8-bit-game.mp3', 'sounds'), ('sounds/click.mp3', 'sounds'), ('sounds/land.mp3', 'sounds'), ('sounds/collect-coin.mp3', 'sounds'), ('sounds/collect-powerup.mp3', 'sounds'), ('fonts/Minecraft.ttf', 'fonts'), ('assets/clouds/cloud1.png', 'assets/clouds'), ('assets/clouds/cloud2.png', 'assets/clouds'), ('assets/clouds/cloud3.png', 'assets/clouds'), ('assets/menu/dino.png', 'assets/menu'), ('assets/menu/hud-controls.png', 'assets/menu'), ('assets/menu/hud-game.png', 'assets/menu'), ('assets/menu/platform.png', 'assets/menu'), ('assets/menu/spritesheet-button.png', 'assets/menu'), ('assets/menu/spritesheet-controls.png', 'assets/menu'), ('assets/menu/spritesheet-music.png', 'assets/menu'), ('assets/menu/spritesheet-sound.png', 'assets/menu'), ('assets/dino/DinoSprites - blue.png', 'assets/dino'), ('assets/dino/DinoSprites - red.png', 'assets/dino'), ('assets/dino/DinoSprites - yellow.png', 'assets/dino'), ('assets/dino/DinoSprites - green.png', 'assets/dino'), ('assets/platforms/blue/small.png', 'assets/platforms/blue'), ('assets/platforms/blue/medium.png', 'assets/platforms/blue'), ('assets/platforms/green/small.png', 'assets/platforms/green'), ('assets/platforms/green/medium.png', 'assets/platforms/green'), ('assets/platforms/red/small.png', 'assets/platforms/red'), ('assets/platforms/red/medium.png', 'assets/platforms/red'), ('assets/platforms/yellow/small.png', 'assets/platforms/yellow'), ('assets/platforms/yellow/medium.png', 'assets/platforms/yellow'), ('assets/items/spritesheet-coin.png', 'assets/items'), ('assets/items/spritesheet-powerup.png', 'assets/items'), ('assets/icon.png', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='game',
)
