regras_plural = {
    "iz": "ízes",
    "r": "res", "z": "zes", "ís": "íses",
    "ês": "eses", "és": "eses", "ês": "eses",
    "m": "ns"
}

regras_singular = {
    "ízes": "iz",
    "ceses": "cês", "ueses": "uês", "eses": "és",
    "es": "",
    "ns": "m"
}

exceções_sg_pl = {
    "mal": ["males"],
    "cônsul": ["cônsules"],
    "mel": ["meles","méis"],
    "fel": ["feles","féis"],
    "real": ["réis"],
    "cal": ["cales","cais"],
    "aval": ["avales","avais"],
    "mol": ["moles","móis"],
    "tem": ["têm"],
    "conexão": ["conexões"], "balão": ["balões"],
    "cão": ["cães"], "pão": ["pães"],
    "charlatão": ["charlatães","charlatões"], "ermitão": ["ermitãos","ermitães", "ermitões"],
        "hortelão": ["hortelãos","hortelões"], "sacristão": ["sacristãos","sacristães"], 
        "ancião": ["anciões","anciãos, anciães"],"cirurgião": ["cirurgiões","cirurgiães"],
        "vião": ["vilões","vilãos, vilães"],"aldeão": ["aldeãos","aldeões, aldeães"],
        "peão": ["peões","peães"],"vulcão": ["vulcões","vulcãos"], "refrão": ["refrãos", "refrães"] 

}


exceções_pl_sg = {}
for exceção in exceções_sg_pl:
    vals = exceções_sg_pl[exceção]
    for val in vals:
        exceções_pl_sg[val] = exceção


def plural(palavra):
    if palavra in exceções_sg_pl:
        return exceções_sg_pl[palavra][0]
    
    for regra in regras_plural:
        if palavra.endswith(regra):
            return palavra[:palavra.rfind(regra)] + regras_plural[regra]
    
    if not palavra.endswith("s"):
        return palavra + "s" # Não foram nenhuma das regras. Tenta acrescentar um s.
    
    return palavra

def singular(palavra):
    if palavra in exceções_pl_sg:
        return exceções_pl_sg[palavra]
    for regra in regras_singular:
        if palavra.endswith(regra):
            return palavra[:palavra.rfind(regra)] + regras_singular[regra]
    if palavra.endswith("s"):
        return palavra[:palavra.rfind("s")] # Não foram nenhuma das regras. Tenta remover um s.
    
    return palavra
