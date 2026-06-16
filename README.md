# Convolyser AI Copilot

An AI-powered conversation intelligence system inspired by Convolyser.

This project analyzes customer conversations to extract meaningful business insights such as sentiment, competitor mentions, and root causes of customer complaints.

## Features

### 1. Sentiment Analysis

Uses Hugging Face Transformers to classify customer sentiment.

Example:

Input:
I am unhappy with your service.

Output:
NEGATIVE (99%)

---

### 2. Competitor Detection (Rule-Based)

Detects known competitors mentioned in customer conversations.

Example:

Input:
I am moving to Airtel.

Output:
Competitor Detected: Airtel

---

### 3. Competitor Detection using NER

Uses Named Entity Recognition (NER) to identify organization names dynamically.

Example:

Input:
I am switching to Google.

Output:
Organization Detected: Google

---

### 4. AI-Based Root Cause Detection

Uses Zero-Shot Classification to identify probable causes behind customer complaints.

Example:

Input:
My internet is slow and support never responds.

Output:

Support Issue: 61%
Technical Issue: 23%
Network Issue: 12%

---

## Tech Stack

* Python
* Hugging Face Transformers
* PyTorch
* Git
* GitHub

---

## Current Project Structure

```text
Convolyser-AI-Copilot
│
├── app
│   ├── sentiment.py
│   ├── competitor_detection.py
│   ├── ner_competitor_detection.py
│   ├── root_cause_ai.py
│   └── conversation_analyzer.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Upcoming Features

* Hybrid Root Cause Detection
* Unified Conversation Analyzer
* Churn Risk Prediction
* Business Insight Dashboard

## Objective

The goal of this project is to build a conversation intelligence platform that can help organizations understand customer sentiment, identify churn risks, detect competitors, and uncover root causes behind customer complaints.

Built as an AIML learning project inspired by Convolyser.

