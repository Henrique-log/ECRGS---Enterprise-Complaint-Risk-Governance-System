from datetime import datetime

fake_db = []
complaint_id_counter = 1


def save_complaint(data: dict):
    global complaint_id_counter

    data["id"] = complaint_id_counter
    data["created_at"] = datetime.utcnow()

    fake_db.append(data)
    complaint_id_counter += 1

    return data
