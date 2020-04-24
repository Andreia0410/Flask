from flask import Flask

app = Flask(_name_)

@app.route('/home')

    def ola():
        return '<h1>Olá Mundo!</h1>'

app.run()