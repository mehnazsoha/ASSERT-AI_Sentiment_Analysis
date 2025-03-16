# ASSERT

## AI Sentiment Analysis for Post Approval

This snippet integrates a **FastAPI-based Sentiment Analysis API** with a **Node.js application** to approve or reject posts based on sentiment automatically.

## **Features**
✅ FastAPI server for sentiment analysis  
✅ Uses **TextBlob** for sentiment classification  
✅ Node.js client to communicate with the API  
✅ Approves **positive/neutral** posts, forwards **negative** posts for admin approval  

---

## **Install Dependencies**
pip install fastapi uvicorn textblob

python3 -m textblob.download_corpora [Download required corpora]

npm install axios [Node.js Dependencies]

## **Run the FastAPI Server**
uvicorn sentiment_api:app --host 0.0.0.0 --port 8000 --reload

## **Run the Node.js Client**
node analyzePost.js
