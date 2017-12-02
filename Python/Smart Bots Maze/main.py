from genetic import Genetic


def main():
    genetic = Genetic(100, 100, 50, 0.1, [(400, 0, 20, 300)])
    genetic.simulate_with_graphics()

if __name__ == "__main__":
    main()