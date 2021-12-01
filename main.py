"""This is the main module of the project."""

from modules import get_class_from_name

print(get_class_from_name('Dog')().__str__())
print(get_class_from_name('Snake')().__str__())
print(get_class_from_name('Undef')().__str__())
