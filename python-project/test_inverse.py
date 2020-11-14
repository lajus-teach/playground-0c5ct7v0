from inverse import inverse_couples

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        dup1 = inverse_couples([('Obiwan', 'Anakin'), ('Yoda', 'Luke')])
        assert dup1 == [('Anakin', 'Obiwan'), ('Luke', 'Yoda')], "Running inverse_couples([('Obiwan', 'Anakin'), ('Yoda', 'Luke')])... Expected [('Anakin', 'Obiwan'), ('Luke', 'Yoda')], got {}".format(dup1)
        dup3 = inverse_couples([(2, 3), (1, 0), (1, 12)])
        assert dup3 == [(3, 2), (0, 1), (12, 1)], "Running inverse_couples([(2, 3), (1, 0), (1, 12)])... Expected [(3, 2), (0, 1), (12, 1)], got {}".format(dup3)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Utilise le tuple matching pour itérer sur les couples.")

if __name__ == "__main__":
    test_count_all_stars()
