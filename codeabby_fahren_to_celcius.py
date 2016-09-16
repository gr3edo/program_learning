degr_mas = '424 557 453 415 387 48 452 527 66 581 319 591 322 255 128 356 332 592 561 360 51 580 372 535 285 478 46 152 126 509 93 518 466 515 333 253 531 184 179'.split()
celcius = []

for item in degr_mas:
    item = int(item)
    celcius.append(round( (item - 32) * (5/9) ))

print (' '.join(list(map(str, celcius))))
