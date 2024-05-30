This API is part of an AI web app that predicts the SEO from a screenshot.

# Prerequisites

- Python 3.8+ (I used 3.11.3)
- Trained model (.h5 file)

# Installation

1. Initiate a Python environment

```sh
python -m venv .venv
```

This will create a `.venv` file within the project.

2. Activate the environment

`Windows`

```sh
.venv\Scripts\activate
```

`Unix`

```sh
source venv/bin/activate
```

A preffix `(.venv)` should appear before the path, example:

`(.venv) C:\Users\user\BetterSEODataFactory>`

3. Install packages using `pip`

```sh
pip install -r requirements.txt
```

Expect this step to take some time since TensorFlow is a bit hefty.

I don't expect it to happen, but if you encountered any problems with TensorFlow on Linux, let met know, since "pip install tensorflow" may automatically install different sub-packages for each system.

# Execution

Before executing, put the trained model .h5 file into the `model` folder and **make sure to name it** `BetterSEOModel.h5`.

With the Python environment initiated, run:

```sh
fastapi dev main.py
```

This should get the API up and running on localhost:8000.

And that's it!