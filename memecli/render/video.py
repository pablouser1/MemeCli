from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from ..helpers.Misc import randomString

class VideoRender:
    config = {}
    clips: list[VideoFileClip, TextClip] = []
    template: VideoFileClip
    out: CompositeVideoClip

    def __init__(self, template: str, config: dict):
        self.config = config
        self.template = VideoFileClip(template)
        self.clips.append(self.template)

    def addText(self, config_item: dict, text: str)-> TextClip:
        clip_text = TextClip(text, size=config_item["size"], method='caption')
        clip_text = clip_text.set_position(tuple(config_item["pos"]))
        # Touple with minutes and seconds of the appearance of the text
        starts = (config_item["duration"][0][0], config_item["duration"][0][1])
        clip_text = clip_text.set_start(starts)
        # If end is not null sets an end to the text
        if config_item["duration"][1]:
            ends = (config_item["duration"][1][0], config_item["duration"][1][1])
            clip_text = clip_text.set_end(ends)
        self.clips.append(clip_text)

    def run(self, texts: list):
        # Procress texts
        if 'texts' in self.config:
            for i in range(len(self.config["texts"])):
                self.addText(self.config["texts"][i], texts[i])

        self.out = CompositeVideoClip(self.clips)
        self.out.duration = self.template.duration

    def save(self, file: str):
        temp_audio = 'tmp/tmp_' + randomString(6) + '.mp3'
        # Write to output
        self.out.write_videofile(file, fps=30, temp_audiofile=temp_audio)

    def cleanup(self):
        for clip in self.clips:
            clip.close()

        self.out.close()
