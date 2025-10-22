from flask import Flask, request, render_template
import subprocess
import csv
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data.csv")
C_EXE = os.path.join(BASE_DIR, "calculate.exe")  # Use "./calculate" on Linux/Mac

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    output = ""
    message = ""
    if request.method == 'POST':
        date = request.form.get('date')
        category = request.form.get('category')
        amount = request.form.get('amount')
        if date and category and amount:
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([date, category, amount])
            message = "Expense Added Successfully!"
        else:
            message = "Fill all fields!"

        # Call C program
        if os.path.exists(C_EXE):
            output = subprocess.getoutput(C_EXE)
        else:
            output = "C executable not found!"
        output = f"{message}\n{output}"

    return render_template('add_expense.html', output=output)

@app.route('/report')
def report():
    if os.path.exists(C_EXE):
        output = subprocess.getoutput(C_EXE)
    else:
        output = "C executable not found!"
    return render_template('view_report.html', output=output)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
