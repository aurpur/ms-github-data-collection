# Desc: Init file for collector package
# It contains the configuration of the collector package.
#

import configparser

config = configparser.ConfigParser()
config.read('resources/config.properties')