# pythonPractice

## Install different python alongside Ubuntu system python

Install Python 3.11 via deadsnakes PPA

Add `deadsnakes PPA` to software sources
```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

Install Python 3.11 and venv support
```
sudo apt install -y python3.11 python3.11-venv python3.11-dev
```

Verify installation
```
python3.11 --version
```

## Creare virtual environment with specific python version

Using Python 3.11
```
python3.11 -m venv venv311
source venv311/bin/activate
```

## Check which `python` or `pip` you are using and their versions

```
which python
which pip

python --version
python -m pip --version
```

## Check pip for a specific Python version

```
python3.11 -m pip --version
python3.10 -m pip --version
```
