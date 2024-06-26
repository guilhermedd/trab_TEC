def get_input_file(in_file):
    with open(in_file, "r") as f:
        file = f.read()
        return file, file.split("\n")[0][-1]
        # ;S = fita com inicio a esquerda
        # ;I = fita duplamente infinita


def open_file(quant, out, in_file):
    new_file = ""
    machine_type = ''

    try:
        with open(in_file, "r") as f:
            file = f.read()
            for line in file.splitlines():
                if line.startswith(';'):
                    machine_type = line.split(';')[1]
                    new_file += initial_jump_one(machine_type)
                    continue
                else:
                    cur_st, cur_sy, new_sy, direc, new_st = line.split(" ")
                    try:
                        new_file += f"{int(cur_st) + quant} {cur_sy} {new_sy} {direc} {int(new_st) + quant}\n"
                    except ValueError as e:
                        new_file += f"{int(cur_st) + quant} {cur_sy} {new_sy} {direc} {new_st}\n"

        with open(out, 'w') as f:
            f.write(new_file)

        return new_file, machine_type
    except FileNotFoundError as e:
        print(e)
        return None, None


def initial_jump_one(machine_type):
    if machine_type == 'I':
        return \
            """0 _ * r *
0 1 * * q0
0 0 * * q0
q0 1 * r *
q0 0 * r *
q0 _ _ r qz
qz _ _ l qz1
qz 1 * * q0
qz 0 * * q0
qz1 _ $ l q1
q1 0 # r q2
q1 # * l q4z
q1 1 # r q3
q2 $ 0 l q1
q2 # 0 l q1
q3 # 1 l q1
q3 $ 1 l q1
q4 # ! r 1
q4 _ _ r q4
q4 0 0 * q1
q4 1 1 * q1
q4z # * * q4
q4z 1 * * q4
q4z 0 * * q4
"""
    return \
        """0 1 * r 0
0 0 * r 0
0 _ $ l q1
q1 $ * l q1
q1 # * l q1
q1 0 # r q2
q1 1 # r q3
q1 _ * r q5
q2 $ * r q2
q2 # * r q2
q2 _ 0 l q4
q2 0 * r q2
q2 1 * r q2
q3 $ * r q3
q3 # * r q3
q3 _ 1 l q4
q3 0 * r q3
q3 1 * r q3
q4 0 * l q4
q4 1 * l q4
q4 $ * l q4
q4 # * * q1
q5 # _ r q5
q5 $ _ r q5
q5 1 * r q5
q5 0 * r q5
q5 _ * l 1
"""


def add_blanc(return_to, next_q):
    q0, q1, q2, q3, q4, q5 = [f"q{i}" for i in range(next_q, next_q + 6)]
    new_lines = f"""{return_to} ! * r {q0}z
{q0}z _ * r *
{q0}z 1 * * {q0}
{q0}z 0 * * {q0}

{q0} 1 * r *
{q0} 0 * r *
{q0} _ $ l {q1}

{q1} 0 # r {q2}
{q1} # * l {q4}z
{q1} 1 # r {q3}

{q2} $ 0 l {q1}
{q2} # 0 l {q1}

{q3} # 1 l {q1}
{q3} $ 1 l {q1}

{q4} # _ r {return_to}
{q4} _ _ r {q4}
{q4} 0 0 * {q1}
{q4} 1 1 * {q1}

{q4}z _ _ r {q5}
{q4}z # * * {q4}
{q4}z 1 * * {q4}
{q4}z 0 * * {q4}

{q5} # _ l {return_to}\n"""
    return new_lines


def translate_to_s(file, out_file, next_q, changed_states):
    final_file = ''
    final_file += file

    for line in file.split('\n'):
        try:
            cur_st, cur_sy, new_sy, direct, new_st = line.split()

            if not cur_st in changed_states and not cur_st.startswith('q'):
                changed_states.append(cur_st)

                final_file += add_blanc(cur_st, next_q)
                next_q += 6
        except ValueError:
            final_file += ""

    with open(out_file, 'w') as f:
        f.write(final_file)


def translate_to_i(file, out_file):
    final_file = ''

    for line in file.split('\n'):
        try:
            cur_st, cur_sy, new_sy, direct, new_st = line.split()

            if not cur_st.startswith('0') and not cur_st.startswith('q'):
                if direct != '*':
                    direct = 'r' if direct == 'l' else 'l'

            final_file += f"{cur_st} {cur_sy} {new_sy} {direct} {new_st}\n"
        except ValueError:
            final_file += f""

    with open(out_file, 'w') as f:
        f.write(final_file)


def main(input_file, output_file, next_q, changed_states):
    file, machine_type = open_file(1, 'testando.txt', input_file)

    if machine_type == 'I':
        return translate_to_s(file, output_file, next_q, changed_states)

    return translate_to_i(file, output_file)


if __name__ == '__main__':
    input_file = input('Digite o nome do arquivo de entrada:\n')
    out_file = input('Digite o nome do arquivo de saída:\n')
    next_q = 5
    changed_states = []
    main(input_file, out_file, next_q, changed_states)
