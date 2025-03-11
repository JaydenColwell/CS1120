# Written by Jayden Colwell

def main():
    winner_dict = {}
    years_dict = {}
    year = 1902
    rerun = 'y'
    with open("WorldSeriesWinners.txt", 'r') as infile:
        for winner in infile:
            if winner.rstrip('\n') in winner_dict.keys():
                winner_dict[winner.rstrip('\n')] += 1
            else:
                winner_dict[winner.rstrip('\n')] = 1

            years_dict[year] = winner.rstrip('\n')
            year += 1

    while rerun.lower() == 'y':
        test_year = int(input("\nEnter a year between 1902 and 1995: "))
        if test_year < 1902 or test_year > year:
            print("This is not a year in the dataset.")
        elif years_dict[test_year] == 'There was no World Series':
            print("The world series did not take place this year.")
        else:
            print(f'In the year {test_year}, {years_dict[test_year]} won.')
            print(f'The team, {years_dict[test_year]}, has {winner_dict[years_dict[test_year]]} wins.')
        rerun = input("\nWould you like to run again? (y or n): ")

main()