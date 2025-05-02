import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_club_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        def extract(pattern):
            match = re.search(pattern, text, re.IGNORECASE)
            return match.group(1).strip() if match else None

        return {
            "Delegació": extract(r"Delegació:\s*(.+?)\n"),
            "Responsable": extract(r"Responsable:\s*(.+?)\n"),
            "Domicili": extract(r"Domicili:\s*(.+?)\n"),
            "Codi Postal": extract(r"Codi Postal:\s*(.+?)\n"),
            "Fax": extract(r"Fax:\s*(.+?)\n"),
            "Correu Electrònic": extract(r"Correu Electrònic:\s*(.+?)\n"),
            "error": None
        }
    except Exception as e:
        return {"Delegació": None, "Responsable": None, "Domicili": None, 
                "Codi Postal": None, "Fax": None, "Correu Electrònic": None,
                "error": str(e)}

def scrape_all_club_data(df_clubs):
    scraped_data_list = []
    for i, row in df_clubs.iterrows():
        print(f"📥 Scraping ({i+1}/{len(df_clubs)}): {row['Link']}")
        scraped_data_list.append(scrape_club_data(row['Link']))
    df_scraped = pd.DataFrame(scraped_data_list)
    return pd.concat([df_clubs, df_scraped], axis=1)
