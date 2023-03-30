from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/temples")
def temples():
    return render_template("temples.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == [username] and password == [password]:
            return render_template("index.html")
        return render_template("login.html", err ="Login Failed, Please try againa" )
        # return render_template("failed.html")
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    # username_list = []
    # password_list = []
    if request.method == "POST":
        username = request.form.get("username")
        
        password = request.form.get("password")

        # username.append(username_list)

        # password.append(password_list)

        return render_template("index.html")
        # return render_template("failed.html")
    
    return render_template("register.html")

@app.route("/<string:file>")
def html_file(file):
    return render_template(f"htmls/{file}")
    
if __name__ == '__main__':
    app.run(debug=True) #host="0.0.0.0", port=8000