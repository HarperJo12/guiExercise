#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# for i, char in enumerate(picture):
#   for y, char in enumerate(picture[i]):
#     if picture[i][y] == 0:
#       print(' ', end='')
#     else:
#       print('*', end='')
#   print()

for rows in picture:
  for pixel in rows:
    if pixel:
      print('*', end='')
    else:
      print(' ', end='')
  print()
