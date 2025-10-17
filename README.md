````markdown
# auto_content

auto_content est un script Python permettant de :

- Télécharger automatiquement les vidéos (y compris Shorts) d'une chaîne YouTube.
- Reformatter les vidéos au format vertical 1080x1920 pour TikTok.
- (Stub) Publier les vidéos sur TikTok via l’API ou automatisation.

> ⚠️ Cette application est destinée à un usage personnel, éducatif ou de recherche. Respectez toujours les droits d'auteur et la propriété intellectuelle.

---

## Fonctionnalités

1. Téléchargement des vidéos d'une chaîne ou d'une page Shorts sans API YouTube.
2. Reformat vertical optimisé pour TikTok.
3. Suivi des vidéos déjà traitées pour éviter les doublons.
4. Stub d’upload TikTok pour développement et tests.

---

## Installation

1. Cloner le repo :
```bash
git clone https://github.com/tonpseudo/auto_content.git
````

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

* yt-dlp
* requests
* moviepy

---

## Usage

```bash
python auto_content.py
```

* Configurez les variables dans le script (`CHANNEL_URL`, `DOWNLOAD_DIR`, `TIKTOK_ACCESS_TOKEN`, etc.).
* Les vidéos seront téléchargées dans le dossier `downloads`.

---

## Terms of Service

Vous utilisez cette application à vos risques et périls.
L’application ne garantit pas la disponibilité des fonctionnalités TikTok.
Respectez toujours les droits d’auteur.

Lien : [Terms of Service](https://www.termsfeed.com/live/362e540f-50b8-45b7-b597-52a5882034ed)

---

## Privacy Policy

Cette application ne collecte aucune donnée personnelle.
Les vidéos sont stockées localement sur votre machine.
Aucune donnée n’est partagée avec des tiers.

Lien : [Privacy Policy](https://www.termsfeed.com/live/ff969fca-ac79-4b14-a42b-ba236ccee5bd)

---

## Contact

Pour toute question : [GitHub Issues](https://github.com/tonpseudo/auto_content/issues)

```
