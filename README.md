# ⚽ Futsal Scraper - Federació Catalana de Futbol

Este proyecto permite realizar un scraping automatizado de **datos de clubes y jugadores** de fútbol sala desde la página oficial de la [Federació Catalana de Futbol (www.fcf.cat)](https://www.fcf.cat). El objetivo es recopilar información útil como contacto de clubes, ubicación, y datos de jugadores por categoría y jornada.

---

## 📁 Estructura del proyecto

```
futsal_scraper/
├── main.py                        # Script principal
├── modules/                      # Módulos organizados por funcionalidad
│   ├── data_loader.py            # Carga de archivo Excel de clubes
│   ├── data_exploration.py       # Análisis exploratorio básico del archivo
│   ├── club_scraper.py           # Scraping de datos de clubes
│   ├── player_scraper.py         # Scraping de datos de jugadores (por categoría y grupo)
│   └── utils.py                  # Utilidades generales (futuro uso)
├── data/
│   └── clubs.xlsx                # Archivo Excel de entrada con links de clubes
├── outputs/
│   └── scraped_data.xlsx         # Archivo de salida con datos scrapeados
└── requirements.txt              # Librerías necesarias
```

---

## 🚀 ¿Qué hace cada parte?

- `main.py`: Orquesta el proceso completo:
  - Carga el Excel de clubes.
  - Muestra estadísticas del archivo.
  - Hace scraping de los datos de contacto del club.
  - Lanza scraping de datos de jugadores (por categoría, división y grupo).

- `modules/club_scraper.py`: Extrae datos como:
  - Delegació, Responsable, Domicili, Codi Postal, Fax, Correu Electrònic.

- `modules/player_scraper.py`: Extrae URLs de jornadas y actas de partidos para múltiples combinaciones:
  - Categorías: Aleví, Infantil, Cadet, Juvenil, Senior.
  - Divisiones: Honor, Preferent, Primera, Segona, Tercera.
  - Grupos: Grup-únic, BCN-gr-1 a BCN-gr-16.

---

## 🛠️ Requisitos

Python 3.8 o superior.

Instala los paquetes necesarios:

```bash
pip install -r requirements.txt
```

---

## 📦 Ejecución

Asegúrate de tener `data/clubs.xlsx` con una columna llamada `Link` que contenga las URLs a las páginas de clubes de la FCF.

Después, ejecuta:

```bash
python main.py
```

Los resultados se guardarán automáticamente en `outputs/scraped_data.xlsx`.

---

## 🧠 Notas

- Las solicitudes están limitadas a 1 cada 0.3 segundos por cortesía con el servidor web.
- Si un jugador tiene solo un nombre, no se intenta dividirlo en apellidos.
- El scraping de jugadores actualmente lista los enlaces de jornadas disponibles, pero puedes expandirlo para recolectar más estadísticas u otros datos por acta.

---

## 📄 Licencia

MIT License. Proyecto educativo y sin ánimo de lucro.

---

## ✍️ Autor

**Daniel Rojano Naranjo**  
Proyecto para recopilación automatizada de datos de fútbol sala en Cataluña.

