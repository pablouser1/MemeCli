import argparse
from memecli.render.photo import PhotoRender
from memecli.render.video import VideoRender
from memecli.helpers.Config import getConfig

cli = argparse.ArgumentParser()
cli.add_argument('template')
cli.add_argument('output', default='out/meme')
cli.add_argument('-t', '--texts', nargs='+', default=[])
args = cli.parse_args()

path = f'templates/{args.template}'
config = getConfig(path)
if config["type"] == "video":
    parser = VideoRender(f'{path}/template.mp4', config)
elif config["type"] == "photo":
    parser = PhotoRender(f'{path}/template.jpg', config)

parser.run(args.texts)
parser.save(args.output)
