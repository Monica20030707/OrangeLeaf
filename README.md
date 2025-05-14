\documentclass[11pt]{article}       % set main text size
\usepackage[letterpaper,            % set paper size to letterpaper. change to a4paper for resumes outside of North America
top=0.5in,                          % specify top page margin
bottom=0.5in,                       % specify bottom page margin
left=0.5in,                         % specify left page margin
right=0.5in]{geometry}              % specify right page margin
                       
\usepackage{XCharter}               % set font
\usepackage[T1]{fontenc}            % output encoding
\usepackage[utf8]{inputenc}         % input encoding
\usepackage{enumitem}               % enable lists for bullet points: itemize and \item
\usepackage[colorlinks=true, linkcolor=black, urlcolor=blue]{hyperref}    % format hyperlinks
\usepackage{titlesec}               % enable section title customization
\raggedright                        % disable text justification
\pagestyle{empty}                   % disable page numbering
\usepackage{comment}                % block comment

% ensure PDF output will be all-Unicode and machine-readable
\input{glyphtounicode}
\pdfgentounicode=1

% format section headings: bolding, size, white space above and below
\titleformat{\section}{\bfseries\large}{}{0pt}{}[\vspace{1pt}\titlerule\vspace{-6.5pt}]

% format bullet points: size, white space above and below, white space between bullets
\renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$}
\setlist[itemize]{itemsep=-2pt, leftmargin=12pt, topsep=6pt} %%% Test various topsep values to fix vertical spacing errors

% resume starts here
\begin{document}

% name
\centerline{\Huge Thuy Nguyen}

\vspace{5pt}

