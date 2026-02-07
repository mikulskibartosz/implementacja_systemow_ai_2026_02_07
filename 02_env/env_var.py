import os

print("get: " + str(os.environ.get("DATABASE_URL")))
print("os.environ: " + str(os.environ["DATABASE_URL"]))

liczba = os.environ.get("LICZBA", -1)
print("liczba: " + str(liczba))