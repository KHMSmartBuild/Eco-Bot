# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME EcoBot

# Run Streamlit app when the container launches
CMD ["streamlit", "run", "streamlit_app/Eco-BotAPP.py"]
