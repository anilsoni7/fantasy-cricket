# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\anacondaproj\fantasy Cricket\fantasycricket.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import json
from Dialog import Dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selection_label = QtWidgets.QLabel(self.centralwidget)
        self.selection_label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.selection_label.setObjectName("selection_label")
        self.batsman_label = QtWidgets.QLabel(self.centralwidget)
        self.batsman_label.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.batsman_label.setObjectName("batsman_label")
        self.batsman = QtWidgets.QLabel(self.centralwidget)
        self.batsman.setGeometry(QtCore.QRect(110, 50, 21, 16))
        self.batsman.setObjectName("batsman")
        self.bowler_label = QtWidgets.QLabel(self.centralwidget)
        self.bowler_label.setGeometry(QtCore.QRect(140, 50, 71, 16))
        self.bowler_label.setObjectName("bowler_label")
        self.bowler = QtWidgets.QLabel(self.centralwidget)
        self.bowler.setGeometry(QtCore.QRect(220, 50, 21, 16))
        self.bowler.setObjectName("bowler")
        self.allrounder_label = QtWidgets.QLabel(self.centralwidget)
        self.allrounder_label.setGeometry(QtCore.QRect(250, 50, 81, 16))
        self.allrounder_label.setObjectName("allrounder_label")
        self.allrounder = QtWidgets.QLabel(self.centralwidget)
        self.allrounder.setGeometry(QtCore.QRect(340, 50, 21, 16))
        self.allrounder.setObjectName("allrounder")
        self.wicket_keeper_label = QtWidgets.QLabel(self.centralwidget)
        self.wicket_keeper_label.setGeometry(QtCore.QRect(370, 50, 101, 16))
        self.wicket_keeper_label.setObjectName("wicket_keeper_label")
        self.wicket_keeper = QtWidgets.QLabel(self.centralwidget)
        self.wicket_keeper.setGeometry(QtCore.QRect(480, 50, 21, 16))
        self.wicket_keeper.setObjectName("wicket_keeper")
        self.points_available_label = QtWidgets.QLabel(self.centralwidget)
        self.points_available_label.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.points_available_label.setObjectName("points_available_label")
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(110, 90, 31, 16))
        self.points_available.setObjectName("points_available")
        self.points_used_label = QtWidgets.QLabel(self.centralwidget)
        self.points_used_label.setGeometry(QtCore.QRect(290, 90, 81, 16))
        self.points_used_label.setObjectName("points_used_label")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(350, 90, 31, 16))
        self.points_used.setObjectName("points_used")
        self.points_available_frame = QtWidgets.QFrame(self.centralwidget)
        self.points_available_frame.setGeometry(QtCore.QRect(30, 110, 211, 231))
        self.points_available_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.points_available_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.points_available_frame.setObjectName("points_available_frame")
        self.allrounder_radio = QtWidgets.QRadioButton(self.points_available_frame)
        self.allrounder_radio.setGeometry(QtCore.QRect(111, 10, 42, 17))
        self.allrounder_radio.setObjectName("allrounder_radio")
        self.bowler_radio = QtWidgets.QRadioButton(self.points_available_frame)
        self.bowler_radio.setGeometry(QtCore.QRect(58, 10, 47, 17))
        self.bowler_radio.setObjectName("bowler_radio")
        self.batsman_radio = QtWidgets.QRadioButton(self.points_available_frame)
        self.batsman_radio.setGeometry(QtCore.QRect(10, 10, 42, 17))
        self.batsman_radio.setObjectName("batsman_radio")
        self.wicket_keeper_radio = QtWidgets.QRadioButton(self.points_available_frame)
        self.wicket_keeper_radio.setGeometry(QtCore.QRect(159, 10, 42, 17))
        self.wicket_keeper_radio.setObjectName("wicket_keeper_radio")
        self.player_available_list = QtWidgets.QListWidget(self.points_available_frame)
        self.player_available_list.setGeometry(QtCore.QRect(0, 0, 211, 241))
        self.player_available_list.setObjectName("player_available_list")
        self.player_available_list.raise_()

        # trigger the method to shift player from available to occupied
        self.player_available_list.currentRowChanged.connect(self.update_avaiable_player_list)

        self.allrounder_radio.raise_()
        self.bowler_radio.raise_()
        self.wicket_keeper_radio.raise_()
        self.batsman_radio.raise_()
        self.points_used_frame = QtWidgets.QFrame(self.centralwidget)
        self.points_used_frame.setGeometry(QtCore.QRect(290, 110, 211, 231))
        self.points_used_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.points_used_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.points_used_frame.setObjectName("points_used_frame")
        self.team_name_label = QtWidgets.QLabel(self.points_used_frame)
        self.team_name_label.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.team_name_label.setObjectName("team_name_label")
        self.team_name = QtWidgets.QLabel(self.points_used_frame)
        self.team_name.setGeometry(QtCore.QRect(88, 10, 86, 13))
        self.team_name.setObjectName("team_name")
        self.player_used_list = QtWidgets.QListWidget(self.points_used_frame)
        self.player_used_list.setGeometry(QtCore.QRect(0, 0, 211, 251))
        self.player_used_list.setObjectName("player_used_list")
        self.player_used_list.raise_()

        # trigger method to shift player to occupied to available when doubled clicked
        self.player_used_list.currentRowChanged.connect(self.update_selected_player_list)

        self.team_name_label.raise_()
        self.team_name.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menuManage_Teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        # Data holding variables
        self.__data_allrounder = None
        self.__data_bowler = None
        self.__data_wicket_keeper = None
        self.__data_batsmen = None
        self.__data_used_player = list()
        self.__data_allrounder_copy = None
        self.__data_bowler_copy = None
        self.__data_wicket_keeper_copy = None
        self.__data_batsmen_copy = None


        # value holding variables
        self.__data_bowler_value = None
        self.__data_batsmen_value = None
        self.__data_wicket_keeper_value = None
        self.__data_allrounder_value = None
        self.__data_used_player_value = list()
        self.__data_player_info = list()

        # databse credentials
        self.__database_name = "fantasy-cricket1.db"
        self.__database_connection = False

        # current radio button selected
        self.current_radio_button_selected = None

        # init dialog box class
        self.error_dialog = Dialog()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selection_label.setText(_translate("MainWindow", "Your Selection"))
        self.batsman_label.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.batsman.setText(_translate("MainWindow", "0"))
        self.bowler_label.setText(_translate("MainWindow", "Bowler (BOW)"))
        self.bowler.setText(_translate("MainWindow", "0"))
        self.allrounder_label.setText(_translate("MainWindow", "Allrounder (AR)"))
        self.allrounder.setText(_translate("MainWindow", "0"))
        self.wicket_keeper_label.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.wicket_keeper.setText(_translate("MainWindow", "0"))
        self.points_available_label.setText(_translate("MainWindow", "Points Available"))
        self.points_available.setText(_translate("MainWindow", "0"))
        self.points_used_label.setText(_translate("MainWindow", "Points Used"))
        self.points_used.setText(_translate("MainWindow", "0"))
        self.allrounder_radio.setText(_translate("MainWindow", "AR"))

        # trigger show_allrounders method when allrounder_radio is clicked
        self.allrounder_radio.clicked.connect(self.show_allrounders)
        
        self.bowler_radio.setText(_translate("MainWindow", "BOW"))

        # trigger show_bowlers method when bowler_radio is clicked
        self.bowler_radio.clicked.connect(self.show_bowlers)

        self.batsman_radio.setText(_translate("MainWindow", "BAT"))

        # trigger show_batsmen method when batsman_radio is clicked
        self.batsman_radio.clicked.connect(self.show_batsmen)
        
        self.wicket_keeper_radio.setText(_translate("MainWindow", "WK"))

        # trigger show_wicket_keepers method when wicket_keeper_radio is clicke
        self.wicket_keeper_radio.clicked.connect(self.show_wicket_keepers)

        self.team_name_label.setText(_translate("MainWindow", "Team Name"))
        self.team_name.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionNew_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))

        # trigger method to create new team
        self.actionNew_Team.triggered.connect(self.new_team)

        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))

        #trigger method to open a saved team
        self.actionOpen_Team.triggered.connect(self.open_team)

        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionSave_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        #trigger method to save a team
        self.actionSave_Team.triggered.connect(self.save_team)
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionEvaluate_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))

        # trigger method to evaluate a team
        self.actionEvaluate_Team.triggered.connect(self.evaluate_team)

        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        # trigger method to ask confirmation to quit game
        self.actionQuit.triggered.connect(self.quit)

    def new_team(self):
        try:
                team_name, okPressed = QtWidgets.QInputDialog.getText(self.centralwidget , "Get Team name",
                                                                      "Enter Team name :",
                                                                      QtWidgets.QLineEdit.Normal, "")

                if okPressed and team_name != '':
                    # Reset current UI for new team selection by user
                    self.reset_ui()
                    self.team_name.setText( str(team_name))
                    self.points_available.setText(str(1000))#set font color different than black same for points used
        except:
            print("error")

    def open_team(self):
        try:
            file_name,_= QtWidgets.QFileDialog.getOpenFileName(None,'Open File',
                                                               options=QtWidgets.QFileDialog.DontUseNativeDialog)

            with open(file_name,'r') as file:
                self.team_name.setText(str(file.readline()))
                self.batsman.setText(str(file.readline()))
                self.bowler.setText( str(file.readline()))
                self.allrounder.setText(file.readline())
                self.wicket_keeper.setText( str(file.readline()))
                self.points_available.setText( str(file.readline()))
                self.points_used.setText( str(file.readline()))
                self.__data_batsmen =  json.loads(file.readline()) or list()
                self.__data_batsmen_copy =  json.loads(file.readline()) or list()
                self.__data_batsmen_value =  json.loads(file.readline()) or list()
                self.__data_bowler =  json.loads(file.readline()) or list()
                self.__data_bowler_copy =  json.loads(file.readline()) or list()
                self.__data_bowler_value =  json.loads(file.readline()) or list()
                self.__data_allrounder =  json.loads(file.readline()) or list()
                self.__data_allrounder_copy =  json.loads(file.readline()) or list()
                self.__data_allrounder_value =  json.loads(file.readline()) or list()
                self.__data_wicket_keeper =  json.loads(file.readline()) or list()
                self.__data_wicket_keeper_copy =  json.loads(file.readline()) or list()
                self.__data_wicket_keeper_value =  json.loads(file.readline()) or list()
                self.__data_used_player = json.loads(file.readline()) or list()
                self.__data_used_player_value =  json.loads(file.readline()) or list()
                
                self.show_batsmen()
                self.show_used_players()
        except:
            self.error_dialog.set_title("Invalid File")
            self.error_dialog.error("The file you selected is invalid")
            print("file open error")

    def save_team(self):
        try:
            file_name, okPressed = QtWidgets.QInputDialog.getText(self.centralwidget, "Get File name",
                                                                  "Enter File name :", QtWidgets.QLineEdit.Normal, "")

            with open(file_name + ".fc",'w+') as file:
                file.write(str(self.team_name.text())+"\n")      #team name
                file.write(str(self.batsman.text())+"\n")        #selected batsman in count
                file.write(str(self.bowler.text())+"\n")         #selected bowler count
                file.write(str(self.allrounder.text())+"\n")     #selected allrounder count
                file.write(str(self.wicket_keeper.text())+"\n")  #selected wicket keeper count
                file.write(str(self.points_available.text())+"\n")#current available points
                file.write(str(self.points_used.text())+"\n")    #current used points
                file.write(json.dumps(self.__data_batsmen)+"\n") #batsman data
                file.write(json.dumps(self.__data_batsmen_copy)+"\n") # batsman copy data
                file.write(json.dumps(self.__data_batsmen_value)+"\n") #batsman value
                file.write(json.dumps(self.__data_bowler)+"\n")  #bowler data
                file.write(json.dumps(self.__data_bowler_copy)+"\n")
                file.write(json.dumps(self.__data_bowler_value)+"\n")
                file.write(json.dumps(self.__data_allrounder)+"\n")
                file.write(json.dumps(self.__data_allrounder_copy)+"\n")
                file.write(json.dumps(self.__data_allrounder_value)+"\n")
                file.write(json.dumps(self.__data_wicket_keeper)+"\n")
                file.write(json.dumps(self.__data_wicket_keeper_copy)+"\n")
                file.write(json.dumps(self.__data_wicket_keeper_value)+"\n")
                file.write(json.dumps(self.__data_used_player)+"\n")
                file.write(json.dumps(self.__data_used_player_value)+"\n")

        except:
            self.error_dialog.set_title("File Not Saved")
            self.error_dialog.error("There was error saving file")
            print("file save error")

    def evaluate_team(self):

        if len(self.__data_used_player) == 0:
            return

        players_query = """select matches.scored, matches.faced, matches.fours, matches.sixes, matches.bowled,
                            matches.maiden, matches.given, matches.wkts, matches.catches, matches.stumping,
                            matches.run_out,player_information.runs,player_information.`100s`, player_information.`50s`,
                            player_category.name,players.name
                            from players, player_category, player_information,matches
                            where player_category.id = players.category and player_information.player_id = players.id 
                            and matches.player_id = players.id"""

        self.__data_player_info = self.get_complete_data_from_database(query= players_query)

        player_names = []
        score = []
        for player in self.__data_player_info:
                batting_score = self.batting_rule(player)
                fielding_score = self.fielding_rule(player)
                bowling_score = self.bowling_rule(player)
                player_names.append(player[15])
                score.append( batting_score + fielding_score + bowling_score )

        self.error_dialog.information(score,player_names,self.__data_used_player)

    def batting_rule(self,player):
        score = 0
        if player[0] >= 2 : # 1 point for 2 runs scored
            score += 1

        if player[13] > 0 : # additional 5 point for half century
            score += 5

        if player[12] > 0 : # additional 10 points for century
            score += 10

        if player[11] >= 80 and player[11] <=100 or player[1] >=80 and player[1] <= 100 :
            # 2 points for strike rate (runs/balls faced) of 80-100
            score += 2

        if player[11] >100 or player[1] > 100 :
            # 4 points for strike rate (runs/balls faced) of 80-100
            score += 4
        if player[2] >= 1 : # 1 point for boundry (four)
            score += 1

        if player[3] >= 1: # 2 point for over boundry (six)
            score += 2

        return score

    def fielding_rule(self,player):
        score =0

        if player[8] > 0 : # 10 point for catch
            score += 10

        if player[9] > 0 : # 10 point for stumping
            score += 10

        if player[10] >0: # 10 point for run out
            score += 10

        return score

    def bowling_rule(self,player):
        score = 0
        if player[7] > 0:
            score += (10 * player[7])

        if player[7] >= 3:
            score += 5

        if player[7] >= 5:
            score += 10

        try:
            economy_rate = player[6] / (player[4] / 6)
            if economy_rate >= 3.5 and economy_rate <= 4.5:
                score += 4

            if economy_rate >= 2.0 and economy_rate <= 3.5:
                score += 7

            if economy_rate < 2.0 :
                score += 10
        except:
            pass    #Division by zero exception
        return score

    def get_complete_data_from_database(self,query=None):

        if query is None:
                print("query error")
                return

        # self.__database_connection is False when initializing so
        if not self.__database_connection or not self.__database_connection.isOpen():
                print("opening connection")
                self.connect_to_database()

        query_db = QtSql.QSqlQuery(self.__database_connection)
        player_info = []
        if query_db.exec_(query):
                while query_db.next():
                    player_info.append( ( query_db.value(0), query_db.value(1), query_db.value(2), query_db.value(3),
                                          query_db.value(4), query_db.value(5), query_db.value(6), query_db.value(7),
                                          query_db.value(8), query_db.value(9), query_db.value(10), query_db.value(11),
                                          query_db.value(12), query_db.value(13),query_db.value(14),query_db.value(15)
                                          )
                                    )
        else:
                print("sql syntax")

        return player_info

    def quit(self):
        self.error_dialog.user_quit_confirm()

    def reset_ui(self):
        self.batsman.setText("0")
        self.bowler.setText("0")
        self.allrounder.setText("0")
        self.wicket_keeper.setText("0")
        self.points_available.setText("0")
        self.points_used.setText("0")
        self.team_name.setText("##")

    def show_allrounders(self):

        self.current_radio_button_selected = "allrounder_radio"
        #all_rounder_query = "select player.name from players as player, player_category as category where
        # category.name = 'AR' and category.id = player.category"
        all_rounder_query = """select player.name,player_information.value from players as player,
                                player_category as category, player_information where category.name = 'AR' 
                                and category.id = player.category and player_information.player_id = player.id"""
        if self.__data_allrounder is None :
                self.__data_allrounder,self.__data_allrounder_value = self.get_player_name_and_value_from_database(
                                                                            query = all_rounder_query
                                                                            )
                self.__data_allrounder_copy = self.__data_allrounder.copy()

        self.player_available_list.clear()
            # leave first 2 position in list blank
        for index in range(2):
                self.player_available_list.addItem("")

        for player_name in self.__data_allrounder:
                self.player_available_list.addItem(player_name)
        
    def show_bowlers(self):
        self.current_radio_button_selected = "bowler_radio"
        #bowlers_query = "select player.name from players as player, player_category as category where
        # category.name = 'BWL' and category.id = player.category"
        bowlers_query = """select player.name,player_information.value from players as player, player_category 
                            as category, player_information where category.name = 'BWL' and 
                            category.id = player.category and player_information.player_id = player.id"""

        if self.__data_bowler is None :
            self.__data_bowler,self.__data_bowler_value = self.get_player_name_and_value_from_database(
                                                                                                query = bowlers_query
                                                                    )   #List of all available Bowlers from database
            self.__data_bowler_copy = self.__data_bowler.copy()

        self.player_available_list.clear()
        # leave first 2 position in list blank
        for index in range(2):
            self.player_available_list.addItem("")

        for player_name in self.__data_bowler:
            self.player_available_list.addItem(player_name)
        
    def show_batsmen(self):
        self.current_radio_button_selected = "batsman_radio"
        #batsmen_query = "select player.name from players as player, player_category as category where
        # category.name = 'BAT' and category.id = player.category"
        batsmen_query = """ select player.name,player_information.value from players as player, player_category
                              as category, player_information where category.name = 'BAT' and 
                              category.id = player.category and player_information.player_id = player.id"""
        if self.__data_batsmen is None :
            self.__data_batsmen, self.__data_batsmen_value = self.get_player_name_and_value_from_database(
                                                query = batsmen_query)   #List of all available batsmen from database
            self.__data_batsmen_copy = self.__data_batsmen.copy()

        self.player_available_list.clear()
        # leave first 2 position in list blank
        for index in range(2):
            self.player_available_list.addItem("")

        for player_name in self.__data_batsmen:
            self.player_available_list.addItem(player_name)

    def show_wicket_keepers(self):
        self.current_radio_button_selected = "wicket_keeper_radio"

        #wicket_keeper_query = "select player.name from players as player, player_category as category where
        # category.name = 'WK' and category.id = player.category"
        wicket_keeper_query = """select player.name,player_information.value from players as player, player_category 
                                as category, player_information where category.name = 'WK' and 
                                category.id = player.category and player_information.player_id = player.id"""
        if self.__data_wicket_keeper is None :
            self.__data_wicket_keeper,self.__data_wicket_keeper_value = self.get_player_name_and_value_from_database(
                                            query = wicket_keeper_query)   #List of all available Bowlers from database
            self.__data_wicket_keeper_copy = self.__data_wicket_keeper.copy()

        self.player_available_list.clear()

        # leave first 2 position in list blank
        for index in range(2):
            self.player_available_list.addItem("")

        for player_name in self.__data_wicket_keeper:
            self.player_available_list.addItem( player_name)

    def get_player_name_and_value_from_database(self, query=None):
        if query is None:
            print("query error")

        # self.__database_connection is False when initializing so
        if not self.__database_connection  or not self.__database_connection.isOpen():
            self.connect_to_database()

        query_db = QtSql.QSqlQuery(self.__database_connection)
        player_name =[]
        player_value = []
        if query_db.exec_(query) :
            while query_db.next():
                player_name.append((query_db.value(0)))
                player_value.append(query_db.value(1))
        else:
            print("sql syntax")

        return player_name,player_value

    def connect_to_database(self):
        self.__database_connection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.__database_connection.setDatabaseName(self.__database_name)
        self.__database_connection.open()

    def update_available_points(self,point):
        self.points_available.setText(str(point))

    def update_used_points(self,points=None):
        if points is None:
            self.points_used.setText( str( 1000 - int(self.points_available.text())) )
        else:
            self.points_used.setText(str(points))

    def update_selected_player_list(self):
        try:
            
            current_row_index = self.player_used_list.currentRow()

            if self.player_used_list.currentRow() != -1 :
                current_selected_text = self.__data_used_player[current_row_index - 2]
                current_selected_text_value = self.__data_used_player_value[current_row_index - 2]
                used_point = int(self.points_used.text()) - current_selected_text_value
                available_point = int(self.points_available.text()) + current_selected_text_value
                self.update_available_points(available_point)
                self.update_used_points(points= used_point)

                player_name = self.__data_used_player.pop(current_row_index - 2)
                self.__data_used_player_value.pop(current_row_index - 2)

                if self.__data_batsmen_copy is not None and current_selected_text in self.__data_batsmen_copy :
                    self.__data_batsmen.append(current_selected_text)
                    self.__data_batsmen_value.append(current_selected_text_value)
                    self.decrement_batsmen_count()

                elif self.__data_wicket_keeper_copy is not None and current_selected_text in  self.__data_wicket_keeper_copy :
                    self.__data_wicket_keeper.append(current_selected_text)
                    self.__data_wicket_keeper_value.append(current_selected_text_value)
                    self.decrement_wicket_keeper_count()

                elif self.__data_bowler_copy is not None and current_selected_text in self.__data_bowler_copy:
                    self.__data_bowler.append(current_selected_text)
                    self.__data_bowler_value.append(current_selected_text_value)
                    self.decrement_bowler_count()

                else:
                    self.__data_allrounder.append(current_selected_text)
                    self.__data_allrounder_value.append(current_selected_text_value)
                    self.decrement_all_rounder_count()

            self.show_used_players()
        except:
            pass



    def update_avaiable_player_list(self):
        try:
            current_row_index = self.player_available_list.currentRow()

            if len(self.__data_used_player) > 11:
                self.show_maximun_team_player_error()
                return

            if self.player_available_list.currentRow() != -1 :

                if self.current_radio_button_selected == "bowler_radio":
                    current_selected_text = self.__data_bowler[current_row_index - 2]
                    current_selected_text_value = self.__data_bowler_value[current_row_index - 2]
                    values = int(self.points_available.text()) - current_selected_text_value
                    if values < 0:
                        self.show_inefficient_points_error()
                        return

                    self.update_available_points(values)
                    self.update_used_points()
                    self.__data_used_player.append(current_selected_text)
                    self.remove_player_from_available_list(current_selected_text)
                    index = self.__data_bowler_value.index(current_selected_text_value)
                    self.__data_used_player_value.append(self.__data_bowler_value.pop(index))
                    self.increment_bowler_count()
                    self.show_bowlers()

                elif self.current_radio_button_selected == "batsman_radio":
                    current_selected_text = self.__data_batsmen[current_row_index - 2]
                    current_selected_text_value = self.__data_batsmen_value[current_row_index - 2]
                    values = int(self.points_available.text()) - current_selected_text_value
                    if values < 0:
                        self.show_inefficient_points_error()
                        return

                    self.update_available_points(values)
                    self.update_used_points()
                    self.__data_used_player.append(current_selected_text)
                    self.remove_player_from_available_list(current_selected_text)
                    index = self.__data_batsmen_value.index(current_selected_text_value)
                    self.__data_used_player_value.append(self.__data_batsmen_value.pop(index))
                    self.show_batsmen()
                    self.increment_batsmen_count()

                elif self.current_radio_button_selected == "wicket_keeper_radio":
                    if self.wicket_keeper.text() == "1":
                        self.show_wicket_keeper_error()
                    else:
                        current_selected_text = self.__data_wicket_keeper[current_row_index - 2]
                        current_selected_text_value = self.__data_wicket_keeper_value[current_row_index - 2]
                        values = int(self.points_available.text()) - current_selected_text_value
                        if values < 0:
                            self.show_inefficient_points_error()
                            return

                        self.update_available_points(values)
                        self.update_used_points()
                        self.__data_used_player.append(current_selected_text)
                        self.remove_player_from_available_list(current_selected_text)
                        self.__data_used_player_value.append(self.__data_wicket_keeper_value.pop(current_row_index - 2))
                        self.show_wicket_keepers()
                        self.increment_wicket_keeper_count()

                elif self.current_radio_button_selected == "allrounder_radio":   # All rounder radio selected
                    current_selected_text = self.__data_allrounder[current_row_index - 2]
                    current_selected_text_value = self.__data_allrounder_value[current_row_index - 2]
                    values = int(self.points_available.text()) - current_selected_text_value
                    if values < 0:
                        self.show_inefficient_points_error()
                        return

                    self.update_available_points(values)
                    self.update_used_points()
                    self.__data_used_player.append(current_selected_text)
                    self.remove_player_from_available_list(current_selected_text)
                    self.__data_used_player_value.append(self.__data_allrounder_value.pop(current_row_index - 2))
                    self.show_allrounders()
                    self.increment_all_rounder_count()
                else:
                    print("error")
                self.show_used_players()
                return
        except:
                pass

    def show_inefficient_points_error(self):
        self.error_dialog.set_title("inefficient error")
        self.error_dialog.error("inefficient points")

    def show_maximun_team_player_error(self):

        self.error_dialog.set_title("Maximum players")
        self.error_dialog.error("Maximum Player Selected")

    def show_wicket_keeper_error(self):
        self.error_dialog.set_title("Wicket Keeper error")
        self.error_dialog.error("Maximum 1 wicket keeper can only be selected")


    def show_used_players(self):
        self.player_used_list.clear()

        # leave first 2 position in list blank
        for index in range(2):
            self.player_used_list.addItem("")

        for player_name in self.__data_used_player:
            self.player_used_list.addItem(player_name)


    def increment_wicket_keeper_count(self):
        current_count = int(self.wicket_keeper.text())
        self.wicket_keeper.setText(str(current_count+1))

    def decrement_wicket_keeper_count(self):
        current_count = int(self.wicket_keeper.text())
        self.wicket_keeper.setText(str(current_count - 1))

    def increment_batsmen_count(self):
        current_count = int(self.batsman.text())
        self.batsman.setText(str(current_count+ 1))

    def decrement_batsmen_count(self):
        current_count = int(self.batsman.text())
        self.batsman.setText(str(current_count - 1))

    def increment_all_rounder_count(self):
        current_count = int(self.allrounder.text())
        self.allrounder.setText(str(current_count + 1))

    def decrement_all_rounder_count(self):
        current_count = int(self.allrounder.text())
        self.allrounder.setText(str(current_count - 1))

    def increment_bowler_count(self):
        current_count = int(self.bowler.text())
        self.bowler.setText(str(current_count + 1))

    def decrement_bowler_count(self):
        current_count = int(self.bowler.text())
        self.bowler.setText(str(current_count - 1))

    def remove_player_from_available_list(self,player_name):
        index = None
        if self.current_radio_button_selected == "bowler_radio":
            index = self.__data_bowler.index(player_name)

            if index != -1 :
                self.__data_bowler.pop(index)

        elif self.current_radio_button_selected == "batsman_radio":
            index = self.__data_batsmen.index(player_name)
            if index != -1:
                self.__data_batsmen.pop(index)

        elif self.current_radio_button_selected == "wicket_keeper_radio":
            index = self.__data_wicket_keeper.index(player_name)
            if index != -1:
                self.__data_wicket_keeper.pop(index)

        else:   # All rounder radio selected
            index = self.__data_allrounder.index(player_name)
            if index != -1:
                self.__data_allrounder.pop(index)
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

