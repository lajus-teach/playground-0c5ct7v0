from duplicate import find_duplicate

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        dup1 = find_duplicate(["Order 66", "Order 66"])
        assert dup1 == "Order 66", "Running find_duplicate(['Order 66', 'Order 66'])... Expected 'Order 66', got {}".format(dup1)
        dup2 = find_duplicate(["Only hope", "Order 66", "Order 66", "Obiwan Kenobi"])
        assert dup2 == "Order 66", "Running find_duplicate(['Only hope', 'Order 66', 'Order 66', 'Obiwan Kenobi'])... Expected 'Order 66', got {}".format(dup2)
        dup3 = find_duplicate([2, 3, 1, 0, 1, 12])
        assert dup3 == 1, "Running find_duplicate([2, 3, 1, 0, 1, 12])... Expected 1, got {}".format(dup3)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "L'élément apparaît-il dans le reste de la liste ?")

if __name__ == "__main__":
    test_count_all_stars()
