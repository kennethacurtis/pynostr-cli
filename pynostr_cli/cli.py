import click
from .key import generate_key_pair

@click.group()
def cli():
    pass

class Keys(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @click.command()
    @click.option('--output', type=click.File('w'), default='-', help='Output file to save the keys. Defaults to stdout')
    @click.option('--format', type=click.Choice(['hex', 'pem']), default='hex', help='Specifies the format of the keys. Defaults to hex string')
    def generate(output, format):
        """Generate a public and private key pair."""
        private_key, public_key = generate_key_pair(format)

        click.echo("Private Key:", file=output)
        click.echo(private_key, file=output)

        click.echo("\nPublic Key:", file=output)
        click.echo(public_key, file=output)

# keys
keys_group = Keys(name='keys')  # Provide a name for the Keys instance
keys_group.add_command(keys_group.generate)
cli.add_command(keys_group)


if __name__ == "__main__":
    cli()
