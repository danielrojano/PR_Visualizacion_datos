# 📊 Scraper Fútbol Sala FCF

Este proyecto permite obtener información detallada de **jugadores** y **clubes** de fútbol sala desde la web oficial de la [Federació Catalana de Futbol (FCF)](https://www.fcf.cat/). Extrae datos desde todas las combinaciones posibles de categoría, división y grupo.

---

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
│   ├── clubes_futsal.xlsx
│   └── codigos.xlsx
└── README.md
```

---

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
- Extrae la información de clubes registrados en la FCF, a partir de un Excel inicial `clubs.xlsx` donde ya se ha recopilado esta información básica desde la web:
  - Nombre
  - Código
  - Localidad
  - Provincia
  - Link a la ficha del club
- Luego visita la ficha de cada club y obtiene datos detallados:
  - Delegación
  - Responsable
  - Domicilio
  - Código Postal
  - Fax
  - Teléfono
- Exporta toda la información integrada en:
  - `data/clubes_futsal.xlsx`

---

## 📄 Archivo adicional: `codigos.xlsx`

Además de los archivos generados por scraping, el proyecto incluye un archivo adicional importante:

- `data/codigos.xlsx`

Este archivo contiene el listado de **equipos inscritos para la temporada 2024-2025**, obtenido a partir de las circulares oficiales publicadas por la FCF:

- [Agrupacions provisionals - 1](https://www.fcf.cat/noticia/les-primeres-agrupacions-provisionals-de-futbol-sala-per-a-la-temporada-2024-2025/17/07/2024)
- [Segones divisions](https://www.fcf.cat/noticia/les-agrupacions-de-les-segones-divisions-de-futbol-sala-per-a-la-temporada-2024-2025/19/07/2024)
- [Agrupacions provisionals - 2](https://www.fcf.cat/noticia/les-darreres-agrupacions-provisionals-de-futbol-sala-per-a-la-temporada-2024-2025/17/09/2024)

Este archivo permite **mapear el nombre del equipo** que aparece en los resultados de partidos con su **código oficial**, y a partir de ahí enlazarlo con los datos detallados del club extraídos por el scraper (`clubes_futsal.xlsx`). No se usa directamente en el código, pero es esencial para hacer análisis cruzados posteriores.

---

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

---

## ▶️ Cómo usar

Ejecuta el archivo principal `main.py` para iniciar todo el proceso de scraping:

```bash
python main.py
```

> 🛠️ El número de jornada puede modificarse fácilmente dentro del archivo `main.py`.

---

## 📂 Archivos generados

Al finalizar, se generarán automáticamente los siguientes archivos en la carpeta `/data`:

- `jugadores_futsal_todas_ligas_jornada20.xlsx`
- `clubes_futsal.xlsx`
- (y se conserva como fuente auxiliar: `codigos.xlsx`)

---

## 📌 Notas adicionales

- El script respeta tiempos de espera (`time.sleep`) para no saturar el servidor de la FCF.
- Se eliminan duplicados antes de exportar.
- Los nombres de los jugadores se formatean correctamente aunque solo contengan un nombre.
- El mapeo de nombres de equipos con códigos oficiales debe hacerse con `codigos.xlsx`.

---

## 🧑‍💻 Autor

Desarrollado por **Daniel Rojano Naranjo**.

> 📬 ¿Tienes sugerencias o mejoras? ¡Abre un issue o pull request!
