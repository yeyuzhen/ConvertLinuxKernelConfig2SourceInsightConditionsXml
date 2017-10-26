#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import re

RE_CONFIG = r'^CONFIG.*=.*'
RE_NORMAL_CONFIG = r'(^CONFIG.*)=[ym]{1}.*'    # examples: CONFIG_PROC_KCORE=y  CONFIG_NF_NAT_IPV4=m
RE_ABNORMAL_CONFIG = r'(^CONFIG.*)=(.*)'    # examples: CONFIG_DEFAULT_TCP_CONG="cubic"  CONFIG_SPLIT_PTLOCK_CPUS=4

pattern_config = re.compile(RE_CONFIG)
pattern_normal_config = re.compile(RE_NORMAL_CONFIG)
pattern_abnormal_config = re.compile(RE_ABNORMAL_CONFIG)

def get_args():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('-s', '--src', default='.config', help='linux kernel config file path, default: .config', dest='src_path')
	arg_parser.add_argument('-d', '--dest', required=True, help='source insight conditional parsing xml file path', dest='dest_path')
	
	args = arg_parser.parse_args()
	
	return (args.src_path, args.dest_path)

def parse_config_line(line):
	if pattern_config.match(line):
		normal_match = pattern_normal_config.match(line)
		if normal_match:
			return normal_match.groups()
		else:
			abnormal_match = pattern_abnormal_config.match(line)
			return abnormal_match.groups()
	return None

def parse_kernel_config(config_path):
	if not os.path.exists(config_path):
		return None
	
	kernel_configs = []
	config_file = None
	try:
		config_file = open(config_path)
		content = config_file.readlines()
		
		for raw_line in content:
			line = raw_line.rstrip()
			config_item = parse_config_line(line)
			if config_item:
				kernel_configs.append(config_item)
	finally:
		if config_file:
			config_file.close()
	return kernel_configs
	
if __name__ == '__main__':
	src_path, dest_path = get_args()
	
	kernel_configs = parse_kernel_config(src_path)
	if not kernel_configs:
		print 'Error: kernel config file "%s" is empty, please check the content.' % (src_path)
		
	for config in kernel_configs:
		print config
	#print src_path
	#print dest_path
	
	# TODO generate source insight conditional parsing xml config file.
