# minecraft-server-eu-bot

## Description
This is a votebot for minecraft-server.eu
With this script you can easily vote for minecraft
servers without doing something

## Presettings

- Firefox
- geckodriver
- Python 3.6+
- pip 3.6
- Selenium ```` pip install selenium ````
- YAML ```` pip install pyyaml ````


## Use
Enter your Minecraft Name and your Vote Website in ````config.yaml````

## Installation

### Windows
- Download the git repo and extract it.
- Download the webdriver latest for Firefox https://github.com/mozilla/geckodriver/releases/.
  Extract the Downloaded File. Put the downloaded ````.exe```` file in the extracted git repo folder 
- Install Python at https://www.python.org/
- Download the latest version pip at https://github.com/pypa/get-pip/releases. 
  Download the zip package. 
  Unpack the package
  double click the extracted ````get-pip.py```` File or open the cmd, go to Downloads and type ````python get-pip.py````
- Install the requred Packages: ````pip install selenium pyyaml````
- Choose Settings in ````config.yaml```` file
- After installation start the script with ````python votebot_windows.py````

### Linux
- Download the git repo and extract it
- Install Python
- Download the latest version pip at https://github.com/pypa/get-pip/releases. 
  Download the zip package. 
  Unpack the package
  double click the extracted ````get-pip.py```` File or open the cmd, go to Downloads and type ````python get-pip.py````
- Install the requred Packages: ````pip install selenium pyyaml get-geckodriver````
- Execute ````get-geckodriver````
- Choose Settings in ````config.yaml```` file
- After installation start the script with ````python votebot_linux.py````


# To-Do
- Self extracting setup for windows
- package install ````install.sh```` for Linux
- Multiple User Vote
- autostart ready ````start.bat```` for Windows
