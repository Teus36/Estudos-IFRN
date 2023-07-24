m = []
m_num = 0

for l in range(3):
    linha = [0] * 3
    m.append(linha)

for l in range(3):
    for c in range(3):
        m[l][c] = int(input(f"Digite o valor da posição [{l + 1},{c + 1}]: "))

for l in range(3):
    if l == 0:
        m_num = m[l][c]
    else:
        if m[l][c] > m_num:
            m_num = m[l][c]
            print(f"O maior número é {m_num} e está localizado na linha {l+1} coluna {c+1}")