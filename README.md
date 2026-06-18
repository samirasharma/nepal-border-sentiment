# Nepal Border Sentiment Analysis

Fine-tuned XLM-RoBERTa on Nepali/English YouTube comments about the Nepal–India border dispute.

## Results
- 71% accuracy on gold-standard eval set (300 manually verified comments)
- 3-class classification: positive / neutral / negative

## Pipeline
1. Scrape comments from 17 Nepali YouTube news channels (youtube-comment-downloader)
2. Translate Nepali → English (google-translator)
3. Auto-label with multilingual sentiment model (silver standard)
4. Manually verify 300 samples (gold standard)
5. Fine-tune XLM-RoBERTa

## Dataset
[Link to HuggingFace dataset coming soon]

## Model
[Link to HuggingFace model coming soon]

## Limitations
Single annotator. Small dataset (~2100 comments). Translation quality varies for Nepali slang.

Contributions welcome — see Issues to contribute labels.
