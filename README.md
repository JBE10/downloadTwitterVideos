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

### Método 1: Modificar el script

1. Abre `twitterDescarga.py`
2. Modifica la variable `url_por_defecto` con la URL del tweet que quieres descargar
3. Ejecuta el script:
```bash
python3 twitterDescarga.py
```

### Método 2: Usar argumentos

```bash
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789" -o "carpeta_destino" -f "mp4"
```

### Opciones

- `-o, --output`: Carpeta donde se guardará el video (por defecto: videos_twitter)
- `-f, --format`: Formato de salida del video (por defecto: mp4)

## Ejemplos

```bash
# Descargar un video usando la URL por defecto
python3 twitterDescarga.py

# Descargar un video específico
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789"

# Especificar carpeta de destino y formato
python3 twitterDescarga.py "https://twitter.com/usuario/status/123456789" -o "mis_videos" -f "mp4"
```

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 