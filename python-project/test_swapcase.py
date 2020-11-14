import swapcase

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_permutation():
    try:
        s = swapcase.swapcase('abc')
        assert s == 'ABC', "Running  swapcase('abc')... Expected 'ABC', got {}".format(s)
        s = swapcase.swapcase('ABC')
        assert s == 'abc', "Running  swapcase('ABC')... Expected 'abc', got {}".format(s)
        s = swapcase.swapcase('abcABC')
        assert s == 'ABCabc', "Running  swapcase('abcABC')... Expected 'ABCabc', got {}".format(s)
        s = swapcase.swapcase('! abcABC, h!')
        assert s == '! ABCabc, H!', "Running  swapcase('! abcABC, h!')... Expected '! ABCabc, H!', got {}".format(s)
        
        s = swapcase.swapcase('ça A été')
        assert s == 'ÇA a ÉTÉ', "Running  swapcase('ça A été')... Expected 'ÇA a ÉTÉ', got {}".format(s)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

if __name__ == "__main__":
    test_permutation()
