def ausgabe(name):
    print("Name: ", name)
    print("__name__ in ausgabe: ", __name__)


if __name__ == "__main__":
    ausgabe("Ulrich")
    print("huhu")
    print("__name__ in call: ", __name__)
