# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\g\\Development\\intex\\src\\intex.py'],
             pathex=['C:\\Users\\g\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\g\\Development\\intex\\src', 'C:\\Users\\g\\Development\\intex'],
             binaries=[('C:\\Users\\g\\Development\\intex\\lib','lib')],
             datas=None,
             hiddenimports=['PyQt5'],
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
          name='intex',
          debug=False,
          strip=False,
          upx=True,
          console=True )
