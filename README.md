
# YouTube Transcript Summarizer Powered by Gemini Pro

![YouTube Video Summarizer](https://img.shields.io/badge/Python-3.7%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-orange) 

## Overview
**YouTube Transcript Summarizer Powered by Gemini Pro** is a Python-based application that transcribes YouTube videos and generates concise summaries using the power of large language models (LLMs) through Google Gemini Pro. This app simplifies long video content by providing transcriptions and key insights in just a few steps.
## Project Interface
<img width="1475" alt="Screenshot 2024-10-24 at 18 06 51" src="https://github.com/user-attachments/assets/6081ae22-d310-45b6-bc48-f7e052ff4c4b">

## Features
- **Transcription**: Automatically fetches video transcripts for YouTube videos.
- **Summarization**: Uses Google Gemini Pro to generate concise summaries of the transcripts.
- **User-Friendly Interface**: Built with Streamlit, offering an intuitive and interactive experience.
- **Thumbnail Display**: Shows video thumbnail for better context.

## Technologies Used
- **Python**: Main programming language.
- **Streamlit**: Framework for building web applications.
- **youtube-transcript-api**: Library for fetching transcripts from YouTube videos.
- **Google Gemini Pro**: AI service for generating text summaries.

## Installation

### Prerequisites
- Python 3.7 or higher
- A Google API key for accessing Google Gemini Pro

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/gamzeakkurt/YouTubeGeminiTranscriber.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd YouTube-Transcript-Summarizer
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   conda activate env # On Mac use
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your Google API key**:
   - Create a `.env` file in the project root and add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run YouTubeGeminiTranscriber.py
   ```

2. **Open your web browser** and go to `http://localhost:8501` to access the application.

3. **Enter a YouTube video link** in the provided input field and click on "Get Detailed Notes" to fetch the transcript and receive a summarized version of the content.

## Example
- **Input**: YouTube URL of a video (e.g., a tutorial or lecture).
- **Output**: Transcription and a concise summary of key points.

## Contributing
Contributions are welcome! Feel free to fork the repository, open issues, and submit pull requests to help enhance this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



---

**Enjoy summarizing your favorite YouTube videos with ease!**
