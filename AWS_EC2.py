#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jingkexin
"""
import boto3

ACCESS_KEY = 'AKIA3HYZXATDMXHROZMX'
SECRET_KEY = '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'

ec2 = boto3.resource(
        'ec2',
        aws_access_key_id = ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY,
        region_name = 'us-east-1'
    )


# Create an instance
ec2.create_instances(ImageId='ami-00068cd7555f543d5', MinCount=1, MaxCount=1)


# Terminate an instance
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
ids = []
for instance in instances:
    print(instance.id, instance.instance_type)
    ids.append(instance.id)
    
ec2.instances.filter(InstanceIds=ids).stop()
ec2.instances.filter(InstanceIds=ids).terminate()
    