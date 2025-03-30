![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green)

# whispify  
Автоматичне створення субтитрів із будь-яких медіа.

Проста CLI-утиліта для генерування субтитрів `.srt` з аудіо- чи відеофайлів за допомогою моделі Whisper від OpenAI.

---

## 🚀 Можливості

- Підтримка форматів `.mp4`, `.mp3`, `.wav`, `.m4a`, `.webm` та ін.
- Автоматичне створення субтитрів `.srt` з таймкодами
- Підтримка розпізнавання англійської мови за замовчуванням
- Простий запуск з аргументом `-p`

---

## 🔧 Вимоги

- Python 3.8+
- Встановлений `ffmpeg` (має бути в PATH)

приклад виведення субтитрів з файлу 38_Track_38.mp4 -> [ 38_Track_38.srt ](https://github.com/yourhostel/whispify/blob/main/subs/38_Track_38.srt)


---

## 📦 Встановлення

```bash
sudo apt install ffmpeg
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📦 Встановлення (без venv)

```bash
sudo apt install ffmpeg
pip install --break-system-packages git+https://github.com/openai/whisper.git
pip install --break-system-packages ffmpeg-python
```
## ⚙️ Опційно: Підтримка GPU (CUDA)

Якщо у вас є відеокарта з підтримкою CUDA, встановіть PyTorch вручну для кращої продуктивності:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## ▶️ Використання

```bash
# За замовчуванням розпізнається англійська. 
python3 recognize.py -p path/to/audio_or_video.mp4
# Щоб змінити мову
python3 recognize.py -p path/to/video.mp4 -l uk
```

Результат буде збережено як `audio_or_video.srt`

---

## 📄 Ліцензія

MIT

