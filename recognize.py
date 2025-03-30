import whisper
import argparse
import os

# Аргументи командного рядка
parser = argparse.ArgumentParser(description="Генератор субтитрів за допомогою Whisper")
parser.add_argument("-p", "--path", required=True, help="Вхідний аудіо- або відеофайл (mp3, wav, mp4 тощо)")
parser.add_argument("-l", "--lang", default="en", choices=["ru", "uk", "en"], help="Мова для розпізнавання (ru, uk, en)")
args = parser.parse_args()

input_path = args.path
language = args.lang
basename = os.path.splitext(os.path.basename(input_path))[0]

# Папка для збереження субтитрів
output_dir = "subs"
os.makedirs(output_dir, exist_ok=True)

srt_output = os.path.join(output_dir, f"{basename}.srt")

# Завантаження моделі
model = whisper.load_model("base")

# Розпізнавання мови
result = model.transcribe(input_path, language=language)

# Вивід тексту в термінал
print(result["text"])

# Збереження субтитрів у форматі .srt
with open(srt_output, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result['segments']):
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()

        def format_time(t):
            h = int(t // 3600)
            m = int((t % 3600) // 60)
            s = int(t % 60)
            ms = int((t - int(t)) * 1000)
            return f"{h:02}:{m:02}:{s:02},{ms:03}"

        f.write(f"{i+1}\n")
        f.write(f"{format_time(start)} --> {format_time(end)}\n")
        f.write(f"{text}\n\n")

print(f"✅ Субтитри збережено у: {srt_output}")

