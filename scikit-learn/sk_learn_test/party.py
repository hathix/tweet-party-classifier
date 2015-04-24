class Party:
    Democrat = 1
    Republican = 0
    
def ind_to_party(i):
    return {Party.Democrat: "Democrat",
            Party.Republican: "Republican"
            }[i]
