#Installing Scikit
It's better to use a virtual environment to install these packages to avoid conflicts with already installed versions.
First install pip and virtualenv. In ubuntu use 
``$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv ``

1. cd to the project 
2. Create a virtual environment by `` virtualenv -p python3 virtual``
3. ``cd virtual/bin`` and ``source activate`` to start the virtual environment
4. install numpy using pip `` pip install numpy``
5. Install scipy using pip `` pip install scipy``
6. Install SciKit using pip `` pip install -U scikit-learn``
7. ``cd ../../`` to come back to root project directory
8. Try something eg: start python by ``python`` and ``from sklearn import datasets`` ('' If success your'e all set")


Read here [http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv] for more about virtualenv.

OR with the virtualenvprop.txt file I have created you can easily set up all.

1. Clone project / Pull
2. Install virtualenv same as above.
3. ``virtualenv -p python3 virtual``
4. ``source virtual/bin/activate`` (Now you'll see ``(virtual)$`` in left of the terminal)
5.  ``pip install -r virtualenvprop.txt``
6. Try something eg: start python by ``python`` and ``from sklearn import datasets`` ('' If success your'e all set")


**Viola you are now ready. Read the official documentation[http://scikit-learn.org/stable/documentation.html] **


