# Subjectivity Classifier API

## Initialization

Build docker:

`docker build -t veraai_subjectivity:latest .
`

Serve the API:

`docker run -v $(pwd)/models/model:/app/model -p 8080:8080 veraai_subjectivity:latest`