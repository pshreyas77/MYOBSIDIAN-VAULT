#!/usr/bin/env python3
"""
Download 35 philosopher images from Wikimedia Commons
Run this script to download all images
"""

import subprocess
import os
import time

# Philosopher images with Wikimedia Commons Special:FilePath URLs
philosophers = [
    ("thales", "https://commons.wikimedia.org/wiki/Special:FilePath/Thales.jpg"),
    ("anaximander", "https://commons.wikimedia.org/wiki/Special:FilePath/Anaximander.jpg"),
    ("pythagoras", "https://commons.wikimedia.org/wiki/Special:FilePath/Pythagoras_Bust_Vatican_Museum.jpg"),
    ("heraclitus", "https://commons.wikimedia.org/wiki/Special:FilePath/Heraclitus_in_Thomas_Stanley_History_of_Philosophy.jpg"),
    ("parmenides", "https://commons.wikimedia.org/wiki/Special:FilePath/Parmenides.jpg"),
    ("buddha", "https://commons.wikimedia.org/wiki/Special:FilePath/Seokguram_Buddha.JPG"),
    ("mahavira", "https://commons.wikimedia.org/wiki/Special:FilePath/12_century_Mahavir.jpg"),
    ("shankara", "https://commons.wikimedia.org/wiki/Special:FilePath/Adi_Shankara.jpg"),
    ("nagarjuna", "https://commons.wikimedia.org/wiki/Special:FilePath/Nagarjuna.JPG"),
    ("laozi", "https://commons.wikimedia.org/wiki/Special:FilePath/Laozi.jpg"),
    ("mencius", "https://commons.wikimedia.org/wiki/Special:FilePath/Mencius.jpg"),
    ("mozi", "https://commons.wikimedia.org/wiki/Special:FilePath/Mozi.jpg"),
    ("hanfeizi", "https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Han_Fei.jpg"),
    ("zoroaster", "https://commons.wikimedia.org/wiki/Special:FilePath/Zoroaster_1.jpg"),
    ("avicenna", "https://commons.wikimedia.org/wiki/Special:FilePath/Avicenna_1271b.jpg"),
    ("averroes", "https://commons.wikimedia.org/wiki/Special:FilePath/Ibn_Rushd.jpg"),
    ("ghazali", "https://commons.wikimedia.org/wiki/Special:FilePath/Al-Ghazali.jpg"),
    ("ibn_arabi", "https://commons.wikimedia.org/wiki/Special:FilePath/Ibn_Arabi.jpg"),
    ("augustine", "https://commons.wikimedia.org/wiki/Special:FilePath/Augustine_of_Hippo.jpg"),
    ("aquinas", "https://commons.wikimedia.org/wiki/Special:FilePath/Saint_Thomas_Aquinas.jpg"),
    ("machiavelli", "https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Niccolò_Machiavelli_by_Santi_di_Tito.jpg"),
    ("francis_bacon", "https://commons.wikimedia.org/wiki/Special:FilePath/Francis_Bacon.jpg"),
    ("spinoza", "https://commons.wikimedia.org/wiki/Special:FilePath/Spinoza.jpg"),
    ("leibniz", "https://commons.wikimedia.org/wiki/Special:FilePath/Gottfried_Wilhelm_von_Leibniz.jpg"),
    ("locke", "https://commons.wikimedia.org/wiki/Special:FilePath/JohnLocke.png"),
    ("hume", "https://commons.wikimedia.org/wiki/Special:FilePath/David_Hume.jpg"),
    ("rousseau", "https://commons.wikimedia.org/wiki/Special:FilePath/Jean-Jacques_Rousseau_(painted_portrait).jpg"),
    ("hegel", "https://commons.wikimedia.org/wiki/Special:FilePath/Hegel.jpg"),
    ("mill", "https://commons.wikimedia.org/wiki/Special:FilePath/Stuart_Mill_G_F_Watts.jpg"),
    ("kierkegaard", "https://commons.wikimedia.org/wiki/Special:FilePath/Kierkegaard_portrait.jpg"),
    ("wittgenstein", "https://commons.wikimedia.org/wiki/Special:FilePath/35._Portrait_of_Wittgenstein.jpg"),
    ("heidegger", "https://commons.wikimedia.org/wiki/Special:FilePath/Heidegger_Martin.jpg"),
    ("sartre", "https://commons.wikimedia.org/wiki/Special:FilePath/Jean-Paul_Sartre_FP.JPG"),
    ("rawls", "https://commons.wikimedia.org/wiki/Special:FilePath/John_Rawls_(1971_photo_portrait).jpg"),
    ("simone_de_beauvoir", "https://commons.wikimedia.org/wiki/Special:FilePath/Simone_de_Beauvoir_1967_(cropped).jpg"),
]

def download_file(name, url):
    """Download a file using wget with proper headers"""
    output_file = f"{name}.jpg"
    
    # Check if file already exists
    if os.path.exists(output_file):
        size = os.path.getsize(output_file)
        if size > 1000:
            return True, f"Already exists: {size} bytes"
    
    try:
        # Use wget with proper user agent and follow redirects
        result = subprocess.run([
            'wget', '-q', '--timeout=30', '--tries=3',
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            '-O', output_file, url
        ], capture_output=True, text=True)
        
        if result.returncode == 0 and os.path.exists(output_file):
            size = os.path.getsize(output_file)
            if size > 1000:
                return True, f"Downloaded: {size} bytes"
            else:
                os.remove(output_file)
                return False, "File too small"
        else:
            return False, f"wget failed: {result.stderr[:100]}"
    except Exception as e:
        return False, str(e)[:100]

def main():
    print("=" * 60)
    print("Downloading 35 Philosopher Images from Wikimedia Commons")
    print("=" * 60)
    print()
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    success = 0
    failed = 0
    failed_list = []
    
    for i, (name, url) in enumerate(philosophers, 1):
        print(f"[{i:2d}/35] {name:25s} ... ", end='', flush=True)
        
        ok, msg = download_file(name, url)
        
        if ok:
            print(f"✅ {msg}")
            success += 1
        else:
            print(f"❌ {msg}")
            failed += 1
            failed_list.append((name, url))
        
        # Small delay to be nice to Wikimedia servers
        time.sleep(0.5)
    
    print()
    print("=" * 60)
    print(f"Download Results:")
    print(f"  Success: {success}/35")
    print(f"  Failed:  {failed}/35")
    print("=" * 60)
    
    if failed_list:
        print("\nFailed downloads:")
        for name, url in failed_list:
            print(f"  - {name}: {url}")
        print("\nYou may need to manually download these images.")
    
    if success == 35:
        print("\n🎉 All images downloaded successfully!")
    
    return success == 35

if __name__ == "__main__":
    main()
