# 📚 NLP Toolkit - Natural Language Processing Tools Collection

Welcome to my **Natural Language Processing (NLP) Toolkit**! This collection includes practical NLP tools for text analysis, keyword extraction, and semantic similarity analysis through hands-on implementations.

## 🎯 Tools & Features

This toolkit includes:

- **Text Preprocessing** and analysis techniques
- **TF-IDF Keyword Analysis** for document importance ranking
- **Word Embeddings & Similarity** using pre-trained models
- **Synonym Finding** with semantic word vectors
- **Tokenization** methods (sentence and word level)
- **Stop word removal** for text cleaning
- **Stemming vs Lemmatization** comparisons

## 🛠️ Technologies Used

### Libraries

- **SpaCy** - Advanced NLP library with pre-trained models
- **NLTK** - Natural Language Toolkit for text processing
- **Gensim** - Topic modeling and word embeddings library
- **Python 3.12+** - Programming language (3.12 recommended for gensim compatibility)

### Models & Data

- **en_core_web_sm** - SpaCy's English language model
- **glove-wiki-gigaword-100** - 128MB GloVe word embeddings for synonym finding
- **NLTK Corpora** - stopwords, wordnet, punkt tokenizers

## 📋 Prerequisites

### For Python 3.12 (Recommended for full compatibility):

```bash
# Create virtual environment with Python 3.12
python3.12 -m venv nlp_env
# On Windows: .\nlp_env\Scripts\Activate.ps1
# On macOS/Linux: source nlp_env/bin/activate

# Install Python packages
pip install spacy nltk gensim

# Download SpaCy English model
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### For Python 3.13:

```bash
# Only basic tools work (gensim may have compatibility issues)
pip install spacy nltk
python -m spacy download en_core_web_sm
```

## 🚀 Usage

### Available Tools

#### 1. **Text Analysis & Comparison** (`nlp_breakdown.py`)

Compare SpaCy vs NLTK processing methods:

```bash
python nlp_breakdown.py
```

#### 2. **TF-IDF Keyword Analysis** (`keyWord_analyze.py`)

Analyze keyword importance across multiple documents:

```bash
python keyWord_analyze.py
```

#### 3. **Synonym Finder** (`gensim-syn.py`)

Find semantically similar words using word embeddings:

```bash
python gensim-syn.py
```

## 🔧 Tool Descriptions

### 1. **nlp_breakdown.py** - Text Analysis Foundation

- **SpaCy vs NLTK comparison** for preprocessing
- **Lemmatization vs Stemming** analysis
- **POS tagging** and linguistic features
- **Stop word filtering** and tokenization

### 2. **keyWord_analyze.py** - TF-IDF Keyword Extraction

- **TF-IDF analysis** across multiple documents
- **Keyword importance ranking**
- **Document similarity comparison**
- **Stop word removal** with spaCy
- Processes multiple text documents to find the most significant terms

### 3. **gensim-syn.py** - Semantic Similarity & Synonyms

- **Word embeddings** using GloVe vectors (128MB model)
- **Synonym finding** with semantic similarity scores
- **Filtered results** (removes contractions and non-words)
- **Real-time word similarity** analysis
- Uses `glove-wiki-gigaword-100` for balanced performance

### Example Input

```
The children were running quickly through the beautiful gardens. They stopped to admire the colorful flowers blooming magnificently.
```

## 📊 What the Script Does

### 1. **SpaCy Analysis**

- Performs **lemmatization** with grammatical context
- Provides **Part-of-Speech tagging**
- Shows word → lemma → POS format

### 2. **NLTK Text Processing**

- **Sentence Tokenization**: Splits text into sentences
- **Word Tokenization**: Breaks sentences into individual words
- **Stop Word Removal**: Filters out common words (the, and, is, etc.)
- **Unique Word Analysis**: Counts distinct meaningful words
- **Shows Removed Words**: Displays filtered-out terms

### 3. **Stemming vs Lemmatization Comparison**

- **Stemming**: Aggressive suffix removal (may create non-words)
- **Lemmatization**: Dictionary-based word reduction (produces real words)

## 🔍 Key Learning Differences

| Aspect       | Stemming              | Lemmatization     |
| ------------ | --------------------- | ----------------- |
| **Speed**    | ⚡ Fast               | 🐌 Slower         |
| **Accuracy** | 📉 Lower              | 📈 Higher         |
| **Output**   | May produce non-words | Always real words |
| **Context**  | Rule-based            | Grammar-aware     |
| **Use Case** | Search engines        | Text analysis     |

### Example Tool Outputs

#### TF-IDF Keyword Analysis

```
Document 1 TF-IDF scores:
  gardens: 0.4521
  flowers: 0.3876
  children: 0.3241
