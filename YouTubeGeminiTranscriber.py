import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API with the API key
genai.configure(api_key="GOOGLE_API_KEY")

# Prompt for summarization
prompt = """You are a YouTube video summarizer. You will take the transcript text 
and summarize the entire video, providing the important points in a summary 
within 250 words. Please provide the summary of the text given here: """

# Function to extract transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        
        # Fetch the transcript for the given video ID
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine transcript text into a single string
        transcript = " ".join([entry["text"] for entry in transcript_data])

        return transcript

    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None
    
# Function to generate summary based on the transcript using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# Streamlit app layout
st.set_page_config(page_title="YouTube Transcript Summarizer", layout="wide")

# Header
st.title("🎥 YouTube Video Transcript Summarizer")
st.write("Enter the YouTube video link below to get a summarized version of the transcript.")

# Input Section
with st.expander("Enter YouTube Video Link", expanded=True):
    youtube_link = st.text_input("YouTube Video URL:", placeholder="e.g., https://www.youtube.com/watch?v=XYZ123")

# Thumbnail display
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to get detailed notes
if st.button("Get Detailed Notes", key="get_notes"):
    if youtube_link:
        with st.spinner("Fetching transcript..."):
            transcript_text = extract_transcript_details(youtube_link)

            if transcript_text:
                with st.spinner("Generating summary..."):
                    summary = generate_gemini_content(transcript_text, prompt)
                    if summary:
                        st.markdown("## 📝 Detailed Notes:")
                        st.write(summary)
            else:
                st.error("No transcript available.")
    else:
        st.error("Please enter a valid YouTube video link.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Gamze Akkurt")
