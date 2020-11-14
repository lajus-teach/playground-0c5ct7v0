from universe import count_all_stars
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        count1 = count_all_stars([2, 3])
        assert count1 == 5, "Running count_all_stars([2, 3])... Expected 5, got {}".format(count1)
        count2 = count_all_stars([9, 4, 8, 7])
        assert count2 == 28, "Running count_all_stars([9, 4, 8, 7])... Expected 28, got {}".format(count2)
        success()

        if sum_builtin_used:
            send_msg("Bien joué", "")
        else:
            send_msg("C'est tout bon, mais...", "Tu peux aussi utiliser directement la fonction sum.")
            send_msg("C'est tout bon, mais...", "Essaye donc:")
            send_msg("C'est tout bon, mais...", "")
            send_msg("C'est tout bon, mais...", "galaxies = [37, 3, 2]")
            send_msg("C'est tout bon, mais...", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Ajoute le nombre d'étoile de chaque galaxie à la variable total_stars.")

if __name__ == "__main__":
    test_count_all_stars()
