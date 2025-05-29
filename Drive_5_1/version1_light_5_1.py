# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_new.ui'
#
# Created: Tue Apr 28 12:59:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from PySide2.QtWebEngineWidgets import QWebEngineView


#Class created for the temperature control in screen bottom right

class TemperatureControl(QtWidgets.QWidget):
    temperature_changed = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        #Layout for the temperature control
        #self.setFixedSize(300,150)

        self.layout = QtWidgets.QHBoxLayout(self)

        # Create the "-" button
        self.minus_button = QtWidgets.QPushButton("-")
        self.minus_button.setFixedSize(75, 75)
        self.minus_button.setStyleSheet(""" QPushButton{
                                            background-color: white;
                                            color:blue;
                                            font-size: 40px;
        }""")
        self.minus_button.clicked.connect(self.decrease_temp)
        self.layout.addWidget(self.minus_button)

        # Create the label to display temperature
        self.temperature_label = QtWidgets.QLabel("20°")
        self.temperature_label.setFixedSize(120, 75)
        self.temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label.setStyleSheet(""" QLabel{
                                                    background-color: #dceaf7;
                                                    color:black;
                                                    font-size: 40px;
                }""")
        self.layout.addWidget(self.temperature_label)

        # Create the "+" button
        self.plus_button = QtWidgets.QPushButton("+")
        self.plus_button.setFixedSize(75, 75)
        self.plus_button.setStyleSheet(""" QPushButton{
                                                    background-color: white;
                                                    color:red;
                                                    font-size: 40px;
                }""")
        self.plus_button.clicked.connect(self.increase_temp)
        self.layout.addWidget(self.plus_button)

        # Set the initial temperature value
        self.current_temperature = 20

    def increase_temp(self):
    # Increase temperature and update the label
        if self.current_temperature < 25:  # Ensure max limit
            self.current_temperature += 1
            self.update_temperature_label()
            self.temperature_changed.emit(self.current_temperature)

    def decrease_temp(self):
    # Decrease temperature and update the label
        if self.current_temperature > 18:  # Ensure min limit
            self.current_temperature -= 1
            self.update_temperature_label()
            self.temperature_changed.emit(self.current_temperature)

    def update_temperature_label(self):
        # Update the temperature label to show the current temperature
        self.temperature_label.setText(f"{self.current_temperature}°")


class CustomSlider(QtWidgets.QSlider):
    def mousePressEvent(self, event):
        # Override the default mouse press event
        super().mousePressEvent(event)  # Call the default implementation

        # Calculate the new position based on mouse click
        if event.button() == QtCore.Qt.LeftButton:
            # Get the pixel position of the mouse relative to the slider
            pos = event.pos().x()

            # Map the pixel position to slider value
            new_value = QtWidgets.QStyle.sliderValueFromPosition(
                self.minimum(),
                self.maximum(),
                pos,
                self.width()
            )

            # Set the slider to the calculated value
            self.setValue(new_value)

