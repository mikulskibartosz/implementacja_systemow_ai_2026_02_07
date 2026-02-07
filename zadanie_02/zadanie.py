import click
import re
from collections import Counter

def get_words(text):
    return re.findall(r'\b\w+\b', text.lower())


def get_word_count(words):
    return len(words)


def get_word_frequency(words):
    return Counter(words)


@click.group()
def cli():
    """Aplikacja do analizy tekstu"""
    pass


@cli.command(help="Oblicza czas potrzebny na przeczytanie tekstu")
@click.option("--file_path", type=click.Path(exists=True, readable=True), required=True)
def calculate_reading_time(file_path):
    """Oblicza czas potrzebny na przeczytanie tekstu"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = get_words(text)
    word_count = get_word_count(words)

    reading_time = word_count / 238
    minutes = reading_time // 60
    seconds = reading_time % 60
    click.echo(f"Czas potrzebny na przeczytanie tekstu: {minutes} minut i {seconds} sekund")


@cli.command(help="Oblicza częstość występowania słów w tekście")
@click.option("--file_path", type=click.Path(exists=True, readable=True), required=True)
@click.option("--n", type=int, help="Liczba słów do wyświetlenia", default=10)
def calculate_word_frequency(file_path, n):
    """Oblicza częstość występowania słów w tekście"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = get_words(text)
    word_frequency = get_word_frequency(words)
    for word, frequency in word_frequency.most_common(n):
        click.echo(f"{word}: {frequency}")


if __name__ == "__main__":
    cli()