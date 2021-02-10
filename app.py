# PYTHON QUIZ
import random
import time
try:
  from colorama import *
  from pyfiglet import figlet_format
  from termcolor import colored
except:
  print("You should install modules: colorama, pyfiglet and termcolor!")

# Utility Functions
def print_ascii(text, color):
  print(colored(figlet_format(text), color))

# Create a list of dicionaries
questions = [
  {
    "id": 1,
    "question": 'How to display to a console "Hello World" in python?',
    "answers": [
      'print("Hello World!")',
      'console.log("Hello World!")',
      'echo "Hello World!"',
      'print "Hello World!"'
    ],
    "correct": 1
  },
  {
    "id": 2,
    "question": 'How to declare a variable "username" which is equals to "Ali Guliyev"?',
    "answers": [
      'var username = "Ali Guliyev"',
      'String username = "Ali Guliyev"',
      'username = "Ali Guliyev"',
      '$username = "Ali Guliyev"'
    ],
    "correct": 3
  },
  {
    "id": 3,
    "question": 'How to display a type of a variable "number" in python?',
    "answers": [
      'typeof number',
      'typeof(number)',
      'type number',
      'type(number)'
    ],
    "correct": 4
  },
  {
    "id": 4,
    "question": 'How to declare a function in python?',
    "answers": [
      'function myFunction() {}',
      'def myFunction():',
      'function myFunction():',
      'def myFunction() {}'
    ],
    "correct": 2
  },
  {
    "id": 5,
    "question": 'Which one is a list/array?',
    "answers": [
      '{"John Doe", "Will Smith", "Michael Jackson"}',
      '["John Doe", "Will Smith", "Michael Jackson"]',
      '("John Doe", "Will Smith", "Michael Jackson")',
      '{"name1": "John Doe", "name2": "Will Smith", "name3": "Michael Jackson"}'
    ],
    "correct": 2
  },
  {
    "id": 6,
    "question": 'Which one is a dictionary?',
    "answers": [
      '{"John Doe", "Will Smith", "Michael Jackson"}',
      '["John Doe", "Will Smith", "Michael Jackson"]',
      '("John Doe", "Will Smith", "Michael Jackson")',
      '{"name1": "John Doe", "name2": "Will Smith", "name3": "Michael Jackson"}'
    ],
    "correct": 4
  },
  {
    "id": 7,
    "question": 'Which one is a set?',
    "answers": [
      '{"John Doe", "Will Smith", "Michael Jackson"}',
      '["John Doe", "Will Smith", "Michael Jackson"]',
      '("John Doe", "Will Smith", "Michael Jackson")',
      '{"name1": "John Doe", "name2": "Will Smith", "name3": "Michael Jackson"}'
    ],
    "correct": 1
  },
  {
    "id": 8,
    "question": 'Which one is a tuple?',
    "answers": [
      '{"John Doe", "Will Smith", "Michael Jackson"}',
      '["John Doe", "Will Smith", "Michael Jackson"]',
      '("John Doe", "Will Smith", "Michael Jackson")',
      '{"name1": "John Doe", "name2": "Will Smith", "name3": "Michael Jackson"}'
    ],
    "correct": 3
  },
  {
    "id": 9,
    "question": 'Which answer is a correct way to print all the numbers from 1 to 10 with for loop in python?',
    "answers": [
      '''for i in range(1, 11):
      print(i)''',
      '''for (i = 0; i < 10; i++):
      print(i)''',
      'Both'
    ],
    "correct": 1
  },
]

# Print "Python Quiz" to the console as an ASCII
print_ascii("Python Quiz", "blue")
time.sleep(1)

# Draw a rectangle with an aount of questions
print(f"""+-------------------------------------+\n| There are {Fore.BLACK}{Back.YELLOW}{len(questions)}{Fore.RESET}{Back.RESET} questions in this quiz! |\n+-------------------------------------+\n""")

results = {
  "correct": 0,
  "wrong": 0
}

# Execute an error
isErrorExcecuted = False
def executeError():
  global isErrorExcecuted
  print(f"{Fore.RED}Something went wrong ¯\_(ツ)_/¯!\nTry to rerun the program!")
  isErrorExcecuted = True

# Loop over an array of objects
for question in questions:
  id = question["id"]
  # Print the question
  print(f'{Fore.YELLOW}{id}. {question["question"]} {Fore.RESET}')

  # Printing Answers
  count = 0
  for answer in question["answers"]:
    count += 1
    print(f' {Fore.LIGHTGREEN_EX}{count}){Fore.RESET} {answer}')

  # Check if there is an error when user pressed enter after typing the answer in the input
  try:
    person_answer = int(input(f"\nYour answer: {Fore.LIGHTBLUE_EX}")) 
    if (person_answer == question["correct"]):
      print(f"{Fore.GREEN}Correct!")
      results["correct"] += 1
    else:
      if person_answer > len(question["answers"]):
        executeError()
        break
      else:
        print(f"{Fore.RED}Wrong!")
        results["wrong"] += 1
    time.sleep(1)
  except:
    executeError()
    break

  print("\n")


# If there is not errors show users results
if isErrorExcecuted == False:
  print(f"""{Fore.GREEN}Correct answers - {results["correct"]}
  {Fore.RED}Wrong answers - {results["wrong"]}
  """)
  print_ascii("You Won!", "green") if results["correct"] > results["wrong"] else print_ascii("You Lost!", "red")