# CapGlue
CapGlue is a small program for analysing media stream.

## Environment Setup
We use virtualenv manage our development environment

* python version: 2.7.*

```
# Ubuntu
sudo apt-get install python-virtualenv
git clone repo/url/CapGlue.git
cd CapGlue
virtualenv env
cd env
source evn/bin/activate
pip install --upgrade pip
pip freeze -r dependencies.txt
```

## Dependencies
* pypcapfile==0.11.1
