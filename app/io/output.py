

def console_out(output):
    '''
    Prints given data in a console.

    Args:
        output (any): any object or data to be printed in a console.

    Examples:
        >>> console_out("Hello World!")
        Hello World!
        >>> console_out([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
    '''
    print(output)


def write_file(data, file_path):
    '''
    Writes provided data in a file.

    Args:
        data (any): any object or data to be wrote in a file.
        file_path (string): path to a file to write in.
    '''
    file_to_write = open(file_path, 'w')
    file_to_write.write(data)
    file_to_write.write('\n')
    file_to_write.close()
