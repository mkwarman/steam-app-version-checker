# Steam App Version Checker

## Basic Information

I built this simple script to check for Valheim server updates and notify me if one is found.
To use it, you just need to copy `settings_example.py` to a new file named `settings.py` and
edit the fields within to use your tokens.

You should also be able to adapt the script to monitor a different app by changing the APP_ID
in your `settings.py`, but I have not tested this personally.

## Installation / Running

It is recommended that you create a virtual environment to run this program.
Once you have actived your virtual environment (or chosen not to make one), execute `python version_checker.py` to run the program

Of course, running the program manually is of little use. Instead, use a tool like Cron to run the program automatically.
