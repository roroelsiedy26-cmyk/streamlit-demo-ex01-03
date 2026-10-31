import streamlit as st

# Page Configuration
st.set_page_config(page_title="Personal CV Builder", page_icon="📄", layout="centered")

st.title("📄 Personal CV Generator App")
st.markdown("Fill out your personal details below to instantly generate a clean, professional **Markdown Profile Card**.")

# Message Box 1: Info Box
st.info("💡 **Tip:** Complete the fields below and click **Show My CV** to render your profile card.")

# --- Widgets (At least 5 different widget types used here) ---
# 1. text_input
name = st.text_input("Full Name", "Alex Smith")

# 2. number_input
age = st.number_input("Age", min_value=16, max_value=100, value=23)

# 3. selectbox
major = st.selectbox("Major / Field of Study", [
    "Computer Science", 
    "Data Science & AI", 
    "Software Engineering", 
    "Information Systems", 
    "Cybersecurity"
])

# 4. slider
gpa = st.slider("GPA (out of 4.0)", min_value=0.0, max_value=4.0, value=3.85, step=0.01)

# 5. text_area
bio = st.text_area(
    "Short Bio & Summary", 
    "An ambitious student passionate about software development, data analytics, and building user-friendly applications."
)

# 6. button (Triggers visible output)
generate_btn = st.button("Show My CV")

# --- Output Logic ---
if generate_btn:
    # Message Box 2: Success Box
    st.success("🎉 CV Generated Successfully!")
    
    st.markdown("---")
    
    # st.markdown section with real formatting (Headers, bold text, lists, blockquotes)
    st.markdown(f"""
    ### 🎓 Professional Profile Card
    
    * **Name:** **{name}**
    * **Age:** {age}
    * **Major:** *{major}*
    * **GPA:** `{gpa} / 4.0`
    
    #### 📝 Bio & Overview
    > {bio}
    
    #### 🚀 Core Highlights
    * Dedicated academic background in {major}.
    * Proven capability in designing interactive Python applications.
    * Eager to collaborate on innovative tech projects.
    """)
