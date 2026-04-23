from app.workers.celery_worker import celery
import time

@celery.task
def send_order_confirmation(email, order_id):
    time.sleep(5)

    print(
        f"Email sent to {email} for order {order_id}"
    )

    return True