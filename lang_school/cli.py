import os
import click

from lang_school.lang_school import LanguageSchool


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'commands')):
            if filename.endswith('.py') and not filename.startswith('__'):
                rv.append(filename.replace('.py', ''))
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f'lang_school.commands.{name}', None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


db_connection = f"sqlite:///:memory:"
my_school = LanguageSchool(connection_string=db_connection, echo=False)


@click.command(cls=ComplexCLI)
def cli():
    """ Welcome to Language scholl!"""

    click.echo((f'My school ID: {id(my_school)}'))
