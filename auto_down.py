import requests

base_url = "https://web-site-name/serie-name/{}.mp4"

for number in range(1, 53):
    url = base_url.format(number)
    filename = f"{number}.mp4"

    try:
        print(f"Downloading {filename}...")
        with requests.get(url, stream=True) as r:
            if r.status_code != 200:
                print(f"Skipped {filename} (status: {r.status_code})")
                continue

            with open(filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

        print(f"Saved {filename}")

    except Exception as e:
        print(f"Error with {filename}: {e}")
