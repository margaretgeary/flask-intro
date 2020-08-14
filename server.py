"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [
    'b****', 'w****', 's***', 'd***', 'a******', 'b*******']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href=\"http://localhost:5000/hello\" >Click here</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    html = """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <br>
          <p>Please select a compliment:</p>
    """
    for i, awesome_word in enumerate(AWESOMENESS):
      html += f"""
          <input id="awesomeradio{i}" type="radio" name="compliment" value="{awesome_word}">
          <label for="awesomeradio{i}">{awesome_word}</label>
          """
    html += """
          <br>
          <br>
        </form>
          <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <br>
          <p>Please select an insult:</p>
    """
    for i, diss_word in enumerate(DISSES):
      html += f"""
          <input id="dissradio{i}" type="radio" name="diss" value="{diss_word}">
          <label for="dissradio{i}">{diss_word}</label>
          """
    html += """
          <br>
        </form>
        <br>
      </body>
    </html>
    """
    return html


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
      <br>
    </html>
    """.format(player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
