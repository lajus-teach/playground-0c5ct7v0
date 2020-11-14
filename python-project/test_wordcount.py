from wordcount import word_count

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        dup1 = word_count("May the Force be with you, Luke!")
        assert dup1 == 7, "Running word_count('May the Force be with you, Luke!')... Expected 7, got {}".format(dup1)
        dup2 = word_count("C'est la chenille qui redémarre !")
        assert dup2 == 6, "Running word_count('C'est la chenille qui redémarre !')... Expected 6, got {}".format(dup2)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

if __name__ == "__main__":
    test_count_all_stars()
