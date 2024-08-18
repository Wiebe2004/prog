import inspect
import pytest
import flags

def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(flags), reason=f'Skipped because {class_name} has not been defined')

def has_property(cls, *, property_name):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    return True

def has_method(cls, *, method_name, parameter_names=None):
    if parameter_names is None:
        parameter_names = []
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True

#TEST FLAG

def test_class_Flag_is_defined():
    assert 'Flag' in dir(flags), 'Class Flag has not been defined'

@if_class_exists('Flag')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'country', 'colors', 'horizontal']
    },
    {
        'method_name': 'get_info',
        'parameter_names': ['self'],
    },
])
def test_Flag_methods(kwargs):
    assert has_method(
        flags.Flag,
        **kwargs), f"Flag's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Flag')
@pytest.mark.parametrize("attr",["country","colors","horizontal"])
def test_Flag_attributes(attr):
    flag = flags.Flag("x",["x"],True)
    assert hasattr(flag,attr), f"Flag's attribute {attr} is missing or incorrect."


#TEST PARADE

def test_class_Parade_is_defined():
    assert 'Parade' in dir(flags), 'Class Parade has not been defined'

@if_class_exists('Parade')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name']
    },
    {
        'method_name': 'add_flag',
        'parameter_names': ['self', 'flag'],
    },
    {
        'method_name': 'remove_flag',
        'parameter_names': ['self', 'country'],
    },
])
def test_Parade_methods(kwargs):
    assert has_method(
        flags.Parade,
        **kwargs), f"Parade's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Flag')
@pytest.mark.parametrize("attr",["name","flags"])
def test_Parade_attributes(attr):
    parade = flags.Parade("x")
    assert hasattr(parade,attr), f"Parade's attribute {attr} is missing or incorrect."
