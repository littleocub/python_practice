from random import randint

def roll_dice():
    """ simulate roll dice """
    results = []
    for num in range(times):
        result = randint(1, sides)
        results.append(result)
    return results

def frequencies(x):
    """ calculate frequency of each time """
    results = []
    for num in range(2, sides*2+1):
        result = x.count(num)
        results.append(result)
    return results

# define the die sides and roll times
sides = 6
times = 1000

# calculate results and the frequency of each side
roll_results_1 = roll_dice()
roll_results_2 = roll_dice()
roll_results = [roll_results_1[i]+roll_results_2[i] for i in range(times)]

# print(roll_results)
frequencies = frequencies(roll_results)
print(frequencies)

# visualize using pygal
import pygal

# plot the chart using bars
freq_visual = pygal.Bar()

# optimize the chart
freq_visual.title = 'Rolling Results of 1,000 times'
freq_visual.x_labels = [str(x) for x in range(2, 13)]
freq_visual.x_title = 'Results'
freq_visual.y_title = 'Frequency'

# plot and save to file
freq_visual.add('6-side Dice *2', frequencies)
freq_visual.render_to_file('dice_two.svg')