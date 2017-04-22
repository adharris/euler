
import click
import requests
import bs4
import html2text

from os import path, makedirs
from jinja2 import Template

from pathlib import Path

@click.command()
@click.argument('problem', type=int)
@click.option('--option', '-o', type=(str, int), multiple=True)
def generate(problem, option):
    create_directory(problem)
    create_python_file(problem, option)
    update_minor_init(problem)
    update_major_init(get_major_path(problem))
    update_major_init(get_problems_path())

def create_directory(problem):
    p = get_minor_path(problem)
    try:
        p.mkdir(parents=True)
    except FileExistsError:
        pass

def create_python_file(problem, options):
    path = get_file_path(problem)
    rendered = render_problem(problem, options)
    if path.exists():
        click.secho('Python file exists, skipping', fg='red')
        return
    with get_file_path(problem).open('w') as f:
        f.write(rendered)


def update_minor_init(problem):
    path = get_minor_path(problem)
    modules = path.glob('problem_*.py')
    methods = [m.stem for m in modules]
    template = Template(minor_init)
    rendered = template.render(methods=methods)
    init_path = path / '__init__.py'
    with init_path.open('w') as f:
        f.write(rendered)


def update_major_init(path):
    children = path.glob('*/__init__.py')
    modules = [c.parent.name for c in children]
    template = Template(major_init)
    rendered = template.render(modules=modules)
    init_path = path / '__init__.py'
    with init_path.open('w') as f:
        f.write(rendered)


def render_problem(problem, options):
    name, content = get_problem_info(problem)   
    template = Template(command_template)
    content = '\n    '.join(r for r in content.splitlines())
    rendered = template.render(
        problem=problem,
        options=options,
        method=create_method_name(problem),
        name=name, 
        content=content)
    return rendered


def get_problems_path():
    return Path('.', 'problems')


def get_major_path(problem):
    return get_problems_path() / get_major_module(problem)


def get_minor_path(problem):
    return get_major_path(problem) / get_minor_module(problem)


def get_file_path(problem):
    return get_minor_path(problem) / get_file_name(problem)


def get_major_module(problem):
    first = (problem // 100) * 100
    last = first + 99
    return "problems_{:03d}_{:03d}".format(first, last)


def get_minor_module(problem):
    first = (problem // 10) * 10
    last = first + 9
    return "problems_{:03d}_{:03d}".format(first, last)


def get_file_name(problem):
    return "problem_{:03d}.py".format(problem)


def create_method_name(problem):
    return "problem_{:03d}".format(problem)


def get_problem_group(problem):
    first = (problem // 10) * 10
    return range(first, first + 10)


def get_problem_info(problem):
    url = 'https://projecteuler.net/problem={}'.format(problem)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    try:
        name = soup.select('h2')[0].get_text()
        content = str(soup.select('.problem_content')[0])
        h = html2text.HTML2Text()
        h.body_width = 74
        return name, h.handle(content)
    except:
        print(response.status_code)
        print(response.text)
        raise


command_template = '''

import click

@click.command('{{ problem }}')
{%- for name, default in options %}
@click.option('--{{ name }}', '-{{ name[0] }}', type=int, default={{ default }})
{%- endfor %}
@click.option('--verbose', '-v', count=True)
def {{ method }}(
{%- for name, default in options -%}
{{ name }}
{%- endfor -%}
, verbose):
    """{{ name }}

    {{ content }}
    """

'''

minor_init = '''

{%- for method in methods %}
from .{{ method }} import {{ method }}
{%- endfor %}

all_commands = [
    {%- for method in methods %}
    {{ method }}, 
    {%- endfor %}
]

__all__ = ['all_commands']
'''


major_init = '''
from itertools import chain

{%- for module in modules %}
from .{{ module }} import all_commands as {{ module }}
{%- endfor %}

all_commands = list(chain(
    {%- for module in modules %}
    {{ module }},
    {%- endfor %}
))

__all__ = ['all_commands']
'''