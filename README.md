✅ FROM python:3.11-slim
This sets the base image.

It means: “Start with a small version of Python 3.11 already installed.”

Docker images are like recipes — this line says, “Start by getting the Python kitchen ready.”

✅ WORKDIR /app
This sets the working directory inside the container.

Any following file commands (like copy) will happen inside this /app folder.

If the folder doesn't exist yet, Docker creates it.

Think of it like:

"CD into /app before doing anything else."

✅ COPY requirements.txt .
This copies the requirements.txt file from your computer into the container’s /app directory.

The . means: “put it right here” (inside /app).

✅ RUN pip install --no-cache-dir -r requirements.txt
This installs Python libraries listed in requirements.txt.

--no-cache-dir just makes the image smaller by not keeping the download cache.

✅ COPY app.py .
This copies your actual Python app (app.py) into the container’s /app folder.

✅ CMD ["python", "app.py"]
This tells Docker:

“When someone runs this container, run this command.”

So it will run your Python script when the container starts.

You can think of this like the main() entry point for your Docker container.

🧪 Summary
This Dockerfile tells Docker:

Start from a lightweight Python setup.

Create a working folder.

Add the dependency list and install it.

Add the app code.

Run the app when the container starts.
