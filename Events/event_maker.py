import os
import sys

# Function to capitalize each word in the event name
def capitalize(s):
	return ' '.join([i.capitalize() for i in s.split(' ')])

# Variables for file paths and outputs
current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'input.txt')
loc_output = os.path.join(current_dir, 'loc_output.yml')
event_output_path = os.path.join(current_dir, 'event_output.txt')

# Read the input file and parse the data
def read_input(starting_id):
	with open(file_path, 'r') as f:
		lines = f.readlines()

	# Extract the prefix
	prefix = lines[0].strip().split('=')[1]
	
	events = []
	line_no = 1  # Skip the prefix line

	while line_no < len(lines):
		# Skip empty lines
		if not lines[line_no].strip():
			line_no += 1
			continue
		
		event_name = lines[line_no].strip()
		line_no += 1
		if line_no >= len(lines):
			# If we are at the last line and there's no next line, assume 1 option for this event
			option_amt = 1
			events.append((event_name, option_amt))
			break

		# Try to get the number of options
		if line_no < len(lines) and lines[line_no].strip().isdigit():
			option_amt = int(lines[line_no].strip())
			line_no += 1
		else:
			# If no option amount is found, assume it's 1
			print(f"No option amount found for '{event_name}', assuming 1 option.")
			option_amt = 1

		events.append((event_name, option_amt))

	return prefix, events

# Generate the localization output (loc_output.yml)
def generate_loc_output(prefix, events, starting_id):
	loc_lines = []
	event_id = starting_id

	for event_name, option_amt in events:
		capitalized_name = capitalize(event_name)

		loc_lines.append(f"\n {prefix}.{event_id}.t:0 \"{capitalized_name}\"")
		loc_lines.append(f" {prefix}.{event_id}.desc:0 \"REPLACE_ME\"")

		for i in range(option_amt):
			option_letter = chr(ord('a') + i)  # 'a', 'b', 'c', ...
			loc_lines.append(f" {prefix}.{event_id}.{option_letter}:0 \"OPTION {i + 1}\"")

		event_id += 1

	with open(loc_output, 'w') as f:
		f.write("\n".join(loc_lines))
	print(f"Localisation created: {loc_output}")

# Generate the event output (event_output.txt)
def generate_event_output(prefix, events, starting_id):
	event_lines = []
	event_id = starting_id

	for event_name, option_amt in events:
		capitalized_name = capitalize(event_name)

		event_lines.append(f"country_event = {{")
		event_lines.append(f"\tid = {prefix}.{event_id} # {capitalized_name}")
		event_lines.append(f"\ttitle = \"{prefix}.{event_id}.t\"")
		event_lines.append(f"\tdesc = \"{prefix}.{event_id}.desc\"")
		event_lines.append(f"\tpicture = GFX_")
		event_lines.append(f"\n\tis_triggered_only = yes\n")

		for i in range(option_amt):
			option_letter = chr(ord('a') + i)  # 'a', 'b', 'c', ...
			event_lines.append(f"\toption = {{")
			event_lines.append(f"\t\tname = {prefix}.{event_id}.{option_letter}\n\t\t")
			event_lines.append(f"\t}}")

		event_lines.append(f"}}\n")
		event_id += 1

	with open(event_output_path, 'w') as f:
		f.write("\n".join(event_lines))
	print(f"Event output written to: {event_output_path}")

# Main function to orchestrate the generation of output files
def main():
	# Allow the user to set the starting event ID (default to 1)
	starting_id = int(input("Enter the starting event ID (default 1): ") or 1)

	prefix, events = read_input(starting_id)
	generate_loc_output(prefix, events, starting_id)
	generate_event_output(prefix, events, starting_id)

if __name__ == '__main__':
	main()
