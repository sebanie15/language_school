import click
from lang_school.cli import my_school


@click.command()
def cli():
    my_school.add_levels([
        ["A1", "Beginner"],
        ["A2", "Pre-Intermediate"],
        ["B1", "Intermediate"],
        ["B2", "Upper-Intermediate"],
        ["C1", "Advanced"],
        ["C2", "Proficient"]
    ]
    )

    my_school.add_categories(
        [
            'kurs konwersacyjny',
            'kurs biznesowy',
            'kurs dla dorosłych',
            'kurs dla dzieci',
            'kurs egzaminacyjny',
            'cena'
        ]
    )
    my_school.add_languages(
        ['English',
         'Niemiecki',
         'Francuski',
         'Hiszpański',
         'Włoski'
         ]
    )
    click.echo('Baza danych zainicjalizowana ;) init_school')
    click.echo((f'My school ID: {id(my_school)}'))
