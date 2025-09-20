# Moments

A photo sharing social networking app built with Python and Flask. The example application for the book *[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)* (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

1. Install uv package manager \
Preferred approaches - \
for Windows : 

```shell
winget install --id=astral-sh.uv  -e
```

for macOS : 

```shell
brew install uv
```

Alternate approach : 

```shell
pip install uv
```

2. Navigate to your project directory <br><br>
3. Sync all dependencies from the pyproject.toml to your project. uv sync creates a virtual environment if one doesn't already exist and it creates a uv.lock file which records the exact version of all dependencies.
```shell
uv sync
```
4. Follow the steps mentioned in the readme : To initialize the app, run the flask init-app command:
```shell
uv run flask init-app
```
If you just want to try it out, generate fake data with flask lorem command then run the app:
```shell
uv run flask lorem
```
(If you see an error for any missing dependencies, you can add them in the following way and try running the command again)
```shell
uv add Faker
uv add azure-ai-vision-imageanalysis
```

Lorem will create a test account:

email: admin@helloflask.com \
password: moments

Now you can run the app:
```shell
uv run flask run
```
* Running on http://127.0.0.1:5000/

5. Create A Computer Vision Azure AI resource and set environment variables for VISION_ENDPOINT and VISION_KEY


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
