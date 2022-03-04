# Вводится целое число k (1 <= k <= 365). Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница,
# суббота или воскресенье) является k-й день не високосного года, в котором 1 января является понедельником.

k = int(input())

days = {
    1: 'понедельник',
    2: 'вторник',
    3: 'среда',
    4: 'четверг',
    5: 'пятница',
    6: 'суббота',
    0: 'воскресенье'}

print(days[k % 7])