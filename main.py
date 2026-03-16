# Drill 2 
from pyscript import document, display


def area_triangle(base, height):
    return {'base': base, 'height': height}


def computation_area(e):
    document.getElementById('output').innerHTML = ''

    base1 = int(document.getElementById('input1').value)
    base2 = int(document.getElementById('input2').value)    
    area = (base1 * base2) / 2

    triangle_info = area_triangle(base1, base2)
    display(f'With a base of {base1} and a height of {base2}, ', target ="output")
    display(f'the Area is {area}', target ="output")
    display(triangle_info, target="output")