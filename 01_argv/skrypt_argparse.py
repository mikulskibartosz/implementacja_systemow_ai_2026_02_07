import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Trenowanie modelu")
    parser.add_argument("position_arg", type=int, help="Argument pozycyjny")
    parser.add_argument("--data_path", type=str, help="Ścieżka do danych treningowych", required=True)
    parser.add_argument("--model_type", type=str, help="Typ modelu", choices=["linear", "random_forest", "gradient_boosting"], default="linear")
    parser.add_argument("--debug", action="store_true", help="Włącza tryb debugowania")
    parser.add_argument("--no-cache", action="store_true", help="Wyłącza cache", dest="cache")
    parser.add_argument("--learning-rate", type=float, help="Współczynnik uczenia", default=0.01)
    parser.add_argument("--features", nargs="+", help="Lista cech", default=[])
    parser.add_argument("-v", action="count", help="Włącza tryb verbose", default=0)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")


    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    print("Argument pozycyjny:", args.position_arg)
    print("Ścieżka do danych treningowych:", args.data_path)
    print("Typ modelu:", args.model_type)
    print("Tryb debugowania:", args.debug)
    print("Wyłączenie cache:", args.cache)
    print("Współczynnik uczenia:", args.learning_rate)
    print("Lista cech:", args.features)
    print("Tryb verbose:", args.v)