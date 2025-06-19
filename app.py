import gradio as gr
import whisper

model = whisper.load_model("large")


def transcribe(file):
    """Transcribe an audio or video file using Whisper."""
    result = model.transcribe(file)
    return result.get("text", "")


ui = gr.Interface(
    fn=transcribe,
    inputs=gr.File(label="Upload audio or video"),
    outputs=gr.Textbox(label="Transcription"),
    title="Whisper Transcriber",
    description="Upload an audio or video file to transcribe it using OpenAI's Whisper 'large' model.",
)

if __name__ == "__main__":
    ui.launch()
