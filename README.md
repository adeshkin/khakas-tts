---
title: Синтез речи для хакасского языка
emoji: 👀
colorFrom: purple
colorTo: yellow
sdk: gradio
sdk_version: 6.12.0
app_file: app.py
pinned: false
---

# Синтез речи для хакасского языка

## О проекте
Данный сайт представляет собой веб-интерфейс для синтеза хакасской речи (Text-to-Speech). Встроенные модели позволяют преобразовывать написанный текст в аудио с естественным звучанием. 

В проекте доступны два голоса: **Карина** и **Сибдей**. Дикторы записали свои голоса весной 2025 года. На основе этих записей компания [Silero](https://silero.ai/) обучила акустические модели. Подробнее о процессе и технологиях можно прочитать в статье [«Обучение TTS моделей» на Habr](https://habr.com/ru/articles/968988/).

## Цитирование
Авторы моделей просят использовать следующее цитирование при упоминании или использовании их разработок:
```bibtex
@misc{Silero Models,
  author = {Silero Team},
  title = {Silero Models: pre-trained text-to-speech models made embarrassingly simple},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/snakers4/silero-models}},
  commit = {insert_some_commit_here},
  email = {hello@silero.ai}
}
```

## To-Do List (Планы по развитию)
- [ ] Анализ других моделей синтеза и генерации речи (Gemini и другие).
- [ ] Добавить модели из репозитория [khakas-text-to-speech](https://github.com/adeshkin/khakas-text-to-speech).
- [ ] Разобраться, нужна ли отдельная модель постановки ударений (сейчас в коде `app.py` закомментирована).
- [ ] Исследовать создание экранной читалки (NVDA и т.п.) — изучить [статью на Habr](https://habr.com/ru/articles/981992/).
- [ ] Voice cloning — исследовать, будет ли работать клонирование голоса для хакасского языка на базе [OmniVoice](https://github.com/k2-fsa/OmniVoice).
- [ ] Изучить [руководство от сообщества](https://github.com/kod-odin/lang-tasks/wiki/6.-Как-создать-синтезатор-речи) по созданию синтезатора речи.
- [ ] Изучить работу ассистента [Irene-Voice-Assistant](https://github.com/janvarev/Irene-Voice-Assistant) для возможных интеграций.
- [ ] Добавить ссылки на сообщество ВКонтакте.
- [ ] Добавить раздел информации (Авторы проекта, контактные данные и т.п.).
- [ ] Добавить счетчик посещений посетителей на сайт.
- [ ] Написать инструкцию для сообщества по созданию аналогичного сайта.
