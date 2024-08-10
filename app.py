import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
import random

def google_pdf_search(query, num_results=10):
    # Delay to mimic human behavior and avoid rapid request detection
    time.sleep(random.uniform(1, 3))
    
    search_url = f"https://www.google.com/search?q=filetype:pdf+{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        g_results = soup.find_all('div', class_='g')
        
        for g in g_results[:num_results]:  # Limit the number of results
            link = g.find('a', href=True)
            title = g.find('h3')
            if link and title:
                href = link['href']
                url = href.split("&")[0].split("?q=")[-1]
                results.append((title.text, url))
        
        return results
    else:
        return []

def main():
    st.set_page_config(page_title="Nami's Library", layout="wide")
    st.title("📚 Nami's Library: Discover PDF Books")
    st.subheader("Explore a vast collection of PDF books across the web")

    query = st.text_input("Enter your search query for PDFs:", help="Search for PDF books by titles, authors, or topics.")

    if st.button("Search PDFs"):
        if query:
            with st.spinner("🔎 Searching PDFs across the web... Please wait."):
                results = google_pdf_search(query)
            if results:
                st.success(f"✨ Found {len(results)} results:")
                for title, link in results:
                    st.markdown(f"[{title}]({link})", unsafe_allow_html=True)
            else:
                st.warning("🚫 No results found. Try a different query.")
        else:
            st.warning("⚠️ Please enter a query to begin searching.")

    # Add an animated footer with the creator's name
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: black;
            animation: fadeInAnimation ease 3s;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
        }
        @keyframes fadeInAnimation {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        </style>
        <div class="footer">
        Created by Deviprasad Shetty
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
