import threading
import time

import keyboard
import schedule

from JogoDoBicho.models import Evento


def agendamento():
    try:
        eventos = Evento.objects.all()
        while not(keyboard.is_pressed("ctrl+c")) and (len(eventos) > 0):
            for evento in eventos:
                if evento.verificarHora():
                    evento.delete()
                time.sleep(.2)
    except:
        return

thread = threading.Thread(target=agendamento)
thread.start()