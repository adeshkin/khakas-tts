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

.vk-link {{
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: #0077FF;
    color: white !important;
    padding: 10px 20px;
    border-radius: 12px;
    text-decoration: none !important;
    font-weight: 600;
    font-size: 16px;
    font-family: system-ui, -apple-system, sans-serif;
    box-shadow: 0 4px 12px rgba(0, 119, 255, 0.3);
    z-index: 1000;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.vk-link:hover {{
    background-color: #005ce6;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 119, 255, 0.4);
}}
"""

vk_link_html = '''
<a href="https://vk.com/translate_khakas" target="_blank" class="vk-link">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12C2 17.523 6.477 22 12 22C17.523 22 22 17.523 22 12C22 6.477 17.523 2 12 2ZM16.892 14.88C17.202 15.187 17.502 15.5 17.8 15.82C17.92 15.948 18.046 16.082 18.17 16.216C18.423 16.488 18.665 16.746 18.847 16.94C18.995 17.098 19.168 17.391 18.956 17.652C18.815 17.824 18.528 17.892 18.324 17.892H16.141C15.86 17.892 15.65 17.838 15.485 17.747C15.297 17.643 15.127 17.472 14.933 17.265C14.717 17.034 14.498 16.786 14.281 16.541C14.07 16.302 13.864 16.069 13.666 15.882C13.435 15.663 13.235 15.553 13 15.553C12.9 15.553 12.805 15.584 12.71 15.637C12.441 15.786 12.316 16.126 12.316 16.598V17.327C12.316 17.657 12.224 17.79 12.112 17.838C11.914 17.923 11.602 17.892 11.168 17.892C10.024 17.892 9.006 17.648 8.163 17.159C7.215 16.609 6.425 15.79 5.826 14.733C4.606 12.58 3.866 9.877 3.866 9.605C3.866 9.387 3.931 9.278 4.025 9.213C4.12 9.148 4.28 9.148 4.49 9.148H6.673C6.887 9.148 7.025 9.167 7.126 9.224C7.227 9.282 7.307 9.39 7.351 9.516C7.382 9.604 7.502 10.005 7.7 10.518C7.994 11.277 8.354 12.115 8.71 12.784C8.945 13.226 9.176 13.567 9.356 13.738C9.554 13.926 9.774 14.02 10.002 14.02C10.145 14.02 10.278 13.982 10.4 13.886C10.655 13.684 10.741 13.256 10.741 12.756V10.292C10.741 9.89 10.686 9.65 10.603 9.539C10.516 9.424 10.378 9.363 10.224 9.34C10.126 9.325 10.158 9.222 10.231 9.17C10.428 9.031 10.82 8.971 11.378 8.971H11.536C12.029 8.971 12.193 9.006 12.316 9.053C12.52 9.13 12.607 9.28 12.607 9.571V12.748C12.607 13.064 12.668 13.22 12.744 13.298C12.836 13.393 13.02 13.435 13.29 13.435C13.511 13.435 13.784 13.332 14.103 13.082C14.475 12.79 14.898 12.32 15.289 11.758C15.69 11.182 16.024 10.457 16.208 10.021C16.273 9.866 16.347 9.742 16.42 9.655C16.513 9.544 16.638 9.489 16.828 9.489H19.011C19.261 9.489 19.467 9.508 19.575 9.569C19.704 9.642 19.78 9.771 19.757 9.948C19.705 10.344 19.34 11.085 18.825 11.892C18.423 12.522 17.962 13.155 17.514 13.676C17.3 13.925 17.07 14.161 16.892 14.341C16.711 14.524 16.619 14.619 16.619 14.73C16.619 14.841 16.72 14.945 16.892 14.88Z" fill="currentColor"/>
    </svg>
    ВКонтакте
</a>
'''

demo = gr.Interface(
    fn=synthesize,
    description=vk_link_html,
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
