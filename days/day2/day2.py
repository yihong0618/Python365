import time

from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
import docker

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)


thread = None
thread_lock = Lock()
FLAG = True


def get_container(ip, container_id):
    cli = docker.DockerClient(base_url= ip + ":2375")
    try:
        container = cli.containers.get(container_id)
    except:
        container = None
    return container




# 后台线程 产生数据，即刻推送至前端
def background_thread(ip, docker_id):
    container = get_container(ip, docker_id)
    if not container:
        return
    """Example of how to send server generated events to clients."""
    count = 0
    queue = []
    while 1:
        if not FLAG:
            break
        socketio.sleep(1)
        count += 1
        for line in container.logs(tail=10, stream=True):
            if not line:
                break
            line = line.decode('utf-8')
            if line not in queue:
                queue.append(line)

                socketio.emit('server_response',
                            {'data': str(queue[-1]), 'count':count},
                            namespace='/test')
    print("test")

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)



# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    container_id = request.args.get('container_id', "")
    ip = request.args.get('ip', "127.0.0.1")
    global thread
    with thread_lock:
        # if thread is None:
        thread = socketio.start_background_task(background_thread, ip, container_id)


@socketio.on('disconnect', namespace='/test')
def change_flag():
    thread.kill()
    FLAG = False

if __name__ == '__main__':
    socketio.run(app, debug=True)