class CpuRanker:
    def __init__(self):
        self.__file = "cpu_specs.txt"
        self.__rank = {}

        with open(self.__file, "r") as file:
            # content = file.read()
            i = 0
            rank = 0
            cpu = ""
            model = ""
            score = 0

            for line in file:
                if i % 4 == 0:
                    rank = line.strip()
                    if rank[-1] == '.':
                        rank = rank[:-1]
                if i % 4 == 1:
                    cpu = line.strip()
                if i % 4 == 2:
                    model = line.strip()
                if i % 4 == 3:
                    score = line.strip()
                    self.__rank[rank] = {
                        "rank": rank,
                        "cpu": cpu,
                        "model": model,
                        "score": score,
                    }
                i += 1

    def get_rank(self):
        return self.__rank

    def get_rank_of(self, model):
        best_no = 0
        best = ""
        for item in self.__rank.items():
            if item[1]["model"] in model:
                if best_no < len(item[1]["model"]):
                    best = item[1]["rank"]
                    best_no = len(item[1]["model"])

        return best if best != "" else "NA"


class GpuRanker:
    def __init__(self):
        self.__file = "gpu_specs.txt"
        self.__rank = {}

        with open(self.__file, "r") as file:
            i = 0
            rank = 0
            brand = ""
            model = ""
            score = 0

            for line in file:
                if i % 5 == 0:
                    rank = line.strip()
                    if rank[-1] == '.':
                        rank = rank[:-1]
                if i % 5 == 1:
                    brand = line.strip()
                if i % 5 == 2:
                    model = line.strip()
                if i % 5 == 3:
                    score = line.strip()
                    self.__rank[rank] = {
                        "rank": rank,
                        "brand": brand,
                        "model": model,
                        "score": score,
                    }
                i += 1

    def get_rank(self):
        return self.__rank

    def get_rank_of(self, model):
        best_no = 0
        best = ""
        for item in self.__rank.items():
            if item[1]["model"] in model:
                if best_no < len(item[1]["model"]):
                    best = item[1]["rank"]
                    best_no = len(item[1]["model"])

        return best if best != "" else "NA"
