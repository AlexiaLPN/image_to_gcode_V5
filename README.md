# 🖨️ Générateur de GCODE - Tartelettes à partir d'une image

Ce projet permet de générer automatiquement du GCODE à partir d'une **image noir sur blanc** (ex: un fruit dessiné en noir sur fond blanc), et de visualiser la forme imprimée à travers une interface simple avec **Streamlit**.

---

### 📂 Votre image

- Préparer une **image au format `.jpg` ou '.png'**
- L'image doit être **noire sur fond blanc**, sans zones blanches à l'intérieur du dessin.

## ✍️ Utilisation

Dans l'application :

- Charger l'image
- Choisissez les dimensions :
  - Longueur de la tartelette
  - Hauteur du bord
  - Type de bord (bord plein, maille fine ou maille haute)
- Cliquez sur **“Générer et visualiser le GCODE”**
- Vous pouvez faire tourner la visualisation en maintenant le clic gauche appuyé et faisant bouger votre souris
- Téléchargez le fichier `.gcode` généré

## 🛠️ Dépendances

Les bibliothèques utilisées sont :

- `streamlit`
- `numpy`
- `opencv-python`
- `matplotlib`
