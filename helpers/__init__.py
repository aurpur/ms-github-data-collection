# Desc: Init file for collector package
# It contains the configuration of the collector package.
#

import configparser
import resources.constant as constant

config = configparser.ConfigParser()
config.read(constant.CONFIG_FILE)