import os
import sentry_sdk

# Налаштування Sentry 
sentry_sdk.init(
    dsn=os.getenv("https://2c99667b160fa2b54e0d002c4eef2bf9@o4511294715396096.ingest.de.sentry.io/4511294867046480"),
    traces_sample_rate=1.0,
)

def count_vowels(text: str) -> int:
    if not text:
        raise ValueError("Текст порожній")
    
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    try:
        user_input = input("Введіть текст: ")
        result = count_vowels(user_input)
        print(f"Кількість голосних: {result}")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Помилка: {e}")
