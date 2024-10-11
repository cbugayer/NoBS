# NoBS

## Description

NoBS is a simple, lightweight, and easy-to-use Python project for renaming Bank Statement pdf files to the format 

```YYYY.MM.DD-YYYY.MM.DD XXXX```

The 1st date is the start date, the 2nd date is the end date of the statement, and XXXX is the last 4 digits of the account number.

## Setup

### 0. Prerequisites

Download and install Python from the official website: [Here's the link](https://www.python.org/downloads/)
- Visit the website and download the latest version of the installer for your operating system.
- Run the installer (check the box "Add Python to PATH" if you see that).
- Open the terminal and run the following command to check if Python is installed correctly:

```bash
python3 --version
```

You should see the version of Python you installed.
If you don't, try running `python --version` instead. 
Otherwise you may need to add Python to the PATH manually or restart your computer.


### 1. Clone the repository

Choose a directory (folder) for the project and copy its path. 
- Right-click and hold the Option key to copy the path on macOS.

Open the terminal. 
Change the directory to the chosen directory and clone the repo by copy and pasting the following commands:

```bash
cd path/to/directory
git clone https://github.com/cbugayer/NoBS.git
```

When you paste into the terminal, make sure there isn't extra "00~...01~". 

At this point, if you didn't have git installed you may be prompted to install it. Click through and follow those instructions. Otherwise, for macOS, you can install git by running the following command:

```bash
xcode-select --install
```
Then run the `git clone` command again.

### 2. Install the required packages

Run the following commands enter the project directory and to install the required package `PyMuPDF` which is used for reading text from the pdf files:

```bash
cd NoBS
pip3 install PyMuPDF
```
If `python --version` worked earlier, use `pip` instead of `pip3`.

## Running the script

Copy the folder path containing the pdf files (or a single pdf file path).
Change the directory to the project directory and run the script by copy and pasting the following commands:

```bash
python3 main.py path/to/pdf/myfiles
```
Similar to `pip`, use `python` if necessary.

The script will create a new folder named `RENAMED_myfiles` in the same directory as the pdf files and will copy the pdf files with the new names to the new folder. If any file fails to be renamed, it will be copied to the new folder with the old name.
It will also create a log file named `LOGS_myfiles.txt` in the same directory as the pdf files. The log file will contain the old and new names of the pdf files. It will also show the files that could not be renamed.

## Detailed Logs

If you add the word `log` after the command like so:
```bash
python3 main.py path/to/pdf/myfiles log
```
the script will create a more detailed log file still named `LOGS_myfiles.txt`. It will show the files that could not be renamed and the reason why they could not be renamed, as well as the text extracted from the pdf files.

**REMEMBER TO DELETE THIS LOG FILE AS IT CONTAINS ALL THE SENSITIVE INFORMATION FROM THE FAILED PDF FILES.**

## Assumptions

- There should be no European dates in the pdf files
- Maximun year is 2099 and minimum year is 1900
- 2 digit years are in the 2000s

## Discussion 

Please feel free to ask for me to add compatibility with other bank statements in the discussion tab. All other discussion is also welcome.

