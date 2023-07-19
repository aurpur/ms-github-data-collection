# Desc: This file is used to initialize the api package.
# It contains the configuration of the api package.
#

import configparser
import resources.constant as constant


config = configparser.ConfigParser()
config.read(constant.CONFIG_FILE)
