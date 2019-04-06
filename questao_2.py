from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from questao_2_pt2 import *


app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade_prova'

@app.route('/')
def pag_princ():
    cursor = mysql.get_db().cursor()
    return render_template('questao_dois.html',professor = list_prof(cursor))

@app.route('/listarProfessores')
def list():
    cursor = mysql.get_db().cursor()
    return render_template('questao_dois.html', professor=list_prof(cursor))


@app.route('/exibirProfessor')
def exibir():
   return render_template('exibir_prof.html')













if __name__ == '__main__':
    app.run(debug=True)