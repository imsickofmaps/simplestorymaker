"""
This file stops circular dependencies
"""

from views import *

if __name__ == '__main__':
    app.run()
