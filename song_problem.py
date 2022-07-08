# Dado uma lista de musicas, o indice representa a musica, e o valor representa
# a duracao em segundos. Um ouvinte so pode escolher musicas em pares para ouvir
# com a restricao que a duracao da soma do par seja multiplo de 60. (60, 120, ...)
# Com isso, retorne a quantidade de pares de musicas possiveis para escutar dado uma
# lista dessas musicas.
# Ex:
# song durations: [20, 80, 40] -> returns 2: (20, 40)=60, (80, 40)=120

# how many pairs of duration 60 or multiples?

# Write your code here
# [20, 100, 80, 40] -> (20, 100), (40, 20) == (20, 40), (100, 80), (80, 40)
# d = {0: []}
# {20, 80} * {100, 40}

def how_many_songs(songs):
    sum_ = 0
    for i, song1 in enumerate(songs[:-1]):
        for song2 in songs[i + 1:]:
            if (song1 + song2) % 60 == 0:
                sum_ += 1
    return sum_


def count_songs(songs):
    sum_ = 0
    especial = 0
    for song1, song2 in zip(songs[:-1], songs[1:]):
        if (song1 + song2) % 60 == 0:
            sum_ += 1 + especial
        if song1*2 % 60 == 0:
            especial += 1
    print(sum_)
    return sum_


def main():
    songs = [30, 30, 30, 30]
    assert count_songs(songs) == 6

    songs = [20, 100, 80, 40]
    assert count_songs(songs) == 4


if __name__ == '__main__':
    main()