class Ui_MainWindow(object):

    def __init__(self):
        self.video_widget = None
        self.video_player = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # sets the object name for the MainWindow
        MainWindow.setEnabled(True)  # Enables the MainWindow

        MainWindow.resize(1045, 765)  # Sets the size of the mainwindow
        MainWindow.setStyleSheet("")  # sets the stylesheet(currently empty)

        # creates the central widget
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")


        # frame with home options (slide 1)
        self.home_frame = self.create_frame(self.centralWidget, 670, 410, 611, 231, "",
                                            "home_frame")
        self.home_frame.setStyleSheet("""
            QFrame {
                background-color: transparent; /* Transparent background */
                border: 1px solid black; /* Black border around the frame */
            }
        """)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.home_frame)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")

        self.home_buttons_blue_highlight = []
        self.home_buttons_bottom_highlight = []

        self.add_h1_home(self.verticalLayout_1, self.home_frame)
        self.add_h2_home(self.verticalLayout_1, self.home_frame)
        self.add_h3_home(self.verticalLayout_1, self.home_frame)
        self.add_h4_home(self.verticalLayout_1, self.home_frame)
        self.add_h5_home(self.verticalLayout_1, self.home_frame)


        #frame with lighting options (slide 2)
        self.light_frame = self.create_frame(self.centralWidget, 670, 410, 611, 231, '', "name: light_frame")
        self.light_frame.setStyleSheet("""
            QFrame {
                background-color: transparent; /* Transparent background */
                border: 1px solid black; /* Black border around the frame */
            }
        """)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.light_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.light_buttons_blue_highlight = []
        self.light_buttons_bottom_highlight = []

        self.add_h1_light(self.verticalLayout_2, self.light_frame)
        self.add_h2_light(self.verticalLayout_2, self.light_frame)
        self.add_h3_light(self.verticalLayout_2, self.light_frame)
        self.add_h4_light(self.verticalLayout_2, self.light_frame)
        self.add_h5_light(self.verticalLayout_2, self.light_frame)

        # ---------------------------------------------------------------------------------------------------------------
        #frame with wiper options (slide 3)
        self.wiper_frame = self.create_frame(self.centralWidget, 670, 410, 611, 231,  "", "wiper_frame")
        self.wiper_frame.setStyleSheet("""
            QFrame {
                background-color: transparent; /* Transparent background */
                border: 1px solid black; /* Black border around the frame */
            }
        """)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wiper_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.add_h1_wiper(self.verticalLayout_3, self.wiper_frame)
        self.add_h2_wiper(self.verticalLayout_3, self.wiper_frame)
        self.add_h3_wiper(self.verticalLayout_3, self.wiper_frame)
        self.add_h4_wiper(self.verticalLayout_3, self.wiper_frame)
        self.add_h5_wiper(self.verticalLayout_3, self.wiper_frame)


        # frame with climate control (slide 4)
        self.climate_frame = self.create_frame(self.centralWidget, 670, 410, 611, 231, "background-color: yellow;",
                                               "climate_frame")
        self.climate_frame.setObjectName("climate_frame")

        self.climate_frame.setStyleSheet(
            "QFrame#climate_frame {"  # Apply only to climate_frame
            "background-color: #D9D9D9;"  # Set the solid color
            "border: 1px solid black;"  # Add 1px solid black border
            "}"
        )

        # Create the version label for the climate frame
        self.version_label = QtWidgets.QLabel("Software v1.0.1", self.climate_frame)
        self.version_label.setStyleSheet("color:  #555555; font-size: 29px; font-family: Arial;")
        self.version_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # Position the label in the top-right corner
        self.version_label.setGeometry(self.climate_frame.width() - 230, 40, 220, 40)

        # Ensure the label adjusts when resized
        self.climate_frame.resizeEvent = lambda event: self.version_label.setGeometry(self.climate_frame.width() - 230,
                                                                                      40, 220, 40)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.climate_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.add_horizontal_sublayout_1(self.verticalLayout_4, self.climate_frame)
        self.add_horizontal_sublayout_2(self.verticalLayout_4, self.climate_frame)
        self.add_horizontal_sublayout_3(self.verticalLayout_4, self.climate_frame)
        self.add_horizontal_sublayout_4(self.verticalLayout_4, self.climate_frame)
        self.add_horizontal_sublayout_5(self.verticalLayout_4, self.climate_frame)


        # frame with climate control (slide 5)
        # self.fan_frame = self.create_frame(self.centralWidget, 670, 410, 611, 231, "", "fan_frame")
        self.fan_background_frame = QtWidgets.QFrame(self.centralWidget)
        self.fan_background_frame.setGeometry(
            QtCore.QRect(400, 750, 480, 180))  # Slightly larger dimensions than fan_frame
        self.fan_background_frame.setStyleSheet("background-color: white;")  # Solid white background
        self.fan_background_frame.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)  # Does not block clicks

        # Fan control frame (actual control elements)
        self.fan_frame = QtWidgets.QFrame(self.centralWidget)
        self.fan_frame.setGeometry(QtCore.QRect(670, 410, 611, 231))  # Original dimensions
        self.fan_frame.setStyleSheet("background-color: none;")  # No additional background, just for controls

        #self.fan_frame.setStyleSheet("QFrame {"
        #                                 "background-image: url('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/map_2.png');"
        #                                 "background-position: center;"
        #                                 "}"
        #                                )


        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fan_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.add_h1_fan(self.verticalLayout_5, self.fan_frame)
        self.add_h2_fan(self.verticalLayout_5, self.fan_frame)
        self.add_h3_fan(self.verticalLayout_5, self.fan_frame)
        self.add_h4_fan(self.verticalLayout_5, self.fan_frame)
        self.add_h5_fan(self.verticalLayout_5, self.fan_frame)

        # set the central widget of the mainwindow to the centralWidget
        MainWindow.setCentralWidget(self.centralWidget)
        # call retranslateUi method to set text for all widgets and connect slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_frame(self, parent, x, y, width, height, style_sheet, name):
        frame = QtWidgets.QFrame(parent)
        frame.setGeometry(QtCore.QRect(x, y, width, height))
        frame.setStyleSheet(style_sheet)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName(name)
        return frame

    def add_h1_light(self, parent_layout, frame):
        self.h1_light = QtWidgets.QHBoxLayout()
        self.h1_light.setObjectName("h1_light")

        self.h1_light_button_left_arrow = QtWidgets.QPushButton(frame) # Create button
        self.h1_light_button_right_arrow = QtWidgets.QPushButton(frame)
        self.h1_light_button_left_arrow.setFixedSize(199, 200)  # set size
        self.h1_light_button_right_arrow.setFixedSize(199, 200)

        self.h1_light_button_left_arrow.setObjectName("h1_light Button Left Arrow")  # set name
        self.h1_light_button_right_arrow.setObjectName("h1_light Button Right Arrow")

        self.h1_light_button_left_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/left_arrow.png'))  # set icon
        self.h1_light_button_left_arrow.setIconSize(QSize(180, 180))
        self.h1_light_button_right_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/right_arrow.png'))
        self.h1_light_button_right_arrow.setIconSize(QSize(180, 180))

        self.h1_light_button_left_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.h1_light_button_right_arrow.setFocusPolicy(QtCore.Qt.NoFocus)

        self.h1_light_button_left_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;  /* Set background color */
                border: none;             /* Remove all borders */
            }
        """)
        self.h1_light_button_right_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;  /* Set background color */
                border: none;             /* Remove all borders */
            }
        """)

        # Create the vertical line
        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)  # Set the frame shape to a vertical line
        vertical_line.setFrameShadow(QtWidgets.QFrame.Plain)  # Use a plain line
        vertical_line.setStyleSheet("border: 1px solid black;")  # Set the line color and width
        vertical_line.setFixedHeight(200)  # Set the height of the line
        vertical_line.setFixedWidth(1)  # Set the width of the line

        self.h1_light_button_spacer = QtWidgets.QPushButton(frame)
        self.h1_light_button_spacer.setFixedSize(2, 200)
        self.h1_light_button_spacer.setObjectName("Spacer")
        self.h1_light_button_spacer.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* Remove all other borders */
                border-left: 1px solid black;  /* Add left border */
            }
        """)

        self.h1_light.addWidget(self.h1_light_button_left_arrow)
        self.h1_light.addWidget(vertical_line)
        self.h1_light.addWidget(self.h1_light_button_right_arrow)  # add to layout
        self.h1_light.addWidget(self.h1_light_button_spacer)

        spacer_h1_light_1 = QtWidgets.QSpacerItem(1000,200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h1_light.addItem(spacer_h1_light_1)
        parent_layout.addLayout(self.h1_light)

        self.light_buttons_blue_highlight.append(self.h1_light_button_left_arrow)
        self.light_buttons_blue_highlight.append(self.h1_light_button_left_arrow)

    def add_h2_light(self,parent_layout,frame):
        self.h2_light = QtWidgets.QHBoxLayout()
        self.h2_light.setObjectName("h2_light")

        self.h2_light_button_label = QtWidgets.QPushButton(frame)  # Create button
        self.h2_light_button_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.h2_light_button_label.setFixedSize(400, 277)
        self.h2_light_button_label.setObjectName("h2_light Label Button")
        self.h2_light_button_label.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/time.png'))  # add icon
        self.h2_light_button_label.setIconSize(QSize(700, 400))
        self.h2_light.addWidget(self.h2_light_button_label)  # add to layout

        self.h2_light_button_label.setStyleSheet("""
            background-color: white;
            border: none;
            border-top: 1px solid black;
            border-right: 1px solid black;
            border-bottom: 1px solid black;
        """)

        spacer_h2_light_1 = QtWidgets.QSpacerItem(1920, 100, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum) # add spacer
        self.h2_light.addItem(spacer_h2_light_1)
        parent_layout.addLayout(self.h2_light)  # Add to the vertical layout

        #self.h2_light_button_extra = QtWidgets.QPushButton(frame)  # Create button
        #self.h2_light_button_extra.setFixedSize(400, 300)
        #self.h2_light_button_extra.setStyleSheet("background-color: white;")  # button color
        #parent_layout.addWidget(self.h2_light_button_extra)  # add button to layout

    def add_h3_light(self, parent_layout, frame):
        self.h3_light = QtWidgets.QHBoxLayout()

        self.h3_light_button_home = QtWidgets.QPushButton(frame)  # Create button
        self.h3_light_button_home.setFixedSize(400, 251)  # set size
        self.h3_light_button_home.setObjectName("h3_light Home Button")  # set name
        self.h3_light_button_home.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/home.png'))
        self.h3_light_button_home.setIconSize(QSize(300, 180))

        self.h3_light_button_home.setStyleSheet("background-color: white;")

        self.h3_light.addWidget(self.h3_light_button_home)  # add button to layout

        spacer_h3_light_1 = QtWidgets.QSpacerItem(200, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_light.addItem(spacer_h3_light_1)
        spacer_h3_light_2 = QtWidgets.QSpacerItem(1900, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_light.addItem(spacer_h3_light_2)

        parent_layout.addLayout(self.h3_light)  # Add to the vertical layout

    def add_h4_light(self, parent_layout, frame):
        self.h4_light = QtWidgets.QHBoxLayout()

        # First horizontal layout (left side)
        self.h4_light_leftLayout = QtWidgets.QHBoxLayout()
        self.h4_light_button_wiper = QtWidgets.QPushButton(frame)  # create button
        self.h4_light_button_light = QtWidgets.QPushButton(frame)
        self.h4_light_button_wiper.setFixedSize(200, 200)  # fix size of button
        self.h4_light_button_light.setFixedSize(200, 200)  #
        self.h4_light_button_light.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/light_bulb.png'))  # set icon for button
        self.h4_light_button_light.setIconSize(QSize(180, 180))
        self.h4_light_button_wiper.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiper.png'))
        self.h4_light_button_wiper.setIconSize(QSize(180, 180))

        self.h4_light_button_wiper.setStyleSheet("background-color: white;")  # button color
        self.h4_light_button_light.setStyleSheet("background-color: #0070c0;")

        self.h4_light_leftLayout.addWidget(self.h4_light_button_wiper)
        self.h4_light_leftLayout.addWidget(self.h4_light_button_light)

        # Add left frame to main layout
        self.h4_light.addLayout(self.h4_light_leftLayout)

        # Second vertical layout (right side)
        self.h4_light_rightLayout = QtWidgets.QVBoxLayout()

        # Second horizontal layout (within right side)
        self.h4_light_rightTopLayout = QtWidgets.QHBoxLayout()

        # Add spacer item to top right layout
        spacer_h4_light_1 = QtWidgets.QSpacerItem(500, 80, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.h4_light_rightTopLayout.addSpacerItem(spacer_h4_light_1)

        # Third horizontal layout (within right side)
        self.h4_light_rightBottomLayout = QtWidgets.QHBoxLayout()

        # extra buttons related to light options
        self.h4_light_button_light_off = QtWidgets.QPushButton(frame)  # create button
        self.h4_light_button_beam = QtWidgets.QPushButton(frame)
        self.h4_light_button_blinker = QtWidgets.QPushButton(frame)
        self.h4_light_button_beam_off = QtWidgets.QPushButton(frame)

        self.h4_light_button_light_off.setFixedSize(150, 120)  # set size
        self.h4_light_button_beam.setFixedSize(150, 120)
        self.h4_light_button_blinker.setFixedSize(150, 120)
        self.h4_light_button_beam_off.setFixedSize(150, 120)

        self.h4_light_button_light_off.setObjectName("Light Off Button")  # set name
        self.h4_light_button_beam.setObjectName("Beam Button")
        self.h4_light_button_beam_off.setObjectName("Beam Off Button")
        self.h4_light_button_blinker.setObjectName("Blinker Button")

        self.h4_light_button_light_off.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/lightoff.png'))
        self.h4_light_button_light_off.setIconSize(QSize(150, 150))
        self.h4_light_button_beam.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/auto.png'))
        self.h4_light_button_beam.setIconSize(QSize(100, 100))
        self.h4_light_button_blinker.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/blinkers.png'))
        self.h4_light_button_blinker.setIconSize(QSize(100, 100))
        self.h4_light_button_beam_off.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/lowbeam.png'))
        self.h4_light_button_beam_off.setIconSize(QSize(100, 100))

        self.h4_light_button_light_off.setStyleSheet("background-color: white;")
        self.h4_light_button_beam.setStyleSheet("background-color: white;")
        self.h4_light_button_beam_off.setStyleSheet("background-color: white;")
        self.h4_light_button_blinker.setStyleSheet("background-color: white;")

        self.h4_light_rightBottomLayout.addWidget(self.h4_light_button_light_off)  # add to layout
        self.h4_light_rightBottomLayout.addWidget(self.h4_light_button_beam)
        self.h4_light_rightBottomLayout.addWidget(self.h4_light_button_blinker)
        self.h4_light_rightBottomLayout.addWidget(self.h4_light_button_beam_off)

        spacer_h4_light_2 = QtWidgets.QSpacerItem(1700, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h4_light_rightBottomLayout.addItem(spacer_h4_light_2)

        # Add top and bottom layouts to right layout
        self.h4_light_rightLayout.addLayout(self.h4_light_rightTopLayout)
        self.h4_light_rightLayout.addLayout(self.h4_light_rightBottomLayout)

        # Add right frame to main layout
        self.h4_light.addLayout(self.h4_light_rightLayout)
        parent_layout.addLayout(self.h4_light)

    def add_h5_light(self, parent_layout, frame):
        self.h5_light = QtWidgets.QHBoxLayout()

        # self.add_temperature_control(self.h5_light)

        self.h5_light_button_seat_1 = QtWidgets.QPushButton(frame)
        self.h5_light_button_seat_2 = QtWidgets.QPushButton(frame)

        self.h5_light_button_seat_1.setFixedSize(213, 150)
        self.h5_light_button_seat_2.setFixedSize(213, 150)

        self.h5_light_button_seat_1.setStyleSheet("background-color: black;")
        self.h5_light_button_seat_2.setStyleSheet("background-color: black;")

        self.h5_light_button_seat_1.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_1.png'))
        self.h5_light_button_seat_1.setIconSize(QSize(140, 140))
        self.h5_light_button_seat_2.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_2.png'))
        self.h5_light_button_seat_2.setIconSize(QSize(140, 140))

        # self.button_temp = QtWidgets.QPushButton(frame)  # Create button
        self.h5_light_button_fan = QtWidgets.QPushButton(frame)
        self.h5_light_button_AC = QtWidgets.QPushButton(frame)
        self.h5_light_button_max = QtWidgets.QPushButton(frame)
        self.h5_light_button_audio = QtWidgets.QPushButton(frame)
        self.h5_light_button_hazard = QtWidgets.QPushButton(frame)
        self.h5_light_button_phone = QtWidgets.QPushButton(frame)
        self.h5_light_button_nav = QtWidgets.QPushButton(frame)
        self.h5_light_button_settings = QtWidgets.QPushButton(frame)

        # self.button_temp.setFixedSize(300, 150)  # set size
        self.h5_light_button_fan.setFixedSize(0, 0)
        self.h5_light_button_AC.setFixedSize(213, 150)
        self.h5_light_button_max.setFixedSize(214, 150)
        self.h5_light_button_audio.setFixedSize(214, 150)
        self.h5_light_button_hazard.setFixedSize(214, 150)
        self.h5_light_button_phone.setFixedSize(213, 150)
        self.h5_light_button_nav.setFixedSize(213, 150)
        self.h5_light_button_settings.setFixedSize(213, 150)

        # self.button_temp.setStyleSheet("background-color: black;")
        self.h5_light_button_fan.setStyleSheet("background-color: black;")
        self.h5_light_button_AC.setStyleSheet("background-color: black;")
        self.h5_light_button_max.setStyleSheet("background-color: black;")
        self.h5_light_button_audio.setStyleSheet("background-color: black;")
        self.h5_light_button_hazard.setStyleSheet("background-color: black;")
        self.h5_light_button_phone.setStyleSheet("background-color: black;")
        self.h5_light_button_nav.setStyleSheet("background-color: black;")
        self.h5_light_button_settings.setStyleSheet("background-color: black;")

        # self.button_temp.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/.png'))
        # self.button_temp.setIconSize(QSize(140, 140))
        self.h5_light_button_fan.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fan.png'))
        self.h5_light_button_fan.setIconSize(QSize(140, 140))
        self.h5_light_button_AC.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/ac.png'))
        self.h5_light_button_AC.setIconSize(QSize(213, 200))
        self.h5_light_button_max.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/airmax.png'))
        self.h5_light_button_max.setIconSize(QSize(140, 140))

        self.h5_light_button_audio.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/audio.png'))
        self.h5_light_button_audio.setIconSize(QSize(140, 140))
        self.h5_light_button_hazard.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/hazard.png'))
        self.h5_light_button_hazard.setIconSize(QSize(140, 140))
        self.h5_light_button_phone.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/phone.png'))
        self.h5_light_button_phone.setIconSize(QSize(140, 140))
        self.h5_light_button_nav.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/nav.png'))
        self.h5_light_button_nav.setIconSize(QSize(140, 140))
        self.h5_light_button_settings.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/settings.png'))
        self.h5_light_button_settings.setIconSize(QSize(140, 140))

        # self.horizontalSubLayout_5.addWidget(self.button_temp)  # add button to layout
        self.h5_light.addWidget(self.h5_light_button_seat_1)
        self.h5_light.addWidget(self.h5_light_button_phone)
        self.h5_light.addWidget(self.h5_light_button_AC)
        self.h5_light.addWidget(self.h5_light_button_max)
        self.h5_light.addWidget(self.h5_light_button_hazard)
        self.h5_light.addWidget(self.h5_light_button_audio)
        self.h5_light.addWidget(self.h5_light_button_nav)
        self.h5_light.addWidget(self.h5_light_button_settings)
        self.h5_light.addWidget(self.h5_light_button_seat_2)

        parent_layout.addLayout(self.h5_light)  # add to vertical layout

    # climate horizontal sublayout 1 = horizontal block with left and right indicator buttons
    def add_horizontal_sublayout_1(self, parent_layout, frame):
        self.horizontalSubLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalSubLayout_1.setObjectName("horizontalSubLayout_1")

        self.button_left_arrow = QtWidgets.QPushButton(frame)  # Create button
        self.button_right_arrow = QtWidgets.QPushButton(frame)
        self.button_right_arrow.setFixedSize(199, 200)  # set size
        self.button_left_arrow.setFixedSize(199, 200)
        self.button_left_arrow.setObjectName("Button Left Arrow")  # set name
        self.button_right_arrow.setObjectName("Button Right Arrow")
        self.button_left_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_right_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_left_arrow.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/left_arrow.png'))  # set icon
        self.button_left_arrow.setIconSize(QSize(180, 180))
        self.button_right_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/right_arrow.png'))
        self.button_right_arrow.setIconSize(QSize(180, 180))

        self.h1_climate_button_spacer = QtWidgets.QPushButton(frame)
        self.h1_climate_button_spacer.setFixedSize(2, 200)
        self.h1_climate_button_spacer.setObjectName("Spacer")
        self.h1_climate_button_spacer.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* Remove all other borders */
                border-left: 1px solid black;  /* Add left border */
            }
        """)

        # Create the vertical line
        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)  # Set the frame shape to a vertical line
        vertical_line.setFrameShadow(QtWidgets.QFrame.Plain)  # Use a plain line
        vertical_line.setStyleSheet("border: 1px solid black;")  # Set the line color and width
        vertical_line.setFixedHeight(200)  # Set the height of the line
        vertical_line.setFixedWidth(1)  # Set the width of the line

        self.horizontalSubLayout_1.addWidget(self.button_left_arrow)  # Add to layout
        self.horizontalSubLayout_1.addWidget(vertical_line)  # Add the vertical line
        self.horizontalSubLayout_1.addWidget(self.button_right_arrow)
        self.horizontalSubLayout_1.addWidget(self.h1_climate_button_spacer)

        spacer_1 = QtWidgets.QSpacerItem(1000, 100, QtWidgets.QSizePolicy.Expanding,
                                         QtWidgets.QSizePolicy.Minimum)  # Add spacer
        self.horizontalSubLayout_1.addItem(spacer_1)
        parent_layout.addLayout(self.horizontalSubLayout_1)  # Add the horizontal layout to the vertical layout

    def update_label(self, value):
        self.label.setText(f"Slider Value: {value}")

    # h2 climate = horizontal block with the image of the time, wifi etc.
    def add_horizontal_sublayout_2(self, parent_layout, frame):
        self.horizontalSubLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalSubLayout_2.setObjectName("horizontalSubLayout_2")

        self.button_label = QtWidgets.QPushButton(frame)  # Create button
        self.button_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.button_label.setFixedSize(400, 277)
        self.button_label.setObjectName("Label Button")
        self.button_label.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/time.png'))  # Add icon
        self.button_label.setIconSize(QSize(700, 400))

        self.button_label.setStyleSheet("""
            QPushButton {
                background-color: white;  /* Button color */
                border: 1px solid black;  /* Default border for all sides */

                border-left:none;
            }
        """)
        self.horizontalSubLayout_2.addWidget(self.button_label)  # Add to layout

        # Spacer button
        self.h2_climate_button_spacer_1 = QtWidgets.QPushButton(frame)
        self.h2_climate_button_spacer_1.setFixedSize(100, 125)
        self.h2_climate_button_spacer_1.setObjectName("Spacer 1")
        self.h2_climate_button_spacer_1.setStyleSheet("background-color: transparent;")
        self.horizontalSubLayout_2.addWidget(self.h2_climate_button_spacer_1)

        # Off button
        self.h2_climate_button_off = QtWidgets.QPushButton(frame)
        self.h2_climate_button_off.setFixedSize(150, 150)
        self.h2_climate_button_off.setObjectName("Off")
        self.h2_climate_button_off.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/off.png'))
        self.h2_climate_button_off.setIconSize(QSize(200, 200))
        self.h2_climate_button_off.setStyleSheet("background-color: white;")
        self.horizontalSubLayout_2.addWidget(self.h2_climate_button_off)

        # Spacer button
        self.h2_climate_button_spacer_2 = QtWidgets.QPushButton(frame)
        self.h2_climate_button_spacer_2.setFixedSize(200, 125)
        self.h2_climate_button_spacer_2.setObjectName("Spacer 2")
        self.h2_climate_button_spacer_2.setStyleSheet("background-color: transparent;")
        self.horizontalSubLayout_2.addWidget(self.h2_climate_button_spacer_2)

        # Create a label for displaying temperature with a degree symbol
        self.twenty_label = QtWidgets.QLabel("18°")  # Default value
        self.twenty_label.setStyleSheet("font-size: 70px; color: black;")
        self.twenty_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create a vertical layout for the temperature label and slider
        label_slider_layout = QtWidgets.QVBoxLayout()
        label_slider_layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins
        label_slider_layout.setSpacing(1)  # Adjust spacing between label and slider

        # Create the slider with a range of 18 to 25
        self.h2_slider = CustomSlider(QtCore.Qt.Horizontal)
        self.h2_slider.setRange(18, 25)  # Set min and max for the slider
        self.h2_slider.setValue(18)  # Set default slider value to match the label

        # Style the slider as specified
        self.h2_slider.setStyleSheet("""
                    QSlider::groove:horizontal {
                        height: 60px;  /* Thicker groove */
                        background: #e0e0e0;  /* Light grey background for groove */
                        border: 1px solid #c0c0c0;  /* Border for better visibility */
                        border-radius: 0px;  /* Remove rounded edges */
                    }
                    QSlider::sub-page:horizontal {
                        background: #000000;  /* Color for the filled part */
                        height: 60px;  /* Match groove thickness */
                        border-radius: 0px;
                    }
                    QSlider::add-page:horizontal {
                        background: #ffffff;  /* Color for the unfilled part */
                        height: 60px;  /* Match groove thickness */
                        border-radius: 0px;
                    }
                    QSlider::handle:horizontal {
                        background: #555555;  /* Handle color */
                        width: 40px;
                        height: 80px;  /* Taller handle for a chunky appearance */
                        border-radius: 20px;  /* Remove rounded edges */
                        margin: -10px 0;  /* Adjust handle alignment */
                    }

                    QSlider::tick-mark:horizontal {
                        width: 40px;  /* Diameter of the notch */
                        height: 80px;  /* Diameter of the notch */
                        background: #808080;  /* Grey color for the notch */
                        border-radius: 20px;  /* Make it circular */
                        margin: -20px 0;  /* Center the notch on the groove */
                    }
                """)
        self.h2_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)  # Display tick marks below the slider
        self.h2_slider.setTickInterval(1)  # Set tick intervals to 1

        self.h2_slider.setMinimumSize(500, 80)
        self.h2_slider.setMaximumSize(1700, 80)

        # Create a horizontal layout for LO label, slider, and HI label
        slider_with_labels_layout = QtWidgets.QHBoxLayout()

        # Create "LO" and "HI" labels
        lo_label = QtWidgets.QLabel("LO  ")
        lo_label.setStyleSheet("font-size: 45px;")
        hi_label = QtWidgets.QLabel("  HI")
        hi_label.setStyleSheet("font-size: 45px;")
        empty_label = QtWidgets.QLabel("  ")
        empty_label.setStyleSheet("font-size: 25px;")

        # Add LO label, slider, and HI label to the horizontal layout
        slider_with_labels_layout.addWidget(lo_label, alignment=QtCore.Qt.AlignLeft)
        slider_with_labels_layout.addWidget(self.h2_slider)
        slider_with_labels_layout.addWidget(hi_label, alignment=QtCore.Qt.AlignRight)

        # Add the twenty_label and slider_with_labels_layout to the vertical layout
        label_slider_layout.addWidget(self.twenty_label, alignment=QtCore.Qt.AlignCenter)

        label_slider_layout.addLayout(slider_with_labels_layout)
        label_slider_layout.addWidget(empty_label, alignment=QtCore.Qt.AlignCenter)

        # Add the vertical layout to the main horizontal layout
        self.horizontalSubLayout_2.addLayout(label_slider_layout)

        # Function to update the temperature label based on the slider's position
        def update_temperature_label(value):
            if value == self.h2_slider.maximum():  # Max value
                self.twenty_label.setText("HI")
            elif value == self.h2_slider.minimum():  # Min value
                self.twenty_label.setText("LO")
            else:
                self.twenty_label.setText(f"{value}°")  # Normal range

        # Connect the slider's valueChanged signal to the update function
        self.h2_slider.valueChanged.connect(update_temperature_label)

        # Spacer at the end
        spacer3 = QtWidgets.QSpacerItem(1920, 100, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalSubLayout_2.addItem(spacer3)

        # Add the horizontal layout to the parent layout
        parent_layout.addLayout(self.horizontalSubLayout_2)

        # Additional button at the bottom
        self.button_extra = QtWidgets.QPushButton(frame)
        self.button_extra.setFixedSize(400, 0)
        self.button_extra.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none; /* Remove all borders */
                border-right: 1px solid black; /* Add a border to the right side */
                border-top: 1px solid black; /* Add a border to the top side */
            }
        """)
        self.button_extra.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        #parent_layout.addWidget(self.button_extra)

    # h3 climate = horizontal block with the home button
    def add_horizontal_sublayout_3(self, parent_layout, frame):
        # Initialize fan level variable
        self.fan_level = 1

        # Define a method to update bar colors based on fan level
        def update_fan_speed_display():
            bars = [self.h3_climate_button_bar_1, self.h3_climate_button_bar_2,
                    self.h3_climate_button_bar_3, self.h3_climate_button_bar_4,
                    self.h3_climate_button_bar_5]

            # Set each bar's color based on the current fan level
            for i in range(5):
                if i < self.fan_level:
                    bars[i].setStyleSheet("background-color: black;")  # Filled color
                else:
                    bars[i].setStyleSheet("background-color: white;")  # Unfilled color

        # Define methods to increase and decrease fan level
        def increase_fan_level():
            if self.fan_level < 5:
                self.fan_level += 1
                update_fan_speed_display()

        def decrease_fan_level():
            if self.fan_level > 1:
                self.fan_level -= 1
                update_fan_speed_display()

        # Create horizontal layout
        self.horizontalSubLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalSubLayout_3.setSpacing(2)  # Set 2-pixel spacing between all items in this layout

        # Add home button
        self.button_home = QtWidgets.QPushButton(frame)
        self.button_home.setFixedSize(400, 251)
        self.button_home.setObjectName("Home Button")
        self.button_home.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/home.png'))
        self.button_home.setIconSize(QSize(300, 180))
        self.button_home.setStyleSheet("background-color: #5CE1E6" if frame == self.home_frame else "background-color: white;")
        self.button_home.setContentsMargins(0, 0, 0, 0)  # Remove padding
        self.button_home.setLayout(QtWidgets.QVBoxLayout())  # Add a layout to the button
        self.button_home.layout().setAlignment(QtCore.Qt.AlignCenter)  # Center-align contents
        self.horizontalSubLayout_3.addWidget(self.button_home)

        # Spacer
        h3_spacer_1 = QtWidgets.QSpacerItem(1000, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h3_climate_button_spacer_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_spacer_1.setFixedSize(100, 125)  # set size
        self.h3_climate_button_spacer_1.setObjectName("Spacer 1")  # set name
        self.h3_climate_button_spacer_1.setStyleSheet("background-color: transparent;")  # Set BG color New buttons
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_spacer_1)

        # Create the fan logo button (without functionality) and set its style
        self.fan_logo_button = QtWidgets.QPushButton(frame)
        self.fan_logo_button.setFixedSize(75, 75)
        self.fan_logo_button.setStyleSheet("background-color: transparent; border: none;")  # Adjust style as needed
        self.fan_logo_button.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fanclimate.png'))  # Add fan icon image
        self.fan_logo_button.setIconSize(QSize(75, 75))  # Adjust icon size to fit button


        # Create the minus button and connect it to decrease fan level
        self.h3_climate_button_minus = QtWidgets.QPushButton("−", frame)
        self.h3_climate_button_minus.setFixedSize(50, 50)
        self.h3_climate_button_minus.setStyleSheet("background-color: white; font-size: 35px; color: black;")
        self.h3_climate_button_minus.clicked.connect(decrease_fan_level)
        empty_label_minus_bottom = QtWidgets.QLabel(" ")
        empty_label_minus_bottom.setStyleSheet("font-size: 1px;")

        # Stack the fan logo and minus button vertically
        logo_and_minus_layout = QtWidgets.QVBoxLayout()
        logo_and_minus_layout.addWidget(self.fan_logo_button, alignment=QtCore.Qt.AlignCenter)
        logo_and_minus_layout.addWidget(self.h3_climate_button_minus, alignment=QtCore.Qt.AlignCenter)
        logo_and_minus_layout.addWidget(empty_label_minus_bottom)

        # Add the combined layout to the main horizontal layout
        self.horizontalSubLayout_3.addLayout(logo_and_minus_layout)

        # Spacer
        self.h3_climate_button_spacer_minus = QtWidgets.QPushButton(frame)
        self.h3_climate_button_spacer_minus.setFixedSize(30, 125)
        self.h3_climate_button_spacer_minus.setStyleSheet("background-color: transparent;")
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_spacer_minus)

        # Create a horizontal layout for the bars
        bars_layout = QtWidgets.QHBoxLayout()

        # Create each bar button and add it to bars_layout with consistent bottom alignment
        self.h3_climate_button_bar_1 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_1.setFixedSize(30, 50)
        self.h3_climate_button_bar_1.setStyleSheet("background-color: white;")
        bars_layout.addWidget(self.h3_climate_button_bar_1, alignment=QtCore.Qt.AlignBottom)

        self.h3_climate_button_bar_2 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_2.setFixedSize(30, 60)
        self.h3_climate_button_bar_2.setStyleSheet("background-color: white;")
        bars_layout.addWidget(self.h3_climate_button_bar_2, alignment=QtCore.Qt.AlignBottom)

        self.h3_climate_button_bar_3 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_3.setFixedSize(30, 70)
        self.h3_climate_button_bar_3.setStyleSheet("background-color: white;")
        bars_layout.addWidget(self.h3_climate_button_bar_3, alignment=QtCore.Qt.AlignBottom)

        self.h3_climate_button_bar_4 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_4.setFixedSize(30, 80)
        self.h3_climate_button_bar_4.setStyleSheet("background-color: white;")
        bars_layout.addWidget(self.h3_climate_button_bar_4, alignment=QtCore.Qt.AlignBottom)

        self.h3_climate_button_bar_5 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_5.setFixedSize(30, 90)
        self.h3_climate_button_bar_5.setStyleSheet("background-color: white;")
        bars_layout.addWidget(self.h3_climate_button_bar_5, alignment=QtCore.Qt.AlignBottom)

        # Create an empty label below to shift the bars upwards
        empty_label_top = QtWidgets.QLabel(" ")
        empty_label_top.setStyleSheet("font-size: 1px;")
        empty_label_bottom = QtWidgets.QLabel(" ")
        empty_label_bottom.setStyleSheet("font-size: 1px;")

        # Create numbered labels below each bar
        number_labels_layout = QtWidgets.QHBoxLayout()
        for i in range(1, 6):
            number_label = QtWidgets.QLabel(str(i))
            number_label.setStyleSheet("font-size: 30px;")  # Set font size to 30 pixels
            number_labels_layout.addWidget(number_label, alignment=QtCore.Qt.AlignHCenter)  # Center align each number

        # Create a vertical layout to hold the bars layout and the number labels
        bars_with_empty_label_layout = QtWidgets.QVBoxLayout()
        bars_with_empty_label_layout.addWidget(empty_label_top)  # Adjust top alignment if needed
        bars_with_empty_label_layout.addLayout(bars_layout)  # Add bars layout
        bars_with_empty_label_layout.addLayout(number_labels_layout)  # Add number labels below bars
        bars_with_empty_label_layout.addWidget(empty_label_bottom)  # Adjust top alignment if needed

        # Add the combined bars layout and empty label to the main horizontal layout
        self.horizontalSubLayout_3.addLayout(bars_with_empty_label_layout)

        # Spacer
        self.h3_climate_button_spacer_plus = QtWidgets.QPushButton(frame)
        self.h3_climate_button_spacer_plus.setFixedSize(30, 125)
        self.h3_climate_button_spacer_plus.setStyleSheet("background-color: transparent;")

        # Add plus button and connect it to increase fan level
        self.h3_climate_button_plus = QtWidgets.QPushButton("+", frame)
        self.h3_climate_button_plus.setFixedSize(50, 50)
        self.h3_climate_button_plus.setStyleSheet("background-color: white; font-size: 35px; color: black;")
        self.h3_climate_button_plus.clicked.connect(increase_fan_level)  # Connect to increase function

        # Initialize the fan speed display
        update_fan_speed_display()

        self.h3_climate_button_spacer_2 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_spacer_2.setFixedSize(425, 125)  # set size
        self.h3_climate_button_spacer_2.setObjectName("Spacer 1")  # set name
        self.h3_climate_button_spacer_2.setStyleSheet("background-color: transparent;")  # Set BG color New buttons
        self.h3_climate_button_spacer_2.setEnabled(False)

        self.h3_climate_button_stickman_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_stickman_1.setFixedSize(100, 125)  # set size
        self.h3_climate_button_stickman_1.setObjectName("Stickman 1")  # set name
        self.h3_climate_button_stickman_1.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/stickman_1.png'))
        self.h3_climate_button_stickman_1.setIconSize(QSize(80, 100))
        self.h3_climate_button_stickman_1.setStyleSheet("background-color: white;") # Set BG color New buttons

        self.h3_climate_button_stickman_2 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_stickman_2.setFixedSize(100, 125)  # set size
        self.h3_climate_button_stickman_2.setObjectName("Stickman 2")  # set name
        self.h3_climate_button_stickman_2.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/stickman_3.png'))
        self.h3_climate_button_stickman_2.setIconSize(QSize(80, 100))
        self.h3_climate_button_stickman_2.setStyleSheet("background-color: white;")  # Set BG color New buttons

        self.h3_climate_button_stickman_3 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_stickman_3.setFixedSize(100, 125)  # set size
        self.h3_climate_button_stickman_3.setObjectName("Stickman 3")  # set name
        self.h3_climate_button_stickman_3.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/stickman_2.png'))
        self.h3_climate_button_stickman_3.setIconSize(QSize(80, 100))
        self.h3_climate_button_stickman_3.setStyleSheet("background-color: white;")  # Set BG color New buttons

        self.h3_climate_button_stickman_4 = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_stickman_4.setFixedSize(100, 125)  # set size
        self.h3_climate_button_stickman_4.setObjectName("Stickman 4")  # set name
        self.h3_climate_button_stickman_4.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/stickman_4.png'))
        self.h3_climate_button_stickman_4.setIconSize(QSize(80, 100))
        self.h3_climate_button_stickman_4.setStyleSheet("background-color: white;")  # Set BG color New buttons

        self.h3_climate_button_defrost = QtWidgets.QPushButton(frame)  # Create button
        self.h3_climate_button_defrost.setFixedSize(100, 125)  # set size
        self.h3_climate_button_defrost.setObjectName("Defrost")  # set name
        self.h3_climate_button_defrost.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/defrost.png'))
        self.h3_climate_button_defrost.setIconSize(QSize(80, 100))
        self.h3_climate_button_defrost.setStyleSheet("background-color: white;")  # Set BG color New buttons

        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_spacer_plus)
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_plus)

        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_spacer_2)
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_stickman_1)  # Add New buttons to layout
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_stickman_2)  # Add New buttons to layout
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_stickman_3)  # Add New buttons to layout
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_stickman_4)  # Add New buttons to layout
        self.horizontalSubLayout_3.addWidget(self.h3_climate_button_defrost)

        spacer4 = QtWidgets.QSpacerItem(200, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.horizontalSubLayout_3.addItem(spacer4)
        spacer5 = QtWidgets.QSpacerItem(1900, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.horizontalSubLayout_3.addItem(spacer5)

        parent_layout.addLayout(self.horizontalSubLayout_3)  # Add to the vertical layout


    # horizontal sublayout 4  = horizontal block with wiper and light buttons
    def add_horizontal_sublayout_4(self, parent_layout, frame):
        self.horizontalSubLayout_4 = QtWidgets.QHBoxLayout()
        #self.horizontalSubLayout_4.setSpacing(2)

        self.button_wiper = QtWidgets.QPushButton(frame)  # Create button
        self.button_light = QtWidgets.QPushButton(frame)
        self.button_wiper.setFixedSize(200, 200)  # set size
        self.button_light.setFixedSize(200, 200)
        self.button_wiper.setObjectName("Wiper Button")  # set name
        self.button_light.setObjectName("Light Button")
        self.button_light.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/light_bulb.png'))
        self.button_light.setIconSize(QSize(180, 180))
        self.button_wiper.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiper.png'))
        self.button_wiper.setIconSize(QSize(180, 180))


        # Climate Buttons

        h4_spacer_1 = QtWidgets.QSpacerItem(500, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.h4_climate_button_spacer_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_spacer_1.setFixedSize(100, 200)  # set size
        self.h4_climate_button_spacer_1.setObjectName("Spacer Button 1")  # set name

        self.h4_climate_button_airflow_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_airflow_1.setFixedSize(200, 125)  # set size
        self.h4_climate_button_airflow_1.setObjectName("Airflow Button 1")  # set name
        self.h4_climate_button_airflow_1.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/airflow_1.png'))
        self.h4_climate_button_airflow_1.setIconSize(QSize(180, 100))

        self.h4_climate_button_spacer_tiny_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_spacer_tiny_1.setFixedSize(2, 200)  # Set size
        self.h4_climate_button_spacer_tiny_1.setObjectName("Spacer Button 1")  # Set name

        # Make the button unclickable
        self.h4_climate_button_spacer_tiny_1.setEnabled(False)

        # Make the button invisible
        self.h4_climate_button_spacer_tiny_1.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Make the background transparent */
                border: none;  /* Remove any borders */
            }
        """)

        self.h4_climate_button_airflow_2 = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_airflow_2.setFixedSize(200, 125)  # set size
        self.h4_climate_button_airflow_2.setObjectName("Airflow Button 2")  # set name
        self.h4_climate_button_airflow_2.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/airflow_2.png'))
        self.h4_climate_button_airflow_2.setIconSize(QSize(180, 100))

        h4_spacer_2 = QtWidgets.QSpacerItem(1200, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.h4_climate_button_max_ac = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_max_ac.setFixedSize(125, 125)  # set size
        self.h4_climate_button_max_ac.setObjectName("MAX A/C")  # set name
        self.h4_climate_button_max_ac.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/max_ac.png'))
        self.h4_climate_button_max_ac.setIconSize(QSize(125, 125))
        #self.h4_climate_button_max_ac.clicked.connect(lambda: self.log_button_click("MAX A/C"))

        # self.h4_climate_button_rear_defrost = QtWidgets.QPushButton(frame)  # Create button
        # self.h4_climate_button_rear_defrost.setFixedSize(125, 125)  # set size
        # self.h4_climate_button_rear_defrost.setObjectName("Rear Defrost")  # set name
        # self.h4_climate_button_rear_defrost.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/rear_defrost.png'))
        #self.h4_climate_button_rear_defrost.setIconSize(QSize(100, 100))

        self.h4_climate_button_auto = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_auto.setFixedSize(125, 125)  # set size
        self.h4_climate_button_auto.setObjectName("AUTO")  # set name
        self.h4_climate_button_auto.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/auto.png'))
        self.h4_climate_button_auto.setIconSize(QSize(100, 100))

        self.button_wiper.setStyleSheet("background-color: white;")
        self.button_light.setStyleSheet("background-color: white;")
        # Set BG color New buttons
        self.h4_climate_button_airflow_1.setStyleSheet("border:5px black;background-color: white;")
        self.h4_climate_button_airflow_2.setStyleSheet("background-color: white;")
        self.h4_climate_button_spacer_1.setStyleSheet("background-color: transparent;")
        self.h4_climate_button_max_ac.setStyleSheet("background-color: white;")
        # self.h4_climate_button_rear_defrost.setStyleSheet("background-color: white;")
        self.h4_climate_button_auto.setStyleSheet("background-color: white;")

        self.horizontalSubLayout_4.addWidget(self.button_wiper)  # Add button to layout
        self.horizontalSubLayout_4.addWidget(self.button_light)

        # Add New buttons to layout
        #self.horizontalSubLayout_4.addItem(h4_spacer_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_airflow_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_tiny_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_airflow_2)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_tiny_1)

        self.horizontalSubLayout_4.addItem(h4_spacer_2)

        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_tiny_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_max_ac)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_tiny_1)
        # self.horizontalSubLayout_4.addWidget(self.h4_climate_button_rear_defrost)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_spacer_tiny_1)
        self.horizontalSubLayout_4.addWidget(self.h4_climate_button_auto)

        spacer7 = QtWidgets.QSpacerItem(1000, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalSubLayout_4.addItem(spacer7)

        parent_layout.addLayout(self.horizontalSubLayout_4)  # Add to the vertical layout

        # horizontal sublayout 4 = horizontal block with wiper and light buttons

    def add_horizontal_sublayout_5(self, parent_layout, frame):
        self.horizontalSubLayout_5 = QtWidgets.QHBoxLayout()

        # self.add_temperature_control(self.horizontalSubLayout_5)

        # self.button_temp = QtWidgets.QPushButton(frame)  # Create button
        self.button_seat_1 = QtWidgets.QPushButton(frame)
        self.button_fan = QtWidgets.QPushButton(frame)
        self.button_AC = QtWidgets.QPushButton(frame)
        self.button_max = QtWidgets.QPushButton(frame)
        self.button_audio = QtWidgets.QPushButton(frame)
        self.button_hazard = QtWidgets.QPushButton(frame)
        self.button_phone = QtWidgets.QPushButton(frame)
        self.button_nav = QtWidgets.QPushButton(frame)
        self.button_settings = QtWidgets.QPushButton(frame)
        self.button_seat_2 = QtWidgets.QPushButton(frame)

        # self.button_temp.setFixedSize(300, 150)  # set size
        self.button_seat_1.setFixedSize(213, 150)
        self.button_seat_2.setFixedSize(213, 150)
        self.button_fan.setFixedSize(0, 0)
        self.button_AC.setFixedSize(213, 150)
        self.button_max.setFixedSize(214, 150)
        self.button_audio.setFixedSize(214, 150)
        self.button_hazard.setFixedSize(214, 150)
        self.button_phone.setFixedSize(213, 150)
        self.button_nav.setFixedSize(213, 150)
        self.button_settings.setFixedSize(213, 150)

        # self.button_temp.setStyleSheet("background-color: black;")
        self.button_seat_1.setStyleSheet("background-color: black;")
        self.button_seat_2.setStyleSheet("background-color: black;")
        self.button_fan.setStyleSheet("background-color: black;")
        self.button_AC.setStyleSheet("background-color: #0070c0;")
        self.button_max.setStyleSheet("background-color: black;")
        self.button_audio.setStyleSheet("background-color: black;")
        self.button_hazard.setStyleSheet("background-color: black;")
        self.button_phone.setStyleSheet("background-color: black;")
        self.button_nav.setStyleSheet("background-color: black;")
        self.button_settings.setStyleSheet("background-color: black;")

        # self.button_temp.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/.png'))
        # self.button_temp.setIconSize(QSize(140, 140))

        self.button_seat_1.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_1.png'))
        self.button_seat_1.setIconSize(QSize(140, 140))
        self.button_seat_2.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_2.png'))
        self.button_seat_2.setIconSize(QSize(140, 140))

        self.button_fan.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fan.png'))
        self.button_fan.setIconSize(QSize(140, 140))
        self.button_AC.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/ac_blue.png'))
        self.button_AC.setIconSize(QSize(213, 200))
        self.button_max.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/rear_defrost_white.png'))
        self.button_max.setIconSize(QSize(140, 140))

        self.button_audio.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/audio.png'))
        self.button_audio.setIconSize(QSize(140, 140))
        self.button_hazard.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/hazard.png'))
        self.button_hazard.setIconSize(QSize(140, 140))
        self.button_phone.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/phone.png'))
        self.button_phone.setIconSize(QSize(140, 140))
        self.button_nav.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/nav.png'))
        self.button_nav.setIconSize(QSize(140, 140))
        self.button_settings.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/settings.png'))
        self.button_settings.setIconSize(QSize(140, 140))

        # self.horizontalSubLayout_5.addWidget(self.button_temp)  # add button to layout
        self.horizontalSubLayout_5.addWidget(self.button_seat_1)
        self.horizontalSubLayout_5.addWidget(self.button_phone)
        self.horizontalSubLayout_5.addWidget(self.button_AC)
        self.horizontalSubLayout_5.addWidget(self.button_max)
        self.horizontalSubLayout_5.addWidget(self.button_hazard)
        self.horizontalSubLayout_5.addWidget(self.button_audio)
        self.horizontalSubLayout_5.addWidget(self.button_nav)
        self.horizontalSubLayout_5.addWidget(self.button_settings)
        self.horizontalSubLayout_5.addWidget(self.button_seat_2)

        parent_layout.addLayout(self.horizontalSubLayout_5)  # add to vertical layout


    def add_h1_wiper(self, parent_layout, frame):
        self.h1_wiper = QtWidgets.QHBoxLayout()
        self.h1_wiper.setObjectName("h1_wiper")

        self.h1_wiper_button_left_arrow = QtWidgets.QPushButton(frame) # Create button
        self.h1_wiper_button_right_arrow = QtWidgets.QPushButton(frame)
        self.h1_wiper_button_left_arrow.setFixedSize(199, 200)  # set size
        self.h1_wiper_button_right_arrow.setFixedSize(199, 200)

        self.h1_wiper_button_left_arrow.setObjectName("h1_wiper Button Left Arrow")  # set name
        self.h1_wiper_button_right_arrow.setObjectName("h1_wiper Button Right Arrow")

        self.h1_wiper_button_left_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/left_arrow.png'))  # set icon
        self.h1_wiper_button_left_arrow.setIconSize(QSize(180, 180))
        self.h1_wiper_button_right_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/right_arrow.png'))
        self.h1_wiper_button_right_arrow.setIconSize(QSize(180, 180))

        self.h1_wiper_button_left_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none;
            }
        """)
        self.h1_wiper_button_right_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none;
            }
        """)
        self.h1_wiper_button_left_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.h1_wiper_button_right_arrow.setFocusPolicy(QtCore.Qt.NoFocus)

        # Create the vertical line
        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)  # Set the frame shape to a vertical line
        vertical_line.setFrameShadow(QtWidgets.QFrame.Plain)  # Use a plain line
        vertical_line.setStyleSheet("border: 1px solid black;")  # Set the line color and width
        vertical_line.setFixedHeight(200)  # Set the height of the line
        vertical_line.setFixedWidth(1)  # Set the width of the line

        self.h1_wiper_button_spacer = QtWidgets.QPushButton(frame)
        self.h1_wiper_button_spacer.setFixedSize(2, 200)
        self.h1_wiper_button_spacer.setObjectName("Spacer")
        self.h1_wiper_button_spacer.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* Remove all other borders */
                border-left: 1px solid black;  /* Add left border */
            }
        """)

        self.h1_wiper.addWidget(self.h1_wiper_button_left_arrow)
        self.h1_wiper.addWidget(vertical_line)
        self.h1_wiper.addWidget(self.h1_wiper_button_right_arrow)  # add to layout
        self.h1_wiper.addWidget(self.h1_wiper_button_spacer)

        spacer_h1_wiper_1 = QtWidgets.QSpacerItem(1000,200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h1_wiper.addItem(spacer_h1_wiper_1)
        parent_layout.addLayout(self.h1_wiper)

        #self.wiper_buttons_blue_highlight.append(self.h1_light_button_left_arrow)
        #self.wiper_buttons_blue_highlight.append(self.h1_light_button_left_arrow)

    def add_h2_wiper(self, parent_layout, frame):
        self.h2_wiper = QtWidgets.QHBoxLayout()
        self.h2_wiper.setObjectName("h2_wiper")

        self.h2_wiper_button_label = QtWidgets.QPushButton(frame)  # Create button
        self.h2_wiper_button_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.h2_wiper_button_label.setFixedSize(400, 277)
        self.h2_wiper_button_label.setObjectName("h2_wiper Label Button")
        self.h2_wiper_button_label.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/time.png'))  # add icon
        self.h2_wiper_button_label.setIconSize(QSize(700, 400))
        self.h2_wiper.addWidget(self.h2_wiper_button_label)  # add to layout

        self.h2_wiper_button_label.setStyleSheet("""
            background-color: white;
            border: none;
            border-top: 1px solid black;
            border-right: 1px solid black;
            border-bottom: 1px solid black;
        """)

        spacer_h2_wiper_1 = QtWidgets.QSpacerItem(1920, 100, QtWidgets.QSizePolicy.Maximum,
                                                  QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h2_wiper.addItem(spacer_h2_wiper_1)
        parent_layout.addLayout(self.h2_wiper)  # Add to the vertical layout

        #self.h2_wiper_button_extra = QtWidgets.QPushButton(frame)  # Create button
        #self.h2_wiper_button_extra.setFixedSize(400, 300)
        #self.h2_wiper_button_extra.setStyleSheet("background-color: white;")  # button color
        #parent_layout.addWidget(self.h2_wiper_button_extra)  # add button to layout

    def add_h3_wiper(self, parent_layout, frame):
        self.h3_wiper = QtWidgets.QHBoxLayout()

        self.h3_wiper_button_home = QtWidgets.QPushButton(frame)  # Create button
        self.h3_wiper_button_home.setFixedSize(400, 251)  # set size
        self.h3_wiper_button_home.setObjectName("h3_wiper Home Button")  # set name
        self.h3_wiper_button_home.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/home.png'))
        self.h3_wiper_button_home.setIconSize(QSize(300, 180))

        self.h3_wiper_button_home.setStyleSheet("background-color: white;")

        self.h3_wiper.addWidget(self.h3_wiper_button_home)  # add button to layout

        spacer_h3_wiper_1 = QtWidgets.QSpacerItem(200, 200, QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_wiper.addItem(spacer_h3_wiper_1)
        spacer_h3_wiper_2 = QtWidgets.QSpacerItem(1900, 200, QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_wiper.addItem(spacer_h3_wiper_2)

        parent_layout.addLayout(self.h3_wiper)  # Add to the vertical layout

    def add_h4_wiper(self, parent_layout, frame):
        self.h4_wiper = QtWidgets.QHBoxLayout()

        # First horizontal layout (left side)
        self.h4_wiper_leftLayout = QtWidgets.QHBoxLayout()
        self.h4_wiper_button_wiper = QtWidgets.QPushButton(frame)
        self.h4_wiper_button_light = QtWidgets.QPushButton(frame)
        self.h4_wiper_button_wiper.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_wiper_button_light.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_wiper_button_light.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/light_bulb.png'))
        self.h4_wiper_button_light.setIconSize(QSize(180, 180))
        self.h4_wiper_button_wiper.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiper.png'))
        self.h4_wiper_button_wiper.setIconSize(QSize(180, 180))

        self.h4_wiper_button_wiper.setStyleSheet("background-color: #0070c0;")
        self.h4_wiper_button_light.setStyleSheet("background-color: white;")

        self.h4_wiper_leftLayout.addWidget(self.h4_wiper_button_wiper)
        self.h4_wiper_leftLayout.addWidget(self.h4_wiper_button_light)

        # Add left frame to main layout
        self.h4_wiper.addLayout(self.h4_wiper_leftLayout)

        # Second vertical layout (right side)
        self.h4_wiper_rightLayout = QtWidgets.QVBoxLayout()

        # Second horizontal layout (within right side)
        self.h4_wiper_rightTopLayout = QtWidgets.QHBoxLayout()

        # Add spacer item to top right layout
        h4_wiper_1_spacer = QtWidgets.QSpacerItem(500, 80, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.h4_wiper_rightTopLayout.addSpacerItem(h4_wiper_1_spacer)

        # Third horizontal layout (within right side)
        self.h4_wiper_rightBottomLayout = QtWidgets.QHBoxLayout()

        # extra buttons for wiper options
        self.h4_wiper_button_wiper_off = QtWidgets.QPushButton(frame)  # create button
        self.h4_wiper_button_one = QtWidgets.QPushButton(frame)
        self.h4_wiper_button_two = QtWidgets.QPushButton(frame)
        self.h4_wiper_button_three = QtWidgets.QPushButton(frame)

        self.h4_wiper_button_wiper_off.setFixedSize(150, 120)  # set size
        self.h4_wiper_button_one.setFixedSize(150, 120)
        self.h4_wiper_button_two.setFixedSize(150, 120)
        self.h4_wiper_button_three.setFixedSize(150, 120)

        self.h4_wiper_button_wiper_off.setObjectName("Wiper Off Button")  # set name
        self.h4_wiper_button_one.setObjectName("One Button")
        self.h4_wiper_button_three.setObjectName("Three Button")
        self.h4_wiper_button_two.setObjectName("Two Button")

        self.h4_wiper_button_wiper_off.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiperoff.png'))
        self.h4_wiper_button_wiper_off.setIconSize(QSize(150, 150))
        self.h4_wiper_button_one.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/one.png'))
        self.h4_wiper_button_one.setIconSize(QSize(100, 100))
        self.h4_wiper_button_two.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/two.png'))
        self.h4_wiper_button_two.setIconSize(QSize(100, 100))
        self.h4_wiper_button_three.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/three.png'))
        self.h4_wiper_button_three.setIconSize(QSize(100, 100))

        self.h4_wiper_button_wiper_off.setStyleSheet("background-color: white;")
        self.h4_wiper_button_one.setStyleSheet("background-color: white;")
        self.h4_wiper_button_three.setStyleSheet("background-color: white;")
        self.h4_wiper_button_two.setStyleSheet("background-color: white;")

        self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_wiper_off)  # add to layout
        self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_one)
        self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_two)
        self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_three)

        h4_wiper_spacer_2 = QtWidgets.QSpacerItem(1700, 0, QtWidgets.QSizePolicy.Maximum,
                                          QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h4_wiper_rightBottomLayout.addItem(h4_wiper_spacer_2)

        # Add top and bottom layouts to right layout
        self.h4_wiper_rightLayout.addLayout(self.h4_wiper_rightTopLayout)
        self.h4_wiper_rightLayout.addLayout(self.h4_wiper_rightBottomLayout)

        # Add right frame to main layout
        self.h4_wiper.addLayout(self.h4_wiper_rightLayout)
        parent_layout.addLayout(self.h4_wiper)

    def add_h5_wiper(self, parent_layout, frame):
        self.h5_wiper = QtWidgets.QHBoxLayout()

        # self.add_temperature_control(self.h5_wiper)
        self.h5_wiper_button_seat_1 = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_seat_2 = QtWidgets.QPushButton(frame)

        self.h5_wiper_button_seat_1.setFixedSize(213, 150)
        self.h5_wiper_button_seat_2.setFixedSize(213, 150)

        self.h5_wiper_button_seat_1.setStyleSheet("background-color: black;")
        self.h5_wiper_button_seat_2.setStyleSheet("background-color: black;")

        self.h5_wiper_button_seat_1.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_1.png'))
        self.h5_wiper_button_seat_1.setIconSize(QSize(140, 140))
        self.h5_wiper_button_seat_2.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_2.png'))
        self.h5_wiper_button_seat_2.setIconSize(QSize(140, 140))

        # self.button_temp = QtWidgets.QPushButton(frame)  # Create button
        self.h5_wiper_button_fan = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_AC = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_max = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_audio = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_hazard = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_phone = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_nav = QtWidgets.QPushButton(frame)
        self.h5_wiper_button_settings = QtWidgets.QPushButton(frame)

        # self.button_temp.setFixedSize(300, 150)  # set size
        self.h5_wiper_button_fan.setFixedSize(0, 0)
        self.h5_wiper_button_AC.setFixedSize(213, 150)
        self.h5_wiper_button_max.setFixedSize(214, 150)
        self.h5_wiper_button_audio.setFixedSize(214, 150)
        self.h5_wiper_button_hazard.setFixedSize(214, 150)
        self.h5_wiper_button_phone.setFixedSize(213, 150)
        self.h5_wiper_button_nav.setFixedSize(213, 150)
        self.h5_wiper_button_settings.setFixedSize(213, 150)

        # self.button_temp.setStyleSheet("background-color: black;")
        self.h5_wiper_button_fan.setStyleSheet("background-color: black;")
        self.h5_wiper_button_AC.setStyleSheet("background-color: black;")
        self.h5_wiper_button_max.setStyleSheet("background-color: black;")
        self.h5_wiper_button_audio.setStyleSheet("background-color: black;")
        self.h5_wiper_button_hazard.setStyleSheet("background-color: black;")
        self.h5_wiper_button_phone.setStyleSheet("background-color: black;")
        self.h5_wiper_button_nav.setStyleSheet("background-color: black;")
        self.h5_wiper_button_settings.setStyleSheet("background-color: black;")

        # self.button_temp.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/.png'))
        # self.button_temp.setIconSize(QSize(140, 140))
        self.h5_wiper_button_fan.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fan.png'))
        self.h5_wiper_button_fan.setIconSize(QSize(140, 140))
        self.h5_wiper_button_AC.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/ac.png'))
        self.h5_wiper_button_AC.setIconSize(QSize(213, 200))
        self.h5_wiper_button_max.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/rear_defrost_white.png'))
        self.h5_wiper_button_max.setIconSize(QSize(140, 140))

        self.h5_wiper_button_audio.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/audio.png'))
        self.h5_wiper_button_audio.setIconSize(QSize(140, 140))
        self.h5_wiper_button_hazard.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/hazard.png'))
        self.h5_wiper_button_hazard.setIconSize(QSize(140, 140))
        self.h5_wiper_button_phone.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/phone.png'))
        self.h5_wiper_button_phone.setIconSize(QSize(140, 140))
        self.h5_wiper_button_nav.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/nav.png'))
        self.h5_wiper_button_nav.setIconSize(QSize(140, 140))
        self.h5_wiper_button_settings.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/settings.png'))
        self.h5_wiper_button_settings.setIconSize(QSize(140, 140))

        # self.horizontalSubLayout_5.addWidget(self.button_temp)  # add button to layout
        self.h5_wiper.addWidget(self.h5_wiper_button_seat_1)
        self.h5_wiper.addWidget(self.h5_wiper_button_phone)
        self.h5_wiper.addWidget(self.h5_wiper_button_AC)
        self.h5_wiper.addWidget(self.h5_wiper_button_max)
        self.h5_wiper.addWidget(self.h5_wiper_button_hazard)
        self.h5_wiper.addWidget(self.h5_wiper_button_audio)
        self.h5_wiper.addWidget(self.h5_wiper_button_nav)
        self.h5_wiper.addWidget(self.h5_wiper_button_settings)
        self.h5_wiper.addWidget(self.h5_wiper_button_seat_2)

        parent_layout.addLayout(self.h5_wiper)  # add to vertical layout

    def add_h1_home(self, parent_layout, frame):
        self.h1_home = QtWidgets.QHBoxLayout()
        self.h1_home.setObjectName("h1_home")

        self.h1_home_button_left_arrow = QtWidgets.QPushButton(frame)  # Create button
        self.h1_home_button_right_arrow = QtWidgets.QPushButton(frame)
        self.h1_home_button_left_arrow.setFixedSize(199, 200)  # set size
        self.h1_home_button_right_arrow.setFixedSize(199, 200)

        self.h1_home_button_left_arrow.setObjectName("h1_home Button Left Arrow")  # set name
        self.h1_home_button_right_arrow.setObjectName("h1_home Button Right Arrow")

        self.h1_home_button_left_arrow.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/left_arrow.png'))  # set icon
        self.h1_home_button_left_arrow.setIconSize(QSize(180, 180))
        self.h1_home_button_right_arrow.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/right_arrow.png'))
        self.h1_home_button_right_arrow.setIconSize(QSize(180, 180))

        self.h1_home_button_left_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;  /* Set background color */
                border: none;             /* Remove all borders */
            }
        """)

        self.h1_home_button_right_arrow.setStyleSheet("""
            QPushButton {
                background-color: white;  /* Set background color */
                border: none;             /* Remove all borders */
            }
        """)
        self.h1_home_button_left_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.h1_home_button_right_arrow.setFocusPolicy(QtCore.Qt.NoFocus)

        # Create the vertical line
        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)  # Set the frame shape to a vertical line
        vertical_line.setFrameShadow(QtWidgets.QFrame.Plain)  # Use a plain line
        vertical_line.setStyleSheet("border: 1px solid black;")  # Set the line color and width
        vertical_line.setFixedHeight(200)  # Set the height of the line
        vertical_line.setFixedWidth(1)  # Set the width of the line

        self.h1_home_button_spacer = QtWidgets.QPushButton(frame)
        self.h1_home_button_spacer.setFixedSize(2, 200)
        self.h1_home_button_spacer.setObjectName("Spacer")
        self.h1_home_button_spacer.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* Remove all other borders */
                border-left: 1px solid black;  /* Add left border */
            }
        """)

        self.h1_home.addWidget(self.h1_home_button_left_arrow)
        self.h1_home.addWidget(vertical_line)
        self.h1_home.addWidget(self.h1_home_button_right_arrow)  # add to layout
        self.h1_home.addWidget(self.h1_home_button_spacer)

        spacer_h1_home_1 = QtWidgets.QSpacerItem(1000, 200, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h1_home.addItem(spacer_h1_home_1)
        parent_layout.addLayout(self.h1_home)

        # self.home_buttons_blue_highlight.append(self.h1_light_button_left_arrow)
        # self.home_buttons_blue_highlight.append(self.h1_light_button_left_arrow)

    def add_h2_home(self, parent_layout, frame):
        self.h2_home = QtWidgets.QHBoxLayout()
        self.h2_home.setObjectName("h2_home")

        self.h2_home_button_label = QtWidgets.QPushButton(frame)  # Create button
        self.h2_home_button_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.h2_home_button_label.setFixedSize(400, 277)
        self.h2_home_button_label.setObjectName("h2_home Label Button")
        self.h2_home_button_label.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/time.png'))  # add icon
        self.h2_home_button_label.setIconSize(QSize(700, 400))
        self.h2_home.addWidget(self.h2_home_button_label)  # add to layout

        self.h2_home_button_label.setStyleSheet("""
            QPushButton {
                background-color: white;      /* Set background color */
                border: none;                 /* Remove all borders */
                border-top: 1px solid black;  /* Add a black border at the top */
                border-right: 1px solid black;  /* Add a black border at the right */
                border-bottom: 1px solid black;  /* Add a black border at the bottom */
            }
        """)

        spacer_h2_home_1 = QtWidgets.QSpacerItem(1920, 100, QtWidgets.QSizePolicy.Maximum,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h2_home.addItem(spacer_h2_home_1)
        parent_layout.addLayout(self.h2_home)  # Add to the vertical layout

        #self.h2_home_button_extra = QtWidgets.QPushButton(frame)  # Create button
        #self.h2_home_button_extra.setFixedSize(400, 300)
        #self.h2_home_button_extra.setStyleSheet("background-color: white;")  # button color
        #parent_layout.addWidget(self.h2_home_button_extra)  # add button to layout

    def add_h3_home(self, parent_layout, frame):
        self.h3_home = QtWidgets.QHBoxLayout()

        self.h3_home_button_home = QtWidgets.QPushButton(frame)  # Create button
        self.h3_home_button_home.setFixedSize(400, 251)  # set size
        self.h3_home_button_home.setObjectName("h3_home Home Button")  # set name
        self.h3_home_button_home.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/home.png'))
        self.h3_home_button_home.setIconSize(QSize(300, 180))

        self.h3_home_button_home.setStyleSheet("background-color: #0070c0;")

        self.h3_home.addWidget(self.h3_home_button_home)  # add button to layout

        spacer_h3_home_1 = QtWidgets.QSpacerItem(200, 200, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_home.addItem(spacer_h3_home_1)
        spacer_h3_home_2 = QtWidgets.QSpacerItem(1900, 200, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_home.addItem(spacer_h3_home_2)

        parent_layout.addLayout(self.h3_home)  # Add to the vertical layout

    def add_h4_home(self, parent_layout, frame):
        self.h4_home = QtWidgets.QHBoxLayout()

        # First horizontal layout (left side)
        self.h4_home_leftLayout = QtWidgets.QHBoxLayout()
        self.h4_home_button_wiper = QtWidgets.QPushButton(frame)
        self.h4_home_button_light = QtWidgets.QPushButton(frame)
        self.h4_home_button_wiper.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_home_button_light.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_home_button_light.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/light_bulb.png'))
        self.h4_home_button_light.setIconSize(QSize(180, 180))
        self.h4_home_button_wiper.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiper.png'))
        self.h4_home_button_wiper.setIconSize(QSize(180, 180))

        self.h4_home_button_wiper.setStyleSheet("background-color: white;")
        self.h4_home_button_light.setStyleSheet("background-color: white;")

        self.h4_home_leftLayout.addWidget(self.h4_home_button_wiper)
        self.h4_home_leftLayout.addWidget(self.h4_home_button_light)

        # Add left frame to main layout
        self.h4_home.addLayout(self.h4_home_leftLayout)

        # Second vertical layout (right side)
        self.h4_home_rightLayout = QtWidgets.QVBoxLayout()

        # Second horizontal layout (within right side)
        self.h4_home_rightTopLayout = QtWidgets.QHBoxLayout()

        # Add spacer item to top right layout
        # h4_home_1_spacer = QtWidgets.QSpacerItem(500, 80, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # self.h4_home_rightTopLayout.addSpacerItem(h4_home_1_spacer)

        # Third horizontal layout (within right side)
        self.h4_home_rightBottomLayout = QtWidgets.QHBoxLayout()

        h4_home_spacer_2 = QtWidgets.QSpacerItem(1700, 150, QtWidgets.QSizePolicy.Maximum,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h4_home_rightBottomLayout.addItem(h4_home_spacer_2)

        # Add top and bottom layouts to right layout
        self.h4_home_rightLayout.addLayout(self.h4_home_rightTopLayout)
        self.h4_home_rightLayout.addLayout(self.h4_home_rightBottomLayout)

        # Add right frame to main layout
        self.h4_home.addLayout(self.h4_home_rightLayout)
        parent_layout.addLayout(self.h4_home)

    def add_h5_home(self, parent_layout, frame):
        self.h5_home = QtWidgets.QHBoxLayout()

        # self.add_temperature_control(self.h5_home)

        # self.button_temp = QtWidgets.QPushButton(frame)  # Create button
        self.h5_home_button_seat_1 = QtWidgets.QPushButton(frame)
        self.h5_home_button_seat_2 = QtWidgets.QPushButton(frame)

        self.h5_home_button_seat_1.setFixedSize(213, 150)
        self.h5_home_button_seat_2.setFixedSize(213, 150)

        self.h5_home_button_seat_1.setStyleSheet("background-color: black;")
        self.h5_home_button_seat_2.setStyleSheet("background-color: black;")

        self.h5_home_button_seat_1.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_1.png'))
        self.h5_home_button_seat_1.setIconSize(QSize(140, 140))
        self.h5_home_button_seat_2.setIcon(
            QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/seat_warmer_2.png'))
        self.h5_home_button_seat_2.setIconSize(QSize(140, 140))

        self.h5_home_button_fan = QtWidgets.QPushButton(frame)
        self.h5_home_button_AC = QtWidgets.QPushButton(frame)
        self.h5_home_button_max = QtWidgets.QPushButton(frame)
        self.h5_home_button_audio = QtWidgets.QPushButton(frame)
        self.h5_home_button_hazard = QtWidgets.QPushButton(frame)
        self.h5_home_button_phone = QtWidgets.QPushButton(frame)
        self.h5_home_button_nav = QtWidgets.QPushButton(frame)
        self.h5_home_button_settings = QtWidgets.QPushButton(frame)

        # self.button_temp.setFixedSize(300, 150)  # set size
        self.h5_home_button_fan.setFixedSize(0, 0)
        self.h5_home_button_AC.setFixedSize(213, 150)
        self.h5_home_button_max.setFixedSize(214, 150)
        self.h5_home_button_audio.setFixedSize(214, 150)
        self.h5_home_button_hazard.setFixedSize(214, 150)
        self.h5_home_button_phone.setFixedSize(213, 150)
        self.h5_home_button_nav.setFixedSize(213, 150)
        self.h5_home_button_settings.setFixedSize(213, 150)

        # self.button_temp.setStyleSheet("background-color: black;")
        self.h5_home_button_fan.setStyleSheet("background-color: black;")
        self.h5_home_button_AC.setStyleSheet("background-color: black;")
        self.h5_home_button_max.setStyleSheet("background-color: black;")
        self.h5_home_button_audio.setStyleSheet("background-color: black;")
        self.h5_home_button_hazard.setStyleSheet("background-color: black;")
        self.h5_home_button_phone.setStyleSheet("background-color: black;")
        self.h5_home_button_nav.setStyleSheet("background-color: black;")
        self.h5_home_button_settings.setStyleSheet("background-color: black;")

        # self.button_temp.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/.png'))
        # self.button_temp.setIconSize(QSize(140, 140))
        self.h5_home_button_fan.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fan.png'))
        self.h5_home_button_fan.setIconSize(QSize(140, 140))
        self.h5_home_button_AC.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/ac.png'))
        self.h5_home_button_AC.setIconSize(QSize(213, 200))
        self.h5_home_button_max.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/rear_defrost_white.png'))
        self.h5_home_button_max.setIconSize(QSize(140, 140))

        self.h5_home_button_audio.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/audio.png'))
        self.h5_home_button_audio.setIconSize(QSize(140, 140))
        self.h5_home_button_hazard.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/hazard.png'))
        self.h5_home_button_hazard.setIconSize(QSize(140, 140))
        self.h5_home_button_phone.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/phone.png'))
        self.h5_home_button_phone.setIconSize(QSize(140, 140))
        self.h5_home_button_nav.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/nav.png'))
        self.h5_home_button_nav.setIconSize(QSize(140, 140))
        self.h5_home_button_settings.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/settings.png'))
        self.h5_home_button_settings.setIconSize(QSize(140, 140))

        # self.horizontalSubLayout_5.addWidget(self.button_temp)  # add button to layout
        self.h5_home.addWidget(self.h5_home_button_seat_1)
        self.h5_home.addWidget(self.h5_home_button_phone)
        self.h5_home.addWidget(self.h5_home_button_AC)
        self.h5_home.addWidget(self.h5_home_button_max)
        self.h5_home.addWidget(self.h5_home_button_hazard)
        self.h5_home.addWidget(self.h5_home_button_audio)
        self.h5_home.addWidget(self.h5_home_button_nav)
        self.h5_home.addWidget(self.h5_home_button_settings)
        self.h5_home.addWidget(self.h5_home_button_seat_2)

        parent_layout.addLayout(self.h5_home)  # add to vertical layout

    def add_h1_fan(self, parent_layout, frame):
        self.h1_fan = QtWidgets.QHBoxLayout()
        self.h1_fan.setObjectName("h1_fan")

        self.h1_fan_button_left_arrow = QtWidgets.QPushButton(frame)  # Create button
        self.h1_fan_button_right_arrow = QtWidgets.QPushButton(frame)
        self.h1_fan_button_left_arrow.setFixedSize(200, 200)  # set size
        self.h1_fan_button_right_arrow.setFixedSize(200, 200)

        self.h1_fan_button_left_arrow.setObjectName("h1_fan Button Left Arrow")  # set name
        self.h1_fan_button_right_arrow.setObjectName("h1_fan Button Right Arrow")

        self.h1_fan_button_left_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/left_arrow.png'))  # set icon
        self.h1_fan_button_left_arrow.setIconSize(QSize(180, 180))
        self.h1_fan_button_right_arrow.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/right_arrow.png'))
        self.h1_fan_button_right_arrow.setIconSize(QSize(180, 180))

        self.h1_fan_button_left_arrow.setStyleSheet("background-color: white;")  # button color
        self.h1_fan_button_right_arrow.setStyleSheet("background-color: white;")

        self.h1_fan.addWidget(self.h1_fan_button_left_arrow)
        self.h1_fan.addWidget(self.h1_fan_button_right_arrow)  # add to layout

        spacer_h1_fan_1 = QtWidgets.QSpacerItem(1000, 200, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h1_fan.addItem(spacer_h1_fan_1)
        parent_layout.addLayout(self.h1_fan)

    def add_h2_fan(self, parent_layout, frame):
        self.h2_fan = QtWidgets.QHBoxLayout()
        self.h2_fan.setObjectName("h2_fan")

        self.h2_fan_button_label = QtWidgets.QPushButton(frame)  # Create button
        self.h2_fan_button_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.h2_fan_button_label.setFixedSize(400, 200)
        self.h2_fan_button_label.setObjectName("h2_fan Label Button")
        self.h2_fan_button_label.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/time.png'))  # add icon
        self.h2_fan_button_label.setIconSize(QSize(700, 400))
        self.h2_fan.addWidget(self.h2_fan_button_label)  # add to layout

        self.h2_fan_button_label.setStyleSheet("background-color: white;")  # button color

        spacer_h2_fan_1 = QtWidgets.QSpacerItem(1920, 100, QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h2_fan.addItem(spacer_h2_fan_1)
        parent_layout.addLayout(self.h2_fan)  # Add to the vertical layout

        self.h2_fan_button_extra = QtWidgets.QPushButton(frame)  # Create button
        self.h2_fan_button_extra.setFixedSize(400, 300)
        self.h2_fan_button_extra.setStyleSheet("background-color: white;")  # button color
        parent_layout.addWidget(self.h2_fan_button_extra)  # add button to layout

    def add_h3_fan(self, parent_layout, frame):
        self.h3_fan = QtWidgets.QHBoxLayout()

        self.h3_fan_button_home = QtWidgets.QPushButton(frame)  # Create button
        self.h3_fan_button_home.setFixedSize(400, 200)  # set size
        self.h3_fan_button_home.setObjectName("h3_fan Fan Button")  # set name
        self.h3_fan_button_home.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/home.png'))
        self.h3_fan_button_home.setIconSize(QSize(300, 180))

        self.h3_fan_button_home.setStyleSheet("background-color: white;")

        self.h3_fan.addWidget(self.h3_fan_button_home)  # add button to layout

        spacer_h3_fan_1 = QtWidgets.QSpacerItem(200, 200, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_fan.addItem(spacer_h3_fan_1)
        spacer_h3_fan_2 = QtWidgets.QSpacerItem(1900, 200, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h3_fan.addItem(spacer_h3_fan_2)

        parent_layout.addLayout(self.h3_fan)  # Add to the vertical layout


    def add_h4_fan(self, parent_layout, frame):

        # Initialize fan level variable
        self.fan_level2 = 1

        # Define a method to update bar colors based on fan level
        def update_fan_speed_display2():
            bars = [self.h3_climate_button_bar_12, self.h3_climate_button_bar_22,
                    self.h3_climate_button_bar_32, self.h3_climate_button_bar_42,
                    self.h3_climate_button_bar_52]

            # Set each bar's color based on the current fan level
            for i in range(5):
                if i < self.fan_level2:
                    bars[i].setStyleSheet("background-color: black;")  # Filled color
                else:
                    bars[i].setStyleSheet("background-color: white;")  # Unfilled color

        # Define methods to increase and decrease fan level
        def increase_fan_level2():
            if self.fan_level2 < 5:
                self.fan_level2 += 1
                update_fan_speed_display2()

        def decrease_fan_level2():
            if self.fan_level2 > 1:
                self.fan_level2 -= 1
                update_fan_speed_display2()

        self.h4_fan = QtWidgets.QHBoxLayout()

        # First horizontal layout (left side)
        self.h4_fan_leftLayout = QtWidgets.QHBoxLayout()
        self.h4_fan_button_wiper = QtWidgets.QPushButton(frame)
        self.h4_fan_button_light = QtWidgets.QPushButton(frame)
        self.h4_fan_button_wiper.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_fan_button_light.setFixedSize(200, 200)  # Check Size Requirements
        self.h4_fan_button_light.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/light_bulb.png'))
        self.h4_fan_button_light.setIconSize(QSize(180, 180))
        self.h4_fan_button_wiper.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/wiper.png'))
        self.h4_fan_button_wiper.setIconSize(QSize(180, 180))

        self.h4_fan_button_wiper.setStyleSheet("background-color: white;")
        self.h4_fan_button_light.setStyleSheet("background-color: white;")

        self.h4_fan_leftLayout.addWidget(self.h4_fan_button_wiper)
        self.h4_fan_leftLayout.addWidget(self.h4_fan_button_light)

        # Add left frame to main layout
        self.h4_fan.addLayout(self.h4_fan_leftLayout)

        # Second vertical layout (right side)
        self.h4_fan_rightLayout = QtWidgets.QVBoxLayout()

        # Second horizontal layout (within right side)
        self.h4_fan_rightTopLayout = QtWidgets.QHBoxLayout()

        # Add spacer item to top right layout
        # h4_fan_1_spacer = QtWidgets.QSpacerItem(500, 80, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # self.h4_fan_rightTopLayout.addSpacerItem(h4_fan_1_spacer)

        # Third horizontal layout (within right side)
        self.h4_fan_rightBottomLayout = QtWidgets.QHBoxLayout()

        h4_fan_spacer_2 = QtWidgets.QSpacerItem(1700, 150, QtWidgets.QSizePolicy.Maximum,
                                                 QtWidgets.QSizePolicy.Minimum)  # add spacer
        self.h4_fan_rightBottomLayout.addItem(h4_fan_spacer_2)


        # Create the fan logo button (without functionality) and set its style
        self.fan_logo_button = QtWidgets.QPushButton(frame)
        self.fan_logo_button.setFixedSize(50, 50)
        self.fan_logo_button.setStyleSheet("background-color: transparent; border: none;")  # Adjust style as needed
        #self.fan_logo_button.setIcon(
            #QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fanclimate.png'))  # Add fan icon image
        self.fan_logo_button.setIconSize(QSize(50, 50))  # Adjust icon size to fit button

        # Create the minus button and connect it to decrease fan level
        self.h3_climate_button_minus2 = QtWidgets.QPushButton("−", frame)
        self.h3_climate_button_minus2.setFixedSize(50, 50)
        self.h3_climate_button_minus2.setStyleSheet("background-color: white; font-size: 35px; color: black;")
        self.h3_climate_button_minus2.clicked.connect(decrease_fan_level2)
        empty_label_minus_bottom = QtWidgets.QLabel(" ")
        empty_label_minus_bottom.setStyleSheet("font-size: 1px;")

        # Stack the fan logo and minus button vertically
        logo_and_minus_layout2 = QtWidgets.QVBoxLayout()
        logo_and_minus_layout2.addWidget(self.fan_logo_button, alignment=QtCore.Qt.AlignCenter)
        logo_and_minus_layout2.addWidget(self.h3_climate_button_minus2, alignment=QtCore.Qt.AlignCenter)
        logo_and_minus_layout2.addWidget(empty_label_minus_bottom)

        # Add first spacer

        self.h4_fan_button_spacer = QtWidgets.QPushButton()  # Create button
        self.h4_fan_button_spacer.setFixedSize(50, 125)  # set size
        self.h4_fan_button_spacer.setObjectName("Spacer")  # set name
        self.h4_fan_button_spacer.setStyleSheet("background-color: transparent;")

        # Add the combined layout to the main horizontal layout
        self.h4_fan.addWidget(self.h4_fan_button_spacer)
        self.h4_fan.addLayout(logo_and_minus_layout2)

        # Spacer
        self.h3_climate_button_spacer_minus = QtWidgets.QPushButton(frame)
        self.h3_climate_button_spacer_minus.setFixedSize(30, 125)
        self.h3_climate_button_spacer_minus.setStyleSheet("background-color: transparent;")
        self.h4_fan.addWidget(self.h3_climate_button_spacer_minus)

        # Create a horizontal layout for the bars
        bars_layout2 = QtWidgets.QHBoxLayout()

        # Create each spacer for each bar button
        self.h4_climate_button_spacer_tiny_1 = QtWidgets.QPushButton(frame)  # Create button
        self.h4_climate_button_spacer_tiny_1.setFixedSize(2, 1)  # set size
        self.h4_climate_button_spacer_tiny_1.setObjectName("Spacer Button 1")  # set name

        # Create each bar button and add it to bars_layout with consistent bottom alignment
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)
        self.h3_climate_button_bar_12 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_12.setFixedSize(30, 50)
        self.h3_climate_button_bar_12.setStyleSheet("background-color: white;")
        bars_layout2.addWidget(self.h3_climate_button_bar_12, alignment=QtCore.Qt.AlignBottom)
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)

        self.h3_climate_button_bar_22 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_22.setFixedSize(30, 60)
        self.h3_climate_button_bar_22.setStyleSheet("background-color: white;")
        bars_layout2.addWidget(self.h3_climate_button_bar_22, alignment=QtCore.Qt.AlignBottom)
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)

        self.h3_climate_button_bar_32 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_32.setFixedSize(30, 70)
        self.h3_climate_button_bar_32.setStyleSheet("background-color: white;")
        bars_layout2.addWidget(self.h3_climate_button_bar_32, alignment=QtCore.Qt.AlignBottom)
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)

        self.h3_climate_button_bar_42 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_42.setFixedSize(30, 80)
        self.h3_climate_button_bar_42.setStyleSheet("background-color: white;")
        bars_layout2.addWidget(self.h3_climate_button_bar_42, alignment=QtCore.Qt.AlignBottom)
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)

        self.h3_climate_button_bar_52 = QtWidgets.QPushButton(frame)
        self.h3_climate_button_bar_52.setFixedSize(30, 90)
        self.h3_climate_button_bar_52.setStyleSheet("background-color: white;")
        bars_layout2.addWidget(self.h3_climate_button_bar_52, alignment=QtCore.Qt.AlignBottom)
        bars_layout2.addWidget(self.h4_climate_button_spacer_tiny_1)

        # Create an empty label below to shift the bars upwards
        empty_label_top = QtWidgets.QLabel(" ")
        empty_label_top.setStyleSheet("font-size: 1px;")
        empty_label_bottom = QtWidgets.QLabel(" ")
        empty_label_bottom.setStyleSheet("font-size: 1px;")

        # Create numbered labels below each bar
        number_labels_layout = QtWidgets.QHBoxLayout()
        for i in range(1, 6):
            number_label = QtWidgets.QLabel(str(i))
            number_label.setStyleSheet("font-size: 30px;")  # Set font size to 30 pixels
            number_labels_layout.addWidget(number_label, alignment=QtCore.Qt.AlignHCenter)  # Center align each number

        # Create a vertical layout to hold the bars layout and the number labels
        bars_with_empty_label_layout = QtWidgets.QVBoxLayout()
        bars_with_empty_label_layout.addWidget(empty_label_top)  # Adjust top alignment if needed
        bars_with_empty_label_layout.addLayout(bars_layout2)  # Add bars layout
        bars_with_empty_label_layout.addLayout(number_labels_layout)  # Add number labels below bars
        bars_with_empty_label_layout.addWidget(empty_label_bottom)  # Adjust top alignment if needed

        # Add the combined bars layout and empty label to the main horizontal layout
        self.h4_fan.addLayout(bars_with_empty_label_layout)

        # Spacer
        self.h3_climate_button_spacer_plus = QtWidgets.QPushButton(frame)
        self.h3_climate_button_spacer_plus.setFixedSize(30, 125)
        self.h3_climate_button_spacer_plus.setStyleSheet("background-color: transparent;")

        # Add plus button and connect it to increase fan level
        self.h3_climate_button_plus2 = QtWidgets.QPushButton("+", frame)
        self.h3_climate_button_plus2.setFixedSize(50, 50)
        self.h3_climate_button_plus2.setStyleSheet("background-color: white; font-size: 35px; color: black;")
        self.h3_climate_button_plus2.clicked.connect(increase_fan_level2)  # Connect to increase function

        # Initialize the fan speed display
        update_fan_speed_display2()

        self.h4_fan.addWidget(self.h3_climate_button_spacer_plus)
        self.h4_fan.addWidget(self.h3_climate_button_plus2)

        # Add top and bottom layouts to right layout
        self.h4_fan_rightLayout.addLayout(self.h4_fan_rightTopLayout)
        self.h4_fan_rightLayout.addLayout(self.h4_fan_rightBottomLayout)

        # Add right frame to main layout
        self.h4_fan.addLayout(self.h4_fan_rightLayout)
        parent_layout.addLayout(self.h4_fan)

        '''
           self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_wiper_off)  # add to layout
           self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_one)
           self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_two)
           self.h4_wiper_rightBottomLayout.addWidget(self.h4_wiper_button_three)
        '''

    def add_h5_fan(self, parent_layout, frame):
        self.h5_fan = QtWidgets.QHBoxLayout()

        self.add_temperature_control(self.h5_fan)

        # self.button_temp = QtWidgets.QPushButton(frame)  # Create button
        self.h5_fan_button_fan = QtWidgets.QPushButton(frame)
        self.h5_fan_button_AC = QtWidgets.QPushButton(frame)
        self.h5_fan_button_max = QtWidgets.QPushButton(frame)
        self.h5_fan_button_audio = QtWidgets.QPushButton(frame)
        self.h5_fan_button_hazard = QtWidgets.QPushButton(frame)
        self.h5_fan_button_phone = QtWidgets.QPushButton(frame)
        self.h5_fan_button_nav = QtWidgets.QPushButton(frame)
        self.h5_fan_button_settings = QtWidgets.QPushButton(frame)

        # self.button_temp.setFixedSize(300, 150)  # set size
        self.h5_fan_button_fan.setFixedSize(200, 150)
        self.h5_fan_button_AC.setFixedSize(200, 150)
        self.h5_fan_button_max.setFixedSize(200, 150)
        self.h5_fan_button_audio.setFixedSize(200, 150)
        self.h5_fan_button_hazard.setFixedSize(200, 150)
        self.h5_fan_button_phone.setFixedSize(200, 150)
        self.h5_fan_button_nav.setFixedSize(200, 150)
        self.h5_fan_button_settings.setFixedSize(200, 150)

        # self.button_temp.setStyleSheet("background-color: black;")
        self.h5_fan_button_fan.setStyleSheet("background-color: black;")
        self.h5_fan_button_AC.setStyleSheet("background-color: black;")
        self.h5_fan_button_max.setStyleSheet("background-color: black;")
        self.h5_fan_button_audio.setStyleSheet("background-color: black;")
        self.h5_fan_button_hazard.setStyleSheet("background-color: black;")
        self.h5_fan_button_phone.setStyleSheet("background-color: black;")
        self.h5_fan_button_nav.setStyleSheet("background-color: black;")
        self.h5_fan_button_settings.setStyleSheet("background-color: black;")

        # self.button_temp.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/.png'))
        # self.button_temp.setIconSize(QSize(140, 140))
        self.h5_fan_button_fan.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/fan.png'))
        self.h5_fan_button_fan.setIconSize(QSize(140, 140))
        self.h5_fan_button_AC.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/ac.png'))
        self.h5_fan_button_AC.setIconSize(QSize(213, 200))
        self.h5_fan_button_max.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/rear_defrost_white.png.png'))
        self.h5_fan_button_max.setIconSize(QSize(140, 140))
        self.h5_fan_button_audio.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/audio.png'))
        self.h5_fan_button_audio.setIconSize(QSize(140, 140))
        self.h5_fan_button_hazard.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/hazard.png'))
        self.h5_fan_button_hazard.setIconSize(QSize(140, 140))
        self.h5_fan_button_phone.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/phone.png'))
        self.h5_fan_button_phone.setIconSize(QSize(140, 140))
        self.h5_fan_button_nav.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/nav.png'))
        self.h5_fan_button_nav.setIconSize(QSize(140, 140))
        self.h5_fan_button_settings.setIcon(QIcon('C:/Users/D-Lab/Documents/TouchScreenInterface/icons/settings.png'))
        self.h5_fan_button_settings.setIconSize(QSize(140, 140))

        # self.horizontalSubLayout_5.addWidget(self.button_temp)  # add button to layout
        self.h5_fan.addWidget(self.h5_fan_button_fan)
        self.h5_fan.addWidget(self.h5_fan_button_AC)
        self.h5_fan.addWidget(self.h5_fan_button_max)
        self.h5_fan.addWidget(self.h5_fan_button_audio)
        self.h5_fan.addWidget(self.h5_fan_button_hazard)
        self.h5_fan.addWidget(self.h5_fan_button_phone)
        self.h5_fan.addWidget(self.h5_fan_button_nav)
        self.h5_fan.addWidget(self.h5_fan_button_settings)

        parent_layout.addLayout(self.h5_fan)  # add to vertical layout

    def add_temperature_control(self, layout):
        temperature_control = TemperatureControl()
        layout.addWidget(temperature_control)

    def retranslateUi(self, MainWindow):
        '''
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Task is ready", None))
        self.btnStart_.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None))
        self.editParticipantID.setText(QtWidgets.QApplication.translate("MainWindow", "Participant ID", None))
        self.btnDone.setText(QtWidgets.QApplication.translate("MainWindow", "DONE", None))
        self.btnUp.setText(QtWidgets.QApplication.translate("MainWindow", "▲", None))
        self.btnDown.setText(QtWidgets.QApplication.translate("MainWindow", "▼", None))
        self.btnLabelUp.setText(QtWidgets.QApplication.translate("MainWindow", "Missions Discover Project", None))
        self.btnLabelDown.setText(QtWidgets.QApplication.translate("MainWindow", "Mistypes Missions Disavows", None))
        self.btnSubmit.setText(QtWidgets.QApplication.translate("MainWindow", "Submit", None))
        self.lblFeedback.setText(QtWidgets.QApplication.translate("MainWindow", "Correct", None))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Task is ready", None))
        self.btnStart.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None))
        self.label_done.setText(QtWidgets.QApplication.translate("MainWindow", "Your drive report is ready.", None))
        self.label_proceed.setText(QtWidgets.QApplication.translate("MainWindow", "Proceed?", None))
        self.label_loading.setText(QtWidgets.QApplication.translate("MainWindow", "Loading...", None))
        '''

# play map video in html:
    def initVideoPlayer(self):
        """ Initialize and embed the video player in the home frame using HTML for MP4 """
        # Create the video player widget using QWebEngineView
        self.video_player = QWebEngineView(self.centralWidget)

        # Define the HTML for the video player with autoplay enabled
        video_html = """
               <html>
               <body style="margin: 0; overflow: hidden;">
               <iframe width="100%" height="100%" 
                   src="https://www.youtube.com/embed/x23iBPlMkyU?autoplay=1&mute=1&loop=1&playlist=x23iBPlMkyU" 
                   frameborder="0" 
                   allow="autoplay; encrypted-media; fullscreen">
               </iframe>
               </body>
               </html>
           """
        self.video_player.setHtml(video_html)

        # Explicitly set size and position
        self.video_player.setGeometry(400, 0, 1520, 930)  # Set position and size
        self.video_player.setFixedSize(1520, 930)  # Ensure fixed size

        # Adjust size policies to avoid layout conflicts
        self.video_player.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # Show the video player
        self.video_player.show()


    def setupWhiteBox(self):
        # Create a new frame for the white box
        self.white_box_frame = QtWidgets.QFrame(self)
        self.white_box_frame.setStyleSheet("background-color: white;")
        self.white_box_frame.setFixedSize(830, 350)  # Adjust width and height as needed

        # Position the white box in the bottom-left corner
        screen_height = self.height()
        screen_width = self.width()
        self.white_box_frame.move(0, screen_height - 350)  # 20 px from left and 20 px above bottom

        # Hide it initially
        self.white_box_frame.hide()