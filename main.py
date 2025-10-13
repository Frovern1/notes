from flask import Flask, render_template, request, redirect, session
import db
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        note_name = request.form.get("note-name")
        note_text = request.form.get("note-text")
        db.add(note_name, note_text)
    notes = db.get_all()    
    return render_template("index.html", notes=notes)


@app.route("/notes/<int:id>",methods=["GET","POST"])
def notes_sites(id):
    if request.method == "POST":
        note_name = request.form.get("note-name")
        note_text = request.form.get("note-text")
        db.change_note(id, note_name, note_text)
    notes = db.get_all()
    current_note =  db.get_note(id)
    return render_template("index.html", notes=notes, current_note=current_note)

@app.route("/delete/note/<int:id>")
def delete_note(id):
    db.delete_note(id)
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def singup():
    if request.method == "POST":
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        if db.get_user(username):
            return "такой пользователь существует"
        db.add_user(username, password)
        return redirect("/login")
    return render_template("signup.html")
   
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        inf = db.get_user(username)
        password = request.form.get("password")
        if inf:
            if check_password_hash(inf[2], password):
                session["userid"] = inf[0]
                return redirect("/")
        return "Неверное имя или пароль"
        
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

