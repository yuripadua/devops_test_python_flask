from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Ola mundo - acaba por favor!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# .github \ workflows
#rnd_VbCiFb1B6s2jTZoem6GxGQfJ3nCC
