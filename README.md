# 📊 Scraper Fútbol Sala FCF

Este proyecto permite obtener información detallada de **jugadores** y **clubes** de fútbol sala desde la web oficial de la [Federació Catalana de Futbol (FCF)](https://www.fcf.cat/). Extrae datos desde todas las combinaciones posibles de categoría, división y grupo.

## 📁 Estructura del Proyecto

```
futsal_scraper/
├── main.py
├── requirements.txt
├── src/
│   ├── scraper_players.py
│   └── scraper_clubs.py
├── data/
│   ├── jugadores_futsal_todas_ligas_jornadaXX.xlsx
│   └── clubes_futsal.xlsx
└── README.md
```

## 🔍 ¿Qué hace el scraper?

### `scraper_players.py`
- Itera por cada categoría, división y grupo posibles.
- Accede a la jornada indicada (por defecto jornada 20).
- Extrae datos de los jugadores que han disputado partidos:
  - Nombre, apellidos, equipo
  - Categoría, división y grupo
  - Goles, partidos jugados
  - Promedio de goles por partido
- Guarda los datos en un archivo Excel:
  - `data/jugadores_futsal_todas_ligas_jornadaXX.xlsx`

### `scraper_clubs.py`
- Extrae la información de clubes registrados en la FCF. A partir de clubs.xlsx donde ya tenemos la siguiente información recopilada de la página de la deferación:
  - Nombre
  - Código
  - Localidad
  - Provincia
  - Link
- Obtiene:
  - Delegación
  - Responsable
  - Domicilio
  - Código Postal
  - Fax
  - Teléfono
- Guarda los resultados en un archivo Excel integrado con clubs.xlsx:
  - `data/clubes_futsal.xlsx`

## ⚙️ Requisitos

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```
beautifulsoup4
pandas
requests
openpyxl
```

## ▶️ Cómo usar

Ejecuta el archivo principal `main.py` para iniciar todo el proceso de scraping:

```bash
python main.py
```

> 🛠️ El número de jornada puede modificarse fácilmente dentro del archivo `main.py`.

## 📂 Archivos generados

Al finalizar, se generarán automáticamente los siguientes archivos en la carpeta `/data`:

- `jugadores_futsal_todas_ligas_jornada20.xlsx`
- `clubes_futsal.xlsx`

## 📌 Notas adicionales

- El script respeta tiempos de espera (`time.sleep`) para no saturar el servidor de la FCF.
- Se eliminan duplicados antes de exportar.
- Los nombres de los jugadores se formatean correctamente aunque solo contengan un nombre.

## 🧑‍💻 Autor

Desarrollado por Daniel Rojano Naranjo.
