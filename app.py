from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

# Fake DB: list of expenses (in memory for now)
expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        amount = float(request.form["amount"])
        id = str(uuid.uuid4())
        expenses.append({"primaryId": id, "title": title, "amount": amount})
        return redirect("/")
    return render_template("index.html", expenses=expenses)

@app.route("/delete/<expense_id>", methods=["POST"])
def delete_expense(expense_id):
    global expenses
    expenses = [e for e in expenses if e["primaryId"] != expense_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
