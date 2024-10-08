# NoBS

## Description

NoBS is a simple, lightweight, and easy-to-use Python project for renaming Bank Statement pdf files to the format 

```YYYY.MM.DD-YYYY.MM.DD XXXX```

The 1st date is the start date, the 2nd date is the end date of the statement, and XXXX is the last 4 digits of the account number.

## Setup

### 0. Prerequisites

Download and install Python from the official website: [Python](https://www.python.org/downloads/)

### 1. Clone the repository

Choose a directory (folder) for the project and copy its path. 
Open the terminal. Change the directory to the chosen directory and clone the repo by copy and pasting the following commands:

```bash
cd path/to/directory
git clone https://github.com/cbugayer/NoBS.git
```

### 2. Install the required packages

Run the following command to install the required package `PyMuPDF` which is used for reading text from the pdf files:

```bash
pip install PyMuPDF==1.24.8
```

## Running the script

Copy the folder path containing the pdf files (or a single pdf file path).
Change the directory to the project directory and run the script by copy and pasting the following commands:

```bash
cd NoBS
python main.py path/to/pdf/myfiles
```

The script will create a new folder named `RENAMED_myfiles` in the same directory as the pdf files and will copy the pdf files with the new names to the new folder. If any file fails to be renamed, it will be copied to the new folder with the old name.
It will also create a log file named `LOGS_myfiles.txt` in the same directory as the pdf files. The log file will contain the old and new names of the pdf files. It will also show the files that could not be renamed.

## Assumptions

- There should be no European dates in the pdf files
- Maximun year is 2099 and minimum year is 1900
- 2 digit years are in the 2000s

