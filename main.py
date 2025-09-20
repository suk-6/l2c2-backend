from konlpy.tag import Okt


def main():
    okt = Okt()
    text = "나는 학교에 간다. 학교가 끝나면 다시 집에 간다."
    print("morphs:", okt.morphs(text))
    print("nouns:", okt.nouns(text))
    print("phrases:", okt.phrases(text))
    print("pos:", okt.pos(text))


if __name__ == "__main__":
    main()
