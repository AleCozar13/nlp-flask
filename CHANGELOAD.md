# Changelog

All notable changes to this project will be documented in this file.


## [1.0.0] - 2024-11-12

### Added

- Full functionality for sentiment analysis, classifying text as positive or negative using Hugging Face.
- Web interface to test sentiment analysis using Flask (routes `/` for the home page and `/sentimentAnalyzer` for analyzing text).
- Docker setup with `docker-compose.yml` and `Dockerfile` to run the app in a containerized environment.
- Basic HTML form in `index.html` for user input and displaying results.
- JavaScript (`mywebscript.js`) to handle user input and display the sentiment result.
- Unit test (`test_sentiment_analysis.py`) for the `sentiment_analyzer` function to validate sentiment classification.

### Changed
- Project structure updated for better organization, separating app logic, Docker files, and frontend code.

### Fixed
- Fixed initial bugs in the sentiment analysis function that caused incorrect classification.

## [0.1.0] - 2024-10-30

### Added
- Initial commit with project structure set up.
- Basic Flask app with a route to serve the home page (`index.html`).
