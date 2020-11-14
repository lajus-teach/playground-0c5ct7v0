from permutation_list import panne_moteur, passe_en_tete, sauve_honneur, tir_blaster, retour_inattendu

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_permutation():
    try:
        classement = ['Gasgano', 'Teemto', 'Sebulba', 'Anakin']
        panne_moteur(classement)
        assert classement == ['Teemto', 'Sebulba', 'Anakin', 'Gasgano'], "Running panne_moteur(['Gasgano', 'Teemto', 'Sebulba', 'Anakin'])... List should now be ['Teemto', 'Sebulba', 'Anakin', 'Gasgano'], got {}".format(classement)
        tir_blaster(classement)
        assert classement == ['Sebulba', 'Anakin', 'Gasgano'], "Running tir_blaster(['Teemto', 'Sebulba', 'Anakin', 'Gasgano'])... List should now be ['Sebulba', 'Anakin', 'Gasgano'], got {}".format(classement)
        passe_en_tete(classement)
        assert classement == ['Anakin', 'Sebulba', 'Gasgano'], "Running passe_en_tete(['Sebulba', 'Anakin', 'Gasgano'])... List should now be ['Anakin', 'Sebulba', 'Gasgano'], got {}".format(classement)
        tir_blaster(classement)
        assert classement == ['Sebulba', 'Gasgano'], "Running tir_blaster(['Anakin', 'Sebulba', 'Gasgano'])... List should now be ['Sebulba', 'Gasgano'], got {}".format(classement)
        retour_inattendu(classement, 'Anakin')
        assert classement == ['Sebulba', 'Gasgano', 'Anakin'], "Running retour_inattendu(['Sebulba', 'Gasgano'], 'Anakin')... List should now be ['Sebulba', 'Gasgano', 'Anakin'], got {}".format(classement)
        sauve_honneur(classement)
        assert classement == ['Sebulba', 'Anakin', 'Gasgano'], "Running sauve_honneur(['Sebulba', 'Gasgano', 'Anakin'])... List should now be ['Sebulba', 'Anakin', 'Gasgano'], got {}".format(classement)
        retour_inattendu(classement, 'Boles')
        assert classement == ['Sebulba', 'Anakin', 'Gasgano', 'Boles'], "Running retour_inattendu(['Sebulba', 'Anakin', 'Gasgano'], 'Boles')... List should now be ['Sebulba', 'Anakin', 'Gasgano', 'Boles'], got {}".format(classement)
        passe_en_tete(classement)
        assert classement == ['Anakin', 'Sebulba', 'Gasgano', 'Boles'], "Running passe_en_tete(['Sebulba', 'Anakin', 'Gasgano', 'Boles'])... List should now be ['Anakin', 'Sebulba', 'Gasgano', 'Boles'], got {}".format(classement)
        sauve_honneur(classement)
        assert classement == ['Anakin', 'Sebulba', 'Boles', 'Gasgano'], "Running sauve_honneur(['Anakin', 'Sebulba', 'Gasgano', 'Boles'])... List should now be ['Anakin', 'Sebulba', 'Boles', 'Gasgano'], got {}".format(classement)
        
        success()
        send_msg("Bien joué !", "Quelle course !")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint", "Pense à bien modifier la liste passée en argument.")

if __name__ == "__main__":
    test_permutation()
