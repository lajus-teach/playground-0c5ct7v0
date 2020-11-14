from yoda import yodaification

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        dup1 = yodaification("Tu devras faire tous les exercices")
        assert dup1.upper() == 'faire tous les exercices Tu devras'.upper(), "Running yodaification('Tu devras faire tous les exercices')... Expected 'faire tous les exercices Tu devras', got {}".format(dup1)
        dup2 = yodaification("ça ne marche pas à tous les coups")
        assert dup2.upper() == 'marche pas à tous les coups ça ne'.upper(), "Running yodaification('ça ne marche pas à tous les coups')... Expected 'marche pas à tous les coups ça ne', got {}".format(dup2)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

if __name__ == "__main__":
    test_count_all_stars()
