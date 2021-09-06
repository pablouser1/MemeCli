import argparse
from pick import pick
from memecli.render.photo import PhotoRender
from memecli.render.video import VideoRender
from memecli.common import templates

def render(slug: str, texts: list, output: str):
    config = templates.one(slug)
    path = f'{templates.base}/{slug}'
    if config["type"] == "video":
        parser = VideoRender(f'{path}/template.mp4', config)
    elif config["type"] == "photo":
        parser = PhotoRender(f'{path}/template.jpg', config)

    parser.run(texts)
    parser.save(output)

def interactive():
    options = []
    all_templates = templates.all()
    for temp_template in all_templates:
        options.append(temp_template["name"])

    option, index = pick(options, 'Choose a template')
    print("Picked " + option)

    template = all_templates[index]["slug"]

    texts = []
    texts_i = int(input("Type amount of texts you want to type: "))
    i = 0
    while i < texts_i:
        text = input("Type text: ")
        texts.append(text)
        i += 1

    output = input('Type an output path, example: ./out/test.mp4: ')
    if not output:
        raise Exception('You need to type an output path')

    render(template, texts, output)

def listing():
    options = []
    all_templates = templates.all()
    for temp_template in all_templates:
        options.append(temp_template["name"])

    option, index = pick(options, 'Choose a template')
    print(f"Details of {option}:\n")
    # Show details of template
    slug = all_templates[index]["slug"]
    template = templates.one(slug)
    print(f'Video source: {template["source"]}')
    if 'texts' in template:
        print(f'Can have {len(template["texts"])} text(s)')
    else:
        print(f"Can't have text")

if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    cli.add_argument('mode', default='interactive', help='Valid options: list, render, interactive')
    cli.add_argument('-i', '--input', help='Template name')
    cli.add_argument('-o', '--output', default='out/meme', help='Output file')
    cli.add_argument('--texts', nargs='+', default=[])
    args = cli.parse_args()

    if args.mode == 'render':
        render(args.input, args.texts, args.output)
    elif args.mode == 'interactive':
        interactive()
    elif args.mode == 'list':
        listing()
    else:
        print(cli.print_usage())
