import yt_dlp
import os
import imageio_ffmpeg
from pathlib import Path

def descargar_youtube(url, ruta_salida=None, formato='mp3'):
    """
    Descarga contenido de YouTube en formato MP3 o MP4.
    
    Args:
        url: URL del video de YouTube
        ruta_salida: Ruta donde guardar la descarga (por defecto: Descargas)
        formato: 'mp3' para audio o 'mp4' para video (por defecto: 'mp3')
    """
    # Si no se especifica ruta, usar carpeta de Descargas del usuario
    if ruta_salida is None:
        carpeta_base = "MusicaYoutube" if formato == 'mp3' else "VideosYoutube"
        ruta_salida = os.path.join(str(Path.home()), "Downloads", carpeta_base)
    
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
    
    # Obtener la ruta de ffmpeg desde imageio_ffmpeg
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # Configurar opciones según el formato
    if formato.lower() == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(ruta_salida, '%(title)s'),
            'ffmpeg_location': ffmpeg_exe,
            'quiet': False,
            'no_warnings': False,
        }
        extension = 'mp3'
    else:  # mp4
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegMerge',
            }],
            'outtmpl': os.path.join(ruta_salida, '%(title)s.%(ext)s'),
            'ffmpeg_location': ffmpeg_exe,
            'quiet': False,
            'no_warnings': False,
        }
        extension = 'mp4'
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n⬇️  Descargando en formato {formato.upper()}: {url}")
            info = ydl.extract_info(url, download=True)
            
            # Para MP4, renombrar el archivo a .mp4 si es necesario
            if formato.lower() == 'mp4':
                titulo = info['title']
                archivo_descargado = None
                
                # Buscar el archivo descargado
                for archivo in os.listdir(ruta_salida):
                    if titulo in archivo:
                        archivo_descargado = archivo
                        break
                
                if archivo_descargado and not archivo_descargado.endswith('.mp4'):
                    ruta_antigua = os.path.join(ruta_salida, archivo_descargado)
                    ruta_nueva = os.path.join(ruta_salida, f"{titulo}.mp4")
                    os.rename(ruta_antigua, ruta_nueva)
                    print(f"✓ ¡Descargado exitosamente!: {titulo}.mp4")
                else:
                    print(f"✓ ¡Descargado exitosamente!: {titulo}.mp4")
            else:
                print(f"✓ ¡Descargado exitosamente!: {info['title']}.{extension}")
            
            print(f"📁 Guardado en: {ruta_salida}")
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    print("=" * 40)
    print("  Descargador de YouTube (MP3/MP4)")
    print("=" * 40)
    
    # Menú para seleccionar formato
    print("\n📋 Elige el formato de descarga:")
    print("  1. MP3 (Solo Audio)")
    print("  2. MP4 (Video)")
    
    while True:
        try:
            opcion = input("\nIngresa tu opción (1 o 2): ").strip()
            if opcion in ['1', '2']:
                formato = 'mp3' if opcion == '1' else 'mp4'
                break
            else:
                print("❌ Opción no válida. Por favor, ingresa 1 o 2.")
        except EOFError:
            print("\n❌ Error: Entrada no disponible. Saliendo...")
            exit()
    
    # Preguntar si quiere cambiar la ruta
    ruta_defecto = os.path.join(str(Path.home()), "Downloads", 
                                "MusicaYoutube" if formato == 'mp3' else "VideosYoutube")
    print(f"\n📁 Ruta por defecto: {ruta_defecto}")
    cambiar_ruta = input("¿Deseas cambiar la ruta de descarga? (s/n): ").lower().strip()
    
    ruta_personalizada = None
    if cambiar_ruta == 's':
        ruta_personalizada = input("Ingresa la ruta completa donde descargar: ").strip()
        if not ruta_personalizada:
            ruta_personalizada = None
            print("Usando ruta por defecto.")
    
    url = input("\nIngresa la URL de YouTube: ").strip()
    
    if url:
        descargar_youtube(url, ruta_personalizada, formato)
    else:
        print("❌ URL no válida.")