#Installing Scikit
It's better to use a virtual environment to install these packages to avoid conflicts with already installed versions.
First install pip and virtualenv. In ubuntu use 
``$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv ``

1. cd to the project 
2. Create a virtual environment by `` virtualenv -p python3 CMARP``
3. install numpy using pip `` pip install numpy``
4. Install scipy using pip `` pip install scipy``
5. Install SciKit using pip `` pip install -U scikit-learn``


**Viola you are now ready. Read the official documentation[http://scikit-learn.org/stable/documentation.html] **


