"""import json


class TestController(object):

    @classmethod
    def setup_class(cls):
        cls.client = None
        cls.headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'cf7c9541c2b477a00cbe2549cda1b5c118c75f7f7a2448eebd831611'
        }
        cls.wrong_headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'hogehoge'
        }
        cls.create_data = json.dumps({
            'name': 'name_01',
            'description': 'description_01',
            'developer': 'developer_01',
            'ram_min': 1,
            'cpu_min': 'cpu_min_01',
            'gpu_min': 'gpu_min_01',
            'OS_min': 'OS_min_01',
            'storage_min': 1,
            'ram_rec': 1,
            'cpu_rec': 'cpu_rec_01',
            'gpu_rec': 'gpu_rec_01',
            'OS_rec': 'OS_rec_01',
            'storage_rec': 1,
        })
        cls.update_data = {
            'name': 'name_02',
            'description': 'description_02',
            'developer': 'developer_02',
            'ram_min': 2,
            'cpu_min': 'cpu_min_02',
            'gpu_min': 'gpu_min_02',
            'OS_min': 'OS_min_02',
            'storage_min': 2,
            'ram_rec': 2,
            'cpu_rec': 'cpu_rec_02',
            'gpu_rec': 'gpu_rec_02',
            'OS_rec': 'OS_rec_02',
            'storage_rec': 2,
        }

    def test_get_game(self):
        path = '/api/v1/games?name=vrkshop'
        response = self.client.get(path, headers=self.headers)
        print(response.get_data())
        assert response.status_code == 200

"""