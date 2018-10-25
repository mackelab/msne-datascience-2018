# Fundamentals Data Science Overview

# Block 1

## Intro talk 
goal of the course, spirit, format, why python shortly, their backgrounds,
  projects, usefulness, oral exam. they are welcome to take all the time of the 
  course. but dont have to. we are offering, they can make use of it, if they want. 
  it is about learning, not about optimizing the grade. 

## General points 
- we will try to set up a small documentation using sphinx, providing links to the slides, material etc. 
- minimize the amount of work for setting up a good course. Use other materials a lot 
- for designing slides consider using https://github.com/damianavila/RISE
- the **content** parts of the sessions should not take longer than 20min. After 20min there should be a break or a 
hands on session, pair programming. 
- have many small breaks, e.g., during programming use pomodoro technique and switch every 25min.
- for presentations, add little quizes with a good tool.
- we should be present in the course for around 45 hours, i.e., around 11h per block. For example, 
    - Thu and Fri 6h and Saturday off
    - Thu and Fri 4h and Saturday 3h  
- the students can or should work on their own, we should therefore give homeworks.
- the main goal is that the students learn a lot and they are happy with the course 
    - we should communicate a schedule to them in the beginning which covers 45h hours
    - if we end up doing less hours or they dont show up, thats fine as long as they are happy with it 
    - we are offering the time for them to learn and they can use it if they want to
- there will be an exam in the end. It will be fair and fairly easy. The whole course should not be about a grade, 
it should be about learning to program. All the students that show up, engage in learning will pass 
- the exam will be a short oral exam done by Jakob, with short live coding exercises and some questions.
- ask for feedback after every day
  - pace
  - content
  - style, clarity
- we give an overview in the beginning and summarize what they learned in the end of the day.
- Piazza or Slack for discussion?


## Session 0: Introduction 
### Goals  
1. overview of course content, format, organisation stuff 
2. justification for using python
3. know who else is attending the course
### Content 
- intro by Jakob
- overall goal of the course 
- why python? 
- course structure, lectures, projects, exam, style
- round of introduction
  
## Session 1: Getting started
### Goals 
1) have python and anaconda installed 
2) navigate in the terminal, install packages, know different editors, run scripts 
3) work with jupyter notebook / lab, run simple arithmetic operations 

### Style
We do this session with our laptop on the beamer, doing stuff in the terminal in real time. Switch between notebook and 
slide presentation using RISE.  

Additionally we could use a whiteboard or flip chart with the essential commands: ls, pwd, mkdir etc. 

### Content  
- install python (using Miniconda / Anaconda)
- intro to terminal/cmd commands 
    - open the terminal
    - navigate through directories, create, move delete
    - create files
- intro to python
  - use python in the terminal for simple arithmetics  
  - move to IPython, do arithmetics and define variables 
  - import math or time package and do more stuff 
  - pip/conda install a non standard package, e.g., 
  - create a file with .py extension and open it in a text editor (implement "Hello World!")
  - run the script in terminal 
- jupyter notebook
  - let them install jupyter
  - open a notebook and show them around, explain everything
  - do a more detailed tutorial, e.g., ?? those at jupyter.org are not useful
- bring everything of the above together into: jupyter lab

### Hands on 
- use python in the terminal 
- install packages using pip or conda 
- hello world 
- install jupyter and do simple tutorial in jupyter lab

## Session 2: Basics of python
### Goals 
1) python syntax and types: make sure they know when to use what: lists, arrays, dictionaries
2) functions, loops, if-else statements, list comprehension 
3) start coding

### Style 
For this session and session 2 we mostly rely on other resources, e.g., the nick del grosso course and 
exercises in codeacademy.org, codewars.com and datacamp.com. For the lecture we could take available notebooks and 
change them a bit (given credit to the author of course). 

### Content  
- python basics, syntax, operations, types etc: 
    - https://github.com/nickdelgrosso/SciPyCourse2016/blob/master/Python%20Course%20Lecture%201.ipynb
    - https://github.com/nickdelgrosso/SciPyCourse2016/blob/master/Python%20Course%20Lecture%202.ipynb
- at the end they should know: booleans, lists, dics, tuples, loops, conditional statements etc.

### Hands on 
- https://www.datacamp.com/courses/intro-to-python-for-data-science
- https://www.codecademy.com/learn/learn-python for complete beginners
- http://www.codewars.com/kata/pillars/train/python for practice 
- http://www.codewars.com/kata/sum-of-positive/train/python

## Session 3: Analysis and Plotting, Numpy and Matplotlib
### Goals 
1. concept/ide of numpy
2. load data, analyse data with numpy 
3. plotting data with matplotlib. anatomy of the figure: axes, labels etc. requirements for a scientific figure

### Content   
- in depth numpy lecture
    - https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.00-Introduction-to-NumPy.ipynb
- hands on 
    - https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy?ex=2
    - https://www.datacamp.com/courses/importing-data-in-python-part-1
