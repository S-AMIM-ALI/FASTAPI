from fastapi import HTTPException
from put import *
@app.delete("/student/delete/{st_id}")
def delete_student(st_id: int):
    data = load_data()

   
    student = next((item for item in data if item["st_id"] == st_id), None)

    if not student:
        raise HTTPException(status_code=404, detail="ID not found")


    data.remove(student)

    save_data(data)

    return {"message": "Data deleted successfully"}
