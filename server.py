from flask import Flask, request
from flask import Flask,jsonify,request, render_template, make_response
from modules.utils.pokemon_qa import qa

# Initialize the Flask app
app = Flask(__name__)
# Set up a route to handle GET requests to the root URL
@app.route('/', methods=['GET'])
def home():
    with open('index.html', 'r') as f:
            return f.read()
# recive una pregunta sobre un pokemon
@app.route('/question', methods=['GET', 'POST'])
def get_question():
    # Get the 'question' argument from the request
    #question = request.args.get('question')
    question = request.args.get('question')
    #llama a la funcion qa encargada de saber que dominio se pregunta y proporcionar una respuesta
    answer = qa(question)
    print(answer)
    # Return the answer as a response to the HTML client
    return  answer 



# Run the app when the script is executed
if __name__ == '__main__':
    app.run()
