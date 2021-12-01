"""This is the package initializer module"""

from inspect import isclass, getmembers
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
import sys

from .base import Species

__module__ = sys.modules[__name__]

# Load all subclasses of the base class 'Species' found in current package
package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    # import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute) and issubclass(attribute, Species):
            globals()[attribute_name] = attribute

def get_class_from_name(class_name):
    """
    Takes a class_name and returns the class of the corresponding classname.
    Only searches through loaded classes in this module.
    """
    try:
        return next(
            m[1] for m in getmembers(__module__, isclass)
                if m[1].__module__.startswith('modules.') and m[1].__name__ == class_name
        )
    except:
        return None
