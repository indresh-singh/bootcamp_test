from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY="ops_digital_asset"
)

@app.route("/", methods=['GET','POST'])
def login():
    user ={"name":"Ajay"}
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run()