import torch
import time
import io
from transformers import BertForSequenceClassification, BertTokenizer, AdamW, get_linear_schedule_with_warmup
import random
import requests
import pandas as pd
import speech_recognition as sr
from pydub import AudioSegment
import playsound
model = BertForSequenceClassification.from_pretrained("class_11.5.h5", num_labels=17)
model2 = BertForSequenceClassification.from_pretrained("class_10.1.h5", num_labels=73)
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')# Press Ctrl+F8 to toggle the breakpoint.
class function:
    def __init__(self, model, model2, tokenizer):
        self.model = model
        self.model2 = model2
        self.tokenizer = tokenizer
        #self.synthesize_audio = synthesize_audio
    def speech(self, text, temp=1):
        #synthesize_audio = SpeechSynthesis(session)
        token = 'QCP6FJLFgjqJKoxrYH1kdwo63f2mv18pKu6QqDGsAUsKcAGDM'
        url = 'https://voice.mcs.mail.ru/tts'
        params = {
            'encoder': 'mp3',
            'model_name': 'pavel-hifigan',
            'tempo': temp,
            'text': text  # Текст для озвучивания
        }
        # Заголовки запроса
        headers = {
            'Authorization': f'Bearer {token}',
        }
        # Отправка GET запроса с текстом в кодировке UTF-8
        response = requests.get(url, params=params, headers=headers)
        # Проверка успешности запроса
        if response.status_code == 200:
            # Получение аудио данных и сохранение их в файл
            with open('output.mp3', 'wb') as output_file:
                output_file.write(response.content)
        else:
            print(f'Ошибка {response.status_code}: {response.text}')
        audio = AudioSegment.from_file("output.mp3")
        playsound.playsound("output.mp3")
    def recognize(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Говорите...")
            recognizer.adjust_for_ambient_noise(source)  # Автоматическая настройка фонового шума
            while True:
                try:
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio, language="ru-RU")
                    print("Распознанный текст:", text)
                    break
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print(f"Произошла ошибка запроса к серверу Google: {e}")
                except KeyboardInterrupt:
                    break
        return text
    def information(self, mind2, txt, s):
        data = pd.read_csv(txt, sep=s).sample(frac=1)
        filtered_array = [item for item in data[f'{int(mind2)}'] if item != "-"]
        return filtered_array[random.randint(0, len(filtered_array)-1)]
    def mind(self, text):
        return torch.argmax(self.model(**self.tokenizer(text, return_tensors='pt'))['logits'])
    def mind2(self, text):
        return torch.argmax(self.model2(**self.tokenizer(text, return_tensors='pt'))['logits'])
phrase = ['Что ж.',
'К примеру.',
'Так сказать.',
'Например.',
'Нуу .',
'Хм, что можно сказать, допустим это.',
'Может быть, `это?',
'Пожалуй это.',
'Итак.',
'Можно сказать. допустим...',
'Конечно.',
'Безусловно.',
'Без сомнения, у меня кое-чт`о есть на ваш запрос.',
'По всей вероятности вы хотите `это.',
'Возможно.',
'Ну, что можно сказать.',
'В общем.',
'Т`ак та.']
def setup():
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    IAM_TOKEN = 't1.9euelZqSz8-WnJPMl5WLyJDKx5iTmu3rnpWay5iZy5iajMqWzZTGyc7Mk43l8_d2DlZW-e9XClR__t3z9zY9U1b571cKVH_-zef1656Vms7LnJaYyZSXlp6eyYudkZyW7_zF656Vms7LnJaYyZSXlp6eyYudkZyW.OIfr90YKbjLu3dWqt1eZjnAKuzDWt9rNg1zzM9nRIHa66zZZZyIVF3zOesO_Kbefh8ANBd4UylW84ZGtgUg0Dg'
    ID_FOLDER= 'b1gupnr4e9b4db5no68v'
    audio = AudioSegment.from_file("horse.mp3")
    f = function(model, model2, tokenizer)
    loop(f)
def loop(f):
    while True:
        start = time.time()
        playsound.playsound('бульк.mp3')
        name = f.recognize()
        a = f.mind(name)
        playsound.playsound('бульк.mp3')
        print(a)
#        if int(a) == 0 or int(a) == 1 or int(a) == 9 or int(a) == 12 or int(a) == 14 or int(a) == 13 or int(a) == 15:
#            txt = f"{random.choice(phrase)} {f.information(a, 'mind.csv', ';')}\n".rstrip()
#            print("Сгенерированный текст:",txt.rstrip())
#            f.speech(txt.rstrip())
#        else:
#            txt = f"{f.information(b, 'mind2.csv', ',')}\n".rstrip()
#            print("Сгенерированный текст:",txt.rstrip())
#            f.speech(txt.rstrip())
        match int(a):
            case 0:
                 txt = f"{f.information(a, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case 1:
                 txt = f"{f.information(a, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case 9:
                 txt = f"^{f.information(2, 'mind.csv', ';')}^".rstrip()
                 print("Сгенерированный текст:",txt.rstrip())
                 f.speech(txt, 1.2)
                 playsound.playsound("horse.mp3")
                 end = time.time()
                 print(f"{end-start}")
            case 12:
                 txt = f"{f.information(3, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case 13:
                 playsound.playsound("horse.mp3")
                 txt = f"{f.information(4, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case 14:
                 txt = f"{f.information(5, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case 15:
                 txt = f"{f.information(6, 'mind.csv', ';')}\n".rstrip()
                 f.speech(txt)
                 end = time.time()
                 print(f"{end-start}")
                 print("Сгенерированный текст:",txt.rstrip())
            case _:
                b = f.mind2(name)
                print(b)
                if int(b) != 72:
                    txt = f"{random.choice(phrase)} {f.information(b, 'mind3.csv', ',')}\n".rstrip()
                else:
                    txt = f"К сожалению я не знаю как вам ответить на вопрос, {name}, на данный момент времени..."
                print("Сгенерированный текст:",txt.rstrip())
                f.speech(txt)
                end = time.time()
                print(f"{end-start}")
        time.sleep(1)
import tkinter as tk

# Функция, которая будет выполняться при нажатии кнопки
def on_button_click():
    setup()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Создание основного окна
    root = tk.Tk()
    root.title("Пример кнопки")
    root.geometry("400x300")

    # Создание кнопки
    button = tk.Button(root, text="Начать диалог", command=on_button_click)
    button.pack()

    # Запуск цикла событий
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
