from genetic import Genetic


def main():
    genetic = Genetic(100, 500, 50, 0.1, [(550, 0, 20, 300),(250, 300, 20, 300)])
    genetic.simulate_with_graphics()

if __name__ == "__main__":
    main()