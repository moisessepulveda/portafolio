from .base import *

DEBUG = False
SECRET_KEY = 'BB68112EBA479FC9AB933ECFC676CFE40469EAA1'


try:
    from .local import *
except ImportError:
    pass
