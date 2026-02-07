import click
import pandas as pd


@click.group()
def cli():
    """Aplikacja do konwertowania danych z CSV"""
    pass


@cli.command(help="Konwertuje dane z CSV do JSON")
@click.option("--input-path", type=str, help="Ścieżka do pliku CSV", required=True)
@click.option("--output-path", type=str, help="Ścieżka do pliku JSON", required=True)
@click.option("--columns", multiple=True, help="Kolumny do konwersji", default=None)
@click.option("--rows", type=int, help="Liczba wierszy do konwersji", default=10)
def to_json(input_path, output_path, columns, rows):
    """Konwertuje dane z CSV do JSON"""
    click.echo(f"Konwertuje dane z {input_path} do {output_path}")
    df = pd.read_csv(input_path)

    if columns:
        df = df[list(columns)]
    if rows:
        df = df.head(rows)

    click.echo(f"Wczytano {df.shape[0]} wierszy i {df.shape[1]} kolumn")

    df.to_json(output_path, orient="records", lines=True)
    click.echo(f"Dane zostały konwertowane do {output_path}")

@cli.command(help="Konwertuje dane z CSV do Markdown")
@click.option("--input-path", type=str, help="Ścieżka do pliku CSV", required=True)
@click.option("--output-path", type=str, help="Ścieżka do pliku Markdown", required=True)
@click.option("--columns", multiple=True, help="Kolumny do konwersji", default=None)
@click.option("--title", type=str, help="Tytuł tabeli", default="Tabela")
def to_markdown(input_path, output_path, columns, title):
    """Konwertuje dane z CSV do Markdown"""
    click.echo(f"Konwertuje dane z {input_path} do {output_path}")
    df = pd.read_csv(input_path)

    if columns:
        df = df[list(columns)]
    if title:
        click.echo(f"# {title}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(df.to_markdown(index=False))
    click.echo(f"Dane zostały konwertowane do {output_path}")

if __name__ == "__main__":
    cli()