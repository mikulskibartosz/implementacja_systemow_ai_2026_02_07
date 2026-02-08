import argparse

from .calculator import predict

def main():
    parser = argparse.ArgumentParser(description="Przewidywanie klasy iris")
    parser.add_argument("--sepal-length", type=float, help="Długość działki", required=True)
    parser.add_argument("--sepal-width", type=float, help="Szerokość działki", required=True)
    parser.add_argument("--petal-length", type=float, help="Długość płatka", required=True)
    parser.add_argument("--petal-width", type=float, help="Szerokość płatka", required=True)
    args = parser.parse_args()

    prediction = predict([args.sepal_length, args.sepal_width, args.petal_length, args.petal_width])
    print(f"Przewidziana klasa: {prediction}")

if __name__ == "__main__":
    main()