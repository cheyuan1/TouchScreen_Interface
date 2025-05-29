import sys
from PySide2 import QtCore, QtWidgets, QtMultimedia
from PySide2.QtWidgets import QMainWindow
from Version2TouchScreen import Ui_MainWindow
from graph import Graph
from datetime import datetime
import os
import time
import csv
from Receiver import Receiver
from DummyReceiver import DummyReceiver


def create_csv_file(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Get the current date and time for the file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"ButtonPresses_{timestamp}.csv"

    # Full path to the file
    full_file_path = os.path.join(folder_path, file_name)

    # Create the file and write the header
    with open(full_file_path, 'w', newline='') as csvfile:
        toFile = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # Write the header row
        toFile.writerow(['Button Name', 'Timestamp', 'Elapsed Time', 'FrameNum'])

    return full_file_path  # Return the full path to the file

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Define the folder for saving logs
        folder_path = 'C:/Users/D-Lab/Documents/TouchScreenInterface/Results/P41/'

        # Initialize the Receiver object
        #self.receiver = DummyReceiver()
        self.receiver = Receiver()
        self.receiver.start()  # Start the Receiver thread

        # Define variables
        self.initAll = False
        self.excel_file = create_csv_file(folder_path)  # Create a new CSV file for this attempt
        self.start_time = time.time()

        # Set up the GUI
        self.setupUi(self)

        # Install event filter to capture all mouse clicks
        QtWidgets.QApplication.instance().installEventFilter(self)

        # Show the application in fullscreen
        self.showFullScreen()

        # Initialize video player after the setup
        self.initVideoPlayer()

        # Setting the frames to be full screen
        width = 1920
        height = 1080

        # Create the graph object
        self.graph = Graph(width, height)

        # Hide all the frames except the initial
        self.home_frame.hide()
        self.fan_background_frame.hide()
        #self.home_frame.raise_()
        self.light_frame.hide()
        self.wiper_frame.hide()
        self.climate_frame.hide()
        self.fan_frame.hide()

        # Position and resize the frames.


        self.home_frame.move(0, 0)
        self.home_frame.resize(width, height)
        self.light_frame.move(0, 0)
        self.light_frame.resize(width, height)
        self.wiper_frame.move(0, 0)
        self.wiper_frame.resize(width, height)

        self.climate_frame.move(0, 0)
        self.climate_frame.resize(width, height)

        self.fan_frame.move(0, 0)
        self.fan_frame.resize(width, height)

        self.video_player.move(400, 0)
        self.video_player.resize(1540, 940)

        ''' BUTTONS '''

        self.ok_button.clicked.connect(self.showHomeFrame)
        self.button_home.clicked.connect(self.showHomeFrame)
        self.h3_home_button_home.clicked.connect(self.showHomeFrame)
        self.h3_light_button_home.clicked.connect(self.showHomeFrame)
        self.h3_wiper_button_home.clicked.connect(self.showHomeFrame)
        self.h3_fan_button_home.clicked.connect(self.showHomeFrame)

        self.button_light.clicked.connect(self.showLightFrame)
        self.h4_wiper_button_light.clicked.connect(self.showLightFrame)
        self.h4_home_button_light.clicked.connect(self.showLightFrame)
        self.h4_light_button_light.clicked.connect(self.showLightFrame)
        self.h4_fan_button_light.clicked.connect(self.showLightFrame)

        self.button_wiper.clicked.connect(self.showWiperFrame)
        self.h4_light_button_wiper.clicked.connect(self.showWiperFrame)
        self.h4_wiper_button_wiper.clicked.connect(self.showWiperFrame)
        self.h4_home_button_wiper.clicked.connect(self.showWiperFrame)
        self.h4_fan_button_wiper.clicked.connect(self.showWiperFrame)

        self.button_AC.clicked.connect(self.showClimateFrame)
        self.h5_light_button_AC.clicked.connect(self.showClimateFrame)
        self.h5_wiper_button_AC.clicked.connect(self.showClimateFrame)
        self.h5_home_button_AC.clicked.connect(self.showClimateFrame)
        self.h5_fan_button_AC.clicked.connect(self.showClimateFrame)

        self.button_fan.clicked.connect(self.showFanFrame)
        self.h5_light_button_fan.clicked.connect(self.showFanFrame)
        self.h5_wiper_button_fan.clicked.connect(self.showFanFrame)
        self.h5_home_button_fan.clicked.connect(self.showFanFrame)
        self.h5_fan_button_fan.clicked.connect(self.showFanFrame)

        # what happens when a button is clicked

        # home frame buttons
        self.h1_home_button_left_arrow.clicked.connect(lambda: self.highlight_button(self.h1_home_button_left_arrow))
        self.h1_home_button_right_arrow.clicked.connect(lambda: self.highlight_button(self.h1_home_button_right_arrow))

        self.h3_home_button_home.clicked.connect(lambda: self.highlight_button(self.h3_home_button_home))

        self.h4_home_button_light.clicked.connect(lambda: self.highlight_button(self.h4_home_button_light))
        self.h4_home_button_wiper.clicked.connect(lambda: self.highlight_button(self.h4_home_button_wiper))

        self.h5_home_button_AC.clicked.connect(lambda: self.highlight_button(self.h5_home_button_AC))
        self.h5_home_button_hazard.clicked.connect(lambda: self.highlight_button(self.h5_home_button_hazard))
        self.h5_home_button_max.clicked.connect(lambda: self.highlight_button(self.h5_home_button_max))
        self.h5_home_button_fan.clicked.connect(lambda: self.highlight_button(self.h5_home_button_fan))
        self.h5_home_button_nav.clicked.connect(lambda: self.highlight_button(self.h5_home_button_nav))
        self.h5_home_button_audio.clicked.connect(lambda: self.highlight_button(self.h5_home_button_audio))
        self.h5_home_button_phone.clicked.connect(lambda: self.highlight_button(self.h5_home_button_phone))
        self.h5_home_button_settings.clicked.connect(lambda: self.highlight_button(self.h5_home_button_settings))

        # fan frame buttons
        self.h1_fan_button_left_arrow.clicked.connect(lambda: self.highlight_button(self.h1_fan_button_left_arrow))
        self.h1_fan_button_right_arrow.clicked.connect(lambda: self.highlight_button(self.h1_fan_button_right_arrow))

        self.h3_fan_button_home.clicked.connect(lambda: self.highlight_button(self.h3_fan_button_home))

        self.h4_fan_button_light.clicked.connect(lambda: self.highlight_button(self.h4_fan_button_light))
        self.h4_fan_button_wiper.clicked.connect(lambda: self.highlight_button(self.h4_fan_button_wiper))

        self.h5_fan_button_AC.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_AC))
        self.h5_fan_button_hazard.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_hazard))
        self.h5_fan_button_max.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_max))
        self.h5_fan_button_fan.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_fan))
        self.h5_fan_button_nav.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_nav))
        self.h5_fan_button_audio.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_audio))
        self.h5_fan_button_phone.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_phone))
        self.h5_fan_button_settings.clicked.connect(lambda: self.highlight_button(self.h5_fan_button_settings))


        # light frame buttons
        self.h1_light_button_left_arrow.clicked.connect(lambda: self.highlight_button(self.h1_light_button_left_arrow))
        self.h1_light_button_right_arrow.clicked.connect(lambda: self.highlight_button(self.h1_light_button_right_arrow))

        self.h3_light_button_home.clicked.connect(lambda: self.highlight_button(self.h3_light_button_home))

        self.h4_light_button_light_off.clicked.connect(lambda: self.highlight_button(self.h4_light_button_light_off))
        self.h4_light_button_blinker.clicked.connect(lambda: self.highlight_button(self.h4_light_button_blinker))
        self.h4_light_button_light.clicked.connect(lambda: self.highlight_button(self.h4_light_button_light))
        self.h4_light_button_beam.clicked.connect(lambda: self.highlight_button(self.h4_light_button_beam))
        self.h4_light_button_beam_off.clicked.connect(lambda: self.highlight_button(self.h4_light_button_beam_off))
        self.h4_light_button_wiper.clicked.connect(lambda: self.highlight_button(self.h4_light_button_wiper))

        self.h5_light_button_AC.clicked.connect(lambda: self.highlight_button(self.h5_light_button_AC))
        self.h5_light_button_hazard.clicked.connect(lambda: self.highlight_button(self.h5_light_button_hazard))
        self.h5_light_button_max.clicked.connect(lambda: self.highlight_button(self.h5_light_button_max))
        self.h5_light_button_fan.clicked.connect(lambda: self.highlight_button(self.h5_light_button_fan))
        self.h5_light_button_nav.clicked.connect(lambda: self.highlight_button(self.h5_light_button_nav))
        self.h5_light_button_audio.clicked.connect(lambda: self.highlight_button(self.h5_light_button_audio))
        self.h5_light_button_phone.clicked.connect(lambda: self.highlight_button(self.h5_light_button_phone))
        self.h5_light_button_settings.clicked.connect(lambda: self.highlight_button(self.h5_light_button_settings))

        # wiper frame buttons
        self.h1_wiper_button_left_arrow.clicked.connect(lambda: self.highlight_button(self.h1_wiper_button_left_arrow))
        self.h1_wiper_button_right_arrow.clicked.connect(lambda: self.highlight_button(self.h1_wiper_button_right_arrow))

        self.h3_wiper_button_home.clicked.connect(lambda: self.highlight_button(self.h3_wiper_button_home))

        self.h4_wiper_button_wiper_off.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_wiper_off))
        self.h4_wiper_button_three.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_three))
        self.h4_wiper_button_light.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_light))
        self.h4_wiper_button_one.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_one))
        self.h4_wiper_button_two.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_two))
        self.h4_wiper_button_wiper.clicked.connect(lambda: self.highlight_button(self.h4_wiper_button_wiper))

        self.h5_wiper_button_AC.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_AC))
        self.h5_wiper_button_hazard.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_hazard))
        self.h5_wiper_button_max.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_max))
        self.h5_wiper_button_fan.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_fan))
        self.h5_wiper_button_nav.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_nav))
        self.h5_wiper_button_audio.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_audio))
        self.h5_wiper_button_phone.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_phone))
        self.h5_wiper_button_settings.clicked.connect(lambda: self.highlight_button(self.h5_wiper_button_settings))

        # misc. buttons
        self.button_left_arrow.clicked.connect(lambda: self.highlight_button(self.button_left_arrow))
        self.button_right_arrow.clicked.connect(lambda: self.highlight_button(self.button_right_arrow))
        self.button_hazard.clicked.connect(lambda: self.highlight_button(self.button_hazard))
        self.button_fan.clicked.connect(lambda: self.highlight_button(self.button_fan))
        self.button_max.clicked.connect(lambda: self.highlight_button(self.button_max))
        self.button_audio.clicked.connect(lambda: self.highlight_button(self.button_audio))
        self.button_phone.clicked.connect(lambda: self.highlight_button(self.button_phone))
        self.button_nav.clicked.connect(lambda: self.highlight_button(self.button_nav))
        self.button_settings.clicked.connect(lambda: self.highlight_button(self.button_settings))

        # climate frame buttons
        self.h2_climate_button_off.clicked.connect(lambda: self.highlight_button(self.h2_climate_button_off))

        self.h3_climate_button_stickman_1.clicked.connect(lambda: self.highlight_button(self.h3_climate_button_stickman_1))
        self.h3_climate_button_stickman_2.clicked.connect(lambda: self.highlight_button(self.h3_climate_button_stickman_2))
        self.h3_climate_button_stickman_3.clicked.connect(lambda: self.highlight_button(self.h3_climate_button_stickman_3))
        self.h3_climate_button_stickman_4.clicked.connect(lambda: self.highlight_button(self.h3_climate_button_stickman_4))
        self.h3_climate_button_defrost.clicked.connect(lambda: self.highlight_button(self.h3_climate_button_defrost))

        self.h4_climate_button_airflow_1.clicked.connect(lambda: self.highlight_button(self.h4_climate_button_airflow_1))
        self.h4_climate_button_airflow_2.clicked.connect(lambda: self.highlight_button(self.h4_climate_button_airflow_2))
        self.h4_climate_button_max_ac.clicked.connect(lambda: self.highlight_button(self.h4_climate_button_max_ac))
       # self.h4_climate_button_rear_defrost.clicked.connect(lambda: self.highlight_button(self.h4_climate_button_rear_defrost))
        self.h4_climate_button_auto.clicked.connect(lambda: self.highlight_button(self.h4_climate_button_auto))

        # LOGS

        self.h2_slider.valueChanged.connect(lambda value: self.log_button_click(f"Slider Value Change: {value}"))
        self.button_seat_1.clicked.connect(lambda: self.log_button_click("Left Seat Warmer"))
        self.button_seat_2.clicked.connect(lambda: self.log_button_click("Right Seat Warmer"))
        self.h5_light_button_seat_1.clicked.connect(lambda: self.log_button_click("Left Seat Warmer"))
        self.h5_light_button_seat_2.clicked.connect(lambda: self.log_button_click("Right Seat Warmer"))
        self.h5_wiper_button_seat_1.clicked.connect(lambda: self.log_button_click("Left Seat Warmer"))
        self.h5_wiper_button_seat_2.clicked.connect(lambda: self.log_button_click("Right Seat Warmer"))
        self.h5_home_button_seat_1.clicked.connect(lambda: self.log_button_click("Left Seat Warmer"))
        self.h5_home_button_seat_2.clicked.connect(lambda: self.log_button_click("Right Seat Warmer"))
        # home frame buttons
        self.h1_home_button_left_arrow.clicked.connect(lambda: self.log_button_click("Left Indicator"))
        self.h1_home_button_right_arrow.clicked.connect(lambda: self.log_button_click("Right Indicator"))

        self.h3_home_button_home.clicked.connect(lambda: self.log_button_click("Home Button"))

        self.h4_home_button_light.clicked.connect(lambda: self.log_button_click("Light Options"))
        self.h4_home_button_wiper.clicked.connect(lambda: self.log_button_click("Wiper Options"))

        self.h5_home_button_AC.clicked.connect(lambda: self.log_button_click("Climate Control"))
        self.h5_home_button_hazard.clicked.connect(lambda: self.log_button_click("Hazard"))
        self.h5_home_button_max.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.h5_home_button_fan.clicked.connect(lambda: self.log_button_click("Fan Settings"))
        self.h5_home_button_nav.clicked.connect(lambda: self.log_button_click("Navigation"))
        self.h5_home_button_audio.clicked.connect(lambda: self.log_button_click("Audio"))
        self.h5_home_button_phone.clicked.connect(lambda: self.log_button_click("Phone"))
        self.h5_home_button_settings.clicked.connect(lambda: self.log_button_click("Settings"))

        # fan frame buttons
        self.h1_fan_button_left_arrow.clicked.connect(lambda: self.log_button_click("Left Indicator"))
        self.h1_fan_button_right_arrow.clicked.connect(lambda: self.log_button_click("Right Indicator"))

        self.h3_fan_button_home.clicked.connect(lambda: self.log_button_click("Home Button"))

        self.h4_fan_button_light.clicked.connect(lambda: self.log_button_click("Light Options"))
        self.h4_fan_button_wiper.clicked.connect(lambda: self.log_button_click("Wiper Options"))
        self.h3_climate_button_minus2.clicked.connect(lambda: self.log_button_click("Decrease Fan Speed"))
        self.h3_climate_button_plus2.clicked.connect(lambda: self.log_button_click("Increase Fan Speed"))

        self.h5_fan_button_AC.clicked.connect(lambda: self.log_button_click("Climate Control"))
        self.h5_fan_button_hazard.clicked.connect(lambda: self.log_button_click("Hazard"))
        self.h5_fan_button_max.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.h5_fan_button_fan.clicked.connect(lambda: self.log_button_click("Fan Settings"))
        self.h5_fan_button_nav.clicked.connect(lambda: self.log_button_click("Navigation"))
        self.h5_fan_button_audio.clicked.connect(lambda: self.log_button_click("Audio"))
        self.h5_fan_button_phone.clicked.connect(lambda: self.log_button_click("Phone"))
        self.h5_fan_button_settings.clicked.connect(lambda: self.log_button_click("Settings"))

        # light frame buttons
        self.h1_light_button_left_arrow.clicked.connect(lambda: self.log_button_click("Left Indicator"))
        self.h1_light_button_right_arrow.clicked.connect(lambda: self.log_button_click("Right Indicator"))

        self.h3_light_button_home.clicked.connect(lambda: self.log_button_click("Home Button"))

        self.h4_light_button_light_off.clicked.connect(lambda: self.log_button_click("Lights Off"))
        self.h4_light_button_blinker.clicked.connect(lambda: self.log_button_click("Side Lights"))
        self.h4_light_button_light.clicked.connect(lambda: self.log_button_click("Light Options"))
        self.h4_light_button_beam.clicked.connect(lambda: self.log_button_click("Automatic Lights"))
        self.h4_light_button_beam_off.clicked.connect(lambda: self.log_button_click("Low Beams"))
        self.h4_light_button_wiper.clicked.connect(lambda: self.log_button_click("Wiper Options"))

        self.h5_light_button_AC.clicked.connect(lambda: self.log_button_click("Climate Control"))
        self.h5_light_button_hazard.clicked.connect(lambda: self.log_button_click("Hazard"))
        self.h5_light_button_max.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.h5_light_button_fan.clicked.connect(lambda: self.log_button_click("Fan Settings"))
        self.h5_light_button_nav.clicked.connect(lambda: self.log_button_click("Navigation"))
        self.h5_light_button_audio.clicked.connect(lambda: self.log_button_click("Audio"))
        self.h5_light_button_phone.clicked.connect(lambda: self.log_button_click("Phone"))
        self.h5_light_button_settings.clicked.connect(lambda: self.log_button_click("Settings"))

        # wiper frame buttons
        self.h1_wiper_button_left_arrow.clicked.connect(lambda: self.log_button_click("Left Indicator"))
        self.h1_wiper_button_right_arrow.clicked.connect(lambda: self.log_button_click("Right Indicator"))

        self.h3_wiper_button_home.clicked.connect(lambda: self.log_button_click("Home Button"))

        self.h4_wiper_button_wiper_off.clicked.connect(lambda: self.log_button_click("Wipers Off"))
        self.h4_wiper_button_three.clicked.connect(lambda: self.log_button_click("Wiper Speed 3"))
        self.h4_wiper_button_light.clicked.connect(lambda: self.log_button_click("Light Options"))
        self.h4_wiper_button_one.clicked.connect(lambda: self.log_button_click("Wiper Speed 1"))
        self.h4_wiper_button_two.clicked.connect(lambda: self.log_button_click("Wiper Speed 2"))
        self.h4_wiper_button_wiper.clicked.connect(lambda: self.log_button_click("Wiper Options"))

        self.h5_wiper_button_AC.clicked.connect(lambda: self.log_button_click("Climate Control"))
        self.h5_wiper_button_hazard.clicked.connect(lambda: self.log_button_click("Hazard"))
        self.h5_wiper_button_max.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.h5_wiper_button_fan.clicked.connect(lambda: self.log_button_click("Fan Settings"))
        self.h5_wiper_button_nav.clicked.connect(lambda: self.log_button_click("Navigation"))
        self.h5_wiper_button_audio.clicked.connect(lambda: self.log_button_click("Audio"))
        self.h5_wiper_button_phone.clicked.connect(lambda: self.log_button_click("Phone"))
        self.h5_wiper_button_settings.clicked.connect(lambda: self.log_button_click("Settings"))

        # misc. buttons
        self.button_left_arrow.clicked.connect(lambda: self.log_button_click("Left Indicator"))
        self.button_right_arrow.clicked.connect(lambda: self.log_button_click("Right Indicator"))
        self.button_hazard.clicked.connect(lambda: self.log_button_click("Hazard"))
        self.button_fan.clicked.connect(lambda: self.log_button_click("Fan Settings"))
        self.button_max.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.button_audio.clicked.connect(lambda: self.log_button_click("Audio"))
        self.button_phone.clicked.connect(lambda: self.log_button_click("Phone"))
        self.button_nav.clicked.connect(lambda: self.log_button_click("Navigation"))
        self.button_settings.clicked.connect(lambda: self.log_button_click("Settings"))

        # climate frame buttons
        self.h2_climate_button_off.clicked.connect(lambda: self.log_button_click("Climate Off"))

        self.button_home.clicked.connect(lambda: self.log_button_click("Home Button"))
        self.button_wiper.clicked.connect(lambda: self.log_button_click("Wiper Options"))
        self.button_light.clicked.connect(lambda: self.log_button_click("Light Options"))

        self.h3_climate_button_minus.clicked.connect(lambda: self.log_button_click(f"Decrease Fan Speed: {self.fan_level}"))
        self.h3_climate_button_plus.clicked.connect(lambda: self.log_button_click(f"Increase Fan Speed: {self.fan_level}"))
        self.h3_climate_button_stickman_1.clicked.connect(lambda: self.log_button_click("Vent to Face Only"))
        self.h3_climate_button_stickman_2.clicked.connect(lambda: self.log_button_click("Vent to Feet Only"))
        self.h3_climate_button_stickman_3.clicked.connect(lambda: self.log_button_click("Vent to Face and Feet"))
        self.h3_climate_button_stickman_4.clicked.connect(lambda: self.log_button_click("Vent to Feet and Windshield"))
        self.h3_climate_button_defrost.clicked.connect(lambda: self.log_button_click("Vent to Windshield Only"))

        self.h4_climate_button_airflow_1.clicked.connect(lambda: self.log_button_click("Outer Air Circulation"))
        self.h4_climate_button_airflow_2.clicked.connect(lambda: self.log_button_click("Inner Air Circulation"))
        self.h4_climate_button_max_ac.clicked.connect(lambda: self.log_button_click("Max AC"))
        # self.h4_climate_button_rear_defrost.clicked.connect(lambda: self.log_button_click("Rear Defrost"))
        self.h4_climate_button_auto.clicked.connect(lambda: self.log_button_click("Automatic Climate"))


    def log_button_click(self, button_name):
        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

        # Format elapsed time
        elapsed_time_str = f"{minutes}m {seconds}s {milliseconds}ms"

        try:
            # Log the button click with current timestamp and FrameNum
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            frame_num = self.receiver.FrameNum  # Get current frame number from Receiver
            with open(self.excel_file, 'a', newline='') as csvfile:
                toFile = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                toFile.writerow([button_name, timestamp, elapsed_time_str, frame_num])

        except Exception as e:
            print(f"Error logging button click: {e}")

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # Use QApplication to find the widget under the cursor
            widget_under_cursor = QtWidgets.QApplication.widgetAt(event.globalPos())

            # Check if the widget under the cursor is a QPushButton or QSlider
            while widget_under_cursor is not None:
                if isinstance(widget_under_cursor, (QtWidgets.QPushButton, QtWidgets.QSlider)):
                    return False  # Allow normal behavior for buttons and sliders
                widget_under_cursor = widget_under_cursor.parent()

            # If no button or slider is detected, log as "Missed Click"
            self.log_button_click("Missed Click")
            return True  # Consume the event

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self._click_logged = False  # Reset the flag

        return super(MainWindow, self).eventFilter(obj, event)

    def closeEvent(self, event):
        if self.receiver:
            self.receiver.terminate()  # Terminate the Receiver thread
        super(MainWindow, self).closeEvent(event)

    def highlight_button(self, clicked_button):

        buttons = [ self.button_left_arrow, self.button_right_arrow,
                    self.button_fan, self.button_AC, self.button_max, self.button_hazard, self.button_audio, self.button_phone, self.button_nav,
                    self.button_settings,
                    # light
                    self.h1_light_button_left_arrow, self.h1_light_button_right_arrow,
                    self.h4_light_button_beam, self.h4_light_button_beam_off, self.h4_light_button_blinker, self.h4_light_button_light_off,
                    self.h5_light_button_AC, self.h5_light_button_audio, self.h5_light_button_phone,
                    self.h5_light_button_settings, self.h5_light_button_nav, self.h5_light_button_fan, self.h5_light_button_hazard,
                    self.h5_light_button_max,
                    # wiper
                    self.h1_wiper_button_left_arrow, self.h1_wiper_button_right_arrow,
                    self.h4_wiper_button_one, self.h4_wiper_button_two, self.h4_wiper_button_three,
                    self.h4_wiper_button_wiper_off, self.h5_wiper_button_AC, self.h5_wiper_button_audio,
                    self.h5_wiper_button_phone,
                    self.h5_wiper_button_settings, self.h5_wiper_button_nav, self.h5_wiper_button_fan,
                    self.h5_wiper_button_hazard,
                    self.h5_wiper_button_max,
                    # home
                    self.h1_home_button_left_arrow, self.h1_home_button_right_arrow,
                    self.h5_home_button_AC, self.h5_home_button_audio,
                    self.h5_home_button_phone,
                    self.h5_home_button_settings, self.h5_home_button_nav, self.h5_home_button_fan,
                    self.h5_home_button_hazard,
                    self.h5_home_button_max,
                    # fan
                    self.h1_fan_button_left_arrow, self.h1_fan_button_right_arrow,
                    self.h5_fan_button_AC, self.h5_fan_button_audio,
                    self.h5_fan_button_phone,
                    self.h5_fan_button_settings, self.h5_fan_button_nav, self.h5_fan_button_fan,
                    self.h5_fan_button_hazard,
                    self.h5_fan_button_max,
                    # Climate
                    self.h2_climate_button_off,

                    self.h3_climate_button_stickman_1, self.h3_climate_button_stickman_2,
                    self.h3_climate_button_stickman_3, self.h3_climate_button_stickman_4, self.h3_climate_button_defrost,
                    self.h4_climate_button_airflow_1, self.h4_climate_button_airflow_2,
                    self.h4_climate_button_max_ac, self.h4_climate_button_auto


                    ]

        #self.button_wiper_off, self.button_one, self.button_two, self.button_three,

        bottom_buttons = [self.button_fan, self.button_AC, self.button_max, self.button_hazard, self.button_audio,
                          self.button_phone, self.button_nav, self.button_settings,
                          self.h5_light_button_AC, self.h5_light_button_audio,
                          self.h5_light_button_phone,
                          self.h5_light_button_settings, self.h5_light_button_nav, self.h5_light_button_fan,
                          self.h5_light_button_hazard,
                          self.h5_light_button_max,
                          self.h5_wiper_button_AC, self.h5_wiper_button_audio,
                          self.h5_wiper_button_phone,
                          self.h5_wiper_button_settings, self.h5_wiper_button_nav, self.h5_wiper_button_fan,
                          self.h5_wiper_button_hazard,
                          self.h5_wiper_button_max,
                          self.h5_home_button_AC, self.h5_home_button_audio,
                          self.h5_home_button_phone,
                          self.h5_home_button_settings, self.h5_home_button_nav, self.h5_home_button_fan,
                          self.h5_home_button_hazard,
                          self.h5_home_button_max,
                          self.h5_fan_button_AC, self.h5_fan_button_audio,
                          self.h5_fan_button_phone,
                          self.h5_fan_button_settings, self.h5_fan_button_nav, self.h5_fan_button_fan,
                          self.h5_fan_button_hazard,
                          self.h5_fan_button_max
                          ]

        black_button = [self.h3_climate_button_minus, self.h3_climate_button_bar_1, self.h3_climate_button_bar_2, self.h3_climate_button_bar_3, self.h3_climate_button_bar_4, self.h3_climate_button_bar_5,]

        for button in buttons:
            if button == clicked_button:
                button.setStyleSheet("background-color: #0070c0;")

            elif button in black_button:
                button.setStyleSheet("QPushButton{border:5px solid black; margin:0px; padding:0px; background-color: black; color:white;}")

            elif button in bottom_buttons:
                button.setStyleSheet("QPushButton{border:0px; margin:0px; padding:0px; background-color: black; color:white;}")
            else:
                button.setStyleSheet("QPushButton{border:0px; margin:0px; padding:0px;background-color: white; color:black;}")

    ''' SHOW/HIDE FRAMES '''
    # Showing the home frame
    def showHomeFrame(self):
        # Reset fan speed and slider value
        self.h2_slider.setValue(18)  # Reset slider to 20
        self.fan_level = 1  # Reset fan level to 1
        # Directly update the fan bar styles
        bars = [self.h3_climate_button_bar_1, self.h3_climate_button_bar_2,
                self.h3_climate_button_bar_3, self.h3_climate_button_bar_4,
                self.h3_climate_button_bar_5]

        for i, bar in enumerate(bars):
            if i == 0:  # First bar
                bar.setStyleSheet("background-color: black;")  # Filled black bar
            else:  # Remaining bars
                bar.setStyleSheet("background-color: white;")  # Empty white bar
        self.home_frame.show()
        self.light_frame.hide()
        self.wiper_frame.hide()
        self.climate_frame.hide()
        self.fan_frame.hide()
        self.video_player.show() # html
        self.home_frame.raise_()
        self.fan_background_frame.hide()
        self.update_frame.hide()

    # Showing the light frame
    def showLightFrame(self):
        self.home_frame.hide()
        self.light_frame.show()
        self.wiper_frame.hide()
        self.climate_frame.hide()
        self.fan_frame.hide()
        self.video_player.show() # html
        # self.video_player.play() # mp4
        self.light_frame.raise_()
        self.fan_background_frame.hide()
        self.update_frame.hide()

    # Showing the wiper frame
    def showWiperFrame(self):
        self.home_frame.hide()
        self.light_frame.hide()
        self.wiper_frame.show()
        self.climate_frame.hide()
        self.fan_frame.hide()
        self.video_player.show() # html
        # self.video_player.play() # mp4
        # Raise the wiper frame to ensure it's on top
        self.wiper_frame.raise_()
        self.fan_background_frame.hide()
        self.update_frame.hide()

    # Showing the fan frame
    def showFanFrame(self):
        # Hide other frames
        self.home_frame.hide()
        self.light_frame.hide()
        self.wiper_frame.hide()
        self.climate_frame.hide()

        # Show all frames in the order you want to stack them
        self.video_player.show()  # Video player at the very bottom
        # self.white_box_frame.show()  # White box as the background layer
        self.fan_background_frame.show()
        self.fan_frame.show()  # Fan frame with buttons on top

        # Set explicit stacking order
        # self.video_player.lower()  # Ensure the video player is at the bottom
        # self.white_box_frame.lower()
        self.fan_background_frame.raise_()
        self.fan_frame.raise_()  # Fan frame on top to keep buttons interactive
        self.update_frame.hide()

    # Showing the climate frame
    def showClimateFrame(self):
        # highlight AC button
        self.button_AC.setStyleSheet("background-color: #0070c0; color: white;")
        self.h5_light_button_AC.setStyleSheet("background-color: #0070c0; color: white;")
        self.h5_wiper_button_AC.setStyleSheet("background-color: #0070c0; color: white;")
        self.h5_home_button_AC.setStyleSheet("background-color: #0070c0; color: white;")

        self.fan_background_frame.hide()
        self.home_frame.hide()
        self.light_frame.hide()
        self.wiper_frame.hide()
        self.climate_frame.show()
        self.fan_frame.hide()
        self.video_player.hide()
        self.update_frame.hide()

        #hide other buttons
        bottom_buttons = [self.button_fan, self.button_max, self.button_hazard, self.button_audio,
                          self.button_phone, self.button_nav, self.button_settings]

        for button in bottom_buttons:
            button.setStyleSheet("QPushButton{border:0px; margin:0px; padding:0px; background-color: black; color:white;}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    frame = MainWindow()
    frame.show()
    app.exec_()