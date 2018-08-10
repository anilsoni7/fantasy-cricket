from PyQt5.QtWidgets import QWidget,QMessageBox
import sys
class Dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.left = 450
        self.top = 250
        self.width = 320
        self.height = 200
        #self.initUI()


    def set_title(self,title):
        self.title = title

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    def error(self,message):
        self.initUI()

        buttonReply = QMessageBox.critical(self, self.title, message,
                                               QMessageBox.Ok)


    def information(self,score,player_names,selected_players):
        self.initUI()
        display_info = ""
        total_score = 0
        for name in selected_players:
            display_info += str(str(name) + " :\t " +str(score[player_names.index(name)])) + "\n"
            total_score += score[player_names.index(name)]

        display_info += str( "Total Team Score : {}".format(total_score))

        buttonReply = QMessageBox.information(self, self.title, display_info,
                                                     QMessageBox.Ok)

    def user_quit_confirm(self):
        self.initUI()
        buttonReply = QMessageBox.question(self, 'Quit', "Are you sure you want to quit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            sys.exit(0)
            sys.exit(0)