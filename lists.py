motorcycles = ['yamaha', 'honda', 'ducati']
print(motorcycles)

motorcycles.insert(0, 'Kawasaki')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")