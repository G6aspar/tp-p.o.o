from flask import Flask, render_template, request
from controller import AnimalController

app = Flask(__name__)
animal_controller = AnimalController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_animal():
    name = request.form.get('animal_name')
    try:
        animal_data = animal_controller.get_animal_info(name)
        return render_template('animal_info.html', animal=animal_data[0])
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

