#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jingkexin
"""

import boto3

ACCESS_KEY = 'AKIA3HYZXATDMXHROZMX'
SECRET_KEY = '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'
BUCKET_NAME = 'kexin'


s3 = boto3.resource(
        's3',
        aws_access_key_id = ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY
     )

# upload a file to S3
data = open('accessKeys.csv', 'rb')

s3.Bucket(BUCKET_NAME).put_object(Key = 'accessKeys.csv', Body = data)

#download a file from S3
KEY = 'accessKeys.csv'
s3.Bucket(BUCKET_NAME).download_file(KEY, 'Keys.csv')

#download all files from S3
s3 = boto3.client(
        's3',
        aws_access_key_id = ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY
    )

list = s3.list_objects(Bucket = 'kexin')

all_files = list['Contents']

for file in all_files:
    s3.download_file(
            Bucket = 'kexin',
            Key = file['Key'],
            Filename = file['Key']
    )


