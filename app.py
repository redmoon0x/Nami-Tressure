import streamlit as st
from googlesearch import search
from urllib.parse import urlparse, unquote

# Function to perform a Google search using googlesearch-python
def google_dork_search(query, num_results=10):
    try:
        search_results = search(query, num_results=num_results, lang="en")
        return list(search_results)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Function to extract PDF name from URL
def extract_pdf_name(url):
    path = urlparse(url).path
    filename = unquote(path.split('/')[-1])
    if filename.endswith('.pdf'):
        return filename
    else:
        return "Unknown PDF"

# Streamlit App
def main():
    st.set_page_config(page_title="Nami's Library", layout="wide")
    st.title("📚 Nami's Library: Discover PDF Books")

    with st.form("book_search"):
        book_title = st.text_input("Enter the book title:", help="Type the title of the book you want to find.")
        submitted = st.form_submit_button("Search")

    if submitted and book_title:
        with st.spinner('Searching for treasure... 🗺️'):
            google_dork_query = f'intitle:"{book_title}" filetype:pdf'
            urls = google_dork_search(google_dork_query)
            if urls:
                st.success(f"Found {len(urls)} treasures!")
                for i, url in enumerate(urls, start=1):
                    pdf_name = extract_pdf_name(url)
                    st.write(f"{i}. **{pdf_name}** - [Download PDF]({url})")
            else:
                st.error("No treasures found. Try adjusting your map!")

if __name__ == "__main__":
    main()
