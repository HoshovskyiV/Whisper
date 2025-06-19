# Whisper Transcription UI

This project provides a simple user interface for transcribing audio and video files using OpenAI's [Whisper](https://github.com/openai/whisper) model. It loads the highest accuracy (`large`) model and exposes a web interface that allows non-technical users to upload files and receive text transcriptions.

## Installation

1. Install Python 3.8 or later.
2. Install the required packages:

```bash
pip install openai-whisper gradio
```

The first time you run the application, the `large` model will be downloaded automatically. This may require several gigabytes of disk space and take a few minutes.

## Usage

Run the application with:

```bash
python app.py
```

A local web page will open in your browser where you can upload an audio or video file. After processing, the transcription will appear in the interface.

## Notes

- Whisper relies on `ffmpeg` to read audio from many formats. Ensure `ffmpeg` is installed and available on your system path.
- The `large` model provides the best accuracy but requires significant memory. If you encounter issues on low-resource machines, consider switching to a smaller model in `app.py`.

