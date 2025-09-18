import whisper
import os

# Вхідна і вихідна папки
input_dir = "media/unit1"
output_dir = "text/unit1"

# Створюємо папку для текстів, якщо її ще нема
os.makedirs(output_dir, exist_ok=True)

# Завантажуємо модель Whisper
model = whisper.load_model("base")

# Перебір файлів у вхідній папці
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".wma"):
        input_path = os.path.join(input_dir, filename)
        basename = os.path.splitext(filename)[0]
        txt_output = os.path.join(output_dir, f"{basename}.txt")

        print(f"🎧 Обробляю: {filename}")

        # Розпізнавання
        result = model.transcribe(input_path)

        # Вивід у консоль
        print(result["text"])

        # Збереження у .txt з тим же ім’ям
        with open(txt_output, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"✅ Збережено: {txt_output}")
