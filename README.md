# Introduction

Using https://streamlit.io/ python package to build a simple web based calculator, not its intended purpose but works.
Streamlit package creates a web based user interface from a simple Python script without all the callbacks as experienced with Plotly Dash.

https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace

# Installation

## Clone git repo to folder

```console
git clone https://github.com/scottmdavies/calculator-example
cd calculator-example
```

## Setup virtual environment (separates python packages from main installation)

### On Windows

Create a virtual environment so packages are local to this folder

```console
python -m venv venv
```

Startup virtual environment and load local packages

```console
.\venv\Scripts\activate
```

Install packages from requirements.txt file

``` console
python -m pip install -r requirements.txt
```

## Run App

```console
streamlit run app.py
```
