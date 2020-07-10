from vk import Answer

def connect_run(data):
    conn = Answer(data)
    conn.process_message()
