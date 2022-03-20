S = ''.join(input().split())
T = ''.join(input().split())

rgb = ['RGB', 'RBG', 'GBR', 'GRB', 'BRG', 'BGR']

print('Yes' if rgb.index(S) % 2 == rgb.index(T) % 2 else 'No')