from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Let's make the message a bit more personal
    return "Bonsoir from my first Docker App in Clermont-Ferrand!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)