import subprocess
import os
import argparse
import sys

def descargar_video_twitter(tweet_url, ruta_descarga=".", formato="mp4"):
    """
    Descarga un video de Twitter usando yt-dlp.

    Args:
        tweet_url (str): La URL del tweet que contiene el video.
        ruta_descarga (str, optional): La carpeta donde se guardará el video.
                                       Por defecto, es la carpeta actual.
        formato (str, optional): Formato de salida del video (mp4, mkv, etc).
                                Por defecto es mp4.
    """
    try:
        # Asegúrate de que la ruta de descarga exista
        if not os.path.exists(ruta_descarga):
            os.makedirs(ruta_descarga)
            print(f"Directorio creado: {ruta_descarga}")

        # Comando para yt-dlp
        comando = [
            'yt-dlp',
            '-P', ruta_descarga,
            '--output', f'%(title)s.{formato}',
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            tweet_url
        ]

        print(f"Intentando descargar el video de: {tweet_url}")
        print(f"Guardando en: {os.path.abspath(ruta_descarga)}")

        # Ejecutar el comando
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proceso.communicate()

        if proceso.returncode == 0:
            print("¡Video descargado exitosamente!")
        else:
            print("Error al descargar el video.")
            print(f"Error: {stderr.decode('utf-8', errors='ignore')}")
            if "Unsupported URL" in stderr.decode('utf-8', errors='ignore'):
                print("Asegúrate de que la URL sea un tweet válido con un video.")
            elif "this tweet is protected" in stderr.decode('utf-8', errors='ignore').lower():
                print("No se pueden descargar videos de tweets protegidos sin autenticación.")
            elif "unable to download webpage" in stderr.decode('utf-8', errors='ignore').lower():
                print("Problema de red o la URL es incorrecta/inaccesible.")
            elif "no video formats found" in stderr.decode('utf-8', errors='ignore').lower():
                print("El tweet no contiene ningún video.")

    except FileNotFoundError:
        print("Error: yt-dlp no está instalado o no se encuentra en el PATH del sistema.")
        print("Por favor, instálalo con 'pip3 install yt-dlp'")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def validar_url(url):
    """Valida que la URL sea de Twitter/X."""
    return url.startswith(("https://twitter.com/", "https://x.com/"))

def main():
    parser = argparse.ArgumentParser(description='Descarga videos de Twitter/X')
    parser.add_argument('url', help='URL del tweet que contiene el video')
    parser.add_argument('-o', '--output', default='/Users/juanbautistaespino/Documents/Geminis/videos',
                      help='Carpeta donde se guardará el video (default: /Users/juanbautistaespino/Documents/Geminis/videos)')
    parser.add_argument('-f', '--format', default='mp4',
                      help='Formato de salida del video (default: mp4)')

    args = parser.parse_args()

    if not validar_url(args.url):
        print("Error: La URL debe ser de Twitter/X (comenzando con https://twitter.com/ o https://x.com/)")
        sys.exit(1)

    descargar_video_twitter(args.url, args.output, args.format)

if __name__ == "__main__":
    main()