- in depth matplotlib lecture 
    - https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb
- hands on 
    - https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=2
- more condensed numpy and matplotlib lecture: 
    - https://github.com/nickdelgrosso/SciPyCourse2016/blob/master/Python%20Course%20Lecture%203.ipynb
- provide an exercise with loading data, using numpy for analysis and plt for plotting
    - ...   

### Homework:
- homeworks by nickdelgrosso: 
    - https://github.com/nickdelgrosso/SciPyCourse2016/blob/master/Homework%201%20Jupyter%20Notebook%20and%20Builtin%20Type%20Methods.ipynb 
- katas, python challenge, links to tutorials
    - codewars.com katas 
    - datacamp.com exercises 

# Block 2

## Session 1, pandas

### Goals 
- get familiar with pandas, basic syntax, data frames
- the concept of pandas: relational database  
- loading data, plotting statistics 
- combining data frames, cover most of the pandas cheatsheet 

### Content
- Loading data
- Indexing and selecting data
- Working with missing data
- Group By: split-apply-combine
- Merge, join, and concatenate
- https://github.com/jahma/Assignments/tree/master/A2
- https://github.com/jahma/Assignments/tree/master/A3

### Hands on, links, homework 
- http://pandas.pydata.org/pandas-docs/stable/tutorials.html
- http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

## Session 2, seaborn
might be an overlap with the session on matplotlib, but should help to get a deeper understand of how to design 
figures in python. 
 
### Goals 
- visualize dataframes with seaborn  
- know the difference between searborn and matplotlib
 
### Content 
- Seaborn vs Matplotlib
- all important types of plots 
- Figure cusotmization
- https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
- https://github.com/jahma/Assignments/tree/master/A2
- https://seaborn.pydata.org/introduction.html#introduction

### Hands on, links, homework 
- https://seaborn.pydata.org/examples/index.html#example-gallery    

## Session 3, scikit learn
### Goals 
- know the broad areas of machine learning, when to use unsupervised, supervised learning  
- know how to train an algorithm from data in general: overfitting, underfitting, hyperparameters, grid search, 
cross validation 
- all these concepts should be introduced via sklearn, they know how to train any model in sklearn including the 
parameter search 
- it is not about leaning machine learning algorithms but about learning how to train them using sklearn. 

### Content 
- Supervised Learning: Classification, Regression models 
- Unsupervised learrning: projection methods, clustering 
- cross validation, over fitting, under fitting, bias variance trade off 
- pipelines in sklearn 

### Hands on, links, homework 
- http://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting
- http://scikit-learn.org/stable/unsupervised_learning.html
- http://scikit-learn.org/stable/supervised_learning.html
- http://scikit-learn.org/stable/modules/cross_validation.html
- http://scikit-learn.org/stable/modules/compose.html
- http://scikit-learn.org/stable/user_guide.html

## Hands on
- simple classification with perceptron: code xor problem
- http://scikit-learn.org/stable/tutorial/index.html

## Homework
- coding exercise from sklearn, kaggle, MI or MHBF
    - apple and oranges perceptron exercise from MI 1
    - more advanced: MI 1 SVM exercise
- maybe this covers it all:
    - http://scikit-learn.org/stable/tutorial/statistical_inference/index.html#stat-learn-tut-index
- or kaggle:
    - https://www.kaggle.com/c/digit-recognizer

# Block 3 and 4, Projects
In blocks 3 and 4 they should mainly work on mini programming projects: 
- we come up with a number, say 5, projects they can work on alone or in pairs 
- these projects should have a clear description and should be scalable, e.g, 
    - classify MNIST, classify MNIST with 4 different classifiers and pick the best, 
    adverserial examples on MNIST 
- they can propose own projects  
- we have short talks in the beginning of project days to make sure they all come in in the beginning
- ask at the LRZ course how to get students use online computing resources
- they have to use git for their project 
    - private and share version of the repo, or
    - separate repo in cne for the projects for them to work on: create forks and do pull requests etc.

## Session 1: 
- Tutorial: git and GitHub
- 

## Session 2: 
- Tutorial: virtual environments
-

## Session 3: 
- Tutorial: Debugging and code profiling
-

## Session 4: 
- Tutorial: editors: sublime, atom, pycharm

## Session 6
- Tutorial: Online computing resources
    - LRZ 
    - https://www.crestle.com/
    - https://www.paperspace.com/
    - https://aws.amazon.com/de/

## Session 5: 
- Tutorial: Pytorch 
-
 
## mini projects ideas
- https://www.kaggle.com/c/nyc-taxi-trip-duration
- https://www.kaggle.com/c/leaf-classification  
- Machine Intelligence 1, 2 lecture assignments TU Berlin 
- MHBF course assignemnts Henning Sprekeler Berlin 
- MNIST classification 
- Andrew Ng Coursera Course assignments
