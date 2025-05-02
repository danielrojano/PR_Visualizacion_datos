import requests
from bs4 import BeautifulSoup
import re
import time

categorias = ["catalana", "juvenil", "cadet", "infantil", "alevi"]
divisiones = ["divisio-honor", "preferent", "primera-divisio", "segona-divisio", "tercera-divisio"]
grupos = ["grup-unic"] + [f"bcn-gr-{i}" for i in range(1, 17)]
base_url = "https://www.fcf.cat/resultats/2425/futbol-sala/lliga-{division}-{categoria}-futbol-sala/{grupo}/jornada-20"

def scrape_players_from_all_categories():
    for categoria in categorias:
        for division in divisiones:
            for grupo in grupos:
                url = base_url.format(division=division, categoria=categoria, grupo=grupo)
                print(f"\n🔍 {categoria.upper()} - {division.upper()} - {grupo}\nURL: {url}")
                try:
                    response = requests.get(url)
                    if response.status_code != 200:
                        print(f"⚠️ No accesible ({response.status_code})")
                        continue

                    soup = BeautifulSoup(response.content, 'html.parser')
                    partidos = [a['href'] for a in soup.find_all('a', href=True) if '/acta/' in a['href']]
                    print(f"✔️ {len(partidos)} partidos")

                    jugadores = []
                    for acta in partidos:
                        try:
                            res = requests.get(acta)
                            s = BeautifulSoup(res.content, 'html.parser')
                            jugadores += [a['href'] for a in s.find_all('a', href=True) if '/jugador/' in a['href']]
                            time.sleep(0.3)
                        except Exception as e:
                            print(f"⚠️ Acta error: {acta} -> {e}")
                    print(f"🎯 Jugadores encontrados: {len(jugadores)}")
                except Exception as e:
                    print(f"❌ Error general: {e}")
