import click


@click.command()
def cli():
    click.echo('Hello in lang school!')
    print('hello lang school')


def main():
    print('in main')


if __name__ == '__main__':
    main()
