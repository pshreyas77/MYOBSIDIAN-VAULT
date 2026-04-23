#!/usr/bin/env python3
import time
import urllib.request
import os

os.chdir("/home/sunny77/Documents/Obsidian Vault/Philosophers Canvas/images")

images = {
    "aquinas": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Spinoza.jpg",
    "buddha": "https://upload.wikimedia.org/wikipedia/commons/3/37/Buddha_in_Sarnath_Museum_%28Dhammajak_Mutra%29.jpg",
    "hegel": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Georg_Wilhelm_Friedrich_Hegel_%28cropped%29.jpg",
    "locke": "https://upload.wikimedia.org/wikipedia/commons/a/aa/John_Locke_by_Herman_Verelst.jpg",
    "spinoza": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Baruch_Spinoza.jpg",
    "wittgenstein": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Ludwig_Wittgenstein.jpg",
    "augustine": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Augustine_of_Hippo2.jpg",
    "heidegger": "https://upload.wikimedia.org/wikipedia/commons/2/28/Heidegger_4_%28cropped%29.jpg",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

downloaded = []
failed = []

for name, url in images.items():
    try:
        print(f"Downloading {name}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            # Check if it's actually an image
            if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                with open(f"{name}.jpg", 'wb') as f:
                    f.write(data)
                downloaded.append(name)
                print(f"  ✓ {name} downloaded")
            else:
                failed.append(name)
                print(f"  ✗ {name} - not an image")
    except Exception as e:
        failed.append(name)
        print(f"  ✗ {name} - {str(e)[:50]}")
    time.sleep(45)  # Wait 45 seconds between requests

print(f"\nDownloaded: {downloaded}")
print(f"Failed: {failed}")
