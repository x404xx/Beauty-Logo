<div align="center">

<img src="assets/logo.png" width="250" height="auto">

**Beauty-Logo** is a simple script for applying a colorful fading effect.

<img src="assets/result.png" width="300" height="auto">

</div>

## Usage Example

```python
from beautylogo import ColorFader, ColorMode

text = """
 ▄████▄  ▒█████    ██▓    ▒█████   ██▀███     █████ ▄▄▄     ▓█████▄  ▓█████ ██▀███
▒██▀ ▀█ ▒██▒  ██▒ ▓██▒   ▒██▒  ██▒▓██ ▒ ██▒ ▓██    ▒████▄   ▒██▀ ██▌ ▓█   ▀▓██ ▒ ██▒
▒▓█    ▄▒██░  ██▒ ▒██░   ▒██░  ██▒▓██ ░▄█ ▒ ▒████  ▒██  ▀█▄ ░██   █▌ ▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒██   ██░ ▒██░   ▒██   ██░▒██▀▀█▄   ░▓█▒   ░██▄▄▄▄██░▓█▄   ▌ ▒▓█  ▄▒██▀▀█▄
▒ ▓███▀ ░ ████▓▒░▒░██████░ ████▓▒░░██▓ ▒██▒▒░▒█░   ▒▓█   ▓██░▒████▓ ▒░▒████░██▓ ▒██▒██
░ ░▒ ▒  ░ ▒░▒░▒░ ░░ ▒░▓  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒ ░   ░▒▒   ▓▒█ ▒▒▓  ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░▒▒
  ░  ▒    ░ ▒ ▒░ ░░ ░ ▒    ░ ▒ ▒░   ░▒ ░ ▒ ░ ░     ░ ░   ▒▒  ░ ▒  ▒ ░ ░ ░    ░▒ ░ ▒ ░
░       ░ ░ ░ ▒     ░ ░  ░ ░ ░ ▒    ░░   ░   ░ ░     ░   ▒   ░ ░  ░     ░    ░░   ░ ░
░ ░         ░ ░  ░    ░      ░ ░     ░     ░             ░     ░    ░   ░     ░      ░
                                BY:ˣ⁴⁰⁴ˣˣ
"""

fader = ColorFader(text)

print(fader.apply_fade(ColorMode.LIGHT_BLUE))
print(fader.apply_fade(ColorMode.BLACK_WHITE))
print(fader.apply_fade(ColorMode.PURPLE_BLUE))
print(fader.apply_fade(ColorMode.LIGHT_GREEN))
print(fader.apply_fade(ColorMode.PINK_RED))
print(fader.apply_fade(ColorMode.WATER))
print(fader.apply_fade(ColorMode.FIRE))
print(fader.apply_fade(ColorMode.BRAZIL))
print(fader.apply_fade(ColorMode.RANDOM))

```
