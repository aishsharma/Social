"""
Author: Aishwarya Sharma
"""

import subprocess


sql_url = "mysql+pymysql://root:root@localhost:3306/social"

command = "sqlacodegen --outfile TempModels.py {0}".format(sql_url)

subprocess.run(command)
