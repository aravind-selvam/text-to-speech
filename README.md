# Text to Speech 

# Text to speech using Python and Flask
Text to Speech is a web application that uses Google Text to Speech gTTS (Google Text-to-Speech), a Python library and CLI tool 
to interface with Google Translate’s text-to-speech API. Writes spoken mp3 data to a file, a file-like object (bytestring) 
for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing.

## How to run?
### STEPS:

Clone the repository

```
https://github.com/aravind9722/text-to-speech.git
```
### STEP 01- Create a conda environment after opening the repository

```
conda create -p venv python=3.9.0 -y
```

```
conda activate venv
```

### STEP 02- install the requirements
```
pip install -r requirements.txt
```
### STEP 03- Change your input you need in Config.yaml interval_config

### STEP 04- run app.py
```
python app.py
```
- Logs are stored in pylogs folder
## Demo
![app_demo](https://user-images.githubusercontent.com/97881558/188140151-f9c69bdc-324e-4496-9880-2d3da73a4c53.png)

## Built With

1. Flask
2. gTTS
3. Python (Python 3.9.0)
3. html


## Authors
iNeuron Private limited
## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/aravind9722/text-to-speech/blob/main/LICENSE) file for details
