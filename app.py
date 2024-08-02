from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    # Call the C++ program with the guess as input
    result = run_cpp_program(guess)
    return render_template('index.html', result=result)


def run_cpp_program(guess):
    # C++ program runs with the guess as input
    process = subprocess.Popen(
        ['./game'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate(input=guess.encode())

    if error:
        return error.decode('utf-8')

    return output.decode('utf-8').strip()


if __name__ == '__main__':
    app.run(debug=True)
