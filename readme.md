# Grouped bar charts in Streamlit

Demonstrates how to show grouped bar charts in Streamlit using Altair & Plotly Express.

To execute:

```
streamlit run app.py
```

## Docker
This code can run using Docker, with hot reload capability (by including the config.toml).

To build the image:

```
docker build -t streamlit_groupbar . 
```

To run with Docker:

```
docker run -d --rm -p 8501:8501 --name streamlit_groupbar -v .:/app streamlit_groupbar
```

To stop the Docker container:

```
docker container stop streamlit_groupbar
```

## Requirements
- Python 3.11
- Streamlit 1.25.0
- Altair 5.0.1
- Plotly 5.16.0