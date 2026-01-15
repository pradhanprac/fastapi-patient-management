from fastapi import FastAPI,Path, HTTPException
import json
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        
        data = json.load(file)
    return data
@app.get("/")
def hello_world():
    return {"message": "Patient Management System API"}


@app.get("/about")

def about():
    return {"message": "A fully funcational Patient Management System API built with FastAPI."}


# Add view endpoint to return patient data
@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(..., description="The ID of the patient to retrieve",example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

