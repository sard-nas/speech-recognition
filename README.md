## Участники команды
- Безлепкин Даниил
- Войнов Артём
- Хусаинова Александра

### Описание
[SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - это библиотека для распознавания речи с поддержкой нескольких движков и API, онлайн и оффлайн.

### Пример использования

```python
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
	audio = recognizer.listen(source)
text = recognizer.recognize_google(audio, language="ru-RU")
print(text)
```
### Архитектура проекта
#### WEB
Для реализации используется библиотека streamlit версии 1.29.0

#### API
Для реализации используется библиотека FastAPI версии 0.87.0

#### Dependencies
Зависимости для модуля `API` описаны в файле `requirements.txt`, при запуске `Dockerfile` он парсится и подгружаются пакеты нужной версии

### Запуск Docker
```bash
cd api/ && make build && make run
```
Сервер будет запущен по адресу ```http://0.0.0.0:8080```
