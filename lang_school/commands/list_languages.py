import click
from lang_school.cli import my_school

@click.command()
def cli():
    click.echo('list of  languages')
    for language in my_school.languages():
        click.echo(language)
