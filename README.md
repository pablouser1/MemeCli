# MemeGenerator
Build your memes easily using just a terminal

# Requierements
* Python 3.7
* Ffmpeg
* PIL (Photo editing)
* MoviePy (Video editing)

# Installation
```bash
python -m pip install -r requirements.txt
```

# Usage
```bash
python cli.py 'TEMPLATE_NAME' 'OUT_DIR' -t 'TEXT1' 'TEXT2' 'TEXT3'
```

# How to add a template
Check the [following file](docs/ADD_TEMPLATE.md) for info

# TODO
* List all memes using command line
* Better text support on photos
* Add photos to video

# Credits
* [MoviePy](https://github.com/Zulko/moviepy)
* [Pillow](https://github.com/python-pillow/Pillow)
* [ImageText helper class](https://gist.github.com/pojda/8bf989a0556845aaf4662cd34f21d269) partially used on [this file](memecli/render/photo.py)
