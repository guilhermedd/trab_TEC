INPUT_FILE = 'input.in'
OUTPUT_FILE = 'output.out'
INITIAL_STATE = '0'


def get_input_file():
    with open(INPUT_FILE, 'r') as input_file:
        file = input_file.read()
        return file, file.split('\n')[0][-1]
        # ;S = fita com inicio a esquerda
        # ;I = fita duplamente infinita


tape, model = get_input_file()
