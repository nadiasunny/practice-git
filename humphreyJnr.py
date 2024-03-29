
def humpty(name):
    length = len(name)
    while length>0:
        length-=1
        print(f'{name}y Dumpty sat on a wall. {name}y, he had a great fall.')
       

print(humpty('Lump'))