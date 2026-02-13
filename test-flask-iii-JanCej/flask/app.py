# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
stiznost = []
json_file = "stiznost.json"

def save_data():
    with open(json_file, "w", encoding="UTF-8") as f:
        json.dump(stiznost, f, ensure_ascii=False)
@app.route("/")
def vitej():
    return render_template("vitej.html")

@app.route("/form")
def form():
    login = request.args.get("login")
    stiznost = request.args.get("stiznost")


    if stiznost and login:
        stiznost[login] = stiznost
        print(stiznost)
        
    if stiznost == "ach":
        print("zákazník byl příliš líný na napsání stížnosti")
    return render_template("form.html")

# app = Flask(__name__)
# from flask import Flask, render_template, request, redirect, url_for
# @app.route("???")
# request.args.get("???")
# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"
# render_template("???", ???, ???)


# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)
# if __name__ == "__main__":app.run(debug=True)  zapíná funkci
    
