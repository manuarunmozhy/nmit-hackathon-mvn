from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# LOGIN PAGE
@app.route("/")
def login():
    return render_template("login.html")


# PROCESS LOGIN
@app.route("/login", methods=["POST"])
def handle_login():

    role = request.form["role"]

    if role == "employee":
        return redirect("/employee")

    elif role == "admin":
        return redirect("/admin")


# EMPLOYEE DASHBOARD
@app.route("/employee")
def employee_dashboard():
    return render_template("employee_dashboard.html")


# ADMIN DASHBOARD
@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)