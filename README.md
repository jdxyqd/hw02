# Personal Website Project

This project is a personal website built using Python and Streamlit. It serves as a portfolio to showcase various projects, provide information about the individual, and allow visitors to get in touch.

## Project Structure

```
personal-website
├── app.py                # Main entry point of the application
├── pages                 # Contains different pages of the website
│   ├── home.py           # Home page layout and content
│   ├── about.py          # About page with personal information
│   ├── projects.py       # Projects page showcasing completed works
│   └── contact.py        # Contact page for visitor inquiries
├── components            # Reusable components for the website
│   ├── navbar.py         # Navigation bar component
│   └── utils.py          # Utility functions for the application
├── assets                # Static assets like styles
│   └── styles.css        # CSS styles for the website
├── data                  # Data files
│   └── products.json     # JSON file holding product data
├── tests                 # Unit tests for the application
│   └── test_app.py       # Tests for main functionalities
├── requirements.txt      # List of dependencies for the project
├── .gitignore            # Files and directories to ignore in Git
└── README.md             # Documentation for the project
```

## Features

- **Home Page**: Welcomes visitors and provides an overview of the website.
- **About Page**: Shares information about the individual or organization.
- **Projects Page**: Displays various projects and works completed.
- **Contact Page**: Allows visitors to reach out through a contact form.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd personal-website
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

- Navigate through the website using the navigation bar.
- Explore the projects and learn more about the individual.
- Use the contact page to send messages or inquiries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.