import random

TRANSLATIONS = {
    "Hindi": "नमस्ते दुनिया",
    "Bengali": "হ্যালো ওয়ার্ল্ড",
    "Tamil": "ஹலோ வேர்ல்ட்",
    "Telugu": "హలో వరల్డ్",
    "Marathi": "हॅलो वर्ल्ड",
    "Gujarati": "હેલો વર્લ્ડ",
    "Kannada": "ಹೆಲೋ ವರ್ಲ್ಡ್",
    "Malayalam": "ഹലോ വേൾഡ്",
    "Punjabi": "ਹੈਲੋ ਵਰਲਡ",
    "Urdu": "ہیلو ورلڈ",
    "Odia": "ହେଲୋ ୱର୍ଲ୍ଡ",
    "Sanskrit": "नमस्ते जगत्",
}


def main() -> None:
    print("HELLO WORLD")
    print()

    choices = random.sample(list(TRANSLATIONS.items()), 5)
    for language, translation in choices:
        print(f"{language}: {translation}")


if __name__ == "__main__":
    main()
