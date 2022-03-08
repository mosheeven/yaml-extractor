import click
import yaml
import jmespath
import sys


@click.command()
@click.option('-f', '--file', help='The name of a yaml file. \nIf the file name is `-`, then it is read from stdin', prompt="Please provide YAML")
@click.option('-e', '--expr', help='The expression to extract.', prompt="Please provide expression to extract")
def yaml_extractor(file, expr):
    """Extract value from yaml by using jmespath expration."""
    if file == "-":
        yaml_data = yaml.safe_load(sys.stdin.read())
    else:    
        with open(file) as f:
            yaml_data = yaml.safe_load(f)
    
    path = jmespath.search(expr, yaml_data)
    click.echo(path)
        


if __name__ == '__main__':
    yaml_extractor()