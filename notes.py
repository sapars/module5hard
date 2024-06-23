users = ['Andy',
         'Freddy',
         'Jonny',
         'Lizzy',
         'Garry'
         ]
ages = [13,
        17,
        35,
        46,
        56
        ]
l = list(zip(users,ages))
z = dict(zip(users, ages))
print(l[1][1])
print(z)
print(list(z.keys()))
print(list(z.values(

)
           )
      )