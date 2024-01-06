from tkinter import *
from tkinter import ttk
import random
import string

guess_count = 0
correct = False

answers_list = []
guesses_list = []

# answers are potential words, guesses can be guessed but not be the answer

answers_txt = open("answers.txt", "r")
for line in answers_txt:
    word_to_add = line.rstrip("\n")
    answers_list.append(word_to_add)
    guesses_list.append(word_to_add)
answers_txt.close()

guesses_txt = open("guesses.txt", "r")
for line in guesses_txt:
    guesses_list.append(line.rstrip("\n"))
guesses_txt.close()
guesses_list.sort()

answer = answers_list[random.randint(0, len(answers_list) - 1)]
# print(answer)


def update(*args):

    global guess_count
    global answer
    global answers_list
    global guesses_list
    global correct

    letter_list = ["Incorrect", "Incorrect", "Incorrect", "Incorrect", "Incorrect"]
    answer_list = []
    for letter in answer:  # list used for duplicate letters, such as "hello" in "slate" only having one valid l
        answer_list.append(letter)

    try:
        guess_string = guess.get().lower()
        output_string.set("")

        if correct:
            output_string.set(f"You got the answer in {guess_count} guesses!")
            raise ValueError
        elif guess_count > 6:
            output_string.set(f"You ran out of guesses! The answer was {answer}.")
        elif guess_string not in guesses_list:
            output_string.set("Invalid Guess")
            raise ValueError
        else:
            for i in range(5):
                letter_variables[guess_count][i].set(guess_string[i])

            if guess_string[0] == answer[0]:  # correct position and letter
                answer_list.remove(guess_string[0])  # once a letter is correct, remove it from being correct for later
                letter_list[0] = "Correct"
                letter_labels[guess_count][0].config(bg="green")
                alphabet_labels[guess_string[0]].config(bg="green")
            if guess_string[1] == answer[1]:
                answer_list.remove(guess_string[1])
                letter_list[1] = "Correct"
                letter_labels[guess_count][1].config(bg="green")
                alphabet_labels[guess_string[1]].config(bg="green")
            if guess_string[2] == answer[2]:
                answer_list.remove(guess_string[2])
                letter_list[2] = "Correct"
                letter_labels[guess_count][2].config(bg="green")
                alphabet_labels[guess_string[2]].config(bg="green")
            if guess_string[3] == answer[3]:
                answer_list.remove(guess_string[3])
                letter_list[3] = "Correct"
                letter_labels[guess_count][3].config(bg="green")
                alphabet_labels[guess_string[3]].config(bg="green")
            if guess_string[4] == answer[4]:
                answer_list.remove(guess_string[4])
                letter_list[4] = "Correct"
                letter_labels[guess_count][4].config(bg="green")
                alphabet_labels[guess_string[4]].config(bg="green")

            if letter_list == ["Correct", "Correct", "Correct", "Correct", "Correct"]:
                output_string.set(f"You got the answer in {guess_count + 1} guesses!")   # guess counter not updated yet
                correct = True
            else:
                output_string.set("Your guess was wrong.")

                if guess_string[0] in answer_list and letter_list[0] != "Correct":  # correct letter, wrong position
                    answer_list.remove(guess_string[0])
                    letter_list[0] = "Incorrect Position"
                    letter_labels[guess_count][0].config(bg="yellow")
                    if not alphabet_labels[guess_string[0]].cget("bg") == "green":
                        alphabet_labels[guess_string[0]].config(bg="yellow")
                elif not letter_labels[guess_count][0].cget("bg") == "green":
                    letter_labels[guess_count][0].config(bg="grey")
                if alphabet_labels[guess_string[0]].cget("bg") == "SystemButtonFace":
                    alphabet_labels[guess_string[0]].config(bg="grey")
                if guess_string[1] in answer_list and letter_list[1] != "Correct":
                    answer_list.remove(guess_string[1])
                    letter_list[1] = "Incorrect Position"
                    letter_labels[guess_count][1].config(bg="yellow")
                    if not alphabet_labels[guess_string[1]].cget("bg") == "green":
                        alphabet_labels[guess_string[1]].config(bg="yellow")
                elif not letter_labels[guess_count][1].cget("bg") == "green":
                    letter_labels[guess_count][1].config(bg="grey")
                if alphabet_labels[guess_string[1]].cget("bg") == "SystemButtonFace":
                    alphabet_labels[guess_string[1]].config(bg="grey")
                if guess_string[2] in answer_list and letter_list[2] != "Correct":
                    answer_list.remove(guess_string[2])
                    letter_list[2] = "Incorrect Position"
                    letter_labels[guess_count][2].config(bg="yellow")
                    if not alphabet_labels[guess_string[2]].cget("bg") == "green":
                        alphabet_labels[guess_string[2]].config(bg="yellow")
                elif not letter_labels[guess_count][2].cget("bg") == "green":
                    letter_labels[guess_count][2].config(bg="grey")
                if alphabet_labels[guess_string[2]].cget("bg") == "SystemButtonFace":
                    alphabet_labels[guess_string[2]].config(bg="grey")
                if guess_string[3] in answer_list and letter_list[3] != "Correct":
                    answer_list.remove(guess_string[3])
                    letter_list[3] = "Incorrect Position"
                    letter_labels[guess_count][3].config(bg="yellow")
                    if not alphabet_labels[guess_string[3]].cget("bg") == "green":
                        alphabet_labels[guess_string[3]].config(bg="yellow")
                elif not letter_labels[guess_count][3].cget("bg") == "green":
                    letter_labels[guess_count][3].config(bg="grey")
                if alphabet_labels[guess_string[3]].cget("bg") == "SystemButtonFace":
                    alphabet_labels[guess_string[3]].config(bg="grey")
                if guess_string[4] in answer_list and letter_list[4] != "Correct":
                    answer_list.remove(guess_string[4])
                    letter_list[4] = "Incorrect Position"
                    letter_labels[guess_count][4].config(bg="yellow")
                    if not alphabet_labels[guess_string[4]].cget("bg") == "green":
                        alphabet_labels[guess_string[4]].config(bg="yellow")
                elif not letter_labels[guess_count][4].cget("bg") == "green":
                    letter_labels[guess_count][4].config(bg="grey")
                if alphabet_labels[guess_string[4]].cget("bg") == "SystemButtonFace":
                    alphabet_labels[guess_string[4]].config(bg="grey")

        guess_count += 1
        if guess_count == 6 and not correct:
            output_string.set(f"You ran out of guesses! The answer was {answer}.")

    except:
        pass

    guess.delete(0, END)
    guess.focus()


