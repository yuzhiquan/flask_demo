import os
from init_log import log


def write_log_file(log_str, logfile_name):
	pwd = os.getcwd()
	logfile_path = os.path.join(pwd, logfile_name)
	with open(logfile_path, "w") as logfile:
		logfile.write(log_str)
	log.debug("Write {} to file {} succ!".format(log_str, logfile_name))
