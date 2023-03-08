import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# from gtts import gTTS

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('何か話してください。')
            print('何か話してください。')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="ja-JP")
            command = command.lower()
            if'アレクサ'in command:
                command = command.replace('アレクサ', '')
                print(command)
    except:
            pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if '再生'in command:
        song = command.replace('再生', '')
        talk(song + '再生して')
        pywhatkit.playonyt(song)
    elif '時刻' in command:
        time = datetime.datetime.now().strftime('%I:%M,&p')
        talk('現在の時刻は' + time)
    elif '調べて' in command:
        person = command.replace('調べて', '')
        wikipedia.set_lang("ja")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif'おはよう'in command:
        talk('おはようございます。')
    elif'おやすみ'in command:
        talk('おやすみなさい。よい夢を。')
    elif'こんにちは'in command:
        talk('こんにちは。ご機嫌いかがですか？')
    elif'調子はどう'in command:
        talk('今日は調子がよいです。')
    elif'独身ですか'in command:
        talk('私は、ワイファイと結婚しています。')

    elif'joke'in command:
        talk(pyjokes.get_joke())
    else:
        talk('もう一度はなしてください。')

while True:
    run_alexa()