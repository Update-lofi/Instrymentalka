from flask import Flask, render_template, redirect, url_for
from controllers.person_controller import person_bp

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Замените на случайную строку

# Регистрация blueprint
app.register_blueprint(person_bp)

@app.route('/')
def home():
    """Главная страница"""
    return render_template('home/index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)