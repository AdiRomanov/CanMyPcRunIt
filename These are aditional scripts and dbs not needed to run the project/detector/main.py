import json

import psutil
import platform
import GPUtil
import cpuinfo
import requests


def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info["brand_raw"]


def get_gpu_info():
    try:
        gpu = GPUtil.getGPUs()[0]
        return gpu.name
    except Exception as e:
        return f"Error at obtaining info about GPU: {str(e)}"


def get_memory_info():
    memory = psutil.virtual_memory()
    return memory.total / (1024 ** 3)


def get_storage_info():
    storage = psutil.disk_usage('/')
    return storage.total / (1024 ** 3), storage.free / (1024 ** 3)


def get_os_info():
    return platform.system(), platform.version()


if __name__ == "__main__":
    system_info = {
        "GPU": f"Model: {get_gpu_info()}",
        "CPU": f"Model: {get_cpu_info()}",
        "RAM": f"Total: {get_memory_info():.2f} GB",
        "OS": f"OS: {get_os_info()[0]} {get_os_info()[1]}",
        "storage": f"Total: {get_storage_info()[0]:.2f} GB, Available: {get_storage_info()[1]:.2f} GB"
    }

    json_data = json.dumps(system_info)

    site_url = "http://127.0.0.1:8000/api/receive-data/"

    # Manually set the CSRF token value
    csrf_token = "EGPgJDekXizwjcVJaa1TU5hXXy3FFxMj"

    # Print the headers before making the POST request
    headers = {'X-CSRFToken': csrf_token}
    # print("Request Headers:", headers)

    # Send data to the site with the CSRF token
    try:
        response = requests.post(site_url, json=json_data, headers=headers)
        if response.status_code == 200:
            print("Data sent successfully.")
        # print("Response from the site:", response.text)  # Log the response content
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print("Response from the site:", response.text)  # Log the response content in case of failure
    except Exception as e:
        print(f"An error occurred: {str(e)}")
input("Press Enter to exit...")