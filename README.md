# OCR using tesseract
This program extracts text from camera.

1) Steps:

- Install tesseract-ocr:
  - >apt-get install tesseract-ocr

- Install pip and virtual env
  ->python3 -m pip install --user --upgrade pip
  ->python3 -m pip install --user virtualenv

- create a virtual env and install packages needed to run the program:
  - >python3 -m venv ocr
  - >source ocr/bin/activate
  - >pip install -r requirements.txt


2) How to run:

  - >python3 main_task.py
  
