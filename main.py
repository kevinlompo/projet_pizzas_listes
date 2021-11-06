def tri_personnalise(e):
    return e


def afficher(collection, n_premiers_elements=-1):
    collection.sort(key=tri_personnalise)
    c = collection
    if not n_premiers_elements == -1:
        c = collection[:n_premiers_elements]
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
    else:
        print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in c:
            print(i)
            print()
        print(f"première pizza : {c[0]}")
        print(f"la dernière pizza : {c[-1]}")


def ajouter_pizza_utilisateur(collection):
    pizza = input("PIZZA à ajouter : ")
    if pizza_existte(collection, pizza.lower()):
        print("Erreur : la pizza existe")
    else:
        collection.append(pizza)
    return collection


def pizza_existte(collection, nouvelle):
    for i in collection:
        if i == nouvelle:
            return True
    return False


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
print(pizzas)
pizzas = ajouter_pizza_utilisateur(pizzas)
print(pizzas)
# vide = ()
afficher(pizzas)
