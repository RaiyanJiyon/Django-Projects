# Installing Python on Mac

To install Python on a Mac, follow these steps:

## Step 1: Check Pre-installed Python

macOS comes with a pre-installed version of Python 2.x. To check the version, open Terminal and type:

```bash
python --version
```

However, it's recommended to install Python 3.x for development purposes.

## Step 2: Install Homebrew
Homebrew is a package manager for macOS that simplifies the installation of software. If you don't have Homebrew installed, follow these steps:

1. Open Terminal.
2. Install Homebrew by pasting the following command and pressing Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Follow the on-screen instructions to complete the installation.

## Step 3: Install Python using Homebrew
Once Homebrew is installed, you can use it to install Python:

1. In Terminal, type the following command and press Enter:

```bash
brew install python
```

This will install the latest version of Python 3.

## Step 4: Verify the Installation
To verify that Python is installed correctly, type the following commands in Terminal:

```bash
python3 --version
```

You should see the installed version of Python 3 printed on the screen.

## Step 5: Install pip
pip is the package installer for Python and should be included with the Homebrew installation. To verify, type:

```bash
pip3 --version
```

If pip is installed, you will see the version number. If not, you can install it by running:

```bash
python3 -m ensurepip
```

## Step 6: Install a Code Editor (Optional)
While you can write Python code in any text editor, using an Integrated Development Environment (IDE) or a code editor like Visual Studio Code can enhance the development experience.

1. Download Visual Studio Code from the official website.
2. Install and launch Visual Studio Code.
3. Install the Python extension for Visual Studio Code from the Extensions marketplace to enhance Python development.

### Conclusion
You have now successfully installed Python on your Mac. You can start writing Python code and using various libraries to develop your applications.