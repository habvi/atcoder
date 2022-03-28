y, m, d = map(int, input().split('/'))

print('Heisei' if m <= 4 and d <= 30 else 'TBD')