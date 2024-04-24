tests = True
input_file = "tests/sameamount10.txt" if tests else "input.in"


def get_input_file(input_file):
    with open(input_file, "r") as f:
        file = f.read()
        return file, file.split("\n")[0][-1]
        # ;S = fita com inicio a esquerda
        # ;I = fita duplamente infinita


def initial_jump_one(start_q, return_to):
    q0, q1, q2, q3, q4 = [f"q{i}" for i in range(start_q, start_q + 5)]
    # cur_st, cur_symb, new_symb, dire, new_st = line.split()

    new_line = f"""q0z _ * r *
q0z 1 * * q0
q0z 0 * * q0

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

q4 # ! r 0
q4 _ _ r q4
q4 0 0 * q1
q4 1 1 * q1

q4z # * * q4
q4z 1 * * q4
q4z 0 * * q4""".split("\n")
    print(new_line)
    with open('teste.txt', 'w') as f:
        # for line in new_line:
        f.write("\n".join(new_line))


# tape, model = get_input_file()
jump_one(10, 1)

"""q0z _ * r *
q0z 1 * * q0
q0z 0 * * q0

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

q4 # ! r 0
q4 _ _ r q4
q4 0 0 * q1
q4 1 1 * q1

q4z _ _ r q5z
q4z # * * q4
q4z 1 * * q4
q4z 0 * * q4

q5z # _ l 1

;---------------


0 _ _ l 1
0 0 0 r 0
0 1 1 r 0
0 B B r 0
0 X X r 0
1 1 _ r 2
1 0 _ r 3
1 _ _ r 4
2 0 1 l 5
2 1 1 l 5
2 _ 1 l 5
2 B 1 l 5
2 X 1 l 5
5 0 0 l 1
5 1 1 l 1
5 _ _ l 1
5 B B l 1
5 X X l 1
1 ! * r q10z

;-----------

q10z _ * r *
q10z 1 * * q10
q10z 0 * * q10

q10 1 * r *
q10 0 * r *
q10 _ $ l q11

q11 0 # r q12
q11 # * l q14z
q11 1 # r q13

q12 $ 0 l q11
q12 # 0 l q11

q13 # 1 l q11
q13 $ 1 l q11

q14 # _ r 1
q14 _ _ r q14
q14 0 0 * q11
q14 1 1 * q11

q14z _ _ r q15z
q14z # * * q14
q14z 1 * * q14
q14z 0 * * q14

q15z # _ l 1


;-----------

3 0 0 l 6
3 1 0 l 6
3 _ 0 l 6
3 B 0 l 6
3 X 0 l 6

6 0 0 l 1
6 1 1 l 1
6 _ _ l 1
6 B B l 1
6 X X l 1

4 _ B r 7

8 1 X l 9
8 0 X l 10
8 X X l 8
8 B B r halt-accept

9 1 1 l 9
9 X X l 9
9 0 X r 7

10 0 0 l 10
10 X X l 10
10 1 X r 7

7 _ _ l 8
7 0 0 r 7
7 1 1 r 7
7 B B r 7
7 X X r 7
"""