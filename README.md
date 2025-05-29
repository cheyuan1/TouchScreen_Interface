# TouchScreen_Interface
Interface python files for the touchscreen project.

👋 Welcome
This repository contains the codebase for our touchscreen-based driver interface project. It is structured to support multiple driving task conditions, and logs all participant interactions (e.g., temperature slider, fan toggles, light control) during simulation.


📁 Folder Overview
Each folder corresponds to a different driving condition task. The interaction logic and logging commands for each task are contained within a runme.py file. Here's a breakdown of the main folders:

✅ High_Drive_Condition/

RUNME I5_light_high.py: The main script that launches the interface and logs user inputs.
version1_light_high.py: Defines the overall GUI layout and integrates control elements like temperature, fan, light, etc.
📝 This is the best place to start if you're looking to understand how input logging works in our codebase.

✅ Low_Drive_Condition/, Drive_5_1/, Drive_5_2/

Similar structure to High_Drive_Condition.
Each folder contains a customized version of RUNME.py, reflecting the specific experimental condition.
Logging functions are consistently placed inside these RUNME.py files.
