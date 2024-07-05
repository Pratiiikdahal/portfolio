import streamlit as st

# Include Bootstrap 5 CSS for styling
st.markdown("""
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css">
""", unsafe_allow_html=True)

# Custom CSS for additional styling
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        /* Navigation bar styling */
        .navbar {
            padding: 0.5rem 1rem;
            border-radius: 5px;
            background-color: transparent; /* Remove grey background */
        }
        .nav-link {
            color: white !important; /* Change to white */
            margin: 0 1rem; /* Space between links */
            text-transform: uppercase; /* Uppercase letters for links */
            font-weight: bold; /* Bold font for links */
            font-size: 1.2rem; /* Increase font size */
            text-decoration: none; /* Remove underline */
        }
        .nav-link:hover {
            color: #ddd !important; /* Lighter shade on hover */
            text-decoration: none; /* Ensure underline doesn't appear on hover */
        }
        .navbar-nav {
            display: flex; /* Ensure links are inline horizontally */
            justify-content: center; /* Center the links */
        }
        .nav-item {
            list-style: none; /* Remove bullets */
        }
        /* Custom styling for title with animation */
        .animated-title {
            color: pink; /* Pink color */
            font-size: 3rem;
            animation: slideIn 2s ease-in-out; /* Apply slide-in animation */
        }
        @keyframes slideIn {
            from {
                transform: translateX(-100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        /* Download button */
        .download-button {
            display: block;
            margin-top: 0.5rem; /* Adjusted margin top */
            padding: 0.75rem 1rem;
            background-color: #007bff;
            color: white;
            text-decoration: none; /* Remove underline */
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
            text-decoration: none; /* Ensure underline doesn't appear on hover */
        }
        .download-button:focus {
            outline: none; /* Remove focus outline */
        }
        /* Social buttons */
        .social-buttons {
            display: flex;
            justify-content: center; /* Center horizontally */
            padding: 20px;
        }
        .social-buttons a {
            display: inline-block;
            margin: 0 10px;
        }
        /* Centered text next to the image */
        .description-container {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-top: 2rem;
        }
        .description-text {
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 600px; /* Limit text width for better readability */
            margin-left: 1rem; /* Space between image and text */
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <nav class="navbar">
        <div class="navbar-collapse">
            <ul class="navbar-nav mx-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#about-me">About Me</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#projects">My Works</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact Me</a>
                </li>
            </ul>
        </div>
    </nav>
""", unsafe_allow_html=True)

# Page title with animation
st.markdown('<h1 class="animated-title">Welcome to My Portfolio</h1>', unsafe_allow_html=True)
st.markdown("Explore my projects, learn about me, and contact me for collaborations!")

# About Me section
st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)  # Anchor for the About Me section
st.title("About Me")

# Use columns for layout
col1, col2 = st.columns([1, 2])  # Adjust column ratios to give more space to text

# Column 1: Display image with reduced size using Streamlit image function
with col1:
    st.image('pratik.jpg', caption='Pratik Dahal', use_column_width=True, width=150)  # Reduced width for smaller size

# Column 2: About Me text centered with respect to image
with col2:
    st.markdown("""
        <div class="description-container">
            <div class="description-text">
                Data & ML enthusiast 
                with love of exploring data to 
                uncover insights
                and build predictive models 
                that can make a real impact.
                I enjoy working with Python,
                BeautifulSoup,
                Pandas, Numpy, Matplotlib,
                Seaborn, scikit-learn, 
                and other tools to
                solve complex problems and
                create innovative solutions.
            </div>
        </div>
    """, unsafe_allow_html=True)

# Centered "Download Resume" button
resume_path = 'Pratik_Dahal_Resume.pdf'  # Update with your actual file path

st.markdown(f'<a href="{resume_path}" download="Pratik_Dahal_Resume.pdf" class="download-button">Download Resume</a>', unsafe_allow_html=True)

# Projects section
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)  # Anchor for the Projects section
st.title('Explore My Projects')

# Project data (you can replace this with your actual project information)
projects = [
    {
        "title": "School Dropout Analysis",
        "description": "A comprehensive analysis of factors contributing to school dropout rates.",
        "github_link": "https://github.com/Pratiiikdahal/school_dropout_analysis"
    },
    {
        "title": "Parkinson's Disease Prediction",
        "description": "Using machine learning to predict Parkinson's disease progression.",
        "github_link": "https://github.com/Pratiiikdahal/final-year-parkinsonsdisease-prediction"
    }
]

# Display cards for each project
for project in projects:
    col1, col2 = st.columns([1, 3])  # Adjust column ratios as needed

    with col1:
        st.image('project.jpg', caption="View the project here", use_column_width=True)

    with col2:
        st.markdown(f"## {project['title']}")
        st.write(project['description'])
        st.markdown(f'<a href="{project["github_link"]}" target="_blank">View on GitHub</a>', unsafe_allow_html=True)

# Contact Me section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)  # Anchor for the Contact section
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

st.text('E-mail:')
st.markdown('notpratikdahal@gmail.com')

# Include Bootstrap 5 JavaScript for responsive navigation
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.min.js"></script>
""", unsafe_allow_html=True)

