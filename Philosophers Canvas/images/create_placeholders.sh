#!/bin/bash
cd "/home/sunny77/Documents/Obsidian Vault/Philosophers Canvas/images"

# List of philosophers needing images
philosophers=(
  "thales:Thales of Miletus"
  "anaximander:Anaximander"
  "pythagoras:Pythagoras"
  "heraclitus:Heraclitus"
  "parmenides:Parmenides"
  "buddha:Siddhartha Gautama"
  "mahavira:Mahavira"
  "shankara:Adi Shankaracharya"
  "nagarjuna:Nagarjuna"
  "laozi:Laozi"
  "mencius:Mencius"
  "mozi:Mozi"
  "hanfeizi:Han Feizi"
  "zoroaster:Zoroaster"
  "avicenna:Avicenna"
  "averroes:Averroes"
  "ghazali:Al-Ghazali"
  "ibn_arabi:Ibn Arabi"
  "aquinas:St. Thomas Aquinas"
  "augustine:St. Augustine"
  "machiavelli:Machiavelli"
  "francis_bacon:Francis Bacon"
  "spinoza:Baruch Spinoza"
  "leibniz:Gottfried Leibniz"
  "locke:John Locke"
  "hume:David Hume"
  "rousseau:Jean-Jacques Rousseau"
  "mill:John Stuart Mill"
  "kierkegaard:Søren Kierkegaard"
  "hegel:Georg Hegel"
  "wittgenstein:Ludwig Wittgenstein"
  "heidegger:Martin Heidegger"
  "sartre:Jean-Paul Sartre"
  "rawls:John Rawls"
  "simone:Simone de Beauvoir"
)

# Create images
for phil in "${philosophers[@]}"; do
  IFS=':' read -r filename name <<< "$phil"
  convert -size 400x500 xc:lightblue \
    -pointsize 30 -fill black -gravity center \
    -annotate +0+0 "$name\n\n📷\n\n(Image Placeholder)" \
    "${filename}.jpg" 2>/dev/null && echo "Created: ${filename}.jpg" || echo "Failed: ${filename}"
done

echo "Done!"
