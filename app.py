from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    return render_template('index.html', students = students)


@app.route('/insert', methods = ["POST"])
def insert():
    if request.method == 'POST':
        flash("muvaffaqiyatli saqlandi")
        cur = mysql.connection.cursor()

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        student = (name, email, phone)
        query = f"INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)"
        cur.execute(query, student)
        return redirect(url_for('index'))
    

@app.route('/update', methods = ["POST", "GET"])
def update():
    index = 0
    if request.method == 'POST':
        flash("muvaffaqiyatli yangilandi")
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        student = (name, email, phone, id_data)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE students
            SET name = %s, email = %s, phone = %s
            WHERE id = %s
        """, student)
        return redirect(url_for('index'))   
    

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("muvaffaqiyatli o\'chirildi")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", [id_data])
    return redirect(url_for('index'))    

if __name__ == "__main__":
    app.run()   
