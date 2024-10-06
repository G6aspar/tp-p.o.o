from flask import Flask, render_template, jsonify, request
from controller import AnimalController

app = Flask(__name__)
animal_controller = AnimalController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animal/<name>', methods=['GET'])
def get_animal(name):
    try:
        response = animal_controller.get_animal_info(name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
