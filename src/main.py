# main.py

from src.scraper_players import scrape_players
from src.scraper_clubs import scrape_clubs

def main():
    jornada = 20  # Puedes cambiar el número de jornada aquí
    print(f"\n=== SCRAPING FÚTBOL SALA - JORNADA {jornada} ===\n")

    try:
        print("📦 Scraping de jugadores...")
        scrape_players(jornada=jornada)
    except Exception as e:
        print(f"❌ Error durante el scraping de jugadores: {e}")

    try:
        print("\n🏟️ Scraping de clubes...")
        scrape_clubs()
    except Exception as e:
        print(f"❌ Error durante el scraping de clubes: {e}")

    print("\n🎉 Todo el proceso ha finalizado.")

if __name__ == "__main__":
    main()
