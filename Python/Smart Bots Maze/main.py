from genetic import Genetic


def main():
    genetic = Genetic(200, 200, 50, 0.1, [(130, 130, 200, 150),(20, 20, 100, 50)])
    genetic.simulate_with_graphics()

if __name__ == "__main__":
    main()