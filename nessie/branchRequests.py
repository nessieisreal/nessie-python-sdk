import requests
<<<<<<< HEAD

from nessie.models.branch import Branch
from nessie.utils import constants
from nessie.utils.exceptions import NessieApiError, BranchValidationError
=======
from models.branch import Branch
import utils.constants
from utils.exceptions import NessieApiError, BranchValidationError
>>>>>>> master

class BranchRequest(object):

    def __init__(self, api_key):
<<<<<<< HEAD
        self.base_url = constants.baseUrl
=======
        self.base_url = utils.constants.baseUrl
>>>>>>> master
        self.key = api_key

    def __build_params(self):
        return {'key': self.key}

    def __format_response(self, json_array):
        resp_list = []
        for branch_dict in json_array:
            resp_list.append(Branch(branch_dict))
        return resp_list

    def __validate_path(self, id_string):
        if len(id_string) != 24:
            raise BranchValidationError(id_string)
        try:
            int(id_string, 16)
<<<<<<< HEAD
        except ValueError:
=======
        except ValueError as e:
>>>>>>> master
            raise BranchValidationError(id_string)

    def get_branches(self):
        req_url = '%s/branches' % self.base_url
        par = self.__build_params()

        r = requests.get(req_url, params=par)

        if r.status_code != 200:
            raise NessieApiError(r)

        branch_list = r.json()
        return self.__format_response(branch_list)

    def get_branch_by_id(self, id_string):
        self.__validate_path(id_string)
        req_url = '%s/branches/%s' % (self.base_url, id_string)
        par = self.__build_params()

        r = requests.get(req_url, params=par)

        if r.status_code != 200:
            raise NessieApiError(r)

        return Branch(r.json())


def main():
    print("Import this class to use Nessie's Branch APIs!")

if __name__ == "__main__":
    main()
