from operator import itemgetter
from typing import List
from typing import Dict
from typing import Tuple

fp = "input"


def parse_stacks(v: List[str]) -> Dict[int, List[str]]:
    indices = [int(i) for i in v.pop().split(" ") if i]
    rows = [itemgetter(*range(1, 4*indices[-1]-2, 4))(r) for r in v]
    return {i: [j[i-1] for j in rows if j[i-1] != " "][::-1] for i in indices}
    

def parse_move(v: str) -> Tuple[int]:
    return map(int, itemgetter(1, 3, 5)(v.strip(" ").split(" ")))


def process_moves(stacks: Dict[int, List[str]], moves: Tuple[int]):
    for n, a, b in moves:
        for _ in range(n):
            stacks[b].append(stacks[a].pop())
    return stacks


with open(fp, "r") as f:
    lines = f.read().split("\n")

    stacks = []
    while line:=lines.pop(0):
        stacks.append(line)

    stacks = parse_stacks(stacks)
    moves = list(map(parse_move, lines))
    stack = process_moves(stacks, moves)

answer = "".join([stacks[i][-1] for i in stacks])

print(f"{answer=}")
