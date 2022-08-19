import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Serge Amoungui, IT Eng.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced educator, researcher and administrator with nearly ten years of experience in the data-driven environment and a passion for providing insights based on predictive modeling. 
- Strong verbal and written communication skills
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/serges-amoungui-441074220/" target="_blank">Serge Amoungui</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#eng-tools">Eng Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Artificial Intelligence & Management**, *IA SCHOOL*, France','2020-2022')
st.markdown('''
- Professional End-of-Study Project Master `Implementing a Recommendation Engine API`.
- Has obtained professional certifications from Data Scientist (https://www.datacamp.com/certificate/DS0016658517671), Data Analyst (https://www.datacamp.com/certificate/DA0015853128558) and a Python Developer certificate, and SQL Fundamental on the DataCamp platform.
''')

txt('**Pedagogical Eng** (Computer Science), *ENS of University of Yde I*, Cameroon', '2013-2016')
st.markdown('''
- Professional end-of-study project `Development and application of an APC (Learning by Competence) learning process for middle school students in IT`.
''')

txt('**IT engineer** (Software Engineer & Telecom), *ISS of University of Maroua*, Cameroon', '2010-2012')
st.markdown('''
- Professional Project at the end of an Engineer's study `Implementation of an application for archiving Campost maintenance operations`
- captain of the basketball team.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist & Administrator**, kwin\'s hair E-commerce Platform, Remote, (https://kwinshair.com/fr/)', ' Jun 2022 - Today')
st.markdown('''
- Development of functionalities 
- Administration of the platform
- Content manager & Web SEO            
''')

txt('**Web Developer Freelancer**, WTC Start-up, Remote', '2020-2021')
st.markdown('''
- Development of a content management platform
- Realization of reporting, development of tests
- Technology: PHP/Laravel, HTML5/CSS3, ReactJS     
''')

txt('**High School Professor**,  Ministry of Secondary Education, Official, Cameroon', '2016-2021')
st.markdown('''
- Pedagogical Manager of the Department of Computer Science
- Elaboration and application of educational projects.
- Maintenance of the computer park
- Teaching algorithmic courses in Pascal language
''')

txt('**Web Developer**, at AMSCorp, Cameroon', '2017-2019')
st.markdown('''
- Development of the different functionalities of the sites
- Realization of reporting
- development of tests.
''')

txt('**IT Engineer**, at TheoBusiness, Cameroon', '2013')
st.markdown('''
In partnership with the start-up Cyxwiz, tasks: 
- Maintenance and network installation within the partner establishments
- Installation of the information systems and ERP of the Start-up Cyxwiz
- Web application development
''')

txt('**Systems Engineer Intern**, at Campost, Cameroon', '2012')
st.markdown('''
- Maintenance and installation of networks of the computer park of the post offices of Campost
- Professional Project: Implementation of the information system for archiving maintenance operations of campost DRH
''')

#####################
st.markdown('''
## Eng Tools
''')
txt4('ABCTools', 'Desktop Software package for affine application, using Java', '')
txt4('i-Library', 'A library management software, implement in c language', 'https://github.com/serges007/Gestion-d-une-bibliotheque-en-C')
txt4('ProgiLab', 'Matlab learning software package, implement with matlab language','https://github.com/serges007/progiciel-matlab')
txt4('Contact Package', 'Laravel 5.* Contact Management Package', 'https://packagist.org/packages/amoungui/contact-form')
txt4('Newsletter Package', 'Laravel 5.* Newsletter Management Package', 'https://packagist.org/packages/scaffolder/newsletter')
txt4('Blockchain Tool (Free Solution)', 'A blockchain projet implementation with Typescript, using TypeORM Framework', 'https://github.com/amoungui/blockchain')
txt4('Allocine DataViz', 'Allociné Data Analysis Projet', 'https://amoungui-allocine-visualization-data-app-a2ujok.streamlitapp.com/')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux/Ubuntu` ')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `PySpark`, `Hadoop`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`, `Power BI`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `Keras`')
txt3('Database Management', '`PostgreSQL`, `MongoDB`, `MySQL` ')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Scrapy`, `PHP/Laravel`, `Node.js/Typescript`, `Java`, `WordPress`')
txt3('Model deployment', '`streamlit`, `R Shiny`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/serges-amoungui-441074220/')
txt2('Twitter', 'https://twitter.com/Amoungui')
txt2('GitHub', 'https://github.com/amoungui')
txt2('GitHub', 'https://github.com/serges007/')
txt2('Instagram', 'https://www.instagram.com/jazzmastaz/')
