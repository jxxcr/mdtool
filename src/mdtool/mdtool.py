import click
from mdtool.cli import (
    convert,
    wrap,
    extract,
    data,
    plot,
)


@click.group(name='cli')
@click.pass_context
@click.version_option()
def cli(ctx):
    """tools for md or dft"""
    pass


cli.add_command(convert.main)
cli.add_command(wrap.main)
cli.add_command(extract.main)
cli.add_command(data.main)
cli.add_command(plot.main)


if __name__ == '__main__':
    cli()