# 31game
pyinstaller 31game.spec
nuitka --include-data-dir=./res/=./res/ --mingw64 --follow-imports --onefile --enable-plugin=tk-inter --disable-console 31game.pyw