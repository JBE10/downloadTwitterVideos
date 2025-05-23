# DownloadTwitterVideos

Un script en Python para descargar videos de Twitter/X de forma sencilla.

## Características

- Descarga videos de tweets públicos
- Soporta URLs de twitter.com y x.com
- Permite especificar la carpeta de destino
- Permite elegir el formato de salida
- Descarga la mejor calidad disponible

## Requisitos

- Python 3.x
- yt-dlp

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/JBE10/downloadTwitterVideos.git
cd downloadTwitterVideos
```

2. Instala yt-dlp:
```bash
pip install yt-dlp
```

## Uso

El script se usa desde la terminal. La URL del tweet es obligatoria:

```bash
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789"
```

### Opciones

- `-o, --output`: Carpeta donde se guardará el video (por defecto: /Users/juanbautistaespino/Documents/Geminis/videos)
- `-f, --format`: Formato de salida del video (por defecto: mp4)

### Ejemplos

```bash
# Descargar un video (se guardará en la carpeta por defecto)
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789"

# Especificar carpeta de destino
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789" -o "/ruta/a/tu/carpeta"

# Especificar formato de salida
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789" -f "mp4"

# Especificar carpeta y formato
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789" -o "/ruta/a/tu/carpeta" -f "mp4"
```

## Notas

- El script creará automáticamente la carpeta de destino si no existe
- Los videos se guardan con el título del tweet como nombre del archivo
- Se descarga la mejor calidad disponible del video

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 