from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    submitted_data = None
    
    if request.method == "POST":
        # Capture form inputs from the HTML contact form
        submitted_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "topic": request.form.get("topic"),
            "message": request.form.get("message")
        }
        print("New Form Submission:", submitted_data)

    return render_template("index.html", submitted_data=submitted_data)

if __name__ == "__main__":
    # Runs the built-in development server
    app.run(debug=True, host="0.0.0.0", port=5000)
