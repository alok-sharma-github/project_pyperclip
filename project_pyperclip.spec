# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['project_pyperclip.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/alok/.cache/huggingface/hub/models--t5-small', 'huggingface/models--t5-small'), ('clipboard.png', '.')],
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
    a.binaries,
    a.datas,
    [],
    name='project_pyperclip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
