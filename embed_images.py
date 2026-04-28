import os
import base64

def get_data_url(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    ext = os.path.splitext(file_path)[1][1:]
    return f"data:image/{ext};base64,{encoded}"

# Read original index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Images to replace
images = [
    "dashboard_hero_bg.png",
    "graph_1.png",
    "graph_2.png",
    "graph_4.png",
    "graph_5.png",
    "graph_8.png",
    "text_analysis.png"
]

for img in images:
    path = os.path.join("images", img)
    data_url = get_data_url(path)
    if data_url:
        html = html.replace(f"./images/{img}", data_url)

# Save the self-contained html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Self-contained index.html generated with embedded images.")
