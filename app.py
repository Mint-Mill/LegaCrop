from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "GET":
        return render_template("analyze.html")
    elif request.method == "POST":
        # Get the file from post request
        # f = request.files['file']

        # # Save the file to ./uploads
        # basepath = os.path.dirname(__file__)
        # file_path = os.path.join(
        #     basepath, 'uploads', secure_filename(f.filename))
        # f.save(file_path)

        # # Make prediction
        # preds = model_predict(file_path, model)
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        # result=pred_class[0]                          # Convert to string
        result = "Tomato"
        return result
    return None

if __name__ == "__main__":
    app.run(debug=True, port=8000)

