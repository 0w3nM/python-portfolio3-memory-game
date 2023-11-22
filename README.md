# MEMORY GAME
A game designed for a Python terminal, running on Heroku provided by Code Institute

Players are presented with a randomised 5 Digit Number that disappear and must test their memory capabilities and match it.
It is targeted at an audience that wishes to train or improve on their memory skills


## Rules
The rules are simple. Repeat the sequence that was shown 5 times. Anything less than 3 correct answers ends in failure.

# Features
## Existing Features
* Greetings message to the user with the rules.
![Greeting Message](img/pp3_opening_message_&_sequence.png)
* Name input box to start the game.
![Name Box]()
* Error message on invalid entry input to Name input box.
![Input Name Error]()
* Randomised sequence of digits for the user to remeber.
* Sequence dissappears after 5 seconds.
* User guess and message returns correct or incorrect with the sequence it was.
* Message shows if the user won or lost
* Message if the user wishes to continue with either a 'Y' or 'N'

## Future Features
 * Sequence is on the screen for less time.
 * Pass rate is raised to all guesses must be correct.

# Testing
Manual testing was carried out with:
* Code vaidated through PEP8 linter.
* Inputs checked for validity by testing, numbers that are not within limits and inputing strings instead of numbers and vise vera entering integers instead of strings
* Tested on both local and Heroku terminal.

## Validator Testing
* No errors reported through PEP8online.com
![PEP8 Results](img/pp3_validator_check.png)

# Deployment
* Create a new Heoku App
* Set buildpacks - Python then NodeJS
* Link Heroku App to repository.
* Click Deploy
* Deploy Branch
* Open App (At the top of the page)

# Credits
* Code Institute for layout, game repeat and while loop functions and validation code.
* Stack Overflow for guess_limit function.
* Djangocentral.com for number of guesses function.
* 
* 
