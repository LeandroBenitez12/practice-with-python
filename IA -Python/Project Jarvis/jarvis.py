#IA librerias
from mimetypes import init
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json

name = "roman"#definimos nombre de variable del programa llamar
key = "AIzaSyBR8SYprtnXZM9NPE_d-D12zfQcIAOQKrI"

listener = sr.Recognizer()#reconoce la voz

engine = pyttsx3.init()#inicializamos paquete

#traemos listado de voces solo el 0 = latino
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
#funcion para pasarle un text y que nos diga lo que le pasamos
def talk(text):
    engine.say(text)
    engine.runAndWait()


def start():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)# escuchamos el microfono
            rec = listener.recognize_google(voice, language='es-ES')# utilizamos la api de google
            rec = rec.lower()
            if name in rec: #condicion que el name este dentro del texto que decimos
                rec = rec.replace(name, "")#sacamos else name para que no lo imprima
                print(rec)#imprimimos
    except:
        pass
    return rec # reornando lo que dice

def run():# lo que vamos a ejecutar
    rec = start()#rec = rec(return)
    if "reproduce" in rec: # si dice reproduce va a entrar al paquete de buscar en youtube
        music = rec.replace("reproduce", "")
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)

    elif 'cuántos suscriptores tiene' in rec:
        name_subs = rec.replace('cuántos suscriptores tiene', '')
        data = urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " tiene {:,d}".format(int(subs)) + " suscriptores!")
           
run()