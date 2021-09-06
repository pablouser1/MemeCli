# MemeCli
Build your memes easily using just a terminal

# Requierements
* Python 3.7
* Ffmpeg
* PIL (Photo editing)
* MoviePy (Video editing)

# Meme List
Check [this file](LIST_MEMES.md) for a list with all the available memes

# Installation
```bash
python -m pip install -r requirements.txt
```

After you install the dependencies, you need to start creating the config.
Copy the file settings.sample.json as settings.json and follow [this structure](docs/SETTINGS.md)

# Usage
There are multiple modes, the first one is render mode which is non-interactive and accepts arguments
```bash
python cli.py render -i 'TEMPLATE_NAME' -o 'OUT_DIR' --texts 'TEXT1' 'TEXT2' 'TEXT3'
```

The second one is interactive mode, is interactive and asks the details it needs to generate a meme
```bash
python cli.py interactive
```

The third one is listing mode, which only shows the available memes and details about them
```bash
python cli.py listing
```

# TODO
* Better text support on photos
* Add photos to video

# How to add a template
Check [this file](docs/ADD_TEMPLATE.md) for info

# Credits
* [MoviePy](https://github.com/Zulko/moviepy)
* [Pillow](https://github.com/python-pillow/Pillow)
* [ImageText helper class](https://gist.github.com/pojda/8bf989a0556845aaf4662cd34f21d269) partially used on [this file](memecli/render/photo.py)
