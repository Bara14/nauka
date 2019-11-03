class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()

X[6]

for i in range(5):
    print(X[i], end= ' ')nor