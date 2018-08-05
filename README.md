Medical Text Modeling
-------------------------------

You are faced with a problem, you have documents on your system that you want
to possibly share with others but you want to make sure you don't share any
of your medical infomation with them.  

So the question is: 

**How do you determine whether a complete document or portion of a document
contains medical information**.  

## Approaches

Like any computer problem, there is often many different ways that you could
attempt to solve the problem.  

We want to try out a few of these different approaches in order to have a better
grasp as to the pros/cons of each.  

1. Text Matching
2. 

### Naive Approach

As a programmer, a naive approach that I might have come up with would be
to use a list of words that we would categorize as medical.  We could then
iterate through each word in a document and if any of the words are in
our predefined list we could call the document a "medical" document.  

This approach has some drawback though.  While some medical words, such as
"melanoma", may not really be used outside of a medical context, other words,
such as "finger" can be used in a non-medical fashion as well as a medical one. 

    "I broke my finger last night"
    vs
    "Don't point the finger at me"



## Setting up Development

The initial setup is built to support windows (powershell), ubuntu (maybe debian) however the steps for manual
install in your custom environment is pretty simple.  

1. Windows: `bin\setup.ps1`
2. Ubuntu: `bin/setup.sh`

### Manual install steps

1. Install python >= 3.6 (with .venv module)
2. Create a python virtual environment and activate
3. Install the pip packages

        pip install -r requirements.txt

4. Enable jupyter contrib extensions

        jupyter contrib nbextension install --user

5. (optional) Enable `vim` in jupyter

        jupyter nbextension enable select_keymap/main

6. (optional) Enable other plugins for jupyter

        Start jupyter
        navigate to [localhost:8888/nbextensions](http://localhost:8888/nbextensions)

### Installing in WSL (Windows Subsystem Linux)

Since WSL is available directly on windows now, I am going to demonstrate how to install using `pipenv` and
the `ubuntu` distro.  

1. Install WSL (follow instructions from Microsoft)
2. Install the following dependencies using apt

    sudo apt install python3 python3-dev python3-venv python3-pip build-essential cmake pkg-config \
        libjpeg-dev libtiff-dev libpng-dev \
        libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
        libxvidcore-dev libx264-dev libatlas-base-dev gfortran \
        libsm6 libxext6
        
3. Install `pipenv` globally using `pip3`

    sudo pip3 install pipenv
    
3b (optional). If pipenv is not found in your path you may need to add the following to your bash prompt

    PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
    export PATH=$PATH:$PYTHON_BIN_PATH

4. Install virtualenv using `pipenv`

    pipenv install --dev
    
5. Start virtualenv using `pipenv shell`

#### Docker with windows and WSL

To get the docker environment correctly setup for WSL you will need to do the following. 

1. Enable hyper-v and containers in windows addon
2. Install Docker for windows
3. Enable the option in Docker for Windows for access from localhost without TSL
4. Add a DOCKER_HOST export to `~/.bashrc`

    export DOCKER_HOST=tcp://localhost:2375
    
5. Adjust the WSL to mount to `/` instead of `/mnt` so that the `C:\` drive is now `/c/`
    This allows for `docker run -v $PWD:/workdir` to function correctly

## Development practices


### Coding Styles

* [Python styler - Black](https://github.com/ambv/black) 


### Data References


### Setup References

* [WSL for VSCode Terminal](https://stackoverflow.com/questions/44450218/how-do-i-use-bash-on-ubuntu-on-windows-wsl-for-my-vs-code-terminal)
* [MobaXTerm - X11 for windows](https://mobaxterm.mobatek.net/)
* [WSL - Moba for Windows Linux Dev](https://nickjanetakis.com/blog/using-wsl-and-mobaxterm-to-create-a-linux-dev-environment-on-windows)
* [Setting up docker for WSL](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)
* [Mininet - Virtual Network on your laptop](http://mininet.org/)
* [WSL Startup Task for cmder](https://i1.wp.com/gingter.org/wp-content/uploads/2016/11/Bash-in-Cmder.png?ssl=1)
* [Pandoc - Convert documents between formats](https://pandoc.org/installing.html)
