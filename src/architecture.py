#define the architecture of the system

import simpy

class IoTDevice:
    def __init__(self, env, name, fog_node):
        self.env = env
        self.name = name
        self.fog_node = fog_node
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(5)  # Generate a task every 5 time units
            print(f'{self.name} generated a task at time {self.env.now}')
            task = f"Task from {self.name}"
            self.fog_node.receive_task(task, self.env.now)

class FogNode:
    def __init__(self, env, name, cloud_server):
        self.env = env
        self.name = name
        self.cloud_server = cloud_server

    def receive_task(self, task, created_time):
        print(f'{self.name} received {task} at time {self.env.now}')
        processing_time = 3  # Assume fog node takes 3 units of time to process
        yield self.env.timeout(processing_time)
        print(f'{self.name} processed {task}')
        self.cloud_server.receive_task(task, created_time)

class CloudServer:
    def __init__(self, env, name):
        self.env = env
        self.name = name

    def receive_task(self, task, created_time):
        print(f'{self.name} received {task} for further processing')
        processing_time = 10  # Assume cloud takes 10 units to process
        yield self.env.timeout(processing_time)
        print(f'{self.name} completed {task} at time {self.env.now}')
        print(f'Total time taken for {task} is {self.env.now - created_time}')