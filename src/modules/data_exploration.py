def explore_club_data(df):
    print(f"🔢 Number of rows: {df.shape[0]}")
    print(f"📊 Number of columns: {df.shape[1]}")
    print("\n🧬 Data types:\n", df.dtypes)
    print(f"\n🔗 Unique links: {df['Link'].nunique()}")
    print(f"🚫 Missing 'Link': {df['Link'].isnull().sum()}")
    print(f"📎 Duplicated 'Link': {df['Link'].duplicated().sum()}")

    # Sample HTML
    import requests
    sampled_links = df['Link'].dropna().sample(n=5, random_state=42)
    for link in sampled_links:
        try:
            response = requests.get(link)
            response.raise_for_status()
            print(f"\n🌐 Link: {link}\n{response.text[:500]}")
        except Exception as e:
            print(f"⚠️ Error fetching {link}: {e}")