```

#### Synonym Finder Results

```
Enter your word: happy
The synonyms of 'happy' are:
  glad: 0.7833
  good: 0.7822
  proud: 0.7702
```

#### Text Processing Comparisons

- `running` → Stem: `run` vs Lemma: `running`
- `children` → Stem: `children` vs Lemma: `child`
- `quickly` → Stem: `quickli` vs Lemma: `quickly`
- `beautiful` → Stem: `beauti` vs Lemma: `beautiful`

## 📝 Sample Output Structure

```
Using Spacy...
word -> lemma -> POS_TAG

Using NLTK...
Original Sentence: [input text]
Sentence Tokenization: [list of sentences]
Word Tokenization: [list of words]
Filtered Sentence: [words after stop word removal]
Analysis (unique words): [unique content words] -> Count: X
Removed Words: [stop words and punctuation]

===============Stemming==============
word -> stemmed_form

===============Lemmatization==============
word -> lemmatized_form
```

## 📚 Learning Notes

### When to Use What?

- **Stemming**: Information retrieval, search engines, keyword matching
- **Lemmatization**: Sentiment analysis, text classification, language understanding
- **SpaCy**: Complex NLP tasks requiring accuracy and linguistic features
- **NLTK**: Educational purposes, prototyping, basic text processing

### Key Insights

1. **Lemmatization is generally better** for most NLP applications
2. **SpaCy provides richer linguistic information** than basic NLTK processing
3. **Stop word removal is crucial** for focusing on meaningful content
4. **Tokenization is the foundation** of most NLP tasks

## 🎓 Learning Progress

- [x] Basic text tokenization
- [x] Stop word filtering
- [x] Stemming implementation
- [x] Lemmatization comparison
- [x] SpaCy integration
- [x] POS tagging understanding
- [x] **TF-IDF keyword analysis** - _Completed_
- [x] **Word embeddings & similarity** - _Completed_
- [x] **Synonym finding with gensim** - _Completed_
- [ ] Named Entity Recognition (NER) - _Next goal_
- [ ] Text classification - _Future learning_
- [ ] Sentiment analysis - _Planned_

## 🤝 Educational Purpose

This project is part of my journey to understand:

- **Text preprocessing pipelines**
- **NLP library ecosystems**
- **Preprocessing impact on downstream tasks**
- **Performance vs accuracy trade-offs**

## 📞 Notes for Future Development

### Potential Enhancements

- Add **Named Entity Recognition** to existing tools
- Include **dependency parsing** visualization
- Implement **document clustering** with TF-IDF
- Add **n-gram analysis** for phrase detection
- Create **interactive word similarity** exploration
- Include **sentiment analysis** pipeline
- Add **text classification** capabilities
- Implement **topic modeling** with LDA

### Learning Resources Referenced

- SpaCy Documentation
- NLTK Book
- NLP with Python tutorials
- Various NLP research papers

---

**Happy Learning!** 🚀📖

_This project demonstrates fundamental NLP concepts and serves as a foundation for more advanced natural language processing techniques._
