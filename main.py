from app.io import input, output

def main():
    output.console_out("Hello World!")
    input_data = input.console_in("Enter something: ")
    output.console_out(f"You entered: {input_data}")

    txt_file_data = input.read_file("data/info.txt")
    for line in txt_file_data:
        output.console_out(line)
    
    csv_file_data_string = input.pandas_read_file("data/stats.csv")
    output.write_file(csv_file_data_string, "data/output.txt")

    output_file_data = input.read_file("data/output.txt")
    for line in output_file_data:
        output.console_out(line)


if __name__ == '__main__':
    main()
