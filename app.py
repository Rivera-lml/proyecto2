from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template
from bd_connector import selectData

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('4.html')

@app.route('/resultados')
def resultados():
    personList = selectData()
    return render_template('resultados.html', persons=personList)


if __name__ == '__main__':
    app.run(debug=True)
