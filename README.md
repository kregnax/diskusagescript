# Disk Usage Report

This program takes a mount point as an argument and returns both a JSON print of files with their size in bytes as well as
a .json file.

## Requirements

Requires Python 2.7.10 or greater

## Installation

No installation required

## Usage

Call the script from the command line, passing in a mount point as an argument, e.g.:

~~~
getdiskusage.py C:\Data\UserFiles
~~~

JSON will output in the cmd window as well as to a file named data.json in the same directory the script is located.
