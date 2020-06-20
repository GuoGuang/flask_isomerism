from config.env_config import manager
from flask_script import Server, Command
from interceptors.system_handler import *
from jobs.launcher import runJob
from eureka import setEureka


"""
 register the command and start the program with the command;
 
 Run with "python manager.py runjob -m movie" start the crawler
 Run with "python manager.py runserver" start the web
 
"""
manager.add_command("runserver", Server(host="0.0.0.0",port= 9004, use_debugger=True, use_reloader=True))
manager.add_command("runjob", runJob)

def main():
    manager.run()


if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
