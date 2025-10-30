import streamlit as st

st.set_page_config(page_title="Bio Data", page_icon=":bust_in_silhouette:", layout="centered")

st.title("Bio Data")

# Consolidated styling (single block)
st.markdown("""
<style>
body {
    background-color: #f0f2f5;
}
h1, h2, h3, h4, h5, h6 {
    color: #333;
}
img {
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
""", unsafe_allow_html=True)

st.write("**Name:** K. Srilatha")
st.write("**Age:** 36")
st.write("**Gender:** Female")
st.write("**Country:** India")
st.write("**Education:** M.Tech in computer science")
st.write("**Profession:** Assistant Professor in computer science")
st.write("**Hobbies:** reading books, cooking, gardening")
st.write("**Favorite Food:** biryani, sweets")
st.write("**Favorite Movie:** Inception, The Shawshank Redemption")

st.header("Contact Information")
st.write("**Email:** k.srilatha@example.com")
st.write("**Phone:** +91-9876543210")
st.image("https://example.com/profile_picture.jpg", caption="Profile Picture")
