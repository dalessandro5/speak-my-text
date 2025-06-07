import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()

    # Opcional: configuración de velocidad y volumen
    engine.setProperty('rate', 150)     # Velocidad (por defecto ~200)
    engine.setProperty('volume', 1.0)   # Volumen (0.0 a 1.0)

    # Habla el texto
    engine.say(texto)
    engine.runAndWait()

    # Si deseas guardar el audio en archivo .mp3, descomenta esto:
    # engine.save_to_file(texto, "salida.mp3")
    # engine.runAndWait()
    # print("Archivo 'salida.mp3' guardado con éxito.")

if __name__ == "__main__":
    print("=== Conversor de Texto a Voz ===")
    texto = input("Escribe el texto que quieres escuchar: ").strip()

    if texto:
        texto_a_voz(texto)
    else:
        print("⚠️ No ingresaste ningún texto.")
