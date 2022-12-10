from random import *
from PyQt5.QtWidgets import *
from view_dice import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

##Seeding the random num generator
seed()

##Controller class to make everything work
class Controller(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        ##set window title to Dice Roller
        self.setWindowTitle('Dice Roller')

        ##clicking submit
        self.submit.clicked.connect(lambda: self.submit_button())

        ##clicking clear
        self.clear.clicked.connect(lambda: self.clear_button())

        ##Default Radio Buttons
        self.Dice20.setChecked(True)
        self.one_.setChecked(True)

        ##Default Message:
        self.output_label.setText(f'Use radio buttons to pick dice type, enter how many dice you want to roll,\n and add any relevant modifiers\n\nNote: Please use integers when typing \nD12-D4 are set up for damage rolls')


    ##Setting what happens when the submit button is selected
    def submit_button(self):
        ##Start of the try/except block
        try:
            ##modifier set
            modifier = int(self.modifier.text())

            ##if else for which dice is selected AND how many:
            ##D20 roll generation
            if self.Dice20.isChecked():
                ##if else for number of dice
                if self.one_.isChecked():
                    self.output_label.setText(f'')
                    dice1 = randint(1,20)

                elif self.two_.isChecked():
                    self.output_label.setText(f'')
                    dice1 = randint(1, 20)
                    dice2 = randint(1, 20)

            ##D100 roll generation
            elif self.Dice100.isChecked():
                ##if else for number of dice
                if self.one_.isChecked():
                    self.output_label.setText(f'')
                    dice1 = randint(1,100)

            ##D12 roll generation
            elif self.Dice12.isChecked():
                self.output_label.setText(f'')
                ##if else for number of dice
                if self.one_.isChecked():
                    dice1 = randint(1, 12)

                elif self.two_.isChecked():
                    dice1 = randint(1, 12)
                    dice2 = randint(1, 12)

                elif self.three_.isChecked():
                    dice1 = randint(1, 12)
                    dice2 = randint(1, 12)
                    dice3 = randint(1, 12)

                elif self.four_.isChecked():
                    dice1 = randint(1, 12)
                    dice2 = randint(1, 12)
                    dice3 = randint(1, 12)
                    dice4 = randint(1, 12)


            ##D10 roll generation
            elif self.Dice10.isChecked():
                self.output_label.setText(f'')
                ##if else for number of dice
                if self.one_.isChecked():
                    dice1 = randint(1, 10)

                elif self.two_.isChecked():
                    dice1 = randint(1, 10)
                    dice2 = randint(1, 10)

                elif self.three_.isChecked():
                    dice1 = randint(1, 10)
                    dice2 = randint(1, 10)
                    dice3 = randint(1, 10)

                elif self.four_.isChecked():
                    dice1 = randint(1, 10)
                    dice2 = randint(1, 10)
                    dice3 = randint(1, 10)
                    dice4 = randint(1, 10)

            ##D8 roll generation
            elif self.Dice8.isChecked():
                self.output_label.setText(f'')
                ##if else for number of dice
                if self.one_.isChecked():
                    dice1 = randint(1, 8)

                elif self.two_.isChecked():
                    dice1 = randint(1, 8)
                    dice2 = randint(1, 8)

                elif self.three_.isChecked():
                    dice1 = randint(1, 8)
                    dice2 = randint(1, 8)
                    dice3 = randint(1, 8)

                elif self.four_.isChecked():
                    dice1 = randint(1, 8)
                    dice2 = randint(1, 8)
                    dice3 = randint(1, 8)
                    dice4 = randint(1, 8)

            ##D6 roll generation
            elif self.Dice6.isChecked():
                self.output_label.setText(f'')
                ##if else for number of dice
                if self.one_.isChecked():
                    dice1 = randint(1, 6)

                elif self.two_.isChecked():
                    dice1 = randint(1, 6)
                    dice2 = randint(1, 6)

                elif self.three_.isChecked():
                    dice1 = randint(1, 6)
                    dice2 = randint(1, 6)
                    dice3 = randint(1, 6)

                elif self.four_.isChecked():
                    dice1 = randint(1, 6)
                    dice2 = randint(1, 6)
                    dice3 = randint(1, 6)
                    dice4 = randint(1, 6)

            ##D4 roll generation
            elif self.Dice4.isChecked():
                self.output_label.setText(f'')
                ##if else for number of dice
                if self.one_.isChecked():
                    dice1 = randint(1, 4)

                elif self.two_.isChecked():
                    dice1 = randint(1, 4)
                    dice2 = randint(1, 4)

                elif self.three_.isChecked():
                    dice1 = randint(1, 4)
                    dice2 = randint(1, 4)
                    dice3 = randint(1, 4)

                elif self.four_.isChecked():
                    dice1 = randint(1, 4)
                    dice2 = randint(1, 4)
                    dice3 = randint(1, 4)
                    dice4 = randint(1, 4)

            ##Actual rolls:

            ##Error/dice number limiting
            if self.Dice100.isChecked() and (self.two_.isChecked() or self.three_.isChecked() or self.four_.isChecked()):
                self.output_dice.setText(f'')
                self.output_label.setText(f'Only 1 D100 can be rolled at a time')

            elif self.Dice20.isChecked() and (self.three_.isChecked() or self.four_.isChecked()):
                self.output_dice.setText(f'')
                self.output_label.setText(f'Only 1 or 2 D20s can be rolled at a time')

            ##outputs the two individual D20 values as individual rolls
            elif self.two_.isChecked() and self.Dice20.isChecked():
                total_roll1 = dice1 + modifier
                total_roll2 = dice2 + modifier
                self.output_dice.setText(f'Dice 1 = {dice1}\nDice 2 = {dice2}\nModifier = {modifier}\nRoll total 1 = {total_roll1}\nRoll total 2 = {total_roll2}')

            ##Labeled differently as "Dice 1" doesn't make sense
            elif self.one_.isChecked():
                total_roll = dice1 + modifier
                self.output_dice.setText(f'Dice Roll = {dice1}\nModifier = {modifier}\nRoll total = {total_roll}')

            ##the rest of the elifs create a total from all the dice rolls as they would likely be damage and need a sum
            elif self.two_.isChecked():
                total_roll = dice1 + dice2 + modifier
                self.output_dice.setText(f'Dice 1 = {dice1}\nDice 2 = {dice2}\nModifier = {modifier}\nRoll Total = {total_roll}')

            elif self.three_.isChecked():
                total_roll = dice1 + dice2 + dice3 + modifier
                self.output_dice.setText(f'Dice 1 = {dice1}\nDice 2 = {dice2}\nDice 3 = {dice3}\nModifier = {modifier}\nRoll Total = {total_roll}')

            elif self.four_.isChecked():
                total_roll = dice1 + dice2 + dice3 + dice4 + modifier
                self.output_dice.setText(f'Dice 1 = {dice1}\nDice 2 = {dice2}\nDice 3 = {dice3}\nDice 4 = {dice4}\nModifier = {modifier}\nRoll Total = {total_roll}')

        ##Exception for if a non-int is entered for the modifier value
        except ValueError:
            self.output_dice.setText(f'')
            self.output_label.setText(f'Please enter a whole number for the modifier')

    ##Setting up the clear button, it sets the default radio buttons to D20 and 1 and clears labels to the opening message
    def clear_button(self):
        self.modifier.setText('')
        self.Dice20.setChecked(True)
        self.Dice100.setChecked(False)
        self.Dice12.setChecked(False)
        self.Dice10.setChecked(False)
        self.Dice8.setChecked(False)
        self.Dice6.setChecked(False)
        self.Dice4.setChecked(False)
        self.one_.setChecked(True)
        self.two_.setChecked(False)
        self.three_.setChecked(False)
        self.four_.setChecked(False)
        self.output_dice.setText(f'')
        self.output_label.setText(f'Use radio buttons to pick dice type, enter how many dice you want to roll,\n and add any relevant modifiers\n\nNote: Please use integers when typing \nD12-D4 are set up for damage rolls')
