# Subjectivity Classifier API

## Initialization

Build docker:

`docker build -t veraai_subjectivity:latest .
`

Serve the API:

`docker run -dit -v $(pwd)/models/model:/app/model -p 80:8080 veraai_subjectivity:latest`
