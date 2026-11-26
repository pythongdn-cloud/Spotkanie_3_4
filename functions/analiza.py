import re

states = ["   Alabama    ", "Georgia!", "Georgia", "georgia", "FlOrIda", "south carolina##", "West virginia?"]
clean_ops = [str.title, str.strip, usun_znaki_interpunkcyjne]
#opisywanie funkcji
def mean(delays):
  """
  Oblicza średnie opóźnienie lotów.

  Args:
    delays: lista opóźnień lotów w minutach.
  
  Returns:
    Średnie opóźnienie
  """
  return sum(delays)/len(delays)
# zadanie 1 
def greet(imie):
  print(f"Hej, {imie}!")
# zadanie 2 
def pole_i_obwod_slownik(a, b):
    return {
        "pole": a * b,
        "obwod": 2 * a + 2 * b
    }
# zadanie 3
def calculator (a,b,operation):

  operators ={
    "+": a+b,
    "-": a-b,
    "*": a*b,
    '/': a/b
  }

  if operation not in operators:
    print(f"Kalkulator nie obsługuje działania {operation}. Spróbuj ponownie!")

  else:
  
    result = operators[operation]
    print(f"Wynik działania to {result}")

    return result
# zadanie 4
def clean_strings(cities):
  """
  Args:
  cities - a list of cities with editorial errors

  Returns:
  list of cities without editorial errors 
  """
  cities_clean = []
  for city in cities:
    city = re.sub("[!#?]","",city)
    city = city.strip()
    city = city.title()
    cities_clean.append(city)
  return cities_clean
# zadadnie 4 alternate solution
def usun_znaki_interpunkcyjne(slowa):
  return re.sub("[!?*#,:']","",slowa)

def clean_strings2(cities,ops):
  clean_cities = []
  for city in cities:
    for func in ops:
      city = func(city)
    clean_cities.append(city)
  return clean_cities





if __name__ == "__main__":
  print(f"\n")
  wynik = calculator(4,5,"**")
  print(f"\n")
  wynik = calculator(2,3,"+")
  print(f"\n")
  greet("Tomek")

  clean = clean_strings(states)
  print(clean)

  clean_2 = clean_strings2(states,clean_ops)
  print(clean_2)

