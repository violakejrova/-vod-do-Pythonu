#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string

def vymaz_znaky(text):

    text_mala = text.lower()
    nezadouci_znaky = set(string.punctuation + string.whitespace + '—' + '-')
    final_text = ""
    for znak in text_mala:
        if znak not in nezadouci_znaky:
            final_text += znak
    
    return final_text
    
def nejdelsi_sekvence(text):
    max_delka = 0
    vysledky = []

    for i in range(len(text)): 
        seen = set()
        
        for j in range(i, len(text)):
            znak = text[j]
            
            if znak in seen:    #duplikát
                aktualni_delka = len(seen)
                break
            else:
                seen.add(znak)
        
        else: 
            aktualni_delka = len(seen)

        if aktualni_delka > max_delka:
            max_delka = aktualni_delka
            vysledky = [text[i : i + max_delka]] 
        
        elif aktualni_delka == max_delka and max_delka > 0:
            sekvence_text = text[i : i + max_delka]
            
            if sekvence_text not in vysledky:
                vysledky.append(sekvence_text)
                
    return max_delka, vysledky


with open("raven.txt", "r") as file:
    obsah_raven = file.read()

vycisteny_text = vymaz_znaky(obsah_raven)
maximalni_delka, vysledne_sekvence = nejdelsi_sekvence(vycisteny_text)

print(f"Nejdelší délka unikátních písmen: {maximalni_delka}")
print("Nalezené sekvence:")
print(vysledne_sekvence)


# In[ ]:




