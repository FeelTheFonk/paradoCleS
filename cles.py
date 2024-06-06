import random as r
import pdfplumber
import logging
import math
from spellchecker import SpellChecker  # Assurez-vous d'installer cette bibliothèque

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Définition des symboles ésotériques et des groupes de fichiers PDF associés
SYMBOLS = ['🜁', '🜂', '🜃', '🜄']
PDF_GROUPS = {
    '🜁': ['src/bible.pdf', 'src/coran.pdf'],
    '🜂': ['src/rigveda.pdf', 'src/bhagavadgita.pdf'],
    '🜃': ['src/avesta.pdf', 'src/popolvuh.pdf'],
    '🜄': ['src/tao.pdf', 'src/bardo.pdf', 'src/dhammapada.pdf', 'src/srigourougranthsahib.pdf']
}

# Constantes mystiques
MAX_ATTEMPTS = 112358132134
MAX_POPULATION = 1123
PHI = (1 + math.sqrt(5)) / 2  # Nombre d'or
PI = math.pi

# Fonction pour extraire un texte aléatoire à partir d'un fichier PDF
def extract_random_text(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            num_pages = len(pdf.pages)
            for attempt in range(MAX_ATTEMPTS):
                random_page = r.randint(0, num_pages - 1)
                page = pdf.pages[random_page]
                text = page.extract_text()

                if text:
                    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
                    if sentences:
                        random_sentence = r.choice(sentences)
                        logging.info(f"Phrase sélectionnée de la page {random_page} du fichier {pdf_file}.")
                        return random_sentence

                logging.warning(f"Page {random_page} vide ou illisible dans le fichier {pdf_file}.")

            return "Erreur : Impossible de trouver une page valide après plusieurs tentatives."
    except FileNotFoundError:
        logging.error(f"Erreur : Fichier {pdf_file} introuvable.")
        return f"Erreur : Fichier {pdf_file} introuvable."
    except pdfplumber.PDFSyntaxError:
        logging.error(f"Erreur : Problème de syntaxe dans le fichier {pdf_file}.")
        return f"Erreur : Problème de syntaxe dans le fichier {pdf_file}."
    except Exception as e:
        logging.error(f"Erreur lors de l'extraction du texte : {str(e)}")
        return f"Erreur lors de l'extraction du texte : {str(e)}"

# Fonction pour transformer le texte de manière mystérieuse
def mystical_transformation(text):
    transformations = [
        lambda t: t[::-1],  # Inverser le texte
    ]
    transformation = r.choice(transformations)
    return transformation(text)

# Fonction de nettoyage du texte
def clean_text(text):
    words = text.split()
    cleaned_text = ' '.join(words)
    spell = SpellChecker(language='fr')  # Préciser que la langue est le français
    corrected_words = [spell.correction(word) if word in spell else word for word in cleaned_text.split()]
    corrected_text = ' '.join(corrected_words)
    return corrected_text

# Fonction principale pour exécuter la transmutation
def transmutation(population=int(MAX_POPULATION / PHI)):
    logging.info(f"Début de la transmutation pour une population de {population}")

    # Sélection aléatoire des symboles
    chosen_symbols = [r.choice(SYMBOLS) for _ in range(population)]
    symbol_counts = {sym: chosen_symbols.count(sym) for sym in SYMBOLS}
    major_symbol = max(symbol_counts, key=symbol_counts.get)
    logging.info(f"Symbole majoritaire : {major_symbol}")

    # Sélection du premier fichier PDF basé sur le symbole majoritaire
    pdf_list_1 = PDF_GROUPS[major_symbol]
    pdf_file_1 = r.choice(pdf_list_1)
    logging.info(f"Premier PDF sélectionné : {pdf_file_1}")

    # Sélection d'un deuxième symbole différent du premier pour plus de diversité
    other_symbol = r.choice([sym for sym in SYMBOLS if sym != major_symbol])
    pdf_list_2 = PDF_GROUPS[other_symbol]
    pdf_file_2 = r.choice(pdf_list_2)
    logging.info(f"Deuxième PDF sélectionné : {pdf_file_2}")

    # Extraction de textes aléatoires des deux fichiers PDF sélectionnés
    text_1 = extract_random_text(pdf_file_1)
    text_2 = extract_random_text(pdf_file_2)

    # Combinaison et transformation des textes pour obtenir un message final
    final_message = mystical_transformation(text_1 + " " + text_2)

    # Nettoyage du message final
    cleaned_message = clean_text(final_message)

    # Affichage des résultats
    logging.info(f"Message Mystique : {final_message}")
    logging.info(f"Message Mystique Nettoyé : {cleaned_message}")

    print(f"Population : {population}")
    for sym, count in symbol_counts.items():
        print(f"{sym} : {count}")
    print(f"Symbole majoritaire : {major_symbol}")
    print(f"Premier PDF : {pdf_file_1}")
    print(f"Deuxième PDF : {pdf_file_2}")
    print(f"Message Mystique : {final_message}")
    print(f"Message Mystique Nettoyé : {cleaned_message}")

# Exécution de la transmutation
if __name__ == "__main__":
    transmutation()
