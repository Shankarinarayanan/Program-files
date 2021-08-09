from flask import Flask,render_template,url_for,request,redirect

from flask_mysqldb import MySQL

web = Flask(__name__)

web.config["MYSQL_HOST"]="localhost"
web.config["MYSQL_USER"]="root"
web.config["MYSQL_PASSWORD"]="Shank09@"
web.config["MYSQL_DB"]="crud"
web.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(web)

@web.route('/')
@web.route('/home')
@web.route('/crud')
def page_1():
    con=mysql.connection.cursor()
    sql="SELECT * FROM info"
    con.execute(sql)
    result=con.fetchall()
    return render_template('page_1.html',details=result)

@web.route('/addusers',methods=['GET','POST']) 
def addusers():
    if request.method=='POST':
        name=request.form['NAME']
        age=request.form['AGE']
        city=request.form['CITY']
        mobile=request.form['MOBILE']
        con=mysql.connection.cursor()
        sql="INSERT INTO info (NAME,AGE,CITY,MOBILE) VALUES (%s,%s,%s,%s)"
        con.execute(sql,[name,age,city,mobile])
        mysql.connection.commit()
        con.close()
        return redirect(url_for('page_1'))
    return render_template('add.html')   

@web.route('/updateusers/<string:ID>',methods=['GET','POST'])
def updateusers(ID):
        con=mysql.connection.cursor()
        if request.method=='POST':
            name=request.form['NAME']
            age=request.form['AGE']
            city=request.form['CITY']
            mobile=request.form['MOBILE']
            sql="UPDATE info SET NAME=%s,AGE=%s,CITY=%s,MOBILE=%s WHERE ID=%s"
            con.execute(sql,[name,age,city,mobile,ID])
            mysql.connection.commit()
            con.close()
            return redirect(url_for('page_1'))
        con=mysql.connection.cursor()
        sql="SELECT * FROM info WHERE ID=%s"  
        con.execute(sql,[ID])
        result=con.fetchone()  
        return render_template('updateusers.html',details=result)
    



@web.route('/deleteusers/<string:ID>',methods=['GET','POST'])
def deleteusers(ID):
        con=mysql.connection.cursor()
        sql="DELETE FROM info WHERE ID=%s"
        con.execute(sql,ID)
        mysql.connection.commit()
        con.close()
        return redirect(url_for('page_1'))

if __name__ == "__main__" :
    web.run(debug=True)