import gradio as gr
import torch

device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language='ru',
                          speaker='v5_cis_base_nostress',
                          trust_repo=True)
model.to(device)


def synthesize(text, speaker, sample_rate=48000):
    if not text or not text.strip():
        return None

    audio_tensor = model.apply_tts(text=text,
                                   speaker=speaker,
                                   sample_rate=sample_rate)

    audio_np = audio_tensor.squeeze().cpu().numpy()

    return (sample_rate, audio_np)


demo = gr.Interface(
    fn=synthesize,
    inputs=[
        gr.Textbox(
            label="Введите текст для озвучки",
            lines=3,
            placeholder="Чылтыстар кемни? – перініп ала сурған идінҷек."
        ),
        gr.Radio(
            choices=["kjh_sibday", "kjh_karina"],
            value="kjh_sibday",
            label="Выберите голос"
        )
    ],
    outputs=gr.Audio(label="Результат",
                     type="numpy"),
    title="Простая озвучка текста"
)

demo.launch()
