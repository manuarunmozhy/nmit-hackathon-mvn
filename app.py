from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage
leave_requests = []
attendance_status = "Not Checked In"


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


# ATTENDANCE

@app.route("/attendance")
def attendance():
    return render_template(
        "attendance.html",
        status=attendance_status
    )


@app.route("/check-in")
def check_in():
    global attendance_status

    attendance_status = "Present"

    return redirect("/attendance")


@app.route("/check-out")
def check_out():
    global attendance_status

    attendance_status = "Checked Out"

    return redirect("/attendance")


# LEAVE

@app.route("/leave", methods=["GET", "POST"])
def leave():

    if request.method == "POST":

        new_request = {
            "name": "Manu",
            "type": request.form["leave_type"],
            "from_date": request.form["from_date"],
            "to_date": request.form["to_date"],
            "remarks": request.form["remarks"],
            "status": "Pending"
        }

        leave_requests.append(new_request)

        return redirect("/leave")

    return render_template(
        "leave.html",
        requests=leave_requests
    )


@app.route("/leave-approvals")
def leave_approvals():
    return render_template(
        "leave_approvals.html",
        requests=leave_requests
    )


@app.route("/approve/<int:index>")
def approve_leave(index):

    leave_requests[index]["status"] = "Approved"

    return redirect("/leave-approvals")


@app.route("/reject/<int:index>")
def reject_leave(index):

    leave_requests[index]["status"] = "Rejected"

    return redirect("/leave-approvals")


# PAYROLL

@app.route("/payroll")
def payroll():
    return render_template("payroll.html")


if __name__ == "__main__":
    app.run(debug=True)