czstats = { "A":0.09589269,
            "B":0.0177612,
            "C":0.02999077,
            "D":0.03774841,
            "E":0.10904081,
            "F":0.0017506,
            "G":0.00219812,
            "H":0.02497482,
            "I":0.06686138,
            "J":0.02305759,
            "K":0.03528082,
            "L":0.05720782,
            "M":0.0360545,
            "N":0.05917244,
            "O":0.08029999,
            "P":0.03114961,
            "Q":0.00005933,
            "R":0.04396827,
            "S":0.0558597,
            "T":0.05385289,
            "U":0.03579031,
            "V":0.03952464,
            "W":0.00054266,
            "X":0.0003591,
            "Y":0.02857512,
            "Z":0.03302643,}

encodekey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()


def getstats(arg):
    slovnik = {}

    for x in encodekey:
        slovnik[x] = 0

    for x in arg:
        if x in slovnik:
            slovnik[x] += 1

    for x in slovnik:
        slovnik[x] = slovnik[x] / len(encodekey)
        print(slovnik)

    return slovnik


def porovnanistat(stat1, stat2):
    stat3 = {}
    vysledek = 0

    for x in encodekey:
        stat3[x] = abs(stat1[x] - stat2[x])

    for x in encodekey:
        vysledek += stat3[x]

    return vysledek


def posunutitextu(arg):
    text2 = ''

    for x in arg:
        try:
            text2 += encodekey[encodekey.find(x) + 1]
        except:
            text2 += encodekey[0]
    return text2


def main():
    finaltext = ''
    textscore = 100
    newtext = text

    for x in range(0,len(encodekey)):
        newtext = posunutitextu(newtext)
        score = porovnanistat(getstats(newtext), czstats)

        if score < textscore:
            textscore = score
            finaltext = newtext

    print(finaltext)


main()
