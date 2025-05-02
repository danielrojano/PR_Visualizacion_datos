import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import os

def scrape_players(jornada=20, output_path="data/jugadores_futsal_todas_ligas_jornada{jornada}.xlsx"):
    categorias = ["catalana", "juvenil", "cadet", "infantil", "alevi"]
    divisiones = ["divisio-honor", "preferent", "primera-divisio", "segona-divisio", "tercera-divisio"]
    grupos = [
        "grup-unic", "bcn-gr-1", "bcn-gr-2", "bcn-gr-3", "bcn-gr-4", "bcn-gr-5",
        "bcn-gr-6", "bcn-gr-7", "bcn-gr-8", "bcn-gr-9", "bcn-gr-10", "bcn-gr-11",
        "bcn-gr-12", "bcn-gr-13", "bcn-gr-14", "bcn-gr-15", "bcn-gr-16"
    ]

    base_url = "https://www.fcf.cat/resultats/2425/futbol-sala/lliga-{division}-{categoria}-futbol-sala/{grupo}/jornada-{jornada}"
    todos_jugadores = []

    for categoria in categorias:
        for division in divisiones:
            for grupo in grupos:
                url_resultados = base_url.format(division=division, categoria=categoria, grupo=grupo, jornada=jornada)
                print(f"\n🔍 Procesando: {categoria.upper()} - {division.upper()} - {grupo}")
                print(f"URL de resultados: {url_resultados}")

                try:
                    response = requests.get(url_resultados)
                    if response.status_code != 200:
                        print(f"⚠️  No se pudo acceder a la URL ({response.status_code}): {url_resultados}")
                        continue
                    soup = BeautifulSoup(response.content, 'html.parser')
                    enlaces_partidos = [link['href'] for link in soup.find_all('a', href=True) if '/acta/' in link['href']]
                    print(f"✔️  {len(enlaces_partidos)} partidos encontrados.")
                except Exception as e:
                    print(f"❌ Error al procesar la página de resultados: {e}")
                    continue

                enlaces_jugadores = []
                for enlace_partido in enlaces_partidos:
                    try:
                        r = requests.get(enlace_partido)
                        s = BeautifulSoup(r.content, 'html.parser')
                        nuevos = [link['href'] for link in s.find_all('a', href=True) if '/jugador/' in link['href']]
                        enlaces_jugadores += nuevos
                        time.sleep(0.3)
                    except Exception as e:
                        print(f"⚠️  Error accediendo a acta: {enlace_partido} -> {e}")

                print(f"🎯 Total enlaces a jugadores encontrados: {len(enlaces_jugadores)}")

                for i, url_jugador in enumerate(enlaces_jugadores, 1):
                    try:
                        res = requests.get(url_jugador)
                        s = BeautifulSoup(res.content, 'html.parser')
                        datos_jugador = {}

                        nombre_element = s.find('p', class_='m-0 fs-30 va-b bold')
                        if nombre_element:
                            texto = nombre_element.text.strip().title()
                            if ',' in texto:
                                apellidos_str, nombre = [part.strip() for part in texto.split(',')]
                                apellidos = [a for a in apellidos_str.split() if a.lower() != 'i']
                                apellido1 = apellidos[0] if len(apellidos) > 0 else None
                                apellido2 = apellidos[1] if len(apellidos) > 1 else None
                            else:
                                nombre = texto
                                apellido1 = apellido2 = None
                        else:
                            nombre = apellido1 = apellido2 = None

                        datos_jugador['Nombre'] = nombre
                        datos_jugador['Apellido1'] = apellido1
                        datos_jugador['Apellido2'] = apellido2
                        datos_jugador['Nombre_Completo'] = f"{apellido1 or ''} {apellido2 or ''}, {nombre or ''}".strip(', ').strip()

                        equipo_element = s.find('p', class_='mt-5 fs-20 va-t darkgrey italic')
                        if equipo_element:
                            texto_equipo = equipo_element.text.strip()
                            equipo = re.split(r'\d+a |JUVENIL|CADET|ALEVÍ|INFANTIL|BENJAMÍ|PREBENJAMÍ|SÈNIOR|VETERANS',
                                              texto_equipo, flags=re.IGNORECASE)[0].strip()
                        else:
                            equipo = None

                        datos_jugador['Equipo'] = equipo
                        datos_jugador['Categoria'] = categoria.capitalize()
                        datos_jugador['División'] = division.replace('-', ' ').capitalize()
                        datos_jugador['Grupo'] = grupo

                        goles = None
                        for div in s.find_all('div', class_='comptador'):
                            try:
                                goles = int(div.text.strip())
                                break
                            except:
                                continue

                        partidos = None
                        for div in s.find_all('div', class_='percent'):
                            sibling = div.find_next_sibling('div', class_='skill')
                            if sibling and 'Convocat' in sibling.text:
                                try:
                                    partidos = int(div.text.strip())
                                    break
                                except:
                                    continue

                        datos_jugador['Goles'] = goles
                        datos_jugador['Partidos'] = partidos
                        datos_jugador['Goles_por_partido'] = round(goles / partidos, 1) if goles is not None and partidos else None

                        todos_jugadores.append(datos_jugador)
                        print(f"🧾 [{i}] {datos_jugador['Nombre_Completo']} - Goles: {goles} - Partidos: {partidos}")
                        time.sleep(0.3)
                    except Exception as e:
                        print(f"⚠️  Error con jugador {i} ({url_jugador}): {e}")
                        continue

    os.makedirs("data", exist_ok=True)
    output_file = output_path.format(jornada=jornada)
    df = pd.DataFrame(todos_jugadores).drop_duplicates()
    df.to_excel(output_file, index=False)
    print(f"\n✅ FINALIZADO: Datos guardados en '{output_file}'")
