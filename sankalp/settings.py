try:
    from sankalp.local_settings import *
except ImportError as e:
    from sankalp.production_settings import *
