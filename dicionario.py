contato = {
    "@camila":"Camila",
        "@paola":"Paola",
    "@sheron":"Sheron",
    "@bruna":"Bruna",
    "@joao":"Joao",

}

print("chaves:")
for insta in contato.keys():
    print(nome)

 print("\n valores")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

 print("Ordenar por chaves:")
 for insta, nome in contato.item():
   print(f"{insta}-->(nome)")

   contato = {
      "@camila": 1.66,
      "@paola": 1.50,
      "@sheron": 1.80,
      "@bruna": 1.60,
      "@joao": 1.70,
   } 

   print("ordenar por chaves: ")
   for insta in sorted(contato.keys()):
      print(f"(insta)-->(contato[insta]:.2f)")

   from operator import itemgetter 
   print("\n Ordenar por valor (altura)")
   for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta}-->{estrutura:.21}m")        