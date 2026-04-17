import gradio as gr
import torch
import base64

device = torch.device('cpu')

model_nostress, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                   model='silero_tts',
                                   language='ru',
                                   speaker='v5_cis_base_nostress',
                                   trust_repo=True)
model_nostress.to(device)


# model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
#                           model='silero_tts',
#                           language='ru',
#                           speaker='v5_cis_base',
#                           trust_repo=True)
# model.to(device)

# #!pip install -q silero-stress
# from silero_stress.simple_accentor import SimpleAccentor
# lang = 'kjh'
# accentor = SimpleAccentor(lang=lang)


def synthesize_accentor(text, speaker, sample_rate=48000):
    if not text or not text.strip():
        return None

    accentor_text = accentor(text)

    audio_tensor = model.apply_tts(text=accentor_text,
                                   speaker='kjh_karina' if speaker == 'Карина' else 'kjh_sibday',
                                   sample_rate=sample_rate)

    audio_np = audio_tensor.squeeze().cpu().numpy()

    return (sample_rate, audio_np)


def synthesize(text, speaker, sample_rate=48000):
    if not text or not text.strip():
        return None

    audio_tensor = model_nostress.apply_tts(text=text,
                                            speaker='kjh_karina' if speaker == 'Карина' else 'kjh_sibday',
                                            sample_rate=sample_rate)

    audio_np = audio_tensor.squeeze().cpu().numpy()

    return (sample_rate, audio_np)


def get_base64_of_encoded_file(filepath):
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode('utf-8')
    except Exception:
        return ""

back_base64 = get_base64_of_encoded_file("images/back.svg")
logo_base64 = get_base64_of_encoded_file("images/logo.svg")

custom_css = f"""
html {{
    background-image: url('data:image/svg+xml;base64,{back_base64}') !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
}}
body, .gradio-container {{
    background: transparent !important;
}}
html::before {{
    content: "";
    position: absolute;
    top: 20px;
    left: 20px;
    width: 200px;
    height: 100px;
    background-image: url('data:image/svg+xml;base64,{logo_base64}');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: left top;
    z-index: 1000;
    pointer-events: none;
}}
"""

demo = gr.Interface(
    fn=synthesize,
    inputs=[
        gr.Textbox(
            label="Введите текст для озвучки",
            lines=3,
            placeholder="Чылтыстар кемни? – перініп ала сурған идінҷек."
        ),
        gr.Radio(
            choices=["Сибдей", "Карина"],
            value="Сибдей",
            label="Выберите голос"
        )
    ],
    outputs=gr.Audio(label="Результат",
                     type="numpy"),
    title="Озвучка текста на хакасском языке",
    css=custom_css,
    submit_btn="Озвучить",
    clear_btn="Очистить",
)

demo.launch()
