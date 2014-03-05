# -*- mode: python -*-
a = Analysis(['../../src/hackandslash.py'],
             pathex=['/home/samgeen/Programming/MakeWee/workspace/hackandslash/build/linux'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'hackandslash'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
