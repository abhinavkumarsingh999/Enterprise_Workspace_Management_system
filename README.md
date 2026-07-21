# Overview
A project <b>Enterprise Workspace Scaffolding<\b> used in real companies focusing not building a machine learning model, but on creating a well-organized development workspace with proper configuration, logging, testing, and building management.

# Enterprise Workspace Scaffolding
A complete skeleton(foundation) of a software project before actual development begins.
It is a proper project raw structure before building the project (machine learning)

# Importance
1. Companies have large numbers of python and other files which are messy to handle, Enterprice Workspace Scaffolding makes the structure understandable and gives a proper filemap.

2. Companies have multiple developers by which they can work on different modules with conflicts.

3. Many sensitive data containing files are placed seperate from normally accessing files defined on scaffolding.

# Structure of the Enterprice Workspace Scaffolding

Enterprice Workspace Scaffolding
    |_.pytest_cache
    |   |_v
    |   | |_cache
    |   |     |_lastfailed
    |   |     |_nodeids
    |   |     
    |   |_.gitignore
    |   |_CACHEDIR.TAG
    |   |_README.md
    |
    |_.venv
    |   |_Scripts
    |   |   |_activate
    |   |   |_activate.bat
    |   |   |_activate.ps1
    |   |   |_deactivate.bat
    |   |   |_pip.exe
    |   |   |_pip3.12.exe
    |   |   |_pip3.exe
    |   |   |_python.exe
    |   |   |_pythonw.exe
    |   |
    |   |_Include
    |   |
    |   |_Lib
    |   |   |_site-packages
    |   |       |_pip-23.2.1.dist-info
    |   |       |   |_INSTALLER
    |   |       |   |_RECORD
    |   |       |   |_REQUESTED
    |   |       |   |_AUTHORS.txt
    |   |       |   |_entry_points.txt
    |   |       |   |_METADATA
    |   |       |   |_top_level.txt
    |   |       |   |_WHEEL
    |   |       |
    |   |       |_pip
    |   |
    |   |_pyvenv.cfg
    |
    |_logs
    |   |_disgnostics.txt
    |   |_test.txt
    |
    |_src
    |   |_core
    |   |   |_logger.py
    |   |   
    |   |
    |   |_utils
    |   |   
    |   |_services
    |   |
    |   |_ __pycache__ 
    |           |_ __init__.cpython-312.pyc
    |   
    |_tests
    |   |___pycache__
    |   |       |_test_logger.cpython-312-pytest-9.1.1.pyc
    |   |
    |   |_test_logger.py
    |
    |_docs
    |   
    |_scripts
    |   |_diagnostics.py
    |
    |_vscode
    |   |_settings.json
    |
    |_.dist
    |   
    |_setup.py
    |
    |_README.md
    |
    |_requirements.txt
