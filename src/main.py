from modules.data_loader import load_club_data
from modules.data_exploration import explore_club_data
from modules.club_scraper import scrape_all_club_data
from modules.player_scraper import scrape_players_from_all_categories

def main():
    df_clubs = load_club_data("data/clubs.xlsx")
    if df_clubs is None:
        return

    explore_club_data(df_clubs)

    df_scraped = scrape_all_club_data(df_clubs)
    df_scraped.to_excel("outputs/scraped_data.xlsx", index=False)

    scrape_players_from_all_categories()

if __name__ == "__main__":
    main()
