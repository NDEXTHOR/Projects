# Projects

Nota: El descargador lo hizo copilot en modo agente, hasta le puedes pedir que te haga un .exe

# Projects - Operador de matrices

El operador es bastante basico, solo hace sumas, resas y multiplicaciones, algo que se debe tener en cuenta es que no tiene el mejor formato, no puestra procedimiento o algo parecido y no cuenta con validaciones, pero en si haces las operaciones correctamente

# Projects - Descargador de YouTube

## 📥 Descargador de YouTube (MP3/MP4)

Descarga videos de YouTube en formato **MP3** (solo audio) o **MP4** (video completo).

### Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 🚀 Instalación rápida

```bash
# 1. Clonar o descargar el repositorio
git clone <tu-repositorio-url>
cd Projects

# 2. Instalar las dependencias
pip install -r requirements.txt
```

### 📝 Uso

```bash
python DescargadorYoutube.py
```

**Pasos:**
1. Selecciona formato: `1` para MP3 o `2` para MP4
2. Indica si cambias la ruta de descarga (opcional)
3. Pega la URL de YouTube
4. ¡Listo! Se descargará automáticamente

### 📂 Rutas por defecto

- **MP3**: `Descargas/MusicaYoutube`
- **MP4**: `Descargas/VideosYoutube`

### ⚙️ Dependencias

Están en `requirements.txt`:
- `yt-dlp` - Descargador de YouTube
- `imageio-ffmpeg` - Herramienta para procesar audio/video

### 🔧 Solución de problemas

**Error "ModuleNotFoundError":**
```bash
pip install -r requirements.txt
```

**FFmpeg no encontrado:**
```bash
pip install --upgrade imageio-ffmpeg
```

### 📌 Notas

- Requiere conexión a Internet
- Respeta derechos de autor
- FFmpeg se instala automáticamente