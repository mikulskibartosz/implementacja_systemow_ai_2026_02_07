import click

@click.command()
@click.argument("position_arg", type=int, required=True)
@click.option("--data_path", type=str, help="Ścieżka do danych treningowych", required=True)
@click.option("--model_type", help="Typ modelu", type=click.Choice(["linear", "random_forest", "gradient_boosting"]), default="linear")
@click.option("--debug", is_flag=True, help="Włącza tryb debugowania")
@click.option("--cache/--no-cache", default=True, help="Wyłącza cache")
@click.option("--learning-rate", type=float, help="Współczynnik uczenia", default=0.01)
@click.option("--features", multiple=True, help="Lista cech", default=[])
@click.option("-v", count=True, help="Włącza tryb verbose", default=0)
@click.version_option("1.0.0")
def train(position_arg, data_path, model_type, debug, cache, learning_rate, features, v):
    print("Argument pozycyjny:", position_arg)
    print("Ścieżka do danych treningowych:", data_path)
    print("Typ modelu:", model_type)
    print("Tryb debugowania:", debug)
    print("Wyłączenie cache:", cache)
    print("Współczynnik uczenia:", learning_rate)
    print("Lista cech:", features)
    print("Tryb verbose:", v)

if __name__ == "__main__":
    train()