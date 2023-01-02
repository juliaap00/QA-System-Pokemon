from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)

# Set up a route to handle GET requests to the root URL
@app.route('/', methods=['GET'])
def home():
    # Get the 'question' argument from the request
    #question = request.args.get('question')
    # Return the answer as a response
    with open('index.html', 'r') as f:
        return f.read()
@app.route('/question', methods=['GET'])
def get_pokemon():
    # Get the 'question' argument from the request
    question = request.args.get('question')
    print(question )

    # Return the answer as a response
    return question

# Run the app when the script is executed
if __name__ == '__main__':
    app.run()
