# This file exists so that Python will treat the `lib` directory
# as a module. You can also export functions from here and they
# will appear at the top level of a module.
#
# For example, because following line imports the get_number function
# from the other file, and this file automatically re-exports it
# for python files that import it, you can use:
#
# from lib import get_number
#
# ...instead of:
#
# from lib.get_number import get_number
#
from .get_number import get_number
