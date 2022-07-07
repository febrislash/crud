

from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql

app=Flask(__name__)

app.secret_key='312321asdasd3123'

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("pelanggan.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from data_pelanggan")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        nama=request.form['nama']
        alamat=request.form['alamat']
        telpon=request.form['telpon']
        jumlah_ac=request.form['jumlah_ac']
        tanggal_service=request.form['tanggal_service']
        con=sql.connect("pelanggan.db")
        cur=con.cursor()
        cur.execute("insert into data_pelanggan(nama, alamat, telpon, jumlah_ac, tanggal_service) values (?,?,?,?,?)",(nama,alamat,telpon,jumlah_ac,tanggal_service))
        con.commit()
        flash('User Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:id>",methods=['POST','GET'])
def edit_user(id):
    if request.method=='POST':
        name=request.form['nama']
        alamat=request.form['alamat']
        telpon=request.form['telpon']
        jumlah_ac=request.form['jumlah_ac']
        tanggal_service=request.form['tanggal_service']
        con=sql.connect("pelanggan.db")
        cur=con.cursor()
        cur.execute("update data_pelanggan set nama=?, alamat=?, telpon=?, jumlah_ac=?, tanggal_service=?  where id=?",(name,alamat,telpon,jumlah_ac,tanggal_service,id))
        con.commit()
        flash('User Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("pelanggan.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from data_pelanggan where id=?",(id,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<string:id>",methods=['GET'])
def delete_user(id):
    con=sql.connect("pelanggan.db")
    cur=con.cursor()
    cur.execute("delete from data_pelanggan where id=?",(id,))
    con.commit()
    flash('User Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.run(debug=True)

