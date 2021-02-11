# PYTHON QUIZ
from pyfiglet import figlet_format
from termcolor import colored
import random
import time
from colorama import *
import json

# Utility Functions
def print_ascii(text, color):
  print(colored(figlet_format(text), color))

# Create a list of dicionaries
questions = json.load(open("questions.json"))

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
  print(f'{Fore.GREEN}Correct answers - {results["correct"]}\n{Fore.RED}Wrong answers - {results["wrong"]}')
  print_ascii("You Won!", "green") if results["correct"] > results["wrong"] else print_ascii("You Lost!", "red")