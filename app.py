from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greating to the user."""
    return "Are you there, world? It's me, Ducky!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes bases on the favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a funny story using an adjective and nound passed to the function."""
    return f'Every single day for the past twenty years I eat on Christmas two {adjective} {noun}.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display the multiplication of two numbers pass as parameters."""
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers.'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display the word pass as a parameters an ammount of times also passed as a parameters. """

    words_to_return = ""
    if n.isdigit():
        for _ in range(int(n)):
            words_to_return += word + " "
    else:
        return f'Invalid input. Please try again by entering a word and a number!'
    
    return words_to_return

@app.route('/dicegame')
def dicegame():
    """Display a random number from 1 to 6 including both ends. If the value is 6 the user wins."""
    dice_value = randint(1,6)

    if dice_value == 6:
        return f'You rolled a {dice_value}. You won!'
    else:
        return f'You rolled a {dice_value}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)