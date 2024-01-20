import psutil
import platform
import GPUtil
import cpuinfo

from ranking import CpuRanker, GpuRanker


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


def get_current_specs():
    system_info = {
        "GPU": f"Model: {get_gpu_info()}",
        "CPU": f"Model: {get_cpu_info()}",
        "RAM": f"Total: {get_memory_info():.2f} GB",
        "OS": f"OS: {get_os_info()[0]} {get_os_info()[1]}",
        "storage": f"Total: {get_storage_info()[0]:.2f} GB, Available: {get_storage_info()[1]:.2f} GB"
    }

    return system_info


def test_ranking():
    mypc = get_current_specs()
    cpu_ranking = CpuRanker()
    gpu_ranking = GpuRanker()
    # print(cpu_ranking.get_rank())
    print("cpu: ", cpu_ranking.get_rank_of(mypc["CPU"]))
    print("gpu: ", gpu_ranking.get_rank_of(mypc["GPU"]))


if __name__ == "__main__":
    # print(get_current_specs())
    test_ranking()
