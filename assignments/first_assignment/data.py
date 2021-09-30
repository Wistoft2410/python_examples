filename = open('/Users/computer/Documents/GitHub/python_examples/assignments/first_assignment/data/municipalities-2005-2019.csv')
lines = []

def read_file(filename):
	#write your function here.	
	for row in filename:
		lines.append(row.strip()) # since 'insert' is used every entry is added on top of 0 and pushed to the bottom. As opposed to 'append' which adds every entry as the last 
	return lines

def parse_csv_lines(lines):
	#write your function here. It might possibly call other functions you wrote.
	#jeg skal først kunne loop gennem alle mine strings
	#dernæst skal jeg kunne splitte hver enkelt string baseret på ";"
	#dem jeg splitter skal så tilføjes til deres respektive string[][] 
	#måden jeg splitter hver string 
	
	list_of_list = [[]]

	for line in lines:
		list_of_list.append(line.split(";"))
	
	print(list_of_list[2][0])
	return list_of_list


def parse_delimited_lines(lines, delimiter):
	#write your function here. It might possibly call other functions you wrote.
	return

def age_difference(lines):
	#write your function here. It might possibly call other functions you wrote.

	return

def find_unisex_names(male_names, female_names):
	#write your function here. It might possibly call other functions you wrote.
	return # This function has to return a set.

def build_name_dataset(female_names, male_names, unisex_names):
	#write your function here. It might possibly call other functions you wrote.
	# Should not return anything.
	return

def write_sorted_names(names):
	#write your function here. It might possibly call other functions you wrote.
	print("Done")
	return None





def main():
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
	read_file(filename)
	parse_csv_lines(lines)
	#parse_delimited_lines()
	#age_difference()
	#find_unisex_names()
	#write_tuples()
	#build_name_dataset()
	#write_sorted_names()


if __name__ == "__main__":
	# Executes only if run as a script
	main()
