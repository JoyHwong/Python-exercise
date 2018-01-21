motorcycles = ['honda', 'yamaha', 'suzuku']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
