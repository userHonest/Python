all: build

build:
	pyinstaller --additional-hooks-dir=hooks --onefile --add-data 'selection.py:.' --add-data 'userAuth.py:.' main.py -n KeyGuard
	
	# for windows
   #pyinstaller --additional-hooks-dir=hooks --onefile --add-data 'selection.py;.' main.py
clean:
	rm -rf __pycache__/
	rm -rf build/
	rm -rf dist/
	rm *.spec

.PHONY: all build clean

