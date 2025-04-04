from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from summarizer_utils import summarize_with_gemini
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

def extract_video_id(url: str) -> str:
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        return parse_qs(query.query).get("v", [None])[0]
    return None

@app.get("/summarize")
async def summarize_youtube_video(url: str = Query(...)):
    video_id = extract_video_id(url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        context = " ".join([entry['text'] for entry in transcript])
        summary = summarize_with_gemini(context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse(content={"summary": summary})
