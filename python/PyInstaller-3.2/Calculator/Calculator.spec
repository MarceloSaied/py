# -*- mode: python -*-

block_cipher = None


a = Analysis(['c:\\Dropbox\\shared\\central@iaacob\\py\\python\\Calculator1\\Calculator.py'],
             pathex=['c:\\Dropbox\\shared\\central@iaacob\\py\\python\\PyInstaller-3.2\\Calculator'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Calculator',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='C:\\Dropbox\\shared\\central@iaacob\\py\\python\\Calculator1\\Calculator.ico')
