#!/usr/bin/env python
# coding: utf-8

# In[9]:


def reverse_ascending(seznam):
    vysledek = []
    aktualni_skupina = []

    for cislo in seznam:
        if not aktualni_skupina:
            aktualni_skupina.append(cislo)
        else:
            if cislo > aktualni_skupina[-1]:
                aktualni_skupina.append(cislo)
            else:
                vysledek.extend(reversed(aktualni_skupina))
                aktualni_skupina = [cislo]
    vysledek.extend(reversed(aktualni_skupina))

    return vysledek

print(reverse_ascending([1, 2, 3, 4, 5]))
print(reverse_ascending([5, -7, 10, 4, 2, 0, 8, 1, 3]))




# In[ ]:




