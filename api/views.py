from db_models import SessionLocal, QueueStatus


def current_status():
    db = SessionLocal()
    status = db.query(QueueStatus).first()
    if status:
        return {"status": status.current_status}
    db.add(QueueStatus(current_status=1))
    db.commit()
    status = db.query(QueueStatus).first()
    return {"status": status.current_status}

def change_status():
    db = SessionLocal()
    status = db.query(QueueStatus).first()
    last_status = status.current_status
    if last_status == 0:
        status.current_status = 1
    else:
        status.current_status = 0
    db.commit()
    return {"status was": last_status, "new status is": status.current_status}