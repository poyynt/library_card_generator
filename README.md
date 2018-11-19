# library_card_generator
**Install**
```bash
python3 install_requirements.py
```

**Run**

Change the following constants according to your template:
```
TEMPLATE_FILENAME -> filename of your template. PNG recommended otherwise color problems may occur.
FONT_NAME -> font name
FONT_SIZE -> font size
FOREGROUND_COLOR -> text foreground color
QRCODE_FOREGROUND_COLOR -> qrcode foreground color
NAME_LT_COORDINATES -> top left corner coordinates (x,y) for the name field
CODE_LT_COORDINATES -> top left corner coordinates (x,y) for the code field
QRCODE_LT_COORDINATES -> top left corner coordinates (x,y) for the QR Code
```
and run the program:
```bash
python3 generate.py
```
