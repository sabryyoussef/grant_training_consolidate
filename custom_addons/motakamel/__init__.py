# -*- coding: utf-8 -*-

from . import models
from . import controllers

def post_init_hook(env):
    """Load demo data after module installation"""
    from . import demo_data_loader
    demo_data_loader.load_demo_data(env)

