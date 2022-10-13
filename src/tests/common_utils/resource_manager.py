import csv
import os



class ResourceManager:
    """Resource Manager that handles the object resource objects in Jeenie for iOS and Android."""

    def __init__(self, resource_path, platform, platform_version=''):
        """Initialize the manager with dictionary of resources based on the given file path."""
        with open(resource_path + '/resource.csv') as csv_file:
            resource_file = csv.DictReader(csv_file)
            self.resources = {}
            if platform_version:
                platform_version = platform_version + '_'
            for row in resource_file:
                if platform == 'iOS':
                    column_name = 'IOS_{}RESOURCE'.format(platform_version)
                    resource_value = row[column_name]
                elif platform == 'Android':
                    column_name = 'ANDROID_{}RESOURCE'.format(platform_version)
                    resource_value = row[column_name]
                else:
                    resource_value = "Not Found"
                self.resources.update({row['RESOURCE_ID']: resource_value})

    def __init__(self, resource_path):
        """Initialize the manager with dictionary of resources based on the given file path."""
        with open(resource_path + '/resource.csv') as csv_file:
            resource_file = csv.DictReader(csv_file)
            self.resources = {}
            for row in resource_file:
                column_name = 'RESOURCE_VAL'
                resource_value = row[column_name]
                self.resources.update({row['RESOURCE_ID']: row['RESOURCE_VAL']})

    def get_resource(self, resource_key):
        """Get resource selector according to the given key."""
        try:
            resource_value = self.resources[resource_key]
            return resource_value
        except Exception as e:
            print(str(e))
            return "No resource for key: " + resource_key

    @staticmethod
    def get_resource_path(module):
        wb_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if module == "home":
            resource_path = wb_path + os.path.sep + "common_utils"
        else:
            resource_path = wb_path + os.path.sep + module
        return resource_path
