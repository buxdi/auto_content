# tiktok_upload.py
"""
Module d'upload vers TikTok.
"""

import requests

# -------- CONFIG --------
TIKTOK_ACCESS_TOKEN = "TON_TIKTOK_ACCESS_TOKEN"
TIKTOK_UPLOAD_ENDPOINT = "https://open.tiktokapis.com/v1/video/upload/"

# -------- UPLOAD --------
def upload_to_tiktok(filepath, title=""):
    headers = {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}"}
    data = {"title": title}

    print("Upload vers TikTok :", filepath)
    with open(filepath, "rb") as f:
        files = {"video_file": f}
        resp = requests.post(TIKTOK_UPLOAD_ENDPOINT, headers=headers, files=files, data=data)

    print("Réponse TikTok :", resp.status_code, resp.text)
    return resp.ok
