from permutation import panne_moteur, passe_en_tete, sauve_honneur

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_permutation():
    try:
        classement = ('Gasgano', 'Sebulba', 'Anakin')
        panne = panne_moteur(classement)
        assert panne == ('Sebulba', 'Anakin', 'Gasgano'), "Running panne_moteur(('Gasgano', 'Sebulba', 'Anakin'))... Expected ('Sebulba', 'Anakin', 'Gasgano'), got {}".format(panne)
        en_tete = passe_en_tete(panne)
        assert en_tete == ('Anakin', 'Sebulba', 'Gasgano'), "Running passe_en_tete(('Sebulba', 'Anakin', 'Gasgano'))... Expected ('Anakin', 'Sebulba', 'Gasgano'), got {}".format(en_tete)
        fin = sauve_honneur(en_tete)
        assert fin == ('Anakin', 'Gasgano', 'Sebulba'), "Running sauve_honneur(('Anakin', 'Sebulba', 'Gasgano'))... Expected ('Anakin', 'Gasgano', 'Sebulba'), got {}".format(fin)
        
        classement = (1, 2, 3)
        panne = panne_moteur(classement)
        assert panne == (2, 3, 1), "Running panne_moteur((1, 2, 3))... Expected (2, 3, 1), got {}".format(panne)
        en_tete = passe_en_tete(classement)
        assert en_tete == (2, 1, 3), "Running passe_en_tete((1, 2, 3))... Expected (2, 1, 3), got {}".format(en_tete)
        fin = sauve_honneur(classement)
        assert fin == (1, 3, 2), "Running sauve_honneur((1, 2, 3))... Expected (1, 3, 2), got {}".format(fin)
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)

if __name__ == "__main__":
    test_permutation()
