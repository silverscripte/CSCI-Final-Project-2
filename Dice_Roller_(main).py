from dice_gui_controller import *

##The main function that initializes the whole GUI
def main():
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()