% contact information
\centerline{\href{mailto:thuybohr@gmail.com}{thuybohr@gmail.com} | 206-423-9827 |
\href{https://www.linkedin.com/in/thuy-nguyen-46505121b/}{linkedin.com/in/thuy-nguyen-46505121b}}

\centerline{\href{https://github.com/Monica20030707}{github.com/Monica20030707} | 
\href{https://monica20030707.github.io/}{monica20030707.github.io/}} 

\vspace{-9pt}

% education section
\section*{Education}
\textbf{Bellevue College} -- BS in Computer Science -- 3.5/4.0 GPA \hfill September 2021 -- June 2025\\
\vspace{-9pt}
\begin{itemize}
  \item Award: Amazon Scholarship, Activities: Social Media Manager of Computer Science Club
\end{itemize}

\vspace{-18.5pt}

% experience section
\section*{Experience}
\textbf{Open-Source Intern,} {CodeDay} -- Seattle, WA \hfill April 2025 -- May 2025 \\
\vspace{-9pt}
\begin{itemize}
  \item Led team progress as Scrum Master, ensuring timely delivery by coordinating client communications.
  \item Resolved two OED tickets in Agile, through the implementation of database test cases.
  \item Ran and tested the website in various environments with Docker, ensuring its functionality and performance.
\end{itemize}

\textbf{Teaching Assistant,} {Bellevue College} -- Bellevue, WA \hfill April 2024 -- December 2024 \\
\vspace{-9pt}
\begin{itemize}
  \item Guided 40+ students in Java and SQL, with class materials during and after class.
  \item Educated students in relational database design and MySQL Workbench operations.
  \item Elevated student proficiency in JUnit and Javadoc, enhancing assignment quality by 20\%.
  \item Delivered detail feedback and recommended lecture topics based on student needs.
\end{itemize}

\textbf{Coding Competition Developer,} {Bellevue College} -- Bellevue, WA \hfill April 2024 -- Present \\
\vspace{-9pt}
\begin{itemize}
  \item Developed real-time score updates using SQL and PHP, increasing efficiency by 40\%.
  \item Enhanced web interfaces with HTML and CSS, boosting user satisfaction by 30\%.
  \item Created coding problems with auto test cases for Java, Python, C++, and Golang.
  \item Assisted onsite at a competition with 30+ participants to ensure smooth operations.
\end{itemize}

\textbf{Web Design Intern,} {RSVP} -- Sai Gon, Vietnam \hfill July 2022 -- September 2022 \\
\vspace{-9pt}
\begin{itemize}
  \item Designed a Figma mock-up for the company's planned landing page refresh.
  \item Collaborated in a team of 4 developers, handled minor coding tickets and assisted with design works.
  \item Worked closely with clients to ensure our HTML email template suited the clients needs.
\end{itemize}

\begin{comment}
\textbf{Front Desk Assistant,} {Bellevue College} -- Bellevue, WA \hfill June 2023 -- April 2024 \\
\vspace{-9pt}
\begin{itemize}
  \item Managed tasks with precision in a fast-paced environment.
  \item Using Canva to design Parking Bookmark for advertising & assisting users.
  \item Utilized Microsoft Word, Excel and Outlook for efficient data management.
  \item Collaborated with team members to ensure accurate and prompt assistance.
\end{itemize}
\end{comment}

\vspace{-18.5pt}

% projects section
\section*{Projects}
\textbf{Balance Tester}{ - React, Redux Toolkit, Tailwind CSS, Express.js, Jest} \hfill \href{https://main.d22cx9qmwqrer1.amplifyapp.com/}{Demo} \\
\vspace{-9pt}
\begin{itemize}
  \item Built a real-time full-stack web app that detects balance issues using pose recognition from MediaPipe's ML.
  \item Integrated webcam functionality with React Webcam to capture user movements.
  \item Managed state flow using Redux Toolkit and styled the UI with Tailwind CSS for responsiveness.
  \item Wrote unit tests with Jest, including webcam mock to simulate user behavior and component reliability.
\end{itemize}

\textbf{Stock Ratio Tracker}{ - Python, React, Typescript} \hfill \href{https://github.com/Monica20030707/tradingDashboard-UI}{github.com} \\
\vspace{-9pt}
\begin{itemize}
  \item Fixed broken files in the repository to make web application output correctly. 
  \item Set up a local development environment by downloading the necessary files, tools and dependencies. 
  \item Used JPMorgan Chase’s open-source library called Perspective to generate a live graph that displays a data feed in a clear and visually appealing way for traders to monitor. 
\end{itemize}

\begin{comment}
\textbf{Read MNIST Handwritten Dataset}{ - Python, Numpy Library} \hfill \href{https://github.com/Monica20030707/Artificial-Neutral-Network_ML}{github.com} \\
\vspace{-9pt}
\begin{itemize} 
  \item Built an Artificial Neural Network (ANN) from scratch to classify handwritten digits (0-9). 
  \item Achieved over 90\% accuracy using Backpropagation algorithm.
\end{itemize}
\end{comment}


\textbf{Traffic Violation Detection System}{ - Javascript, AWS Cloud Services} \hfill \href{https://github.com/Monica20030707/AWS_rekonigition-N-read-database}{github.com} \\
\vspace{-9pt}
\begin{itemize}
  \item Processed license plate images from S3, sending email notices to offenders with violation details and fines.
  \item Engineered Regex to identify California plates, routed through SQS and EventBridge for proper handling.
\end{itemize}

% alternate formatting for projects section
\begin{comment}
%  \begin{itemize}
%   \item \textbf{QuantSoftware Toolkit:} Open source Python library for data analysis and machine learning for finance
%   \item \textbf{GitHub Visualization:} Data visualization of Git Log data using D3 to analyze project trends over time
%   \item \textbf{Recommendation System:} Music and movie recommender systems using collaborative filtering on public datasets
%   \item \textbf{Mac Setup:} Book that gives step by step instructions on setting up developer environment on Mac OS
% \end{itemize}
\end{comment}

\vspace{-18.5pt}


% skills section
\section*{Skills}
\textbf{Languages:} Java, Python, Kotlin, C++, Flutter, Next.js, Typescript, JavaScript, MySQL\\
\textbf{Skills:} Full-stack Web Developing, Agile Coaching, Clean Code, Scrum Master, Collaboration, Customer Service
\textbf{Tools:} React, Redux Toolkit, Redux Thunk, Docker, VS Code, Android Studio, AWS Cloud Services\\

\vspace{-6.5pt}

\end{document}