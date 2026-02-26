# asciify

A lightweight Python script that convert your videos into beautiful ASCII art animations.

## Features

- **Video to ASCII Conversion** — Transform any video into ASCII art
- **Colored ASCII** — Characters are colored to match the original video
- **Customizable ASCII Sets** — Use different character sets for different effects
- **MP4 Output** — Exports your ASCII video as an MP4 file
- **Frame-by-Frame Processing** — High-quality conversion with proper frame rates

## Requirements

- Python 3.6+
- OpenCV (`cv2`)
- Pillow (`PIL`)
- imgkit
- wkhtmltoimage (system dependency)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JLeTien/asciify.git
cd asciify
```

# asciify

Convert videos to ASCII art animations. Watch your favorite videos reimagined in the terminal with colored characters.

## Features

- **Video to ASCII Conversion** — Transform any video into ASCII art
- **Colored ASCII** — Characters are colored to match the original video
- **Customizable ASCII Sets** — Use different character sets for different effects
- **MP4 Output** — Save your ASCII video as an MP4 file
- **Frame-by-Frame Processing** — High-quality conversion with proper frame rates

## Requirements

- Python 3.6+
- OpenCV (`cv2`)
- Pillow (`PIL`)
- imgkit
- wkhtmltoimage (system dependency)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JLeTien/asciify.git
cd asciify
```

2. Create and activate a virtual environment:

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python3 -m venv venv
venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install wkhtmltoimage:

**macOS (Homebrew):**
Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)

## Usage

1. Place your video in a `video/` folder, or specify the path directly
2. Run the script:
```bash
python asciify.py
```

3. Update the video path in the `main()` call at the bottom of the script:
```python
main("path/to/your/video.mp4")
```

The output video will be saved as `final_[videoname].mp4`

## How It Works

1. **Extract Frames** — Reads video frame-by-frame and saves as images
2. **Pixelate** — Resizes images to ASCII-friendly dimensions
3. **Grayscale** — Converts to monochrome for ASCII mapping
4. **ASCII Conversion** — Maps brightness values to ASCII characters
5. **Colorize** — Preserves original colors by mapping RGB values
6. **Render** — Creates HTML files with styled ASCII art and relies on wkhtmltoimage for conversion to image
7. **Video Assembly** — Combines image frames back into an MP4 video

## Customization

### ASCII Character Sets

Change the `ascii_string` variable in `main()` to use different characters:

```python
ascii_string = [" ",".",":","-","=","+","*","#","%","@","&"]
```

### Pixelation Level

Adjust the `final_width` parameter in `pixelate_image()` (default: 75):
- Lower values = more pixelated, faster processing
- Higher values = more detail, slower processing

### Font Size

Edit the `font-size` in the `print_ascii()` function to adjust output size (default: 32px)

## Output Files

The script creates temporary folders during processing:
- `Images/` — Extracted video frames
- `HtmlImages/` — HTML files with ASCII art
- `TextImages/` — Rendered ASCII images
- `final_[videoname].mp4` — Final output video

These folders are cleaned up and recreated with each run.

## Performance

Processing time depends on:
- Video length and resolution
- ASCII pixelation level
- System performance

## Future Improvements

- Parallel Processing — Use Python multiprocessing to convert multiple frames simultaneously for faster processing
- macOS Widget — Desktop application with drag-and-drop support for easy video conversion without using the terminal
- GUI — Interactive interface to customise of select ASCII character sets, pixelation levels, and colour palette settings in real-time

Feel free to leave comments for potential future improvements!

