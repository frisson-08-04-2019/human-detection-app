@echo off
PATH = %PATH%;%USERPROFILE%\Miniconda3\Scripts
conda create -n human-detection-app pip python=3.6 -y
call activate human-detection-app
git submodule init
git submodule update
pip install -r requirements.txt
pip install -r human_detection_engine\requirements.txt
