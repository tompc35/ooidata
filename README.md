### ooidata

Python module for working with Ocean Observatories Initiative data.

Under development.

#### Installation

To install on your local machine there are several options. Option 1 is the simplest and best for working on Google Colab. Option 2 is best if you want to edit the package and contribute to the repository.

##### 1. Use pip to install directly from git

```
!pip install git+https://github.com/tompc35/ooidata.git
```

##### 2. Fork, clone and install using pip:

* First fork the repository on Github. This will create a new repository on Github under your account at https://github.com/username/ooidata.git (your Github username will be in the place of `username`).

* Next, clone the forked repository and use pip to install. The `-e` option installs in developer mode so that you do not reinstall every time you want to make a change to the package (although you do still have to restart the kernel).
```
git clone https://github.com/username/ooidata.git
pip install -e .
```
