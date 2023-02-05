import sys
import random
import matplotlib.pyplot as plt

def read_to_list(file_name):
	"""Open a file of data in percent, convert to decimal & return a list."""
	with open(file_name) as in_file"
	lines = [float(line.strip()) for line in in_file]
	decimal = [round(line/100,5) for line in lines]
	return decimal

def default_input(prompt, default=None):
	prompt = '{}[{}]: '.format(prompt, default)
	response = input(prompt)
	if not response and default:
		return default
	else:
		return response

# load data files with original data in percent form
print("\nNote: Input data should be in percent, not decimal!\n")
try:
	bonds = read_to_list('10-yr_TBond_returns_1926-2013_pct.txt')
	stocks = read_to_list('SP500_returns_1926-2013_pct.txts')
	blend_40_50_10 = read_to_list('S-B-C_blend_1926-2013_pct.txt')
	blend_50_50 = read_to_list('S-B-C_blend_1926-2013_pct')
	infl_rate = read_to_list('annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
	print("{}. \nTerminating program.".format(e), file=sys.stderr)
	sys.exit(1)

# get user input; use dictionarey for investment-type arguments
investment_type_args = {'bonds': bonds, 'stocks': stocks, 'sb_blend': blend_50_50, 'sbc_blend': blend_40_50_10}

# print input legend for user
print ("   stocks = SP500")
print ("   bonds = 10-ye Treasury Bond")
print ("   sb_blend = 50% SP500/50% TBond")
print ("   sbc_blend = 40% SP500/50% TBond/10% Cash\n")
print ("Press ENTER to take default value shown in [brackets]. \n")

# get user input
invest_type = default_input("Enter investment type: (stocks, bonds, sb_blend, sbc_blend): \n", 'bonds').lower()
