from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

def analyze_text(text):
    words = text.split()
    
    word_count = len(words)
    char_count = len(text)
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    
    longest_word = max(words, key=len) if words else ""
    
    reversed_text = text[::-1]
    
    # Frequent words
    freq = Counter(words)
    top_words = freq.most_common(3)
    
    # Palindromes
    palindromes = [w for w in words if w.lower() == w[::-1].lower() and len(w) > 1]

    return {
        "word_count": word_count,
        "char_count": char_count,
        "vowels": vowels,
        "longest_word": longest_word,
        "reversed_text": reversed_text,
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "top_words": top_words,
        "palindromes": palindromes
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        text = request.form['text']
        result = analyze_text(text)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)