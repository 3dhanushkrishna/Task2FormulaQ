from flask import Flask, render_template, request

app = Flask(__name__)


def draw_pattern(word, lines):
    result = ""
    for i in range(lines):
        result += " " * (lines - i - 1)
        for k in range(i + 1):
            result += word[(k + i) % len(word)] + " "
        result += "<br>"
    for i in range(lines - 2, -1, -1):
        result += " " * (lines - i - 1)

        for k in range(i + 1):
            result += word[(k + i) % len(word)] + " "

        result += "<br>"

    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/draw', methods=['POST','GET'])
def draw():
    user_word = request.form['word']
    user_lines = int(request.form['lines'])
    result = draw_pattern(user_word, user_lines)
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

