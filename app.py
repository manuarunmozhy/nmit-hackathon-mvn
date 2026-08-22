from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():

    role = request.form["role"]

    if role == "employee":
        return redirect("/employee")

    elif role == "admin":
        return redirect("/admin")


@app.route("/employee")
def employee_dashboard():
    return render_template("employee_dashboard.html")


@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


@app.route("/leave")
def leave():
    return render_template("leave.html")


@app.route("/payroll")
def payroll():
    return render_template("payroll.html")


@app.route("/leave-approvals")
def leave_approvals():
    return render_template("leave_approvals.html")


if __name__ == "__main__":
    app.run(debug=True)