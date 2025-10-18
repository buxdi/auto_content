````markdown
# 🎯 Module `tiktok_upload`

Ce module fournit une fonction unique pour **envoyer une vidéo sur TikTok via l’API officielle**.  
Il est conçu pour être intégré dans un pipeline d’automatisation (par exemple un uploader YouTube → TikTok).

---

## ⚙️ Fonctionnalité

```python
upload_to_tiktok(filepath, title="")
````

**Paramètres :**

* `filepath` — chemin complet du fichier vidéo à envoyer
* `title` — titre ou description de la vidéo (optionnel)

**Retourne :**

* `True` si l’upload a réussi (`status_code == 200`)
* `False` sinon

---

## 🔑 Configuration requise

Avant toute utilisation, il faut obtenir une **clé API TikTok** (access token).

### Étapes pour obtenir un access token :

1. Crée un compte développeur sur [https://developers.tiktok.com](https://developers.tiktok.com)
2. Dans ton **Developer Dashboard**, crée une nouvelle application :

   * Type : *Content Uploading*
   * Nom : par exemple `TikTok Auto Upload`
3. Dans la section **"Manage App"**, récupère ton **Access Token**
4. Copie ce token dans le fichier `tiktok_upload.py` :

```python
TIKTOK_ACCESS_TOKEN = "VOTRE_CLE_API_ICI"
```

---

## 🧱 Structure du fichier

```python
# tiktok_upload.py
import requests

TIKTOK_ACCESS_TOKEN = "TON_TIKTOK_ACCESS_TOKEN"
TIKTOK_UPLOAD_ENDPOINT = "https://open.tiktokapis.com/v1/video/upload/"

def upload_to_tiktok(filepath, title=""):
    headers = {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}"}
    data = {"title": title}
    print("Upload vers TikTok :", filepath)
    with open(filepath, "rb") as f:
        files = {"video_file": f}
        resp = requests.post(TIKTOK_UPLOAD_ENDPOINT, headers=headers, files=files, data=data)
    print("Réponse TikTok :", resp.status_code, resp.text)
    return resp.ok
```

---

## 🧪 Exemple d’utilisation

```python
from tiktok_upload import upload_to_tiktok

ok = upload_to_tiktok("videos/test.mp4", title="Ma première vidéo auto-uploadée")
print("Upload réussi :", ok)
```

---

## 📦 Dépendances

```bash
pip install requests
```

---

## ⚠️ Remarques

* TikTok peut limiter le nombre d’uploads par jour selon ton compte développeur.
* La vidéo doit être **< 1 Go** et respecter les formats pris en charge (MP4, MOV, etc.).
* Ce module ne gère **que l’upload direct**. Toute étape de transformation ou de génération de token doit être faite avant.

---

© 2025 – Module utilitaire d’upload TikTok, à usage expérimental.

```
