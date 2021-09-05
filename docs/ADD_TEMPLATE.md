# Add template

## Structure
This project use the following structure for a template:

    .
    ├── config.json                   # Config of template
    ├── template.mp4                  # Source file if video
    └── template.jpg                  # Source file if photo

The folder containing all this files will be used to access it.

## Config file
The JSON file needs to have the following structure
```json
{
  "type": "video", // Set template type, can be "photo" or "video"
  "source": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", // Source of template, not used yet
  "texts": [
    {
      "pos": [0, 0], // Initial position of text. First element of array is for the x axis and the second one is for the y axis.
      "size": [360, 120], // Max width and height the text can use
      "duration": [
        [0, 0], // Start time of text, the first element is for minutes and the second one is for seconds
        null // End time of text, if null assume it never ends
      ]
    }
  ]
}
```

## Media files
The videos must be MP4 and the photos must be JPG
