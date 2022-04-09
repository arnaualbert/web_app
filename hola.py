from webbrowser import get
from flask import Flask, render_template
import random
from flask import request


app = Flask(__name__)


@app.route("/")

def index():
    
    dna = request.args.get("1","")

    if dna:
        count = get_dna_nucleotides(dna)
    else:
        count="put a sequence to get the number of nucleotides"

    adn = request.args.get("2","")

    if adn:
        transcription = get_transcription(adn)
    else:
        transcription="Put a sequence to get the treanscription to rna"
    
    fasta = request.args.get("3","")

    if fasta:
        reverse_fasta = get_complement(fasta)
    else:
        reverse_fasta="Put a sequence to get the complement"

    data={'dna':count,'adn':transcription,'fasta':reverse_fasta}
    return render_template('index.html',data=data)


def get_dna_nucleotides(dna: str):

    # count the total of each base
    a = dna.count('A')
    t = dna.count('T')
    c = dna.count('C')
    g = dna.count('G')

    return (f'A = {a} C = {c} G = {g} T = {t}')

def get_transcription(adn: str):

    # change the T to U
    transcription = adn.replace('T','U')

    return transcription

def get_complement(fasta: str):

    # reverse de bases i mean from left to right to right to left
    fasta = reversed(fasta)
    # create the complement 
    reverse_fasta = ''
    for base in fasta:
        if base == 'A':
            reverse_fasta += 'T'
        elif base == 'T':
            reverse_fasta += 'A'
        elif base == 'G':
            reverse_fasta += 'C'
        else:
            reverse_fasta += 'G'

    return reverse_fasta




if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # app.run(host="127.0.0.1", port=8080, debug=True)