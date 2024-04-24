def get_input_file(in_file):
    with open(in_file, "r") as f:
        file = f.read()
        return file, file.split("\n")[0][-1]
        # ;S = fita com inicio a esquerda
        # ;I = fita duplamente infinita


def open_file(quant, out, in_file):
    new_file = ""
    machine_type = ''

    new_file += initial_jump_one()

    with open(in_file, "r") as f:
        file = f.read()
        for line in file.splitlines():
            if line.startswith(';'):
                machine_type = line.split(';')[1]
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


def initial_jump_one():
    return \
        f"""0 _ * r *
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

    try:
        for line in file.split('\n'):
            cur_st, cur_sy, new_sy, direct, new_st = line.split()

            if not cur_st in changed_states and not cur_st.startswith('q'):
                print(cur_st)
                changed_states.append(cur_st)

                final_file += add_blanc(cur_st, next_q)
                next_q += 6
    except:
        pass

    with open(out_file, 'w') as f:
        f.write(final_file)


def translate_to_i(file):
    pass

def main(input_file, output_file, next_q, changed_states):
    file, machine_type = open_file(1, 'testando.txt', input_file)

    if machine_type == 'I':
        return translate_to_s(file, output_file, next_q, changed_states)

    return translate_to_i(file)


if __name__ == '__main__':
    tests = False
    input_file = "tests/sameamount10.txt" if tests else "input.in"
    out_file = "output.out"
    next_q = 5
    changed_states = []
    main(input_file, out_file, next_q, changed_states)


"""
0 1 * r 0
0 0 * r 0
0 _ $ l 1

1 $ * l 1
1 # * l 1
1 0 # r 2
1 1 # r 3

2 $ * r 2
2 # * r 2
2 _ 0 l 4
2 0 * r 2
2 1 * r 2

3 $ * r 3
3 # * r 3
3 _ 1 l 4
3 0 * r 3
3 1 * r 3

4 0 * l 4
4 1 * l 4
4 $ * l 4
4 # * * 1


Inverter
"""