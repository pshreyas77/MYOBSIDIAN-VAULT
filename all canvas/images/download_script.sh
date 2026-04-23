#!/bin/bash
# Wikipedia has rate limits. Run this at different times.

cd "/home/sunny77/Documents/Obsidian Vault/Philosophers Canvas/images"

# Aquinas
curl -sL -o aquinas.jpg "https://upload.wikimedia.org/wikipedia/commons/c/c7/Spinoza.jpg"
sleep 5

# Buddha  
curl -sL -o buddha.jpg "https://upload.wikimedia.org/wikipedia/commons/3/37/Buddha_in_Sarnath_Museum_%28Dhammajak_Mutra%29.jpg"
sleep 5

# Hegel
curl -sL -o hegel.jpg "https://upload.wikimedia.org/wikipedia/commons/1/1f/Georg_Wilhelm_Friedrich_Hegel_%28cropped%29.jpg"
sleep 5

# Locke
curl -sL -o locke.jpg "https://upload.wikimedia.org/wikipedia/commons/a/aa/John_Locke_by_Herman_Verelst.jpg"
sleep 5

# Spinoza
curl -sL -o spinoza.jpg "https://upload.wikimedia.org/wikipedia/commons/e/ec/Baruch_Spinoza.jpg"
sleep 5

# Wittgenstein
curl -sL -o wittgenstein.jpg "https://upload.wikimedia.org/wikipedia/commons/a/a2/Ludwig_Wittgenstein.jpg"
sleep 5

# Augustine
curl -sL -o augustine.jpg "https://upload.wikimedia.org/wikipedia/commons/e/ea/Sandro_Botticelli_-_Saint_Augustine_in_hi%E2%80%A6.jpg"
sleep 5

# Heidegger
curl -sL -o heidegger.jpg "https://upload.wikimedia.org/wikipedia/commons/2/28/Heidegger_4_%28cropped%29.jpg"

echo "Downloads complete! Check file sizes:"
ls -la *.jpg
