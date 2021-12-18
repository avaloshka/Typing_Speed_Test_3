from tkinter import *
from timeit import default_timer as timer
from difflib import SequenceMatcher

import random

list_of_texts = ['Ministers are desperately trying to find ways to offer financial\n'
                 ' support to Welsh businesses hit by cancellations in response to\n'
                 ' the phenomenal spread of Omicron.',
                 'This is my text that I want to test myself for subject of typing efficiency. Good luck!\n',
                 'Two people have been confirmed missing after a block of flats was gutted by fire in a suspected\n '
                 'arson attack.'
                 'One person has been confirmed dead following the blaze.',
                 'Voters have begun to cast their ballots in the North Shropshire by-election as they choose \n'
                 'a replacement for former Conservative MP Owen Paterson.From 7am this morning to 10pm tonight,\n'
                 ' voters in the constituency will decide on a new local MP following ex-cabinet minister Mr Paterson\n'
                 'decision to quit the House of Commons last month.']
selected_text = random.choice(list_of_texts)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        self.starting_timing = None
        self.finishing_timing = None
        # create Label for displaying text
        self.lbl = Label(self, text='Hi, you can now test your skills,\n'
                               'Press the button "Start" and start typing.', font=22)
        self.lbl.place(x=10, y=10)

        # Text input goes here
        self.entry_box = StringVar()
        entry = Entry(self, font=18, textvariable=self.entry_box).place(x=10, y=300, width=700, height=100)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=750, y=550)

        startButton = Button(self, text='Start', command=self.clickStartButton)
        startButton.place(x=700, y=550)

        self.stopButton = Button(self, text='Stop', command=self.clickStopButton)
        self.stopButton.place(x=700, y=500)

    def clickStopButton(self, *args):
        # Import timer
        self.finishing_timing = timer()

        # Difference befween time finished and time started
        time_spent = self.finishing_timing - self.starting_timing

        # Get the input, split, if no input- quit.
        inp = self.entry_box.get()
        inp = inp.split(' ')
        if inp == '':
            quit()

        selected_text_split = selected_text.split(' ')
        # calculate same words that you managed to type
        same = SequenceMatcher(None, inp, selected_text_split).ratio()
        # Find words typed correctly
        different_words = set(inp).symmetric_difference(set(selected_text_split))
        same_words = len(selected_text_split) - len(different_words)
        # Calculate words per minute
        sec_per_word = time_spent/len(inp)
        words_per_minute = 60 / sec_per_word

        # Display results in self.lbl
        self.lbl.config(text=f'Time spent for the test is: {time_spent} seconds.\n'
                             f'Percent effectiveness: {same}%\n'
                             f'You typed {same_words} words right\n'
                             f'YOU TYPED {words_per_minute} WORDS PER MINUTE!!!')
        # Disable the stop button so no more calculations could be done on same test
        self.stopButton['state'] = 'disabled'

    def clickExitButton(self):
        exit()

    def clickStartButton(self):
        # Display new text that you want to be displayed
        self.lbl.config(text=f'{selected_text}')
        # Timer start timing
        self.starting_timing = timer()


