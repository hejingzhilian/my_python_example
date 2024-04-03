import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def initdb(count,name):
    print(f" option {count}, argument name {name} ")
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

@click.group()
def cli_sub():
    pass

@click.command()
def sub_dropdb():
    click.echo('sub_dropdb ')

## add_command 即可以是command 也可以是 group
cli_sub.add_command(sub_dropdb)

cli.add_command(cli_sub)
if __name__ == "__main__":
    cli()