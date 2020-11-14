import moyenne
import math

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def test_count_all_stars():
    try:
        m1 = moyenne.moyenne([1.2, 3.2, 3.6, 4.2, 5.7])
        assert math.isclose(m1, 3.58), "Running moyenne([1.2, 3.2, 3.6, 4.2, 5.7])... Expected 3.58, got {}".format(m1)
        m2 = moyenne.moyenne([1, 4, 12, 32])
        assert math.isclose(m2, 12.25), "Running moyenne([1, 4, 12, 32])... Expected 12.25, got {}".format(m2)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

if __name__ == "__main__":
    test_count_all_stars()
