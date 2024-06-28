import streamlit as st

# Custom CSS for styling (including button styling)
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        .container {
            display: flex;
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            height: 100vh; /* Full viewport height */
            padding: 2rem;
        }
        .section {
            margin-bottom: 2rem;
            width: 50%;
            text-align: center; /* Center text */
        }
        .section-header {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section-content {
            font-size: 1.1rem;
            line-height: 1.6;
        }
        .contact-info {
            margin-top: 2rem;
            font-size: 1.1rem;
        }
        .download-button {
            display: block;
            margin-top: 0.5rem; /* Adjusted margin top */
            padding: 0.75rem 1rem;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            text-align: center;
            border-radius: 5px;
            transition: background-color 0.3s;
            width: 200px; /* Adjust button width as needed */
            border: none; /* Remove border */
            cursor: pointer;
            margin: 0 auto; /* Center horizontally */
        }
        .download-button:hover {
            background-color: #0056b3;
            text-decoration: none; /* Remove underline on hover */
        }
        .download-button:focus {
            outline: none; /* Remove focus outline */
        }
        .rounded-image {
            border-radius: 50%;
            width: 100%; /* Ensure the image fits within the container */
            max-width: 150px; /* Adjust size as needed */
            height: auto; /* Maintain aspect ratio */
            display: block;
            margin: 0 auto 20px; /* Center image and add spacing */
        }
        .social-buttons {
            display: flex;
            justify-content: center; /* Center horizontally */
            padding: 20px;
        }
        .social-buttons a {
            display: inline-block;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and introduction
st.title("Welcome to My Portfolio")
st.markdown("Explore my projects, learn about me, and contact me for collaborations!")

# Use columns for layout
col1, col2 = st.columns(2)

# Column 1: Display image
with col1:
    st.image('pratik.jpg', caption='Pratik Dahal', use_column_width=True, output_format='JPEG')

# Column 2: About Me section
with col2:
    st.markdown('## About Me')
    st.text(""" 
            Data & ML enthusiast 
            with love of exploring data to 
            uncover insights
            and build predictive models 
            that can make a real impact.
            I enjoy working with Python,
            BeautifulSoup,
            Pandas,Numpy,Matplotlib,
            Seaborn,scikit-learn, 
            and other tools to
            solve complex problems and
            create innovative solutions.
          """)

# Centered "Download Resume" button
resume_path = 'Pratik_Dahal_Resume.pdf'  # Update with your actual file path

st.markdown(f'<a href="{resume_path}" download="Pratik_Dahal_Resume.pdf" class="download-button">Download Resume</a>', unsafe_allow_html=True)

st.title('Explore My Projects')

# Project data (you can replace this with your actual project information)
projects = [
    {
        "title": "School Dropout Analysis",
        "description": "School Dropout Analysis",
        "github_link": "https://github.com/Pratiiikdahal/school_dropout_analysis"
    },
    {
        "title": "Parkinsons Disease Prediction",
        "description": "Descr.",
        "github_link": "https://github.com/Pratiiikdahal/final-year-parkinsonsdisease-prediction"
    }]

# Display cards for each project
for project in projects:
    col3, col4 = st.columns([1, 3])  # Adjust column ratios as needed

    with col3:
        st.image('project.jpg', caption="view the project here", use_column_width=True)

    with col4:
        st.markdown(f"## {project['title']}")
        st.write(project['description'])
        st.markdown(f'<a href="{project["github_link"]}" target="_blank">View on GitHub</a>', unsafe_allow_html=True)
        

st.title('Contact Me')

# Display social media buttons
st.markdown('<div class="social-buttons">', unsafe_allow_html=True)

social_links = {
    "LinkedIn": "https://www.linkedin.com/in/pratik-dahal-101782239/",
    "Instagram": "https://www.instagram.com/pratiiikdahal/",
    "Facebook": "https://www.facebook.com/pratik.dahal.142/",
    "GitHub": "https://github.com/Pratiiikdahal"
}

for platform, link in social_links.items():
    if platform == "LinkedIn":
        logo_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
    elif platform == "Instagram":
        logo_url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
    elif platform == "Facebook":
        logo_url = "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
    elif platform == "GitHub":
        logo_url = "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"
    else:
        continue

    st.markdown(f'<a href="{link}" target="_blank"><img src="{logo_url}" alt="{platform}" width="50" height="50"></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
