# 🏠 Galerie Photos - Appartement à Louer

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://saumon.github.io/loc-appart/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

Une galerie photo moderne et responsive pour présenter un appartement à louer. Site statique optimisé pour GitHub Pages avec une interface élégante compatible desktop et mobile.

## 🌟 Démonstration

**[🚀 Voir le site en live](https://saumon.github.io/loc-appart/)**

## ✨ Fonctionnalités

### 🎨 Interface Moderne

- **Design responsive** adapté à tous les écrans (desktop, tablette, mobile)
- **Interface élégante** avec palette de couleurs professionnelle
- **Animations fluides** et transitions CSS optimisées
- **Header attractif** avec titre et description
- **Favicon personnalisé** avec icône maison 🏠

### 🖼️ Galerie Photo Avancée

- **37 photos haute qualité** de l'appartement
- **Grille adaptive** qui s'ajuste automatiquement à la taille d'écran
- **Cartes photo** avec effets de hover et overlay informatif
- **Lazy loading** pour des performances optimales
- **Thumbnails optimisés** pour un chargement rapide

### 🔍 Lightbox Interactive

- **Navigation intuitive** avec boutons précédent/suivant
- **Compteur d'images** (ex: 1/37)
- **Gestes tactiles** pour naviguer sur mobile (swipe gauche/droite)
- **Raccourcis clavier** :
  - `←` / `→` : Navigation entre les images
  - `Échap` : Fermer la lightbox
- **Fermeture multiple** : clic extérieur, bouton X, ou touche Échap
- **Design immersif** avec fond flouté et contrôles élégants

### 📱 Optimisation Mobile

- **Interface tactile** optimisée pour smartphones
- **Gestes swipe** pour navigation naturelle
- **Tailles adaptatives** pour une lisibilité parfaite
- **Performance optimisée** sur connexions lentes

## 🛠️ Technologies Utilisées

- **HTML5** - Structure sémantique moderne
- **CSS3** - Styling avancé avec CSS Grid, Flexbox et animations
- **JavaScript Vanilla** - Interactions et fonctionnalités avancées
- **Font Awesome** - Icônes professionnelles
- **GitHub Pages** - Hébergement gratuit et fiable

## 📁 Structure du Projet

```text
loc-appart/
├── index.html              # Page principale
├── photos/                 # Photos haute résolution
│   ├── IMG_20231129_*.jpg  # Images originales
│   ├── IMG_20231202_*.jpg  # Images supplémentaires
│   └── thumbnails/         # Miniatures optimisées
│       └── *.jpg          # Versions allégées pour la grille
└── README.md              # Documentation du projet
```

## 🚀 Déploiement

### GitHub Pages (Recommandé)

1. **Fork** ce repository
2. Allez dans `Settings` > `Pages`
3. Sélectionnez `Source: Deploy from a branch`
4. Choisissez `Branch: main` et `/ (root)`
5. Votre site sera disponible à : `https://[votre-username].github.io/loc-appart/`

### Hébergement Local

```bash
# Cloner le projet
git clone https://github.com/saumon/loc-appart.git
cd loc-appart

# Ouvrir avec un serveur local (optionnel)
python -m http.server 8000
# ou
npx serve .

# Puis ouvrir http://localhost:8000
```

## 🎯 Personnalisation

### Modifier les Photos

1. Remplacez les images dans `/photos/`
2. Créez les thumbnails correspondants dans `/photos/thumbnails/`
3. Mettez à jour le tableau `images` dans le JavaScript (ligne ~560)

### Changer le Titre et Description

Modifiez les balises dans `<head>` :

```html
<title>Votre Titre - Galerie Photos</title>
<meta name="description" content="Votre description">
```

Et dans le header :

```html
<h1><i class="fas fa-home"></i> Votre Titre</h1>
<p>Votre description personnalisée</p>
```

### Personnaliser les Couleurs

Modifiez les variables CSS dans `:root` :

```css
:root {
    --primary-color: #2563eb;    /* Couleur principale */
    --bg-color: #f8fafc;         /* Arrière-plan */
    --surface-color: #ffffff;    /* Cartes */
    --text-color: #334155;       /* Texte */
}
```

## 📊 Performance

- **Lazy Loading** : Chargement progressif des images
- **Thumbnails optimisés** : Versions allégées pour la grille
- **CSS optimisé** : Animations hardware-accelerated
- **Code minifié** : JavaScript optimisé pour la performance
- **Compatible PWA** : Peut être installé comme application

## 🌐 Compatibilité Navigateurs

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+
- ✅ Mobile Safari (iOS 13+)
- ✅ Chrome Mobile (Android 8+)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- 🐛 Signaler des bugs
- 💡 Proposer des améliorations
- 🔧 Soumettre des pull requests

## 📞 Contact

Pour toute question concernant l'appartement ou le projet :

- 📧 Email : [votre-email@example.com]
- 🐙 GitHub : [@saumon](https://github.com/saumon)

---

⭐ **N'hésitez pas à mettre une étoile si ce projet vous a été utile !**
