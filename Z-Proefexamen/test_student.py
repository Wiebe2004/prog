import inspect
import pytest
import student

def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(student), reason=f'Skipped because {class_name} has not been defined')

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

@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'csom',
        'parameter_names' : ['n'],
    }
])
def test_csom(kwargs):
    assert has_method(
        student,
        **kwargs) , f"Method {kwargs['method_name']} is missing or incorrect."
    
@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'isPalindroom',
        'parameter_names' : ['t'],
    }
])
def test_isPalindroom(kwargs):
    assert has_method(
        student,
        **kwargs) , f"Method {kwargs['method_name']} is missing or incorrect."

def test_class_Attractie_is_defined():
    assert 'Attractie' in dir(student), 'Class Attractie has not been defined'

@if_class_exists('Attractie')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'naam', 'grootte']
    },
    {
        'method_name': 'bezoek',
        'parameter_names': ['self', 'grootte'],
    },
])
def test_attractie_methods(kwargs):
    assert has_method(
        student.Attractie,
        **kwargs), f"Attractie's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Attractie')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'naam',
    },
    {
        "property_name": 'grootte',
    },
])
def test_attractie_properties(kwargs):
    assert has_property(student.Attractie, **kwargs), f"Attractie's property {kwargs['property_name']} is missing or incorrect"

def test_class_Pretpark_is_defined():
    assert 'Pretpark' in dir(student), 'Class Pretpark has not been defined'

@if_class_exists('Pretpark')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'naam']
    },
    {
        'method_name': 'voegAttractieToe',
        'parameter_names': ['self', 'attractie'],
    },
    {
        'method_name': 'printOverzicht',
        'parameter_names': ['self'],
    },
])
def test_pretpark_methods(kwargs):
    assert has_method(
        student.Pretpark,
        **kwargs), f"Pretpark's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Pretpark')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'naam',
    },
])
def test_pretpark_properties(kwargs):
    assert has_property(student.Pretpark, **kwargs), f"Pretpark's property {kwargs['property_name']} is missing or incorrect"

@if_class_exists('Pretpark')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': 'veiligheidsupdate',
        'parameter_names': ['self','bestand']
    },
])
def test_pretpark_uitbreiding(kwargs):
    assert has_method(
        student.Pretpark,
        **kwargs), f"Pretpark's method {kwargs['method_name']} is missing or incorrect."