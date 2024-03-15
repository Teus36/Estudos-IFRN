let objeto = [ {
    raio: 5,
    altura: 30,
    },
    {
    raio: 4,
    altura: 12,
    },
    {
    raio: 10,
    altura: 7,
    }
]

for (i = 0; i < 3; i++) {
    const V = Math.PI * objeto[i].raio **2 * objeto[i].altura
    console.log(V.toFixed(2))
}