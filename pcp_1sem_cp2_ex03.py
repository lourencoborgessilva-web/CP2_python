cp1 = float(input("Nota do Checkpoint 1 (cp1): "))
cp2 = float(input("Nota do Checkpoint 2 (cp2): "))
cp3 = float(input("Nota do Checkpoint 3 (cp3): "))
sp1 = float(input("Nota da Sprint 1 (sp1): "))
sp2 = float(input("Nota da Sprint 2 (sp2): "))
gs = float(input("Nota da Global Solution (gs): "))


menor_cp = min(cp1, cp2, cp3)


media = (cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4


mediaPeso = media * 0.4 + gs * 0.6


print(f"Média dos 2 maiores CPs + 2 Sprints: {media:.2f}")
print(f"Média final com peso: {mediaPeso:.2f}")
