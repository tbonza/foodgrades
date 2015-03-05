#!/usr/bin/env python
import os
from api.app import create_app
from flask.ext.script import Manager

manager = Manager(create_app)

if __name__ == "__main__":
    manager.run()
