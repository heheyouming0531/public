print('\n'.join([''.join([('ILoveU'[(x-y) % len('ILoveU')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-25, 25)]) for y in range(13, -13, -1)]))
