from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
