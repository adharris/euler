import click

from tools.generate import generate

@click.group()
def cli():
    pass
    
from problems import all_commands

for command in all_commands:
    cli.add_command(command)

cli.add_command(generate)