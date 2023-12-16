import os

def swap_quotes(input_string):
    swapped_string = ""
    
    for char in input_string:
        if char == "'":
            swapped_string += '"'
        elif char == '"':
            swapped_string += "'"
        else:
            swapped_string += char
    
    return swapped_string

def convert_log_to_json(input_log_file):
    file = open(input_log_file)
    print("Parsing file: {}".format(file.name))
    output_json_file = open(input_log_file.replace('log', 'json'), "w")
    print("Output file: {}".format(output_json_file.name))
    output_json_file.write("[")
    text_out = []
    for index, line in enumerate(file, start=1):
        line_text = line
        if "Amount Available for Withdrawal:" in line_text or "error" in line_text:
            continue
        line_text = swap_quotes(line_text)
        line_text = line_text.replace("Maker Buy: ", "")
        line_text = line_text.replace("True", "true")
        line_text = line_text.replace("False", "false")
        text_out.append(line_text)
    output_json_file.write(",".join(text_out))
    output_json_file.write("]")
    output_json_file.close()
    file.close()
