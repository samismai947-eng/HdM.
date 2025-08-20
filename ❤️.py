

import time


nombre = "Marileth"
base = "¡FELIZ CUMPLEAÑOS!"
msg = (base + (" " + nombre if nombre else "") + " ").upper()


ancho = 60
alto = 30
vel_linea = 0.03  


PINK = "\033[95m"
RESET = "\033[0m"

k = 0
for y in range(alto, -alto-1, -1):
    linea = []
    for x in range(-ancho, ancho+1):
        X = x / float(ancho)
        Y = y / float(alto)
        inside = (X*X + Y*Y - 1)**3 - (X*X)*(Y**3) <= 0
        if inside:
            linea.append(PINK + msg[k % len(msg)] + RESET)
            k += 1
        else:
            linea.append(" ")
    print("".join(linea).rstrip())
    time.sleep(vel_linea)
