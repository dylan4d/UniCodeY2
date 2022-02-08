'''Seek to record the frequency of first digit occurences, compare to Benfords Law using chi-square test, and present comparisons.'''
import sys
import math
from collections import defaultdict
import matplotlib.pyplot as plt

#Benfords Laws percentages 1-9
benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def load_data(filename):
    '''open file + return a list of strings'''
    with open(filename) as f:
        return f.read().strip().split('\n')

def count_first_digits(data_list):
    '''count first digits in lst, return count + stochastics'''
    first_digits = defaultdict(int)
    for sample in data_list:
        if sample == '':
            continue
        try:
            int(sample)
        except ValueError as e:
            print(e, file=sys.stderr)
            print('Samples must be integers', file=sys.stderr)
            sys.exit(1)
        first_digits[sample[0]] += 1
        keys = [str(digit) for digit in range(1, 10)]
        for key in keys:
            if key not in first_digits:
                first_digits[key] = 0
        data_count = [v for (k, v) in sorted(first_digits.items())]
        total_count = sum(data_count)
        data_pct = [(i / total_count) * 100 for i in data_count]
    return data_count, data_pct, total_count

def get_expected_counts(total_count):
    '''return lst of expected counts for a total sample count under bedfords law.'''
    return [round(p * total_count / 100) for p in benford]

def chi_square_test(data_count, expected_counts):
    '''return boolean on chisquare test with 95% level of confidence and 8 degrees of freedom (n-1) (9-1 digits)'''
    chi_square_stat = 0
    for data, expected in zip(data_count, expected_counts):
        chi_square = math.pow(data - expected, 2)
        chi_square_stat += chi_square / expected
    print('\nChi-squared t val = {:.3f}'.format(chi_square_stat))
    print('Critical value at a p-val of 0.05 is 15.51')

    return chi_square_stat <= 15.51

def bar_chart(data_pct):
    '''make bar chart of observed vs expected first digit frequency'''
    fig, ax  = plt.subplots()

    index = [i + 1 for i in range(len(data_pct))]

    fig.canvas.set_window_title('Percentage First Digits')
    ax.set_title('Data vs. Benford Values', fontsize = 15)
    ax.set_ylabel('Frequency', fontsize = 16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize = 14)

    rects = ax.bar(index, data_pct, width = 0.95, color = 'black', label = 'Data')

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height, '{:0.1f}'.format(height), ha = 'center', va = 'bottom', fontsize = 13)

    ax.scatter(index, benford, s=150, c='red', zorder=2, label='benford')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(prop = {'size': 15}, frameon = False)

    plt.show()

def main():
    '''call functions and print stats'''
    while True:
        filename = input('\nName of file with count data: ')
        try:
            data_list = load_data(filename)
        except IOError as e:
            print('{}. Try again.'.format(e), file=sys.stderr)
        else:
            break
    
    data_count, data_pct, total_count = count_first_digits(data_list)
    expected_counts = get_expected_counts(total_count)
    print('\nobserved counts = {}'.format(data_count))
    print('expected counts = {}'.format(expected_counts), '\n')
    
    print('First Digit Probabilities:')
    for i in range(1, 10):
        print('{}: observed: {:.3f} expected: {:.3f}'.format(i, data_pct[i-1] / 100, benford[i-1] / 100))
    
    if chi_square_test(data_count, expected_counts):
        print('Observed distribution matches expected distribution.')
    else:
        print('Observed distribution does not match expected distribution.', file = sys.stderr)
    
    bar_chart(data_pct)

if __name__ == '__main__':
    main()
