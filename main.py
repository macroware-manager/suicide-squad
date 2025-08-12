from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    images_folder = os.path.join(app.static_folder, "images")
    image_files = [
        f"images/{img}"
        for img in os.listdir(images_folder)
        if img.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))
    ]
    return render_template("index.html", images=image_files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
