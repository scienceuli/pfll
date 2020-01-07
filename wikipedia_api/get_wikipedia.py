import textwrap

import click
import requests

API_URL = "https://de.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
def main():
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg='green')
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main()
