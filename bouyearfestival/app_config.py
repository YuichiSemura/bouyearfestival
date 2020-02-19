import os

class AppConfig:
    def __init__(self, file_name, base_dir):
        self.port = 8080
        self.debug_path = "logs/debug.log"
        self.error_path = "logs/error.log"
        self.auth_dir = "data/"
        self.sec_name = "sec.pem"
        self.pub_name = "pub.pem"

        # load my configure
        with open(file_name, "r") as f:
            for line in f:
                arr = line.strip().split("=")
                assert len(arr) == 2, "invalid line in configure: " + line
                key = arr[0].strip()
                value = arr[1].strip()

                if key == "port":
                    self.port = value
                elif key == "debug_path":
                    self.debug_path = value
                elif key == "error_path":
                    self.error_path = value
                elif key == "auth_dir":
                    self.auth_dir = value
                elif key == "sec_name":
                    self.sec_name = value
                elif key == "pub_name":
                    self.pub_name = value

        if self.debug_path[0] != "/":
            self.debug_path = os.path.join(base_dir, self.debug_path)

        if self.error_path[0] != "/":
            self.error_path = os.path.join(base_dir, self.error_path)

        if self.auth_dir[0] != "/":
            self.auth_dir = os.path.join(base_dir, self.auth_dir)
            
    def get_sec_path(self):
        return self.auth_dir + self.sec_name

    def get_pub_path(self):
        return self.auth_dir + self.pub_name
