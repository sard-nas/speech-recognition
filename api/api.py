import speech_recognition as sr
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
	return {"message": "Распознавание речи"}


@app.get("/record")
async def record_voice():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		audio = recognizer.listen(source, timeout=5.0)
	try:
		text = recognizer.recognize_google(audio, language="ru-RU")
		return {"text": text}
	except sr.UnknownValueError:
		return {"error": "Речь не распознана"}
	except BaseException as error:
		return {"error": f"Неизвестная ошибка: error"}


