# Session 1 Notes 
### Round of introduction
- introduce me: background, how I learned programming 
- everyone quickly talks about his or her background
- show the google form results
- teaching style, question and mistake policy

### Goals 
1) have python and anaconda installed 
2) navigate in the terminal, install packages, know different editors, run scripts 
3) work with jupyter notebook / lab, run simple arithmetic operations

### Command line lecture 
- open the terminal, explain the purpose, show some commands, 
- google for command line tutorial
- get a codeacademy account: codeacademy.com 

### Command line practice with codeacademy
https://www.codecademy.com/learn/learn-the-command-line
#### Navigation
open terminal, start with 
	- ls, list files and dirs
	- pwd, print working directory
	- cd, change dir
	- touch file.t, create a file
#### Manipulation 
- ls -alt, cp, mv, rm, rm -r, wildcards 

#### Redirection and Environment tutorials are homework

#### Exercise 
- create a directory for the course 
- git clone the repository of the course 

### Installing anaconda, intro to python
- everyone download and install anaconda if not done already 
- point to conda cheat sheet 

- in the meantime: intro to python
	- interpreted, high-level, general purpose
	- difference to matlab: free, open source, 
		- python is a programming language, Matlab a commercial numerical computing environment 
	- difference to R: python is general purpose with readable syntax, R is built by statisticians 
		- lots of data science packags available in R, fantastic tools for generating figures, tables, etc. 
		- python is catching up 
		- Most of the data science job can be done with five Python libraries: Numpy, Pandas, Scipy, Scikit-learn and Seaborn. 
		
### Python 
- use python in the terminal for simple arithmetics: 
	- plus, minus, slash, asterisk, percent, less-than, greater-than, less-than equal, greater-than equal

#### Exercise 
- start python in the terminal, exit again, start again
- import time package 
- get current time in sec, time.time()
- find out w.r.t what data this time is counted. 

### IPython
- tab completion, syntax high lighting, more help and documentation, interactive
- open ipython and show how it works: import math, calculate cos(pi) demonstrating tab completion and help

#### Exercise 
- open ipython, import time, 
- checkout the functions the package provide using the tab completion 
- look for time.strftime( and get help on this function

### Python program
- create a file with .py ending, print hello world 
- open the vi editor, or atom, or any text editor

#### Exercise 
	- create a file with .py ending, read in user data
	https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
	- note, that you can not add together a string and an integer. 
	- but you can tell python to interprete strings as integers, e.g., int('12') will result in a integer with value 12. 

### Installing other packages 
- pip/conda install a non standard package, e.g., jupyterlab, numpy, scipy, matplotlib, pandas, seaborn
- explain pip 

### Jupyter notebook
- let them install jupyter if not included in anaconda 
- open a notebook and show them around, explain everything

### Jupyter lab 
- bring everything of the above together into: jupyter lab
- start jupyter lab, they should see the directory and play around with the IPython console, terminal, jupyter notebook. 
- check out the course repository

## Goals 
1) navigate in the terminal, install packages, know different editors, run scripts 
2) have python and anaconda installed
3) work with jupyter notebook / lab, run simple arithmetic operations

## Tutorial Links
- https://www.codecademy.com/learn/learn-the-command-line
- https://ipython.readthedocs.io/en/stable/interactive/index.html
- https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

