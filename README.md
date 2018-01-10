# win-md-5
## Responsive GUI desktop App
* Python
* Eel
* Pyinstaller
* Work with Google Chrome (!!! must be installed)
* Bootstrap 4 (https://getbootstrap.com/)


## How to Build

link: https://github.com/ChrisKnott/Eel#building-a-distributable-binary

### Building a distributable binary

If you want to package your app into a program that can be run on a computer without a Python interpreter installed, you should use **pyinstaller**.

1. Install pyinstaller `pip install pyinstaller`
2. In your app's folder, run `python -m eel [your_main_script] [your_web_folder]` (for example, you might run `python -m eel hello.py web`)
3. This will create a new folder `dist/`
4. Check the contents of this folder for extra modules that pyinstaller is incorrectly including
5. Exclude these using the flag `--exclude module_name`. For example, you might run `python -m eel file_access.py web --exclude win32com --exclude numpy --exclude cryptography`
7. When you are happy that your app is working correctly, add `--onefile --noconsole` flags to build a single executable file
