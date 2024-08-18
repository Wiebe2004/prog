import inspect
import pytest
import movies

def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(movies), reason=f'Skipped because {class_name} has not been defined')

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

#TEST MOVIE

def test_class_Movie_is_defined():
    assert 'Movie' in dir(movies), 'Class Movie has not been defined'

@if_class_exists('Movie')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'title', 'genres', 'sequel']
    },
    {
        'method_name': 'get_info',
        'parameter_names': ['self'],
    },
])
def test_movie_methods(kwargs):
    assert has_method(
        movies.Movie,
        **kwargs), f"Movie's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Movie')
@pytest.mark.parametrize("attr",["title","genres","sequel"])
def test_Movie_attributes(attr):
    movie = movies.Movie("t",["g"],True)
    assert hasattr(movie,attr), f"Movie's attribute {attr} is missing or incorrect."



#TEST FILMFESTIVAL

def test_class_FilmFestival_is_defined():
    assert 'FilmFestival' in dir(movies), 'Class FilmFestival has not been defined'

@if_class_exists('FilmFestival')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name']
    },
    {
        'method_name': 'add_movie',
        'parameter_names': ['self', 'movie'],
    },
    {
        'method_name': 'remove_movie',
        'parameter_names': ['self', 'title'],
    },
])
def test_FilmFestival_methods(kwargs):
    assert has_method(
        movies.FilmFestival,
        **kwargs), f"FilmFestival's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('FilmFestival')
@pytest.mark.parametrize("attr",["name","movies"])
def test_FilmFestival_attributes(attr):
    festival = movies.FilmFestival("n")
    assert hasattr(festival,attr), f"FilmFestival's attribute {attr} is missing or incorrect."
