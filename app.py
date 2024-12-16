from flask import Flask, render_template, request, flash, redirect, url_for


students = [
    (1, "Aliyev Anvar", "aliyev.anvar@example.com", "+998901234567"),
    (2, "Karimova Dilnoza", "karimova.dilnoza@example.com", "+998901234568"),
    (3, "Tursunov Shohruh", "tursunov.shohruh@example.com", "+998901234569"),
    (4, "Ismoilova Maftuna", "ismoilova.maftuna@example.com", "+998901234570"),
    (5, "Abdullayev Timur", "abdullayev.timur@example.com", "+998901234571"),
    (6, "Usmonova Aziza", "usmonova.aziza@example.com", "+998901234572"),
    (7, "Hamidov Javohir", "hamidov.javohir@example.com", "+998901234573"),
    (8, "Sobirova Shirin", "sobirova.shirin@example.com", "+998901234574"),
    (9, "Nurmatov Baxtiyor", "nurmatov.baxtiyor@example.com", "+998901234575"),
    (10, "Qodirova Madina", "qodirova.madina@example.com", "+998901234576"),
]


app = Flask(__name__)

app.secret_key = 'many random bytes'


@app.route('/')
def index():
    return render_template('index.html', students = students)


@app.route('/insert', methods = ["POST"])
def insert():

    if request.method == 'POST':
        flash("muvaffaqiyatli saqlandi")
        id_data = students[-1][0]+1
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        student = (id_data, name, email, phone)
        students.append(student)
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
        student = (id_data, name, email, phone)
        for i, stu in enumerate(students):
            if stu[0] == int(id_data):
                index = i
                break
        students.pop(index)
        students.insert(index, student)
        return redirect(url_for('index'))   
    

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("muvaffaqiyatli o\'chirildi")
    index = 0
    for i, stu in enumerate(students):
            if stu[0] == int(id_data):
                index = i
                break
    students.pop(index)
    return redirect(url_for('index'))    

if __name__ == "__main__":
    app.run()   