root = Tk()
root.title("Wordle")

content = ttk.Frame(root, padding=(3, 3, 3, 3))
guess_label = ttk.Label(content, text="Enter your guess:")
guess = ttk.Entry(content)

submit = ttk.Button(content, text="Submit", command=update)

output_string = StringVar()
output_string.set("")
output = ttk.Label(content, textvariable=output_string)

content.grid(column=0, row=0, sticky=(N, S, E, W))
guess_label.grid(column=0, row=0, columnspan=2, sticky=(N, E), padx=5, pady=5)
guess.grid(column=2, row=0, columnspan=3, sticky=(N, E, W), padx=5, pady=5)
submit.grid(column=0, row=1, columnspan=5, sticky=N, padx=5, pady=5)
output.grid(column=0, row=2, columnspan=5, sticky=N, padx=5, pady=5)

letter_variables = []
letter_labels = []
for i in range(6):
    letter_variables.append([])
    letter_labels.append([])
    for j in range(5):
        letter_variables[i].append(StringVar())
        letter_variables[i][j].set("")
        letter_labels[i].append(Label(content, textvariable=letter_variables[i][j]))
        letter_labels[i][j].grid(column=j, row=i+3, padx=5, pady=5, sticky=N)

alphabet = ttk.Frame(root, padding=(3, 3, 3, 3))
alphabet_list = list(string.ascii_lowercase)
alphabet_labels = {}
for i in range(len(alphabet_list)):
    alphabet_labels[alphabet_list[i]] = Label(alphabet, text=alphabet_list[i])
    alphabet_labels[alphabet_list[i]].grid(column=i % 13, row=i//13, padx=5, pady=5, sticky=N)
    alphabet.columnconfigure(i % 13, weight=1)

alphabet.grid(column=0, row=9, sticky=(N, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

for i in range(5):
    content.columnconfigure(i, weight=1, minsize=60)

for i in range(3):
    content.rowconfigure(i, weight=0)

for i in range(5):
    content.rowconfigure(i+3, weight=1, minsize=30)

guess.focus()
root.bind("<Return>", update)

root.mainloop()
