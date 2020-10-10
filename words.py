from googletrans import Translator
import wordfreq

lang_dict = {'Arabic': 'ar', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Chinese': 'zh', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Finnish': 'fi', 'French': 'fr', 'German': 'de', 'Greek': 'el', 'Hebrew': 'he', 'Hindi': 'hi', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malay': 'ms', 'Norwegian': 'nb', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Serbian': 'sr', 'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr', 'Ukrainian': 'uk'}
translator = Translator()
# with open("list.txt") as f:
#     r = f.read().split("\n")
#     r = [list(filter(lambda x: x!="", l.split(" "))) for l in r]
#     r = [l[0:2] for l in r]
#     for l in r:
#         lang_dict[l[0]] = l[1]
#     print(lang_dict)

def get_word(language):
    lang = lang_dict[language]
    lang_word = wordfreq.random_words(lang, nwords=1)
    eng_word = translator.translate(lang_word, src=lang, dest='en').text
    if len(lang_word) > 10 or len(eng_word) > 10:
        lang_word, eng_word = get_word(language)

    return lang_word, eng_word
