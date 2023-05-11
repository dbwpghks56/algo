import sys

sys.stdin = open('twelve-inflearn/study/inputscore.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
hakTable = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}
total = 0.0
current = 0.0

def roundTraditional(val, digits):
    return format(round(val+10**(-len(str(val))-1), digits), '.2f')

for _ in range(n):
    strs, hak, sung = map(str, input().split())
    total += int(hak)
    current += int(hak) * hakTable[sung]
    
print(roundTraditional(float(format(current / total, '.3f')), 2))
