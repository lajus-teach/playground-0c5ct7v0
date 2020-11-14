import carre_magique

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def test_carre_magique():
    
    ligne_ok = [
        [1, 2],
        [1, 2]
    ]
    
    ligne_col_ok = [
        [1, 2],
        [2, 1]
    ]
    
    col_ok = [
        [1, 1],
        [2, 2]
    ]
    
    carre3 = [
        [2, 7, 3],
        [9, 5, 1],
        [4, 3, 8]
    ]

    carre4 = [
        [4, 5, 11, 14],
        [15, 10, 8, 1],
        [6, 3, 13, 12],
        [9, 16, 2, 7]
    ]
    
    carre5 = [
        [11, 24, 7, 20, 3],
        [4, 12, 25, 8, 16],
        [17, 5, 13, 21, 9],
        [10, 18, 1, 14, 22],
        [23, 6, 19, 2, 15]
    ]

    try:
        assert carre_magique.lignes_magiques(ligne_ok), "Running lignes_magiques(%s), expected True got %s" % (str(ligne_ok), str(carre_magique.lignes_magiques(ligne_ok)))
        assert carre_magique.lignes_magiques(ligne_col_ok), "Running lignes_magiques(%s), expected True got %s" % (str(ligne_col_ok), str(carre_magique.lignes_magiques(ligne_col_ok)))
        assert not carre_magique.lignes_magiques(col_ok), "Running lignes_magiques(%s), expected False got %s" % (str(col_ok), str(carre_magique.lignes_magiques(col_ok)))
        assert carre_magique.lignes_magiques(carre3), "Running lignes_magiques(%s), expected True got %s" % (str(carre3), str(carre_magique.lignes_magiques(carre3)))
        assert carre_magique.lignes_magiques(carre4), "Running lignes_magiques(%s), expected True got %s" % (str(carre4), str(carre_magique.lignes_magiques(carre4)))
        assert carre_magique.lignes_magiques(carre5), "Running lignes_magiques(%s), expected True got %s" % (str(carre5), str(carre_magique.lignes_magiques(carre5)))
        send_msg("Progression", "La fonction lignes_magiques semble correcte.")
        
        assert carre_magique.somme_colonne(ligne_ok, 0) == 2, "Running somme_colonne(%s, 0), expected 2 got %s" % (str(ligne_ok), str(carre_magique.somme_colonne(ligne_ok, 0)))
        assert carre_magique.somme_colonne(ligne_ok, 1) == 4, "Running somme_colonne(%s, 1), expected 4 got %s" % (str(ligne_ok), str(carre_magique.somme_colonne(ligne_ok, 1)))
        assert carre_magique.somme_colonne(ligne_col_ok, 0) == 3, "Running somme_colonne(%s, 0), expected 3 got %s" % (str(ligne_col_ok), str(carre_magique.somme_colonne(ligne_col_ok, 0)))
        assert carre_magique.somme_colonne(ligne_col_ok, 1) == 3, "Running somme_colonne(%s, 1), expected 3 got %s" % (str(ligne_col_ok), str(carre_magique.somme_colonne(ligne_col_ok, 1)))
        assert carre_magique.somme_colonne(col_ok, 0) == 3, "Running somme_colonne(%s, 0), expected 3 got %s" % (str(col_ok), str(carre_magique.somme_colonne(col_ok, 0)))
        assert carre_magique.somme_colonne(col_ok, 1) == 3, "Running somme_colonne(%s, 1), expected 3 got %s" % (str(col_ok), str(carre_magique.somme_colonne(col_ok, 1)))
        
        assert carre_magique.somme_colonne(carre3, 0) == 12, "Running somme_colonne(%s, 0), expected 12 got %s" % (str(carre3), str(carre_magique.somme_colonne(carre3, 0)))
        assert carre_magique.somme_colonne(carre4, 0) == 34, "Running somme_colonne(%s, 0), expected 34 got %s" % (str(carre4), str(carre_magique.somme_colonne(carre4, 0)))
        assert carre_magique.somme_colonne(carre5, 0) == 65, "Running somme_colonne(%s, 0), expected 64 got %s" % (str(carre4), str(carre_magique.somme_colonne(carre4, 0)))
        send_msg("Progression", "La fonction somme_colonne semble correcte.")
        
        assert not carre_magique.est_magique(ligne_ok), "Running est_magique(%s), expected False got %s" % (str(ligne_ok), str(carre_magique.est_magique(ligne_ok)))
        assert not carre_magique.est_magique(ligne_col_ok), "Running est_magique(%s), expected False got %s" % (str(ligne_col_ok), str(carre_magique.est_magique(ligne_col_ok)))
        assert not carre_magique.est_magique(col_ok), "Running est_magique(%s), expected False got %s" % (str(col_ok), str(carre_magique.est_magique(col_ok)))
        assert carre_magique.est_magique(carre3), "Running est_magique(%s), expected True got %s" % (str(carre3), str(carre_magique.est_magique(carre3)))
        assert carre_magique.est_magique(carre4), "Running est_magique(%s), expected True got %s" % (str(carre4), str(carre_magique.est_magique(carre4)))
        assert carre_magique.est_magique(carre5), "Running est_magique(%s), expected True got %s" % (str(carre5), str(carre_magique.est_magique(carre5)))
        send_msg("Progression", "La fonction est_magique semble correcte.")
        
        success()

        send_msg("Bien joué !", "")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
    except AttributeError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint", "Il faut définir cette fonction.")

if __name__ == "__main__":
    test_carre_magique()
