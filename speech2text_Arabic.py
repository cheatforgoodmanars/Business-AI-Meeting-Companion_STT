import torch 
from transformers import pipeline
import gradio as gr 

#
def transcript_audio(audio_file):
    #
    pipe = pipeline(
        "automatic-speech-recognition",
        model="jonatasgrosman/wav2vec2-large-xlsr-53-arabic",
        chunk_length_s=30,
    )

    #
    result = pipe(audio_file, batch_size=8)["text"]
    return result

#
audio_input = gr.Audio(sources="upload", type='filepath') #
output_text = gr.Textbox() #

iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, outputs=output_text, 
                     title="تطبيق النسخ الصوتي",
                     description="إرفع الملف الصوتي هنا")
# Launch the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860)